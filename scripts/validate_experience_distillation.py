#!/usr/bin/env python3
"""Validate Experience active parts and the single provenance bridge."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
EXPERIENCE_ROOT = REPO_ROOT / "mechanics" / "experience"
LEGACY_ROOT = EXPERIENCE_ROOT / "legacy"
RAW_ROOT = LEGACY_ROOT / "raw"
PARTS_ROOT = EXPERIENCE_ROOT / "parts"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
PROVENANCE_PATH = EXPERIENCE_ROOT / "PROVENANCE.md"

PART_SLUGS = (
    "capture-kernel",
    "certification-proof",
    "adoption-federation",
    "governance-polis",
    "release-deployment",
    "office-operations",
    "service-mesh",
    "continuity-context",
    "runtime-boundary",
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
    "raw/README.md",
)

PART_SURFACES = (
    "README.md",
    "CONTRACT.md",
    "VALIDATION.md",
)

STALE_ACTIVE_REFS = (
    "mechanics/experience/docs/EXPERIENCE_",
    "experience/docs/EXPERIENCE_",
    "docs/EXPERIENCE_",
    "EXPERIENCE_OWNER_REPO_REQUESTS.md",
)

ACTIVE_TEXT_SUFFIXES = (".md", ".py", ".json", ".yaml", ".yml", ".toml", ".txt")
ACTIVE_ARCHIVE_LOAD_PATTERNS = (
    "legacy/",
    "Legacy raw",
    "Primary raw provenance",
    "raw provenance",
    "raw source",
    "raw-source",
)
ACTIVE_ARCHIVE_FILENAME_RE = re.compile(r"EXPERIENCE_[A-Z0-9_]+\.md")


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def load_registry() -> dict[str, object]:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require_file(path: Path, problems: list[str]) -> None:
    if not path.is_file():
        problems.append(f"missing file: {rel(path)}")
        return
    text = read(path)
    if not text.endswith("\n"):
        problems.append(f"{rel(path)}: missing final newline")


def active_text_files() -> list[Path]:
    files: list[Path] = []
    for path in EXPERIENCE_ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in ACTIVE_TEXT_SUFFIXES:
            continue
        relative = path.relative_to(EXPERIENCE_ROOT).as_posix()
        if relative.startswith("legacy/raw/"):
            continue
        files.append(path)
    return files


def active_markdown_files_without_bridge() -> list[Path]:
    files: list[Path] = []
    for path in EXPERIENCE_ROOT.rglob("*.md"):
        if not path.is_file():
            continue
        relative = path.relative_to(EXPERIENCE_ROOT).as_posix()
        if relative.startswith("legacy/") or path == PROVENANCE_PATH:
            continue
        files.append(path)
    return files


def validate_root_surfaces(problems: list[str]) -> None:
    for name in ROOT_SURFACES:
        require_file(EXPERIENCE_ROOT / name, problems)
    for name in LEGACY_SURFACES:
        require_file(LEGACY_ROOT / name, problems)
    require_file(EXPERIENCE_ROOT / "docs" / "AGENTS.md", problems)
    require_file(EXPERIENCE_ROOT / "docs" / "README.md", problems)
    require_file(PARTS_ROOT / "AGENTS.md", problems)
    require_file(PARTS_ROOT / "README.md", problems)

    direction = read(EXPERIENCE_ROOT / "DIRECTION.md") if (EXPERIENCE_ROOT / "DIRECTION.md").exists() else ""
    parts = read(EXPERIENCE_ROOT / "PARTS.md") if (EXPERIENCE_ROOT / "PARTS.md").exists() else ""
    readme = read(EXPERIENCE_ROOT / "README.md") if (EXPERIENCE_ROOT / "README.md").exists() else ""
    for slug in PART_SLUGS:
        if slug not in direction:
            problems.append(f"mechanics/experience/DIRECTION.md: missing part slug {slug}")
        if slug not in parts:
            problems.append(f"mechanics/experience/PARTS.md: missing part slug {slug}")
        if slug not in readme:
            problems.append(f"mechanics/experience/README.md: missing part slug {slug}")
    provenance = read(PROVENANCE_PATH) if PROVENANCE_PATH.exists() else ""
    for needle in ("legacy/INDEX.md", "legacy/DISTILLATION_LOG.md", "legacy/raw/README.md"):
        if needle not in provenance:
            problems.append(f"mechanics/experience/PROVENANCE.md: missing archive route {needle}")
    if "only active Experience surface" not in provenance:
        problems.append("mechanics/experience/PROVENANCE.md: must declare itself the only active archive bridge")
    if "PROVENANCE.md" not in readme and "PROVENANCE" not in readme:
        problems.append("mechanics/experience/README.md: missing provenance bridge route")


def validate_parts(selected: set[str] | None, problems: list[str]) -> None:
    slugs = [slug for slug in PART_SLUGS if selected is None or slug in selected]
    for slug in slugs:
        part_dir = PARTS_ROOT / slug
        if not part_dir.is_dir():
            problems.append(f"missing part directory: {rel(part_dir)}")
            continue
        for name in PART_SURFACES:
            require_file(part_dir / name, problems)
        readme_path = part_dir / "README.md"
        contract_path = part_dir / "CONTRACT.md"
        validation_path = part_dir / "VALIDATION.md"
        readme = read(readme_path) if readme_path.exists() else ""
        contract = read(contract_path) if contract_path.exists() else ""
        validation = read(validation_path) if validation_path.exists() else ""
        if "## Legacy raw sources" in readme or "## Primary raw provenance" in readme:
            problems.append(f"{rel(readme_path)}: active part README carries archival source inventory")
        if "## Must not claim" not in contract:
            problems.append(f"{rel(contract_path)}: missing explicit stop-line section")
        if f"validate_experience_distillation.py --part {slug}" not in validation:
            problems.append(f"{rel(validation_path)}: missing targeted distillation command")


def validate_raw_sources(problems: list[str]) -> None:
    raw_docs = sorted(RAW_ROOT.glob("EXPERIENCE_*.md"))
    if len(raw_docs) < 140:
        problems.append(f"{rel(RAW_ROOT)}: expected at least 140 raw Experience sources, found {len(raw_docs)}")
    old_docs = sorted((EXPERIENCE_ROOT / "docs").glob("EXPERIENCE_*.md"))
    if old_docs:
        for path in old_docs[:10]:
            problems.append(f"active docs directory still contains raw Experience source: {rel(path)}")
        if len(old_docs) > 10:
            problems.append(f"active docs directory has {len(old_docs) - 10} more raw Experience sources")

    index_path = LEGACY_ROOT / "INDEX.md"
    index = read(index_path) if index_path.exists() else ""
    for raw in raw_docs:
        if raw.name not in index:
            problems.append(f"{rel(index_path)}: missing raw source {raw.name}")
    indexed = set(re.findall(r"`(EXPERIENCE_[A-Z0-9_]+\.md)`", index))
    existing = {path.name for path in raw_docs}
    stale = sorted(indexed - existing)
    for name in stale[:10]:
        problems.append(f"{rel(index_path)}: indexed raw source missing on disk: {name}")
    if len(stale) > 10:
        problems.append(f"{rel(index_path)}: {len(stale) - 10} more stale raw index entries")


def validate_no_stale_active_refs(problems: list[str]) -> None:
    for path in active_text_files():
        text = read(path)
        for needle in STALE_ACTIVE_REFS:
            if needle in text:
                problems.append(f"{rel(path)}: stale active Experience ref {needle!r}")
                break


def validate_active_docs_are_lean(problems: list[str]) -> None:
    for path in active_markdown_files_without_bridge():
        text = read(path)
        for pattern in ACTIVE_ARCHIVE_LOAD_PATTERNS:
            if pattern in text:
                problems.append(f"{rel(path)}: active doc carries archive-load marker {pattern!r}")
                break
        if ACTIVE_ARCHIVE_FILENAME_RE.search(text):
            problems.append(f"{rel(path)}: active doc names archived Experience source files")


def validate_registry(problems: list[str]) -> None:
    registry = load_registry()
    experience = next(
        (item for item in registry.get("mechanics", []) if isinstance(item, dict) and item.get("slug") == "experience"),
        None,
    )
    if not isinstance(experience, dict):
        problems.append("mechanics/registry.json: missing experience entry")
        return
    if experience.get("owner_request_doc_ref") != "mechanics/experience/OWNER_REQUESTS.md":
        problems.append("mechanics/registry.json: experience owner_request_doc_ref must point to OWNER_REQUESTS.md")
    canonical = experience.get("canonical_docs")
    if not isinstance(canonical, list) or not canonical:
        problems.append("mechanics/registry.json: experience canonical_docs must be non-empty")
        canonical = []
    for ref in canonical:
        ref_text = str(ref)
        if ref_text.startswith("mechanics/experience/legacy/"):
            problems.append(f"mechanics/registry.json: archive file listed as canonical active doc: {ref_text}")
        if not (REPO_ROOT / ref_text).exists():
            problems.append(f"mechanics/registry.json: canonical doc missing: {ref_text}")
    if "mechanics/experience/PROVENANCE.md" not in canonical:
        problems.append("mechanics/registry.json: experience canonical_docs must include PROVENANCE.md bridge")
    if "scripts/validate_experience_distillation.py" not in experience.get("validation_refs", []):
        problems.append("mechanics/registry.json: missing validate_experience_distillation.py validation ref")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--part", choices=PART_SLUGS, action="append", help="Validate a specific Experience part.")
    return parser.parse_args()


def validate(selected: set[str] | None = None) -> list[str]:
    problems: list[str] = []
    validate_root_surfaces(problems)
    validate_parts(selected, problems)
    validate_raw_sources(problems)
    validate_no_stale_active_refs(problems)
    validate_active_docs_are_lean(problems)
    validate_registry(problems)
    return problems


def main() -> int:
    args = parse_args()
    selected = set(args.part) if args.part else None
    problems = validate(selected)
    if problems:
        print("Experience distillation validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    scope = ", ".join(sorted(selected)) if selected else "all parts"
    print(f"[ok] Experience distillation validated: {scope}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
