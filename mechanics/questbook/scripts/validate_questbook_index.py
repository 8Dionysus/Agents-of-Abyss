#!/usr/bin/env python3
"""Validate generated Questbook global views."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

from questbook_lifecycle_common import (
    GENERATED_FRONTIER_PATH,
    GENERATED_INDEX_PATH,
    LIFECYCLE_STATES,
    OPEN_STATES,
    QUEST_LANES,
    REPO_ROOT,
    iter_quest_sources,
    rel,
)


BUILDER_PATH = REPO_ROOT / "mechanics" / "questbook" / "scripts" / "build_questbook_index.py"


def load_builder():
    spec = importlib.util.spec_from_file_location("build_questbook_index", BUILDER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load build_questbook_index.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_json(path: Path, problems: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        problems.append(f"missing generated Questbook surface: {rel(path)}")
    except json.JSONDecodeError as exc:
        problems.append(f"{rel(path)}: invalid JSON: {exc}")
    return None


def stable_json(payload: object) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def validate_index(index: object, problems: list[str]) -> None:
    if not isinstance(index, dict):
        problems.append(f"{rel(GENERATED_INDEX_PATH)} must contain a JSON object")
        return
    if index.get("schema_version") != "aoa_questbook_index_v1":
        problems.append(f"{rel(GENERATED_INDEX_PATH)} schema_version must be aoa_questbook_index_v1")
    if index.get("source_topology") != "lane-first-lifecycle":
        problems.append(f"{rel(GENERATED_INDEX_PATH)} source_topology must be lane-first-lifecycle")
    if index.get("lanes") != list(QUEST_LANES):
        problems.append(f"{rel(GENERATED_INDEX_PATH)} lanes must match Questbook lane registry")
    if index.get("states") != list(LIFECYCLE_STATES):
        problems.append(f"{rel(GENERATED_INDEX_PATH)} states must match lifecycle registry")

    quests = index.get("quests")
    if not isinstance(quests, list):
        problems.append(f"{rel(GENERATED_INDEX_PATH)} quests must be a list")
        return
    source_paths = {item["path"] for item in iter_quest_sources()}
    indexed_paths = {
        str(item.get("path"))
        for item in quests
        if isinstance(item, dict) and item.get("path")
    }
    missing = sorted(source_paths - indexed_paths)
    extra = sorted(indexed_paths - source_paths)
    if missing:
        problems.append(f"{rel(GENERATED_INDEX_PATH)} missing source paths: {', '.join(missing)}")
    if extra:
        problems.append(f"{rel(GENERATED_INDEX_PATH)} lists unknown paths: {', '.join(extra)}")


def validate_frontier(frontier: object, index: object, problems: list[str]) -> None:
    if not isinstance(frontier, dict):
        problems.append(f"{rel(GENERATED_FRONTIER_PATH)} must contain a JSON object")
        return
    if frontier.get("schema_version") != "aoa_questbook_frontier_v1":
        problems.append(f"{rel(GENERATED_FRONTIER_PATH)} schema_version must be aoa_questbook_frontier_v1")
    if frontier.get("source_index") != "generated/questbook_index.min.json":
        problems.append(f"{rel(GENERATED_FRONTIER_PATH)} must reference generated/questbook_index.min.json")
    if frontier.get("open_states") != list(OPEN_STATES):
        problems.append(f"{rel(GENERATED_FRONTIER_PATH)} open_states must match lifecycle registry")
    if not isinstance(index, dict):
        return
    closed_paths = {
        str(item.get("path"))
        for item in index.get("quests", [])
        if isinstance(item, dict) and item.get("closed") is True
    }
    rendered = json.dumps(frontier, sort_keys=True)
    leaked_closed = sorted(path for path in closed_paths if path in rendered)
    if leaked_closed:
        problems.append(f"{rel(GENERATED_FRONTIER_PATH)} must not list closed quest paths: {', '.join(leaked_closed)}")


def validate_fresh(problems: list[str]) -> None:
    builder = load_builder()
    expected_index = builder.build_index()
    expected_frontier = builder.build_frontier(expected_index)
    current_index = GENERATED_INDEX_PATH.read_text(encoding="utf-8") if GENERATED_INDEX_PATH.exists() else ""
    current_frontier = GENERATED_FRONTIER_PATH.read_text(encoding="utf-8") if GENERATED_FRONTIER_PATH.exists() else ""
    if current_index != stable_json(expected_index):
        problems.append(f"{rel(GENERATED_INDEX_PATH)} is stale")
    if current_frontier != stable_json(expected_frontier):
        problems.append(f"{rel(GENERATED_FRONTIER_PATH)} is stale")


def main() -> int:
    problems: list[str] = []
    index = read_json(GENERATED_INDEX_PATH, problems)
    frontier = read_json(GENERATED_FRONTIER_PATH, problems)
    validate_index(index, problems)
    validate_frontier(frontier, index, problems)
    validate_fresh(problems)
    if problems:
        print("Questbook generated index validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] questbook generated indexes validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
