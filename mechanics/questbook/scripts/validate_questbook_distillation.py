#!/usr/bin/env python3
"""Validate Questbook active parts and the legacy provenance gate."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


REPO_ROOT = _repo_root()
QUESTBOOK_ROOT = REPO_ROOT / "mechanics" / "questbook"
PARTS_ROOT = QUESTBOOK_ROOT / "parts"
LEGACY_ROOT = QUESTBOOK_ROOT / "legacy"
RAW_ROOT = LEGACY_ROOT / "raw"
REGISTRY_PATH = PARTS_ROOT / "registry.json"
PROVENANCE_PATH = QUESTBOOK_ROOT / "PROVENANCE.md"
LEGACY_INDEX_PATH = LEGACY_ROOT / "INDEX.md"
PARTS_INDEX_PATH = QUESTBOOK_ROOT / "PARTS.md"
PARTS_README_PATH = PARTS_ROOT / "README.md"
QUESTBOOK_AGENTS_PATH = QUESTBOOK_ROOT / "AGENTS.md"
QUESTS_ROOT = REPO_ROOT / "quests"
RPG_PLAYABLE_READING_PATH = PARTS_ROOT / "model-spine" / "RPG_PLAYABLE_READING.md"

PART_FILE_NAMES = ("README.md", "CONTRACT.md", "VALIDATION.md")
CONTRACT_HEADINGS = ("## Owner Boundary", "## Allowed Outputs", "## Stop-lines")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ROOT_PART_LINK_RE = re.compile(r"\]\(parts/([a-z0-9-]+)/README\.md\)")
LOCAL_PART_LINK_RE = re.compile(r"\]\(([a-z0-9-]+)/README\.md\)")
DIRECT_RAW_LINK_RE = re.compile(
    r"(?:\]\(|`)?(?:\.\./)+legacy/raw/|(?:\]\()?legacy/raw/|mechanics/questbook/legacy/raw/"
)
RPG_PLAYABLE_READING_REQUIRED_PHRASES = (
    "Questbook owns the source quest object",
    "RPG may derive a playable reading only after the quest source is already legible",
    "Do not add RPG readings to every quest file as boilerplate.",
    "RPG language does not change lifecycle state.",
    "RPG language does not close, promote, or reanchor quests.",
    "mechanics/rpg/parts/quest-campaign/PLAYABLE_OBLIGATION.md",
    "mechanics/rpg/USAGE.md",
)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path, problems: list[str]) -> dict[str, Any]:
    try:
        payload = json.loads(read(path))
    except FileNotFoundError:
        problems.append(f"{rel(path)}: missing")
        return {}
    except json.JSONDecodeError as exc:
        problems.append(f"{rel(path)}: invalid JSON: {exc}")
        return {}
    if not isinstance(payload, dict):
        problems.append(f"{rel(path)} must contain a JSON object")
        return {}
    return payload


def registry_parts(registry: dict[str, Any], problems: list[str]) -> list[dict[str, Any]]:
    parts = registry.get("parts")
    if not isinstance(parts, list) or not parts:
        problems.append(f"{rel(REGISTRY_PATH)} parts must be a non-empty list")
        return []
    valid: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, item in enumerate(parts, start=1):
        if not isinstance(item, dict):
            problems.append(f"{rel(REGISTRY_PATH)} parts[{index}] must be an object")
            continue
        slug = item.get("slug")
        if not isinstance(slug, str) or not SLUG_RE.match(slug):
            problems.append(f"{rel(REGISTRY_PATH)} parts[{index}].slug must be kebab-case")
            continue
        if slug in seen:
            problems.append(f"{rel(REGISTRY_PATH)} duplicates part slug {slug}")
            continue
        seen.add(slug)
        valid.append(item)
    return valid


def validate_registry_shape(registry: dict[str, Any], parts: list[dict[str, Any]], problems: list[str]) -> None:
    expected_strings = {
        "schema_version": "aoa_questbook_parts_registry_v1",
        "mechanic": "questbook",
        "canonical_index": "mechanics/questbook/PARTS.md",
        "parts_index": "mechanics/questbook/parts/README.md",
        "legacy_bridge": "mechanics/questbook/PROVENANCE.md",
        "legacy_index": "mechanics/questbook/legacy/INDEX.md",
    }
    for key, expected in expected_strings.items():
        if registry.get(key) != expected:
            problems.append(f"{rel(REGISTRY_PATH)} {key} must be {expected!r}")

    actual_dirs = {
        path.name
        for path in PARTS_ROOT.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    }
    registered = {str(part["slug"]) for part in parts}
    for slug in sorted(actual_dirs - registered):
        problems.append(f"{rel(PARTS_ROOT / slug)} exists but is not registered in {rel(REGISTRY_PATH)}")
    for slug in sorted(registered - actual_dirs):
        problems.append(f"{rel(REGISTRY_PATH)} registers missing part directory: {slug}")


def validate_part_registry_entry(part: dict[str, Any], problems: list[str]) -> None:
    slug = str(part["slug"])
    expected_paths = {
        "readme": f"mechanics/questbook/parts/{slug}/README.md",
        "contract": f"mechanics/questbook/parts/{slug}/CONTRACT.md",
        "validation": f"mechanics/questbook/parts/{slug}/VALIDATION.md",
    }
    for field, expected in expected_paths.items():
        if part.get(field) != expected:
            problems.append(f"{rel(REGISTRY_PATH)} {slug}.{field} must be {expected}")

    for field in ("title", "role"):
        if not isinstance(part.get(field), str) or not part.get(field):
            problems.append(f"{rel(REGISTRY_PATH)} {slug}.{field} must be a non-empty string")

    for field in ("source_surfaces", "generated_surfaces", "validation_commands"):
        value = part.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
            problems.append(f"{rel(REGISTRY_PATH)} {slug}.{field} must be a string list")

    for field in ("readme", "contract", "validation"):
        value = part.get(field)
        if isinstance(value, str) and not (REPO_ROOT / value).is_file():
            problems.append(f"{rel(REGISTRY_PATH)} {slug}.{field} points to missing file: {value}")

    for field in ("source_surfaces", "generated_surfaces"):
        for path_ref in part.get(field, []) if isinstance(part.get(field), list) else []:
            if not (REPO_ROOT / str(path_ref)).exists():
                problems.append(f"{rel(REGISTRY_PATH)} {slug}.{field} points to missing surface: {path_ref}")


def validate_part_files(part: dict[str, Any], selected: set[str] | None, problems: list[str]) -> None:
    slug = str(part["slug"])
    if selected and slug not in selected:
        return
    part_dir = PARTS_ROOT / slug
    for filename in PART_FILE_NAMES:
        path = part_dir / filename
        if not path.is_file():
            problems.append(f"{rel(path)}: missing active part surface")
            continue
        text = read(path)
        if filename == "README.md":
            if not text.startswith("# "):
                problems.append(f"{rel(path)} must start with an H1")
            if "\n## " not in text:
                problems.append(f"{rel(path)} must include at least one H2 route section")
        elif filename == "CONTRACT.md":
            for heading in CONTRACT_HEADINGS:
                if heading not in text:
                    problems.append(f"{rel(path)} must include {heading}")
        elif filename == "VALIDATION.md":
            if "AGENTS.md#validation" not in text:
                problems.append(f"{rel(path)} must route validation through Questbook AGENTS.md")

    if QUESTBOOK_AGENTS_PATH.is_file():
        agents_text = read(QUESTBOOK_AGENTS_PATH)
        commands = part.get("validation_commands", [])
        if isinstance(commands, list):
            for command in commands:
                if isinstance(command, str) and command not in agents_text:
                    problems.append(f"{rel(QUESTBOOK_AGENTS_PATH)} missing registry command: {command}")


def validate_command_targets(part: dict[str, Any], problems: list[str]) -> None:
    slug = str(part["slug"])
    commands = part.get("validation_commands", [])
    if not isinstance(commands, list):
        return
    for command in commands:
        if not isinstance(command, str):
            continue
        tokens = command.split()
        if len(tokens) < 2 or tokens[0] != "python":
            problems.append(f"{rel(REGISTRY_PATH)} {slug}.validation_commands must start with python: {command}")
            continue
        target = tokens[1]
        if target.endswith(".py") and not (REPO_ROOT / target).is_file():
            problems.append(f"{rel(REGISTRY_PATH)} {slug} command target is missing: {target}")


def validate_indexes(parts: list[dict[str, Any]], problems: list[str]) -> None:
    slugs = [str(part["slug"]) for part in parts]
    root_text = read(PARTS_INDEX_PATH)
    local_text = read(PARTS_README_PATH)
    root_links = ROOT_PART_LINK_RE.findall(root_text)
    local_links = LOCAL_PART_LINK_RE.findall(local_text)

    for path, links in ((PARTS_INDEX_PATH, root_links), (PARTS_README_PATH, local_links)):
        missing = sorted(set(slugs) - set(links))
        extra = sorted(set(links) - set(slugs))
        duplicates = sorted({slug for slug in links if links.count(slug) > 1})
        if missing:
            problems.append(f"{rel(path)} missing part links: {', '.join(missing)}")
        if extra:
            problems.append(f"{rel(path)} links unknown parts: {', '.join(extra)}")
        if duplicates:
            problems.append(f"{rel(path)} repeats part links: {', '.join(duplicates)}")

    registry_text = read(REGISTRY_PATH)
    if "Questbook Parts Index" not in local_text:
        problems.append(f"{rel(PARTS_README_PATH)} must remain the local parts index")
    if "aoa_questbook_parts_registry_v1" not in registry_text:
        problems.append(f"{rel(REGISTRY_PATH)} must declare aoa_questbook_parts_registry_v1")


def active_markdown_paths() -> list[Path]:
    paths: list[Path] = []
    for path in sorted(QUESTBOOK_ROOT.glob("*.md")):
        if path.name in {"PROVENANCE.md", "LANDING_LOG.md"}:
            continue
        paths.append(path)
    for base in (QUESTBOOK_ROOT / "docs", PARTS_ROOT):
        if base.is_dir():
            paths.extend(sorted(base.rglob("*.md")))
    return [path for path in paths if LEGACY_ROOT not in path.parents]


def questbook_markdown_paths() -> list[Path]:
    paths = sorted(QUESTBOOK_ROOT.rglob("*.md"))
    if QUESTS_ROOT.is_dir():
        paths.extend(sorted(QUESTS_ROOT.rglob("*.md")))
    return paths


def validate_validation_commands_are_centralized(problems: list[str]) -> None:
    for path in questbook_markdown_paths():
        if path == QUESTBOOK_AGENTS_PATH:
            continue
        text = read(path)
        if "```bash" in text:
            problems.append(f"{rel(path)} must route validation commands through {rel(QUESTBOOK_AGENTS_PATH)}")


def validate_no_direct_raw_links(problems: list[str]) -> None:
    for path in active_markdown_paths():
        text = read(path)
        if DIRECT_RAW_LINK_RE.search(text):
            problems.append(
                f"{rel(path)} links directly to Questbook legacy/raw; route through {rel(PROVENANCE_PATH)}"
            )


def validate_provenance_bridge(problems: list[str]) -> None:
    if not PROVENANCE_PATH.is_file():
        problems.append(f"{rel(PROVENANCE_PATH)}: missing provenance bridge")
        return
    text = read(PROVENANCE_PATH)
    normalized = " ".join(text.split())
    for phrase in (
        "only active Questbook surface",
        "legacy/INDEX.md",
        "legacy/raw/README.md",
        "Active part docs must not grow per-source inventories.",
    ):
        if phrase not in text and phrase not in normalized:
            problems.append(f"{rel(PROVENANCE_PATH)} must say: {phrase}")


def validate_legacy_index(problems: list[str]) -> None:
    if not LEGACY_INDEX_PATH.is_file():
        problems.append(f"{rel(LEGACY_INDEX_PATH)}: missing legacy index")
        return
    text = read(LEGACY_INDEX_PATH)
    raw_files = sorted(path for path in RAW_ROOT.glob("*") if path.is_file() and path.name != "README.md")
    for raw_file in raw_files:
        raw_ref = f"raw/{raw_file.name}"
        if raw_ref not in text:
            problems.append(f"{rel(LEGACY_INDEX_PATH)} does not map {raw_ref}")
    if raw_files and "parts/" not in text:
        problems.append(f"{rel(LEGACY_INDEX_PATH)} must map raw sources to active parts")


def validate_rpg_playable_reading_bridge(problems: list[str]) -> None:
    if not RPG_PLAYABLE_READING_PATH.is_file():
        problems.append(f"{rel(RPG_PLAYABLE_READING_PATH)}: missing RPG playable reading bridge")
        return
    text = read(RPG_PLAYABLE_READING_PATH)
    normalized = " ".join(text.split())
    for phrase in RPG_PLAYABLE_READING_REQUIRED_PHRASES:
        if phrase not in text and phrase not in normalized:
            problems.append(f"{rel(RPG_PLAYABLE_READING_PATH)} must say: {phrase}")


def validate(selected: set[str] | None = None) -> list[str]:
    problems: list[str] = []
    registry = load_json(REGISTRY_PATH, problems)
    if not registry:
        return problems

    parts = registry_parts(registry, problems)
    validate_registry_shape(registry, parts, problems)
    for part in parts:
        validate_part_registry_entry(part, problems)
        validate_part_files(part, selected, problems)
        validate_command_targets(part, problems)
    validate_indexes(parts, problems)
    validate_no_direct_raw_links(problems)
    validate_validation_commands_are_centralized(problems)
    validate_provenance_bridge(problems)
    validate_legacy_index(problems)
    if selected is None or "model-spine" in selected:
        validate_rpg_playable_reading_bridge(problems)
    if selected:
        registered = {str(part["slug"]) for part in parts}
        for slug in sorted(selected - registered):
            problems.append(f"unknown Questbook part selected: {slug}")
    return problems


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--part", action="append", help="validate one Questbook part slug")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = set(args.part) if args.part else None
    problems = validate(selected)
    if problems:
        print("Questbook distillation validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    scope = ", ".join(sorted(selected)) if selected else "all parts"
    print(f"[ok] Questbook distillation validated: {scope}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
