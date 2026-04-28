#!/usr/bin/env python3
"""Validate the root mechanics package topology and card contract."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
CANONICAL_SLUGS = (
    "method-growth",
    "distillation",
    "growth-cycle",
    "recurrence",
    "checkpoint",
    "experience",
    "agon",
    "antifragility",
    "questbook",
    "rpg",
    "boundary-bridge",
    "release-support",
)
REQUIRED_PACKAGE_FILES = ("AGENTS.md", "README.md", "ROADMAP.md", "LANDING_LOG.md")
REQUIRED_LOG_FIELDS = ("Status:", "Owner boundary:", "Surfaces:", "Validation:", "Stop-lines:", "Next route:")
TEXT_SUFFIXES = (".md", ".py", ".json", ".yaml", ".yml", ".toml", ".txt")
HISTORICAL_REFERENCE_PREFIXES = (
    "docs/landings/",
    "docs/audits/",
    "docs/postmortems/",
    "docs/traces/",
)
HISTORICAL_REFERENCE_PATHS = {
    "CHANGELOG.md",
    "config/link_shape_hygiene.json",
    "docs/agent-lane/AGENTS_ROOT_REFERENCE.md",
}
OLD_ACTIVE_PATTERNS = (
    r"(?:^|/)docs/AGON_[A-Z0-9_]+\.md",
    r"(?<!mechanics/experience/)docs/EXPERIENCE_[A-Z0-9_]+\.md",
    r"(?<!mechanics/rpg/)docs/RPG_[A-Z0-9_]+\.md",
    r"(?<!mechanics/antifragility/)docs/(?:ANTIFRAGILITY|VIA_NEGATIVA)[A-Z0-9_]*\.md",
    r"(?<!mechanics/antifragility/)docs/(?:ANTI_AUTHORITY_RULES|ONE_IN_ONE_OUT)\.md",
    r"(?<!mechanics/recurrence/)docs/(?:RECURRENCE_PRINCIPLE|SELF_AGENCY_CONTINUITY|COMPONENT_REFRESH_LAW)\.md",
    r"(?<!mechanics/method-growth/)docs/(?:ROOTLINE|METHOD_SPINE|REVIEWABLE_GROWTH_REFINERY|CANDIDATE_LINEAGE_CROSSWALK|OWNER_LANDING_AND_PRUNING)\.md",
    r"(?<!mechanics/questbook/)docs/(?:QUESTBOOK_MODEL|QUESTBOOK_FIRST_WAVE)\.md",
    r"(?<!mechanics/boundary-bridge/)docs/(?:COUNTERPART_BRIDGE|WITNESS_COMPOST|TOS_GROWTH_SUPPORT|TOS_TEMPLATE_SUPPORT|TOS_LINEAGE_PILOT_SUPPORT|TOS_SOIL_PREP_SUPPORT)\.md",
    r"(?<!mechanics/release-support/)docs/(?:PUBLIC_SUPPORT_POSTURE|FEDERATION_RELEASE_PROTOCOL|RELEASING|DIRECTION_SURFACES)\.md",
)


def load_registry() -> dict[str, Any]:
    with REGISTRY_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def require_path(rel: str, problems: list[str], label: str = "path") -> None:
    if not rel or not (REPO_ROOT / rel).exists():
        problems.append(f"{label} missing: {rel}")


def is_historical_ref_path(path: Path) -> bool:
    rel = path.relative_to(REPO_ROOT).as_posix()
    return rel in HISTORICAL_REFERENCE_PATHS or rel.startswith(HISTORICAL_REFERENCE_PREFIXES)


def iter_text_files() -> list[Path]:
    paths: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(REPO_ROOT).as_posix()
        if rel.startswith(
            (
                ".git/",
                ".wave_a_backups/",
                ".wave_b_backups/",
                ".wave_c_backups/",
                ".wave_d_backups/",
            )
        ):
            continue
        if path.suffix in TEXT_SUFFIXES:
            paths.append(path)
    return paths


def validate_registry_shape(registry: dict[str, Any], selected: set[str] | None) -> list[str]:
    problems: list[str] = []
    if registry.get("schema_version") != "aoa_mechanics_registry_v1":
        problems.append("mechanics/registry.json: schema_version must be aoa_mechanics_registry_v1")
    require_path(str(registry.get("authority_ref", "")), problems, "authority_ref")
    require_path(str(registry.get("agents_ref", "")), problems, "agents_ref")
    if not str(registry.get("card_contract_ref", "")).strip():
        problems.append("mechanics/registry.json: card_contract_ref is required")
    require_path(str(registry.get("generated_card_index_ref", "")), problems, "generated_card_index_ref")
    for key in ("owner_request_protocol_ref", "owner_request_queue_ref", "owner_request_source_ref", "generated_owner_request_queue_ref"):
        require_path(str(registry.get(key, "")), problems, key)
    owner_request_status_vocabulary = registry.get("owner_request_status_vocabulary")
    if not isinstance(owner_request_status_vocabulary, dict) or not owner_request_status_vocabulary:
        problems.append("mechanics/registry.json: owner_request_status_vocabulary must be a non-empty object")
    required_headings = registry.get("mechanic_card_required_headings")
    if not isinstance(required_headings, list) or not required_headings:
        problems.append("mechanics/registry.json: mechanic_card_required_headings must be a non-empty list")
    status_vocabulary = registry.get("status_vocabulary")
    if not isinstance(status_vocabulary, dict) or not status_vocabulary:
        problems.append("mechanics/registry.json: status_vocabulary must be a non-empty object")
    mechanics = registry.get("mechanics")
    if not isinstance(mechanics, list):
        return ["mechanics/registry.json: mechanics must be a list"]
    slugs = [str(item.get("slug")) for item in mechanics if isinstance(item, dict)]
    if tuple(slugs) != CANONICAL_SLUGS:
        problems.append("mechanics/registry.json: canonical slug order mismatch: " + ", ".join(slugs))
    for entry in mechanics:
        if not isinstance(entry, dict):
            problems.append("mechanics/registry.json: mechanic entry is not an object")
            continue
        slug = str(entry.get("slug", ""))
        if selected and slug not in selected:
            continue
        package_path = str(entry.get("package_path", ""))
        if package_path != f"mechanics/{slug}":
            problems.append(f"{slug}: package_path must be mechanics/{slug}")
        package_dir = REPO_ROOT / package_path
        if not package_dir.is_dir():
            problems.append(f"{slug}: package directory missing: {package_path}")
            continue
        for file_name in REQUIRED_PACKAGE_FILES:
            require_path(f"{package_path}/{file_name}", problems, f"{slug} package file")
        require_path(f"{package_path}/docs", problems, f"{slug} docs dir")
        for key in ("entry_ref", "roadmap_ref", "landing_log_ref", "agents_ref", "docs_path", "owner_request_doc_ref"):
            require_path(str(entry.get(key, "")), problems, f"{slug} {key}")
        for key in ("owner_boundary", "title", "status"):
            if not str(entry.get(key, "")).strip():
                problems.append(f"{slug}: {key} is empty")
        if isinstance(status_vocabulary, dict) and entry.get("status") not in status_vocabulary:
            problems.append(f"{slug}: status must be one of registry status_vocabulary")
        owner_request_ids = entry.get("owner_request_ids")
        if not isinstance(owner_request_ids, list) or not owner_request_ids:
            problems.append(f"{slug}: owner_request_ids must be a non-empty list")
        for key in ("canonical_docs", "validation_refs", "must_not_claim"):
            values = entry.get(key)
            if not isinstance(values, list) or not values:
                problems.append(f"{slug}: {key} must be a non-empty list")
                continue
            if key != "must_not_claim":
                for rel in values:
                    require_path(str(rel), problems, f"{slug} {key}")
        card = entry.get("card")
        if not isinstance(card, dict):
            problems.append(f"{slug}: card must be an object")
        else:
            for key in ("trigger", "center_owns", "stronger_owner_split", "inputs", "outputs", "next_route"):
                value = card.get(key)
                if value in (None, "", []):
                    problems.append(f"{slug}: card.{key} is empty")
    return problems


def validate_landing_log_fields(registry: dict[str, Any], selected: set[str] | None) -> list[str]:
    problems: list[str] = []
    for entry in registry.get("mechanics", []):
        slug = str(entry.get("slug", ""))
        if selected and slug not in selected:
            continue
        rel = str(entry.get("landing_log_ref", ""))
        path = REPO_ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            problems.append(f"{rel}: missing final newline")
        if "### " not in text:
            problems.append(f"{rel}: missing at least one landing entry")
            continue
        for field in REQUIRED_LOG_FIELDS:
            if field not in text:
                problems.append(f"{rel}: missing required field {field}")
    return problems


def validate_compatibility_routes() -> list[str]:
    problems: list[str] = []
    mechanics_route = REPO_ROOT / "docs" / "MECHANICS.md"
    if mechanics_route.exists() and "mechanics/README.md" not in mechanics_route.read_text(encoding="utf-8"):
        problems.append("docs/MECHANICS.md: must route to mechanics/README.md")
    root_blacklist = REPO_ROOT / "FRAGILITY_BLACKLIST.md"
    if root_blacklist.exists() and "mechanics/antifragility/FRAGILITY_BLACKLIST.md" not in root_blacklist.read_text(encoding="utf-8"):
        problems.append("FRAGILITY_BLACKLIST.md: must route to antifragility source")
    questbook = REPO_ROOT / "QUESTBOOK.md"
    if questbook.exists():
        questbook_text = questbook.read_text(encoding="utf-8")
        if "mechanics/questbook/parts/model-spine/README.md" not in questbook_text:
            problems.append("QUESTBOOK.md: must route quest lifecycle law to mechanics/questbook")
    if not (REPO_ROOT / "quests").is_dir():
        problems.append("quests/: quest item store missing")
    return problems


def validate_no_flat_sources() -> list[str]:
    problems: list[str] = []
    for pattern in ("AGON_*.md", "EXPERIENCE_*.md", "RPG_*.md"):
        for path in (REPO_ROOT / "docs").glob(pattern):
            problems.append(f"flat mechanic source remains: {path.relative_to(REPO_ROOT)}")
    return problems


def validate_no_active_old_refs() -> list[str]:
    problems: list[str] = []
    regexes = [re.compile(pattern) for pattern in OLD_ACTIVE_PATTERNS]
    for path in iter_text_files():
        if is_historical_ref_path(path):
            continue
        rel = path.relative_to(REPO_ROOT).as_posix()
        if rel.startswith(("mechanics/", "generated/")):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for regex in regexes:
            match = regex.search(text)
            if match:
                problems.append(f"{rel}: active old mechanics ref {match.group(0)!r}")
                break
    return problems


def run_card_validator(selected: set[str] | None) -> list[str]:
    validator_path = REPO_ROOT / "scripts" / "validate_mechanic_readme_cards.py"
    spec = importlib.util.spec_from_file_location("validate_mechanic_readme_cards", validator_path)
    if spec is None or spec.loader is None:
        return ["cannot load scripts/validate_mechanic_readme_cards.py"]
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    registry = load_registry()
    required_headings = tuple(registry.get("mechanic_card_required_headings") or module.DEFAULT_HEADINGS)
    problems: list[str] = []
    for entry in registry.get("mechanics", []):
        slug = str(entry.get("slug", ""))
        if selected and slug not in selected:
            continue
        problems.extend(module.validate_card(entry, required_headings))
    return problems



def run_owner_request_validator(selected: set[str] | None) -> list[str]:
    validator_path = REPO_ROOT / "scripts" / "validate_owner_request_queue.py"
    if not validator_path.exists():
        return ["scripts/validate_owner_request_queue.py missing"]
    spec = importlib.util.spec_from_file_location("validate_owner_request_queue", validator_path)
    if spec is None or spec.loader is None:
        return ["cannot load scripts/validate_owner_request_queue.py"]
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_queue(selected)


def run_owner_request_doc_validator(selected: set[str] | None) -> list[str]:
    validator_path = REPO_ROOT / "scripts" / "validate_owner_request_docs.py"
    if not validator_path.exists():
        return ["scripts/validate_owner_request_docs.py missing"]
    spec = importlib.util.spec_from_file_location("validate_owner_request_docs", validator_path)
    if spec is None or spec.loader is None:
        return ["cannot load scripts/validate_owner_request_docs.py"]
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_docs(selected)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate root mechanics topology.")
    parser.add_argument(
        "--mechanic",
        choices=CANONICAL_SLUGS,
        action="append",
        help="Mechanic slug to validate; may be passed more than once. Defaults to all.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = set(args.mechanic) if args.mechanic else None
    registry = load_registry()
    problems: list[str] = []
    problems.extend(validate_registry_shape(registry, selected))
    problems.extend(validate_landing_log_fields(registry, selected))
    problems.extend(run_card_validator(selected))
    problems.extend(run_owner_request_validator(selected))
    problems.extend(run_owner_request_doc_validator(selected))
    if selected is None:
        problems.extend(validate_compatibility_routes())
        problems.extend(validate_no_flat_sources())
        problems.extend(validate_no_active_old_refs())
    if problems:
        print("Mechanics topology validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    scope = ", ".join(sorted(selected)) if selected else "all mechanics"
    print(f"[ok] validated mechanics topology: {scope}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
