#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import decision_indexes
except ModuleNotFoundError:  # pragma: no cover - package import route
    from scripts.docs_districts import decision_indexes

REPO_ROOT = Path(__file__).resolve().parents[2]
DECISIONS_DIR = REPO_ROOT / "docs" / "decisions"
README_PATH = DECISIONS_DIR / "README.md"

RECORD_NAME_RE = re.compile(r"^(?P<id>AOA-CENTER-D-(?P<number>\d{4}))-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
DECISION_ID_RE = re.compile(r"^- Decision ID:\s*(?P<id>AOA-CENTER-D-(?P<number>\d{4}))\s*$", re.MULTILINE)
STATUS_SECTION_RE = re.compile(r"^## Status\s*\n+(?P<status>[A-Z][A-Za-z0-9_-]*)\.\s*$", re.MULTILINE)
HEADING_RE = re.compile(r"^##\s+.+$", re.MULTILINE)
README_INDEX_LINK_RE = re.compile(r"\((?P<path>indexes/[a-z0-9-]+\.md)\)")

EXEMPT_FILES = {"AGENTS.md", "README.md", "TEMPLATE.md"}
STATUS_VALUES = {"accepted", "proposed", "superseded", "amended"}
REQUIRED_SECTIONS = (
    "## Status",
    "## Index Metadata",
    "## Context",
    "## Options considered",
    "## Decision",
    "## Rationale",
    "## Consequences",
    "## Source surfaces",
    "## Follow-up route",
)


def repo_rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.name


def decision_record_paths(decisions_dir: Path = DECISIONS_DIR) -> list[Path]:
    return sorted(
        path
        for path in decisions_dir.glob("*.md")
        if path.name not in EXEMPT_FILES
    )


def validate_record(path: Path) -> list[str]:
    problems: list[str] = []
    rel = repo_rel(path)
    match = RECORD_NAME_RE.fullmatch(path.name)
    if not match:
        return [f"{rel}: decision record filename must be AOA-CENTER-D-####-kebab.md"]

    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        problems.append(f"{rel}: missing final newline")
    if not text.startswith("# "):
        problems.append(f"{rel}: must start with an H1 title")

    first_section = HEADING_RE.search(text)
    metadata_block = text[: first_section.start()] if first_section else text

    decision_id_match = DECISION_ID_RE.search(metadata_block)
    if not decision_id_match:
        problems.append(f"{rel}: missing top metadata '- Decision ID: AOA-CENTER-D-####'")
    elif decision_id_match.group("id") != match.group("id"):
        problems.append(
            f"{rel}: Decision ID {decision_id_match.group('id')} does not match filename ID {match.group('id')}"
        )

    status_match = STATUS_SECTION_RE.search(text)
    if not status_match:
        problems.append(f"{rel}: missing ## Status section with one-word status")
    elif status_match.group("status").lower() not in STATUS_VALUES:
        allowed = ", ".join(sorted(STATUS_VALUES))
        problems.append(f"{rel}: unsupported status {status_match.group('status')!r}; allowed: {allowed}")

    for section in REQUIRED_SECTIONS:
        if not re.search(rf"^{re.escape(section)}\s*$", text, re.MULTILINE):
            problems.append(f"{rel}: missing section {section}")

    return problems


def validate_readme_index(records: list[Path]) -> list[str]:
    problems: list[str] = []
    text = README_PATH.read_text(encoding="utf-8")
    linked = set(README_INDEX_LINK_RE.findall(text))
    expected = {
        "indexes/by-number.md",
        "indexes/by-date.md",
        "indexes/by-surface.md",
        "indexes/by-center-facet.md",
        "indexes/by-mechanic.md",
        "indexes/by-guard.md",
    }

    for name in sorted(expected - linked):
        problems.append(f"{repo_rel(README_PATH)}: missing decision index link {name}")

    if "Decision records explain why; current surfaces define what." not in text:
        problems.append(f"{repo_rel(README_PATH)}: missing district law sentence")
    if "AOA-CENTER-D-####" not in text:
        problems.append(f"{repo_rel(README_PATH)}: missing canonical ID policy")
    return problems


def validate_all() -> list[str]:
    problems: list[str] = []
    if not DECISIONS_DIR.is_dir():
        return [f"{repo_rel(DECISIONS_DIR)}: missing decisions directory"]
    if not README_PATH.is_file():
        problems.append(f"{repo_rel(README_PATH)}: missing decisions index")
        return problems

    for path in sorted(DECISIONS_DIR.glob("*.md")):
        if path.name in EXEMPT_FILES:
            continue
        if not RECORD_NAME_RE.fullmatch(path.name):
            problems.append(f"{repo_rel(path)}: unexpected Markdown file in decisions district")

    records = decision_record_paths()
    for path in records:
        problems.extend(validate_record(path))
    problems.extend(validate_readme_index(records))
    for location, message in decision_indexes.validate_decision_index_surfaces(REPO_ROOT):
        problems.append(f"{location}: {message}")
    return problems


def main() -> int:
    problems = validate_all()
    if problems:
        print("Decision record validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] decision records validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
