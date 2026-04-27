#!/usr/bin/env python3
"""Validate the Recurrence mechanic package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "recurrence"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"

REQUIRED_TOP_LEVEL = (
    "AGENTS.md",
    "README.md",
    "DIRECTION.md",
    "PARTS.md",
    "OWNER_MAP.md",
    "PROVENANCE.md",
    "OWNER_REQUESTS.md",
    "ROADMAP.md",
    "LANDING_LOG.md",
    "docs/RECURRENCE_PRINCIPLE.md",
    "docs/SELF_AGENCY_CONTINUITY.md",
    "docs/COMPONENT_REFRESH_LAW.md",
    "docs/RECURRENCE_OWNER_REPO_REQUESTS.md",
    "parts/AGENTS.md",
    "parts/README.md",
)

PARTS = (
    "anchor-return",
    "continuity-window",
    "component-refresh",
    "control-plane-carry",
    "reentry-routing",
    "memory-recall",
    "scenario-choreography",
    "proof-gates",
    "runtime-return",
    "recursor-boundary",
)

PART_FILES = ("README.md", "CONTRACT.md", "VALIDATION.md")
PART_README_HEADINGS = (
    "## Use When",
    "## Do Not Use When",
    "## Route Check",
    "## Active Outputs",
    "## Next Route",
)

OWNER_REQUEST_IDS = (
    "ORQ-RECURRENCE-SDK-001",
    "ORQ-RECURRENCE-ROUTING-001",
    "ORQ-RECURRENCE-MEMO-001",
    "ORQ-RECURRENCE-AGENTS-001",
    "ORQ-RECURRENCE-PLAYBOOKS-001",
    "ORQ-RECURRENCE-EVALS-001",
    "ORQ-RECURRENCE-STATS-001",
    "ORQ-RECURRENCE-KAG-001",
    "ORQ-RECURRENCE-STACK-001",
)

OWNER_REPOS = (
    "aoa-sdk",
    "aoa-routing",
    "aoa-memo",
    "aoa-agents",
    "aoa-playbooks",
    "aoa-evals",
    "aoa-stats",
    "aoa-kag",
    "aoa-techniques",
    "aoa-skills",
    "Dionysus",
    "abyss-stack",
    "ATM10-Agent",
    "Tree-of-Sophia",
    "8Dionysus",
)

MUST_NOT_CLAIM = (
    "ambient continuity",
    "hidden memory sovereignty",
    "runtime self-healing",
    "direct runtime resume",
    "automatic recursor spawn",
)

ACTIVE_PROVENANCE_TERMS = (
    "aoa-sdk/docs/",
    "aoa-routing/docs/",
    "aoa-memo/docs/",
    "aoa-playbooks/docs/",
    "aoa-agents/docs/",
    "aoa-evals/docs/",
    "abyss-stack/",
    "ATM10-Agent/docs/",
    "Dionysus/archive/",
)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def contains_phrase(text: str, phrase: str) -> bool:
    compact_text = re.sub(r"\s+", " ", text).casefold()
    compact_phrase = re.sub(r"\s+", " ", phrase).casefold()
    return compact_phrase in compact_text


def validate_required_files(problems: list[str]) -> None:
    for item in REQUIRED_TOP_LEVEL:
        path = PACKAGE_ROOT / item
        if not path.exists():
            problems.append(f"missing required recurrence surface: {rel(path)}")
        elif path.is_file() and not read(path).endswith("\n"):
            problems.append(f"{rel(path)}: missing final newline")


def validate_card(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "README.md")
    required_phrases = (
        "Status: `landed`",
        "Center return law, drift/anchor/re-entry vocabulary",
        "Generated surfaces may reflect recurrence cards, queues, indexes, or manifests, but they do not author recurrence meaning.",
        "AoA owns recurrence law.",
    )
    for phrase in required_phrases:
        if not contains_phrase(text, phrase):
            problems.append(f"mechanics/recurrence/README.md: missing card phrase {phrase!r}")
    for stop_line in MUST_NOT_CLAIM:
        if not contains_phrase(text, stop_line):
            problems.append(f"mechanics/recurrence/README.md: missing must-not-claim {stop_line!r}")
    for owner in OWNER_REPOS[:8]:
        if owner not in text:
            problems.append(f"mechanics/recurrence/README.md: missing owner route {owner!r}")


def validate_parts(problems: list[str]) -> None:
    parts_text = read(PACKAGE_ROOT / "PARTS.md")
    parts_readme = read(PACKAGE_ROOT / "parts" / "README.md")
    parts_agents = read(PACKAGE_ROOT / "parts" / "AGENTS.md")
    for part in PARTS:
        if f"parts/{part}/README.md" not in parts_text:
            problems.append(f"mechanics/recurrence/PARTS.md: missing part link for {part}")
        if f"{part}/README.md" not in parts_readme:
            problems.append(f"mechanics/recurrence/parts/README.md: missing part link for {part}")
        part_dir = PACKAGE_ROOT / "parts" / part
        if not part_dir.is_dir():
            problems.append(f"missing recurrence part directory: {rel(part_dir)}")
            continue
        for file_name in PART_FILES:
            path = part_dir / file_name
            if not path.is_file():
                problems.append(f"missing recurrence part file: {rel(path)}")
                continue
            text = read(path)
            if not text.endswith("\n"):
                problems.append(f"{rel(path)}: missing final newline")
            if file_name == "README.md":
                for heading in PART_README_HEADINGS:
                    if heading not in text:
                        problems.append(f"{rel(path)}: missing heading {heading}")
            if file_name == "VALIDATION.md" and "Recurrence parts AGENTS" not in text:
                problems.append(f"{rel(path)}: must route executable validation to recurrence parts AGENTS")
    if "validate_recurrence_mechanic.py" not in parts_agents:
        problems.append("mechanics/recurrence/parts/AGENTS.md: missing package validator command")


def validate_owner_map(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "OWNER_MAP.md")
    for owner in OWNER_REPOS:
        if owner not in text:
            problems.append(f"mechanics/recurrence/OWNER_MAP.md: missing owner {owner!r}")
    for stop_line in (
        "A recurrence hint is not owner acceptance.",
        "A return anchor is not ambient continuity.",
        "A runtime return event is not self-healing.",
        "A recursor readiness packet is not permission to spawn.",
    ):
        if stop_line not in text:
            problems.append(f"mechanics/recurrence/OWNER_MAP.md: missing stop-line {stop_line!r}")


def validate_owner_requests(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "OWNER_REQUESTS.md")
    if "A request packet is not owner acceptance" not in text:
        problems.append("mechanics/recurrence/OWNER_REQUESTS.md: missing owner-acceptance stop-line")
    for request_id in OWNER_REQUEST_IDS:
        if request_id not in text:
            problems.append(f"mechanics/recurrence/OWNER_REQUESTS.md: missing request id {request_id}")
    compat = read(PACKAGE_ROOT / "docs" / "RECURRENCE_OWNER_REPO_REQUESTS.md")
    if "../OWNER_REQUESTS.md" not in compat:
        problems.append("mechanics/recurrence/docs/RECURRENCE_OWNER_REPO_REQUESTS.md: must route to ../OWNER_REQUESTS.md")


def validate_provenance_boundary(problems: list[str]) -> None:
    provenance = read(PACKAGE_ROOT / "PROVENANCE.md")
    for term in ACTIVE_PROVENANCE_TERMS:
        if term not in provenance:
            problems.append(f"mechanics/recurrence/PROVENANCE.md: missing provenance term {term!r}")
    allowed = {
        "mechanics/recurrence/PROVENANCE.md",
        "mechanics/recurrence/docs/RECURRENCE_OWNER_REPO_REQUESTS.md",
    }
    for path in PACKAGE_ROOT.rglob("*.md"):
        path_ref = rel(path)
        if path_ref in allowed:
            continue
        text = read(path)
        for term in ACTIVE_PROVENANCE_TERMS:
            if term in text:
                problems.append(f"{path_ref}: sibling source path {term!r} must route through PROVENANCE")


def validate_registry(problems: list[str]) -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    recurrence = next(
        (entry for entry in registry.get("mechanics", []) if entry.get("slug") == "recurrence"),
        None,
    )
    if not isinstance(recurrence, dict):
        problems.append("mechanics/registry.json: missing recurrence entry")
        return
    if recurrence.get("owner_request_doc_ref") != "mechanics/recurrence/OWNER_REQUESTS.md":
        problems.append("mechanics/registry.json: recurrence owner_request_doc_ref must point to root OWNER_REQUESTS.md")
    canonical_docs = set(recurrence.get("canonical_docs", []))
    for rel_path in (
        "mechanics/recurrence/DIRECTION.md",
        "mechanics/recurrence/PARTS.md",
        "mechanics/recurrence/OWNER_MAP.md",
        "mechanics/recurrence/PROVENANCE.md",
        "mechanics/recurrence/OWNER_REQUESTS.md",
        "mechanics/recurrence/parts/anchor-return/README.md",
        "mechanics/recurrence/parts/control-plane-carry/README.md",
        "mechanics/recurrence/parts/recursor-boundary/README.md",
    ):
        if rel_path not in canonical_docs:
            problems.append(f"mechanics/registry.json: recurrence canonical_docs missing {rel_path}")
    validation_refs = set(recurrence.get("validation_refs", []))
    if "mechanics/recurrence/scripts/validate_recurrence_mechanic.py" not in validation_refs:
        problems.append("mechanics/registry.json: recurrence validation_refs missing recurrence validator")


def validate_landing_log(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "LANDING_LOG.md")
    required_fields = ("Status:", "Owner boundary:", "Surfaces:", "Validation:", "Stop-lines:", "Next route:")
    for field in required_fields:
        if field not in text:
            problems.append(f"mechanics/recurrence/LANDING_LOG.md: missing {field}")
    if not re.search(r"^### .+", text, re.MULTILINE):
        problems.append("mechanics/recurrence/LANDING_LOG.md: missing landing entry")
    if "recurrence active-part distillation" not in text.casefold():
        problems.append("mechanics/recurrence/LANDING_LOG.md: missing active-part distillation entry")


def validate() -> list[str]:
    problems: list[str] = []
    validate_required_files(problems)
    if problems:
        return problems
    validate_card(problems)
    validate_parts(problems)
    validate_owner_map(problems)
    validate_owner_requests(problems)
    validate_provenance_boundary(problems)
    validate_registry(problems)
    validate_landing_log(problems)
    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("Recurrence mechanic validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] recurrence mechanic validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
