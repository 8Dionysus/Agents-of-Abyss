#!/usr/bin/env python3
"""Build generated Questbook global views from lane-first quest sources."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from questbook_lifecycle_common import (
    GENERATED_FRONTIER_PATH,
    GENERATED_INDEX_PATH,
    LIFECYCLE_STATES,
    OPEN_STATES,
    QUEST_LANES,
    iter_quest_sources,
)


def stable_json(payload: object) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def build_index() -> dict[str, object]:
    quests = iter_quest_sources()
    by_lane = Counter(str(item["lane"]) for item in quests)
    by_state = Counter(str(item["state"]) for item in quests)
    return {
        "schema_version": "aoa_questbook_index_v1",
        "source": "quests/",
        "source_topology": "lane-first-lifecycle",
        "lanes": list(QUEST_LANES),
        "states": list(LIFECYCLE_STATES),
        "counts": {
            "total": len(quests),
            "by_lane": {lane: by_lane.get(lane, 0) for lane in QUEST_LANES},
            "by_state": {state: by_state.get(state, 0) for state in LIFECYCLE_STATES},
        },
        "quests": sorted(quests, key=lambda item: (str(item["lane"]), str(item["state"]), str(item["id"]))),
    }


def build_frontier(index: dict[str, object]) -> dict[str, object]:
    entries = index.get("quests", [])
    if not isinstance(entries, list):
        entries = []
    lanes: dict[str, dict[str, list[dict[str, object]]]] = {
        lane: {state: [] for state in OPEN_STATES}
        for lane in QUEST_LANES
    }
    for item in entries:
        if not isinstance(item, dict):
            continue
        lane = str(item.get("lane"))
        state = str(item.get("state"))
        if lane not in lanes or state not in lanes[lane]:
            continue
        lanes[lane][state].append(
            {
                "id": item.get("id"),
                "title": item.get("title"),
                "path": item.get("path"),
                "format": item.get("format"),
                "band": item.get("band"),
            }
        )

    nonempty_lanes: dict[str, dict[str, list[dict[str, object]]]] = {}
    for lane, states in lanes.items():
        nonempty_states = {state: items for state, items in states.items() if items}
        if nonempty_states:
            nonempty_lanes[lane] = nonempty_states

    return {
        "schema_version": "aoa_questbook_frontier_v1",
        "source_index": "generated/questbook_index.min.json",
        "open_states": list(OPEN_STATES),
        "lanes": nonempty_lanes,
    }


def write_or_check(path: Path, payload: dict[str, object], check: bool, problems: list[str]) -> None:
    rendered = stable_json(payload)
    if check:
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current != rendered:
            problems.append(f"{path.as_posix()} is stale; run mechanics/questbook/scripts/build_questbook_index.py")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    index = build_index()
    frontier = build_frontier(index)
    problems: list[str] = []
    write_or_check(GENERATED_INDEX_PATH, index, args.check, problems)
    write_or_check(GENERATED_FRONTIER_PATH, frontier, args.check, problems)
    if problems:
        print("Questbook generated index check failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    action = "checked" if args.check else "built"
    print(f"[ok] questbook generated indexes {action}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
