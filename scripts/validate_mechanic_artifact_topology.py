#!/usr/bin/env python3
"""Validate mechanic-owned artifact homes and root artifact districts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MECHANIC_SLUGS = (
    "method-growth",
    "recurrence",
    "experience",
    "agon",
    "antifragility",
    "questbook",
    "rpg",
    "tos-bridge",
    "release-support",
)
ARTIFACT_DIRS = ("schemas", "examples", "config", "generated", "scripts", "tests")
EXPERIENCE_ARTIFACT_MAP = REPO_ROOT / "mechanics" / "experience" / "artifact-map.json"
AGON_ARTIFACT_MAP = REPO_ROOT / "mechanics" / "agon" / "artifact-map.json"

AGON_PREFIXES = ("agon", "test_agon", "build_agon", "validate_agon")
ANTIFRAGILITY_PREFIXES = (
    "deletion_candidate_list",
    "test_via_negativa_surfaces",
)
EXPERIENCE_PREFIXES = (
    "experience",
    "test_experience",
    "validate_experience",
    "appeal_",
    "assistant_office_",
    "authority_resolution_",
    "constitution_runtime_",
    "council_",
    "cross_repo_experience_signal",
    "decision_replay_",
    "federation_",
    "governance_",
    "kag_promotion_gate",
    "multi_office_",
    "office_",
    "pattern_",
    "precedent_",
    "runtime_policy_lock_",
    "sealed_",
    "service_mesh_",
    "shared_experience_",
    "shared_watch_",
    "source_owner_consent_",
    "stay_order",
    "tos_candidate_dossier_boundary",
    "train_",
    "vote_",
)
METHOD_GROWTH_PREFIXES = (
    "lineage_contract_chain",
    "validate_candidate_lineage_contract",
    "test_validate_candidate_lineage_contract",
    "validate_wave4_kernel_automation",
    "test_validate_wave4_kernel_automation",
)
QUESTBOOK_PREFIXES = (
    "build_questbook",
    "questbook_",
    "test_questbook",
    "validate_questbook",
    "validate_questbook_lifecycle",
)
RPG_PREFIXES = ("dual_vocabulary_overlay",)

ROOT_ALLOWLIST = {
    "generated": {
        "agents_mesh.min.json",
        "center_entry_map.min.json",
        "docs_thematic_index.min.json",
        "ecosystem_registry.min.json",
        "federation_supporting_inventory.min.json",
        "link_shape_hygiene.min.json",
        "mechanic_card_index.min.json",
        "owner_request_queue.min.json",
        "questbook_frontier.min.json",
        "questbook_index.min.json",
    },
    "schemas": {
        "center-entry-map.schema.json",
        "ecosystem-registry.schema.json",
        "federation-supporting-inventory.schema.json",
    },
    "config": {
        "agents_mesh.json",
        "link_shape_hygiene.json",
    },
}


def mechanic_for_name(name: str) -> str | None:
    if name.startswith(AGON_PREFIXES) or name == "agon_imposition_common.py":
        return "agon"
    if name.startswith(ANTIFRAGILITY_PREFIXES):
        return "antifragility"
    if name.startswith(EXPERIENCE_PREFIXES):
        return "experience"
    if name.startswith(METHOD_GROWTH_PREFIXES):
        return "method-growth"
    if name.startswith(QUESTBOOK_PREFIXES):
        return "questbook"
    if name.startswith(RPG_PREFIXES):
        return "rpg"
    return None


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def validate_package_dirs(selected: set[str] | None, problems: list[str]) -> None:
    for slug in MECHANIC_SLUGS:
        if selected and slug not in selected:
            continue
        package = REPO_ROOT / "mechanics" / slug
        if not package.is_dir():
            problems.append(f"missing mechanic package: {rel(package)}")
            continue
        for dirname in ARTIFACT_DIRS:
            path = package / dirname
            if path.exists() and not path.is_dir():
                problems.append(f"{rel(path)} must be a directory")


def validate_root_artifacts(selected: set[str] | None, problems: list[str]) -> None:
    for root_dir in ("schemas", "examples", "config", "generated", "scripts", "tests"):
        district = REPO_ROOT / root_dir
        if not district.is_dir():
            continue
        allowlist = ROOT_ALLOWLIST.get(root_dir, set())
        for path in district.iterdir():
            if not path.is_file() and not path.is_symlink():
                continue
            name = path.name
            if name in allowlist:
                continue
            slug = mechanic_for_name(name)
            if selected and slug not in selected:
                continue
            if path.is_symlink():
                problems.append(
                    f"{rel(path)} is a root alias; remove it and route callers to the owning mechanic path"
                )
                continue
            if slug is None:
                continue
            problems.append(
                f"{rel(path)} is mechanic-owned; keep source under mechanics/{slug}/ and update callers"
            )


def validate_mechanic_sources(selected: set[str] | None, problems: list[str]) -> None:
    for root_dir in ("schemas", "examples", "config", "generated", "scripts", "tests"):
        for slug in MECHANIC_SLUGS:
            if selected and slug not in selected:
                continue
            home = REPO_ROOT / "mechanics" / slug / root_dir
            if not home.exists():
                continue
            for path in home.iterdir():
                if path.is_dir():
                    continue
                if path.name == "README.md":
                    continue
                expected_slug = mechanic_for_name(path.name)
                if expected_slug != slug:
                    problems.append(f"{rel(path)} does not match owning mechanic {slug}")


def validate_experience_part_artifacts(selected: set[str] | None, problems: list[str]) -> None:
    if selected and "experience" not in selected:
        return
    if not EXPERIENCE_ARTIFACT_MAP.is_file():
        problems.append(f"missing Experience artifact map: {rel(EXPERIENCE_ARTIFACT_MAP)}")
        return
    data = json.loads(EXPERIENCE_ARTIFACT_MAP.read_text(encoding="utf-8"))
    if data.get("schema_version") != "aoa_experience_artifact_map_v1":
        problems.append(f"{rel(EXPERIENCE_ARTIFACT_MAP)} has invalid schema_version")
    mapped_paths = {
        str(item.get("path"))
        for item in data.get("artifacts", [])
        if isinstance(item, dict) and str(item.get("part")) != "package"
    }
    for path_ref in mapped_paths:
        path = REPO_ROOT / path_ref
        if not path.is_file():
            problems.append(f"{rel(EXPERIENCE_ARTIFACT_MAP)} maps missing artifact: {path_ref}")
    parts_root = REPO_ROOT / "mechanics" / "experience" / "parts"
    for part in parts_root.iterdir() if parts_root.is_dir() else []:
        if not part.is_dir():
            continue
        for dirname in ARTIFACT_DIRS:
            artifact_dir = part / dirname
            if not artifact_dir.exists():
                continue
            for artifact in artifact_dir.iterdir():
                if not artifact.is_file() or artifact.name == "README.md":
                    continue
                path_ref = rel(artifact)
                if path_ref not in mapped_paths:
                    problems.append(f"{path_ref} is not registered in mechanics/experience/artifact-map.json")


def validate_agon_part_artifacts(selected: set[str] | None, problems: list[str]) -> None:
    if selected and "agon" not in selected:
        return
    if not AGON_ARTIFACT_MAP.is_file():
        problems.append(f"missing Agon artifact map: {rel(AGON_ARTIFACT_MAP)}")
        return
    data = json.loads(AGON_ARTIFACT_MAP.read_text(encoding="utf-8"))
    if data.get("schema_version") != "aoa_agon_artifact_map_v1":
        problems.append(f"{rel(AGON_ARTIFACT_MAP)} has invalid schema_version")
    if data.get("mechanic") != "agon":
        problems.append(f"{rel(AGON_ARTIFACT_MAP)} must declare mechanic=agon")

    valid_kinds = {"schema", "example", "config", "generated", "script", "test"}
    valid_statuses = {
        "active-part-schema",
        "active-part-example",
        "active-part-config",
        "active-part-generated",
        "active-part-script",
        "active-part-test",
    }
    package_statuses = {"package-validator", "package-test"}
    mapped_paths: set[str] = set()
    seen_old: set[str] = set()
    seen_new: set[str] = set()
    parts = set(data.get("parts", []))
    for index, item in enumerate(data.get("artifacts", [])):
        if not isinstance(item, dict):
            problems.append(f"{rel(AGON_ARTIFACT_MAP)} artifact {index} must be an object")
            continue
        kind = str(item.get("kind", ""))
        part = str(item.get("part", ""))
        status = str(item.get("status", ""))
        old_path = str(item.get("old_path", ""))
        new_path = str(item.get("path", ""))
        if kind not in valid_kinds:
            problems.append(f"{rel(AGON_ARTIFACT_MAP)} artifact {index} has invalid kind {kind!r}")
        if old_path in seen_old:
            problems.append(f"{rel(AGON_ARTIFACT_MAP)} duplicates old_path {old_path}")
        if new_path in seen_new:
            problems.append(f"{rel(AGON_ARTIFACT_MAP)} duplicates path {new_path}")
        seen_old.add(old_path)
        seen_new.add(new_path)

        if part == "package":
            if status not in package_statuses:
                problems.append(f"{rel(AGON_ARTIFACT_MAP)} package artifact {index} has invalid status {status!r}")
            if old_path != new_path:
                problems.append(f"{rel(AGON_ARTIFACT_MAP)} package artifact path must remain stable: {new_path}")
        else:
            if part not in parts:
                problems.append(f"{rel(AGON_ARTIFACT_MAP)} artifact {index} has invalid part {part!r}")
            if status not in valid_statuses:
                problems.append(f"{rel(AGON_ARTIFACT_MAP)} artifact {index} has invalid status {status!r}")
            expected = f"mechanics/agon/parts/{part}/"
            if not new_path.startswith(expected):
                problems.append(f"{rel(AGON_ARTIFACT_MAP)} maps {new_path} outside {expected}")
            if not (REPO_ROOT / new_path).is_file():
                problems.append(f"{rel(AGON_ARTIFACT_MAP)} maps missing artifact: {new_path}")
            else:
                mapped_paths.add(new_path)
            if (REPO_ROOT / old_path).exists():
                problems.append(f"{rel(AGON_ARTIFACT_MAP)} old flat artifact still exists: {old_path}")

    agon_root = REPO_ROOT / "mechanics" / "agon"
    root_allowlist = {
        "scripts": {"validate_agon_distillation.py"},
        "tests": {"test_agon_distillation.py"},
    }
    for dirname in ARTIFACT_DIRS:
        artifact_dir = agon_root / dirname
        if artifact_dir.exists():
            for artifact in artifact_dir.iterdir():
                if not artifact.is_file() or artifact.name == "README.md":
                    continue
                if artifact.name not in root_allowlist.get(dirname, set()):
                    problems.append(f"{rel(artifact)} is flat Agon artifact; move it to a part-local home")

    parts_root = agon_root / "parts"
    for part in parts_root.iterdir() if parts_root.is_dir() else []:
        if not part.is_dir():
            continue
        for dirname in ARTIFACT_DIRS:
            artifact_dir = part / dirname
            if not artifact_dir.exists():
                continue
            for artifact in artifact_dir.iterdir():
                if not artifact.is_file() or artifact.name == "README.md":
                    continue
                path_ref = rel(artifact)
                if path_ref not in mapped_paths:
                    problems.append(f"{path_ref} is not registered in mechanics/agon/artifact-map.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mechanic", choices=MECHANIC_SLUGS, action="append")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = set(args.mechanic) if args.mechanic else None
    problems: list[str] = []
    validate_package_dirs(selected, problems)
    validate_root_artifacts(selected, problems)
    validate_mechanic_sources(selected, problems)
    validate_experience_part_artifacts(selected, problems)
    validate_agon_part_artifacts(selected, problems)
    if problems:
        print("Mechanic artifact topology validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    scope = ", ".join(sorted(selected)) if selected else "all mechanics"
    print(f"[ok] mechanic artifact topology validated: {scope}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
