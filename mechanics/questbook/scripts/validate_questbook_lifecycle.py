#!/usr/bin/env python3
"""Validate Questbook lane-first lifecycle placement."""

from __future__ import annotations

import sys
from pathlib import Path

from questbook_lifecycle_common import (
    CLOSED_STATES,
    LIFECYCLE_STATES,
    QUESTS_DIR,
    QUEST_LANES,
    REPO_ROOT,
    lane_for_quest_id,
    read_yaml,
    rel,
)


def fail(problems: list[str], message: str) -> None:
    problems.append(message)


def validate_lane_dirs(problems: list[str]) -> None:
    for lane in QUEST_LANES:
        lane_dir = QUESTS_DIR / lane
        if not lane_dir.is_dir():
            fail(problems, f"{rel(lane_dir)}: missing quest lane directory")
            continue
        readme = lane_dir / "README.md"
        if not readme.is_file():
            fail(problems, f"{rel(readme)}: quest lane needs a README gate")
            continue
        text = readme.read_text(encoding="utf-8")
        for phrase in ("lifecycle subdirectories", "Do not create top-level `AOA-Q-*` aliases"):
            if phrase not in text:
                fail(problems, f"{rel(readme)} must say: {phrase}")
        has_sources = any(
            state_dir.is_dir() and any(state_dir.glob("AOA-Q-*"))
            for state_dir in lane_dir.iterdir()
            if state_dir.name != "README.md"
        )
        if has_sources:
            for heading in ("## Lane route", "## Promotion rule", "## Stop-lines"):
                if heading not in text:
                    fail(problems, f"{rel(readme)} must include active-lane heading: {heading}")


def validate_root_entries_absent(problems: list[str]) -> None:
    for path in sorted(QUESTS_DIR.glob("AOA-Q-*")):
        fail(problems, f"{rel(path)}: root quest aliases are not allowed; use quests/<lane>/<state>/{path.name}")
    old_state_dirs = [path for state in LIFECYCLE_STATES if (path := QUESTS_DIR / state).exists()]
    for path in old_state_dirs:
        fail(problems, f"{rel(path)}: root lifecycle directories are not allowed; use quests/<lane>/<state>/")


def validate_yaml(path: Path, lane: str, state: str, problems: list[str]) -> None:
    try:
        payload = read_yaml(path)
    except Exception as exc:  # noqa: BLE001 - report validation context
        fail(problems, f"{rel(path)}: cannot parse YAML quest: {exc}")
        return

    quest_id = payload.get("id")
    if quest_id != path.stem:
        fail(problems, f"{rel(path)}: id must match filename stem")
    payload_state = payload.get("state")
    if payload_state not in LIFECYCLE_STATES:
        fail(problems, f"{rel(path)}: unsupported quest state {payload_state!r}")
    elif payload_state != state:
        fail(problems, f"{rel(path)}: YAML state {payload_state!r} must match lifecycle directory {state!r}")
    payload_lane = payload.get("lane")
    if payload_lane != lane:
        fail(problems, f"{rel(path)}: YAML lane {payload_lane!r} must match quest lane {lane!r}")
    if payload.get("public_safe") is not True:
        fail(problems, f"{rel(path)}: public_safe must be true")


def validate_source_items(problems: list[str]) -> None:
    source_names: set[str] = set()
    for lane in QUEST_LANES:
        lane_dir = QUESTS_DIR / lane
        if not lane_dir.is_dir():
            continue
        for path in sorted(lane_dir.iterdir()):
            if path.name == "README.md":
                continue
            if not path.is_dir():
                fail(problems, f"{rel(path)}: quest lane children must be lifecycle directories")
                continue
            state = path.name
            if state not in LIFECYCLE_STATES:
                fail(problems, f"{rel(path)}: unsupported lifecycle directory")
                continue
            for item in sorted(path.glob("AOA-Q-*")):
                if item.suffix not in {".md", ".yaml"}:
                    fail(problems, f"{rel(item)}: quest source must be markdown or YAML")
                    continue
                if item.name in source_names:
                    fail(problems, f"{rel(item)}: duplicate quest source filename")
                source_names.add(item.name)
                expected_lane = lane_for_quest_id(item.stem)
                if expected_lane != lane:
                    fail(problems, f"{rel(item)}: quest id routes to lane {expected_lane!r}, not {lane!r}")
                if item.suffix == ".yaml":
                    validate_yaml(item, lane, state, problems)


def validate_public_index(problems: list[str]) -> None:
    questbook = (REPO_ROOT / "QUESTBOOK.md").read_text(encoding="utf-8")
    required_phrases = (
        "lane-first lifecycle directories under [`quests/`](quests/)",
        "`quests/<lane>/<state>/AOA-Q-*`",
        "Top-level `quests/AOA-Q-*` aliases are intentionally absent",
    )
    for phrase in required_phrases:
        if phrase not in questbook:
            fail(problems, f"QUESTBOOK.md must say: {phrase}")


def main() -> int:
    problems: list[str] = []
    validate_lane_dirs(problems)
    validate_root_entries_absent(problems)
    validate_source_items(problems)
    validate_public_index(problems)
    if problems:
        print("Questbook lifecycle validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] questbook lane-first lifecycle validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
