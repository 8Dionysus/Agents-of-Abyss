#!/usr/bin/env python3
"""Validate Agon active route surfaces and source-doc bridge."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


REPO_ROOT = _repo_root()
AGON_ROOT = REPO_ROOT / "mechanics" / "agon"
PARTS_ROOT = AGON_ROOT / "parts"
LEGACY_ROOT = AGON_ROOT / "legacy"
RAW_ROOT = LEGACY_ROOT / "raw"
ARTIFACT_MAP_PATH = AGON_ROOT / "artifact-map.json"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"

PART_SLUGS = (
    "imposition-readiness",
    "lawful-move-grammar",
    "owner-binding",
    "gate-routing",
    "trial-handoff",
    "recurrence-adapter",
    "packet-arena",
    "duel-kernel",
    "verdict-retention-rank",
    "epistemic-kag",
    "sophian-threshold",
    "compatibility-bridges",
)

ROOT_SURFACES = (
    "README.md",
    "DIRECTION.md",
    "PARTS.md",
    "PROVENANCE.md",
    "LANDING_LOG.md",
    "ROADMAP.md",
    "OWNER_REQUESTS.md",
    "AGENTS.md",
)

LEGACY_SURFACES = (
    "AGENTS.md",
    "README.md",
    "INDEX.md",
    "DISTILLATION_LOG.md",
    "artifacts/README.md",
    "raw/README.md",
)

PART_SURFACES = ("README.md", "CONTRACT.md", "VALIDATION.md")
PART_ARTIFACT_DIRS = ("schemas", "examples", "config", "generated", "scripts", "tests")
PART_ARTIFACT_KINDS = {"schema", "example", "config", "generated", "script", "test"}
PART_ARTIFACT_STATUSES = {
    "active-part-schema",
    "active-part-example",
    "active-part-config",
    "active-part-generated",
    "active-part-script",
    "active-part-test",
}
PACKAGE_ARTIFACT_STATUSES = {"package-validator", "package-test"}

ACTIVE_TEXT_SURFACES = (
    "README.md",
    "DIRECTION.md",
    "PARTS.md",
    "OWNER_REQUESTS.md",
    "AGENTS.md",
    "parts/README.md",
    "parts/AGENTS.md",
)

ACTIVE_ROUTE_POLLUTION_PATTERNS = (
    "low-context",
    "small enough",
    "legacy/raw",
    "Legacy raw",
    "raw source",
    "raw sources",
    "archival sources consulted",
    "wave",
    "Wave",
)

ACTIVE_PART_ARTIFACT_POLLUTION_PATTERNS = (
    re.compile(r"\bwave\b", re.IGNORECASE),
    re.compile(r"legacy/raw", re.IGNORECASE),
    re.compile(r"AGON_WAVE", re.IGNORECASE),
    re.compile(r"PRE_AGON", re.IGNORECASE),
)

OWNER_REQUEST_IDS = (
    "ORQ-AGON-PLAYBOOKS-001",
    "ORQ-AGON-EVALS-001",
    "ORQ-AGON-MEMO-001",
    "ORQ-AGON-STATS-001",
    "ORQ-AGON-ROUTING-001",
    "ORQ-AGON-AGENTS-001",
    "ORQ-AGON-STACK-001",
    "ORQ-AGON-KAG-001",
    "ORQ-AGON-TOS-001",
)


def read_text(rel: str) -> str:
    return (AGON_ROOT / rel).read_text(encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def validate_artifact_map(problems: list[str]) -> None:
    if not ARTIFACT_MAP_PATH.is_file():
        problems.append(f"missing Agon artifact map: {rel(ARTIFACT_MAP_PATH)}")
        return

    data = json.loads(ARTIFACT_MAP_PATH.read_text(encoding="utf-8"))
    if data.get("schema_version") != "aoa_agon_artifact_map_v1":
        problems.append(f"{rel(ARTIFACT_MAP_PATH)}: invalid schema_version")
    if data.get("mechanic") != "agon":
        problems.append(f"{rel(ARTIFACT_MAP_PATH)}: mechanic must be agon")
    if tuple(data.get("parts", ())) != PART_SLUGS:
        problems.append(f"{rel(ARTIFACT_MAP_PATH)}: parts must match active Agon part order")

    listed_paths: set[str] = set()
    seen_old: set[str] = set()
    seen_new: set[str] = set()
    artifacts = data.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        problems.append(f"{rel(ARTIFACT_MAP_PATH)}: artifacts must be a non-empty list")
        artifacts = []

    for index, item in enumerate(artifacts):
        if not isinstance(item, dict):
            problems.append(f"{rel(ARTIFACT_MAP_PATH)}: artifact {index} must be an object")
            continue
        kind = str(item.get("kind", ""))
        part = str(item.get("part", ""))
        status = str(item.get("status", ""))
        old_path = str(item.get("old_path", ""))
        new_path = str(item.get("path", ""))

        if kind not in PART_ARTIFACT_KINDS:
            problems.append(f"{rel(ARTIFACT_MAP_PATH)}: artifact {index} has invalid kind {kind!r}")
        if old_path in seen_old:
            problems.append(f"{rel(ARTIFACT_MAP_PATH)}: duplicate old_path {old_path}")
        if new_path in seen_new:
            problems.append(f"{rel(ARTIFACT_MAP_PATH)}: duplicate path {new_path}")
        seen_old.add(old_path)
        seen_new.add(new_path)

        if part == "package":
            if status not in PACKAGE_ARTIFACT_STATUSES:
                problems.append(f"{rel(ARTIFACT_MAP_PATH)}: package artifact {index} has invalid status {status!r}")
            if old_path != new_path:
                problems.append(f"{rel(ARTIFACT_MAP_PATH)}: package artifact path changed: {new_path}")
        else:
            if part not in PART_SLUGS:
                problems.append(f"{rel(ARTIFACT_MAP_PATH)}: artifact {index} has invalid part {part!r}")
            if status not in PART_ARTIFACT_STATUSES:
                problems.append(f"{rel(ARTIFACT_MAP_PATH)}: artifact {index} has invalid status {status!r}")
            expected_prefix = f"mechanics/agon/parts/{part}/"
            if not new_path.startswith(expected_prefix):
                problems.append(f"{rel(ARTIFACT_MAP_PATH)}: {new_path} must live under {expected_prefix}")
            if not (REPO_ROOT / new_path).is_file():
                problems.append(f"{rel(ARTIFACT_MAP_PATH)}: mapped artifact missing: {new_path}")
            else:
                listed_paths.add(new_path)
            if (REPO_ROOT / old_path).exists():
                problems.append(f"{rel(ARTIFACT_MAP_PATH)}: old flat artifact still exists: {old_path}")

    for part in PART_SLUGS:
        part_dir = PARTS_ROOT / part
        for dirname in PART_ARTIFACT_DIRS:
            artifact_dir = part_dir / dirname
            if not artifact_dir.exists():
                continue
            for path in artifact_dir.iterdir():
                if not path.is_file() or path.name == "README.md":
                    continue
                path_ref = rel(path)
                if path_ref not in listed_paths:
                    problems.append(f"{path_ref}: part artifact is not listed in artifact-map.json")


def validate_active_part_artifact_hygiene(problems: list[str]) -> None:
    """Keep active part files free of legacy source names and wave-era routing."""
    for path in sorted(PARTS_ROOT.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in ACTIVE_PART_ARTIFACT_POLLUTION_PATTERNS:
            if pattern.search(text):
                problems.append(f"{rel(path)}: active part artifact pollution pattern: {pattern.pattern}")


def validate() -> list[str]:
    problems: list[str] = []

    for rel in ROOT_SURFACES:
        path = AGON_ROOT / rel
        if not path.is_file():
            problems.append(f"missing Agon root surface: {rel}")
        elif not path.read_text(encoding="utf-8").endswith("\n"):
            problems.append(f"{rel}: missing final newline")

    for rel in LEGACY_SURFACES:
        path = LEGACY_ROOT / rel
        if not path.is_file():
            problems.append(f"missing Agon legacy surface: legacy/{rel}")
        elif not path.read_text(encoding="utf-8").endswith("\n"):
            problems.append(f"legacy/{rel}: missing final newline")

    for slug in PART_SLUGS:
        part_dir = PARTS_ROOT / slug
        if not part_dir.is_dir():
            problems.append(f"missing Agon part: {slug}")
            continue
        for rel in PART_SURFACES:
            path = part_dir / rel
            if not path.is_file():
                problems.append(f"{slug}: missing {rel}")
            elif not path.read_text(encoding="utf-8").endswith("\n"):
                problems.append(f"{slug}/{rel}: missing final newline")

    readme = read_text("README.md")
    direction = read_text("DIRECTION.md")
    parts = read_text("PARTS.md")
    provenance = read_text("PROVENANCE.md")
    landing_log = read_text("LANDING_LOG.md")
    owner_requests = read_text("OWNER_REQUESTS.md")
    compatibility = read_text("docs/README.md")
    legacy_index = (LEGACY_ROOT / "INDEX.md").read_text(encoding="utf-8")

    for rel in ("DIRECTION.md", "PARTS.md", "OWNER_REQUESTS.md", "PROVENANCE.md"):
        if f"({rel})" not in readme:
            problems.append(f"README.md: missing active route link to {rel}")

    for slug in PART_SLUGS:
        if f"parts/{slug}/README.md" not in readme:
            problems.append(f"README.md: missing part route for {slug}")
        if f"parts/{slug}/README.md" not in parts:
            problems.append(f"PARTS.md: missing part route for {slug}")
        if f"`{slug}`" not in direction:
            problems.append(f"DIRECTION.md: missing active order entry for {slug}")
        if f"`{slug}`" not in provenance:
            problems.append(f"PROVENANCE.md: missing source-doc map entry for {slug}")

    for rid in OWNER_REQUEST_IDS:
        if rid not in owner_requests:
            problems.append(f"OWNER_REQUESTS.md: missing request id {rid}")

    for rel in ("../DIRECTION.md", "../PARTS.md", "../PROVENANCE.md", "../OWNER_REQUESTS.md"):
        if rel not in compatibility:
            problems.append(f"docs/README.md: must route to {rel}")

    docs_files = sorted(path.name for path in (AGON_ROOT / "docs").glob("*.md"))
    if docs_files != ["AGENTS.md", "README.md"]:
        problems.append("docs/: must contain only AGENTS.md and README.md compatibility surfaces")

    raw_docs = sorted(path.name for path in RAW_ROOT.glob("*.md") if path.name != "README.md")
    if "PRE_AGON_BASELINE.md" not in raw_docs:
        problems.append("legacy/raw/: missing PRE_AGON_BASELINE.md")
    if not any(name.startswith("AGON_") for name in raw_docs):
        problems.append("legacy/raw/: missing AGON_* raw sources")
    for name in raw_docs:
        path = RAW_ROOT / name
        if not path.read_text(encoding="utf-8").endswith("\n"):
            problems.append(f"legacy/raw/{name}: missing final newline")
        if f"`{name}`" not in legacy_index:
            problems.append(f"legacy/INDEX.md: missing raw source `{name}`")

    for phrase in ("legacy/INDEX.md", "legacy/raw/", "docs/`: compatibility route"):
        if phrase not in provenance:
            problems.append(f"PROVENANCE.md: missing legacy route phrase {phrase!r}")
    if "Agon legacy raw provenance district" not in landing_log:
        problems.append("LANDING_LOG.md: missing Agon legacy raw provenance district entry")
    if "Agon part artifact homes" not in landing_log:
        problems.append("LANDING_LOG.md: missing Agon part artifact homes entry")

    validate_artifact_map(problems)
    validate_active_part_artifact_hygiene(problems)

    active_texts = {
        rel: (AGON_ROOT / rel).read_text(encoding="utf-8")
        for rel in ACTIVE_TEXT_SURFACES
        if (AGON_ROOT / rel).exists()
    }
    for slug in PART_SLUGS:
        for rel in PART_SURFACES:
            path = PARTS_ROOT / slug / rel
            if path.exists():
                active_texts[f"parts/{slug}/{rel}"] = path.read_text(encoding="utf-8")

    for rel, text in active_texts.items():
        for pattern in ACTIVE_ROUTE_POLLUTION_PATTERNS:
            if pattern in text:
                problems.append(f"{rel}: active route pollution pattern: {pattern}")

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    agon_entry = next((entry for entry in registry.get("mechanics", []) if entry.get("slug") == "agon"), None)
    if not agon_entry:
        problems.append("mechanics/registry.json: missing Agon entry")
    else:
        if agon_entry.get("owner_request_doc_ref") != "mechanics/agon/OWNER_REQUESTS.md":
            problems.append("mechanics/registry.json: Agon owner_request_doc_ref must point to OWNER_REQUESTS.md")
        refs = set(agon_entry.get("validation_refs", []))
        if "mechanics/agon/scripts/validate_agon_distillation.py" not in refs:
            problems.append("mechanics/registry.json: missing Agon distillation validator ref")
        canonical_docs = set(agon_entry.get("canonical_docs", []))
        for rel in ("DIRECTION.md", "PARTS.md", "PROVENANCE.md", "OWNER_REQUESTS.md"):
            expected = f"mechanics/agon/{rel}"
            if expected not in canonical_docs:
                problems.append(f"mechanics/registry.json: missing canonical doc {expected}")
        for slug in PART_SLUGS:
            expected = f"mechanics/agon/parts/{slug}/README.md"
            if expected not in canonical_docs:
                problems.append(f"mechanics/registry.json: missing canonical part {expected}")

    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("Agon distillation validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] Agon distillation validated: active route and parts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
