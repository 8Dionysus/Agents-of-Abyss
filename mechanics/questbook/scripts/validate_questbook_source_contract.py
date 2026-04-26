#!/usr/bin/env python3
"""Validate Questbook source object reviewability contracts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

from questbook_lifecycle_common import (
    LIFECYCLE_STATES,
    QUESTS_DIR,
    QUEST_LANES,
    lane_for_quest_id,
    read_yaml,
    rel,
)


MARKDOWN_CONTRACT = "quest_markdown_contract_v1"
MARKDOWN_CONTRACT_MARKER = f"source_contract: {MARKDOWN_CONTRACT}"
REQUIRED_MARKDOWN_HEADINGS = (
    "## Quest",
    "## Owner Route",
    "## Next Action",
    "## Acceptance Evidence",
    "## Stop-lines",
)
REQUIRED_YAML_STRING_FIELDS = (
    "schema_version",
    "id",
    "title",
    "repo",
    "lane",
    "owner_surface",
    "kind",
    "state",
    "band",
    "difficulty",
    "risk",
    "control_mode",
    "delegate_tier",
)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
QUEST_KEY_RE = re.compile(r"^(AOA-Q(?:-[A-Z]+)?-\d+)")
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def fail(problems: list[str], path: Path, message: str) -> None:
    problems.append(f"{rel(path)}: {message}")


def first_h1(text: str) -> str | None:
    match = H1_RE.search(text)
    return match.group(1).strip() if match else None


def quest_key_from_stem(stem: str) -> str:
    match = QUEST_KEY_RE.match(stem)
    return match.group(1) if match else stem


def markdown_sections(text: str) -> dict[str, str]:
    matches = list(SECTION_RE.finditer(text))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[f"## {match.group(1).strip()}"] = text[start:end].strip()
    return sections


def validate_yaml_contract(path: Path, lane: str, state: str, payload: dict[str, Any], problems: list[str]) -> None:
    for field in REQUIRED_YAML_STRING_FIELDS:
        if not isinstance(payload.get(field), str) or not str(payload.get(field)).strip():
            fail(problems, path, f"{field} must be a non-empty string")

    quest_id = payload.get("id")
    if quest_id != path.stem:
        fail(problems, path, "id must match filename stem")
    if payload.get("schema_version") != "work_quest_v1":
        fail(problems, path, "schema_version must be work_quest_v1")
    if payload.get("lane") != lane:
        fail(problems, path, "lane must match path lane")
    if payload.get("state") != state:
        fail(problems, path, "state must match path state")
    if payload.get("public_safe") is not True:
        fail(problems, path, "public_safe must be true")

    evidence = payload.get("evidence")
    if not isinstance(evidence, list) or not any(isinstance(item, str) and item.strip() for item in evidence):
        fail(problems, path, "evidence must contain at least one public evidence string")


def validate_markdown_contract(path: Path, lane: str, state: str, text: str, problems: list[str], stats: dict[str, int]) -> None:
    title = first_h1(text)
    if title is None:
        fail(problems, path, "Markdown quest must start with an H1 title")
        return

    quest_id = path.stem
    quest_key = quest_key_from_stem(quest_id)
    if quest_key not in title:
        fail(problems, path, "H1 title must include the quest key")

    has_contract = MARKDOWN_CONTRACT_MARKER in text
    if not has_contract:
        fail(problems, path, f"missing {MARKDOWN_CONTRACT_MARKER}")
        return

    stats["contract_markdown"] += 1
    sections = markdown_sections(text)
    for heading in REQUIRED_MARKDOWN_HEADINGS:
        if heading not in sections:
            fail(problems, path, f"strict Markdown contract must include {heading}")
        elif not sections[heading]:
            fail(problems, path, f"strict Markdown contract section {heading} must not be empty")

    expected_lane = lane_for_quest_id(quest_id)
    if expected_lane != lane:
        fail(problems, path, f"quest ID routes to lane {expected_lane!r}, not {lane!r}")
    if state not in LIFECYCLE_STATES:
        fail(problems, path, f"unsupported lifecycle state {state!r}")


def validate() -> tuple[list[str], dict[str, int]]:
    problems: list[str] = []
    stats = {
        "yaml": 0,
        "contract_markdown": 0,
    }

    for lane in QUEST_LANES:
        lane_dir = QUESTS_DIR / lane
        if not lane_dir.is_dir():
            continue
        for state in LIFECYCLE_STATES:
            state_dir = lane_dir / state
            if not state_dir.is_dir():
                continue
            for path in sorted(state_dir.glob("AOA-Q-*")):
                if path.suffix == ".yaml":
                    stats["yaml"] += 1
                    try:
                        payload = read_yaml(path)
                    except Exception as exc:  # noqa: BLE001 - validation context
                        fail(problems, path, f"cannot parse YAML quest: {exc}")
                        continue
                    validate_yaml_contract(path, lane, state, payload, problems)
                elif path.suffix == ".md":
                    text = path.read_text(encoding="utf-8")
                    validate_markdown_contract(path, lane, state, text, problems, stats)
                else:
                    fail(problems, path, "quest source must be Markdown or YAML")

    return problems, stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    return parser.parse_args()


def main() -> int:
    parse_args()
    problems, stats = validate()
    if problems:
        print("Questbook source contract validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1

    print(
        "[ok] Questbook source contracts validated: "
        f"{stats['yaml']} YAML, "
        f"{stats['contract_markdown']} strict Markdown"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
