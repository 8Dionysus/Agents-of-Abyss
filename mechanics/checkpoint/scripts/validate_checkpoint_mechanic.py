#!/usr/bin/env python3
"""Validate the Checkpoint mechanic package."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "checkpoint"

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
    "docs/CHECKPOINT_LAW.md",
    "docs/CHECKPOINT_OWNER_BOUNDARY.md",
    "parts/README.md",
)

PARTS = (
    "session-carry",
    "review-gate",
    "return-reentry",
    "closeout-bridge",
    "runtime-export",
    "owner-handoff",
)

PART_FILES = ("README.md", "CONTRACT.md", "VALIDATION.md")
PART_README_HEADINGS = ("## Use When", "## Do Not Use When", "## Route Check", "## Active Outputs", "## Next Route")

OWNER_REQUEST_IDS = (
    "ORQ-CHECKPOINT-SDK-001",
    "ORQ-CHECKPOINT-SKILLS-001",
    "ORQ-CHECKPOINT-AGENTS-001",
    "ORQ-CHECKPOINT-MEMO-001",
    "ORQ-CHECKPOINT-PLAYBOOKS-001",
    "ORQ-CHECKPOINT-EVALS-001",
    "ORQ-CHECKPOINT-ROUTING-001",
    "ORQ-CHECKPOINT-STATS-001",
    "ORQ-CHECKPOINT-STACK-001",
    "ORQ-CHECKPOINT-DIONYSUS-001",
)

MUST_NOT_CLAIM = (
    "checkpoint implementation authority",
    "memory canon or recall sovereignty",
    "proof verdicts or stats truth",
    "runtime activation or owner acceptance",
    "hidden scheduler or autonomous self-repair",
)

OWNER_REPOS = (
    "aoa-sdk",
    "aoa-skills",
    "aoa-agents",
    "aoa-memo",
    "aoa-playbooks",
    "aoa-evals",
    "aoa-routing",
    "aoa-stats",
    "Dionysus",
    "abyss-stack",
)

RAW_HISTORY_TERMS = (
    ".aoa/session-growth",
    "checkpoint-note.jsonl",
)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_required_files(problems: list[str]) -> None:
    for item in REQUIRED_TOP_LEVEL:
        path = PACKAGE_ROOT / item
        if not path.exists():
            problems.append(f"missing required checkpoint surface: {rel(path)}")
        elif path.is_file() and not read(path).endswith("\n"):
            problems.append(f"{rel(path)}: missing final newline")


def validate_card(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "README.md")
    required_phrases = (
        "Status: `landed`",
        "Checkpoint law, vocabulary, owner map, stop-lines, and cross-owner route grammar",
        "AoA owns the law and map for checkpoint mechanics.",
        "`aoa-sdk` operates",
    )
    for phrase in required_phrases:
        if phrase not in text:
            problems.append(f"mechanics/checkpoint/README.md: missing card phrase {phrase!r}")
    for stop_line in MUST_NOT_CLAIM:
        if stop_line not in text:
            problems.append(f"mechanics/checkpoint/README.md: missing must-not-claim {stop_line!r}")
    for owner in OWNER_REPOS:
        if owner not in text:
            problems.append(f"mechanics/checkpoint/README.md: missing owner route {owner!r}")


def validate_parts(problems: list[str]) -> None:
    parts_text = read(PACKAGE_ROOT / "PARTS.md")
    for part in PARTS:
        if f"parts/{part}/README.md" not in parts_text:
            problems.append(f"mechanics/checkpoint/PARTS.md: missing part link for {part}")
        part_dir = PACKAGE_ROOT / "parts" / part
        if not part_dir.is_dir():
            problems.append(f"missing checkpoint part directory: {rel(part_dir)}")
            continue
        for file_name in PART_FILES:
            path = part_dir / file_name
            if not path.is_file():
                problems.append(f"missing checkpoint part file: {rel(path)}")
                continue
            text = read(path)
            if not text.endswith("\n"):
                problems.append(f"{rel(path)}: missing final newline")
            if file_name == "README.md":
                for heading in PART_README_HEADINGS:
                    if heading not in text:
                        problems.append(f"{rel(path)}: missing heading {heading}")
            if file_name == "VALIDATION.md" and "AGENTS.md#validation" not in text:
                problems.append(f"{rel(path)}: must route executable validation to checkpoint AGENTS")


def validate_owner_requests(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "OWNER_REQUESTS.md")
    if "A request packet is not owner acceptance" not in text:
        problems.append("mechanics/checkpoint/OWNER_REQUESTS.md: missing owner-acceptance stop-line")
    for request_id in OWNER_REQUEST_IDS:
        if request_id not in text:
            problems.append(f"mechanics/checkpoint/OWNER_REQUESTS.md: missing request id {request_id}")


def validate_raw_history_boundary(problems: list[str]) -> None:
    allowed = {
        "mechanics/checkpoint/AGENTS.md",
        "mechanics/checkpoint/PROVENANCE.md",
        "mechanics/checkpoint/docs/CHECKPOINT_OWNER_BOUNDARY.md",
    }
    for path in PACKAGE_ROOT.rglob("*.md"):
        text = read(path)
        path_ref = rel(path)
        if path_ref in allowed:
            continue
        for term in RAW_HISTORY_TERMS:
            if term in text:
                problems.append(f"{path_ref}: raw checkpoint history term {term!r} must route through PROVENANCE")


def validate_landing_log(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "LANDING_LOG.md")
    required_fields = ("Status:", "Owner boundary:", "Surfaces:", "Validation:", "Stop-lines:", "Next route:")
    for field in required_fields:
        if field not in text:
            problems.append(f"mechanics/checkpoint/LANDING_LOG.md: missing {field}")
    if not re.search(r"^### .+", text, re.MULTILINE):
        problems.append("mechanics/checkpoint/LANDING_LOG.md: missing landing entry")


def validate() -> list[str]:
    problems: list[str] = []
    validate_required_files(problems)
    if problems:
        return problems
    validate_card(problems)
    validate_parts(problems)
    validate_owner_requests(problems)
    validate_raw_history_boundary(problems)
    validate_landing_log(problems)
    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("Checkpoint mechanic validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] checkpoint mechanic validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
