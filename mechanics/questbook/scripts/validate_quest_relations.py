#!/usr/bin/env python3
"""Validate Questbook relation sources and generated relation read model."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

from questbook_lifecycle_common import (
    GENERATED_RELATIONS_PATH,
    RELATION_TYPES,
    REPO_ROOT,
    iter_quest_sources,
    rel,
)


BUILDER_PATH = REPO_ROOT / "mechanics" / "questbook" / "scripts" / "build_questbook_index.py"
RELATION_MODEL_PATH = REPO_ROOT / "mechanics" / "questbook" / "docs" / "quest-relations.md"


def stable_json(payload: object) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def load_builder():
    spec = importlib.util.spec_from_file_location("build_questbook_index", BUILDER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load build_questbook_index.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def relations_for(item: dict[str, Any]) -> dict[str, list[str]]:
    relations = item.get("relations")
    if isinstance(relations, dict):
        return relations
    return {}


def validate_source_relations(items: list[dict[str, Any]], problems: list[str]) -> None:
    by_id: dict[str, dict[str, Any]] = {}
    for item in items:
        quest_id = str(item.get("id"))
        if quest_id in by_id:
            problems.append(f"duplicate quest id in relation sources: {quest_id}")
        by_id[quest_id] = item

    for item in items:
        quest_id = str(item.get("id"))
        path = str(item.get("path"))
        relations = relations_for(item)
        for relation_type, refs in relations.items():
            if relation_type not in RELATION_TYPES:
                problems.append(f"{path}: unknown relation type `{relation_type}`")
                continue
            if not isinstance(refs, list):
                problems.append(f"{path}: relation `{relation_type}` must be a list")
                continue
            seen: set[str] = set()
            for ref in refs:
                if not isinstance(ref, str):
                    problems.append(f"{path}: relation `{relation_type}` contains non-string ref")
                    continue
                if ref == quest_id:
                    problems.append(f"{path}: relation `{relation_type}` must not self-reference {quest_id}")
                if ref in seen:
                    problems.append(f"{path}: relation `{relation_type}` repeats {ref}")
                seen.add(ref)
                if ref not in by_id:
                    problems.append(f"{path}: relation `{relation_type}` references unknown quest id {ref}")

    for item in items:
        quest_id = str(item.get("id"))
        path = str(item.get("path"))
        for parent_id in relations_for(item).get("parent", []):
            parent = by_id.get(parent_id)
            if parent is None:
                continue
            parent_relations = relations_for(parent)
            reciprocal = set(parent_relations.get("sidequest", [])) | set(parent_relations.get("related", []))
            if quest_id not in reciprocal:
                problems.append(
                    f"{path}: parent {parent_id} must list {quest_id} as sidequest or related"
                )


def validate_generated_relation_map(items: list[dict[str, Any]], problems: list[str]) -> None:
    try:
        generated = json.loads(GENERATED_RELATIONS_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        problems.append(f"missing generated relation map: {rel(GENERATED_RELATIONS_PATH)}")
        return
    except json.JSONDecodeError as exc:
        problems.append(f"{rel(GENERATED_RELATIONS_PATH)}: invalid JSON: {exc}")
        return

    if not isinstance(generated, dict):
        problems.append(f"{rel(GENERATED_RELATIONS_PATH)} must contain a JSON object")
        return
    if generated.get("schema_version") != "aoa_questbook_relations_v1":
        problems.append(f"{rel(GENERATED_RELATIONS_PATH)} schema_version must be aoa_questbook_relations_v1")
    if generated.get("relation_types") != list(RELATION_TYPES):
        problems.append(f"{rel(GENERATED_RELATIONS_PATH)} relation_types must match Questbook relation registry")

    builder = load_builder()
    expected_index = builder.build_index()
    expected_relations = builder.build_relation_map(expected_index)
    current = GENERATED_RELATIONS_PATH.read_text(encoding="utf-8")
    if current != stable_json(expected_relations):
        problems.append(f"{rel(GENERATED_RELATIONS_PATH)} is stale")

    source_related_ids = {
        str(item.get("id"))
        for item in items
        if relations_for(item)
    }
    generated_items = generated.get("quests")
    if not isinstance(generated_items, list):
        problems.append(f"{rel(GENERATED_RELATIONS_PATH)} quests must be a list")
        return
    generated_related_ids = {
        str(item.get("id"))
        for item in generated_items
        if isinstance(item, dict) and item.get("id")
    }
    missing = sorted(source_related_ids - generated_related_ids)
    extra = sorted(generated_related_ids - source_related_ids)
    if missing:
        problems.append(f"{rel(GENERATED_RELATIONS_PATH)} missing relation-bearing quests: {', '.join(missing)}")
    if extra:
        problems.append(f"{rel(GENERATED_RELATIONS_PATH)} lists extra relation-bearing quests: {', '.join(extra)}")


def validate_model_stop_lines(problems: list[str]) -> None:
    try:
        text = RELATION_MODEL_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        problems.append(f"missing Questbook relation source doc: {rel(RELATION_MODEL_PATH)}")
        return
    required = "`sidequest` is not ownership, dependency, or automatic closure"
    if required not in text:
        problems.append(f"{rel(RELATION_MODEL_PATH)} must state the sidequest stop-line")


def main() -> int:
    problems: list[str] = []
    items = iter_quest_sources()
    validate_source_relations(items, problems)
    validate_generated_relation_map(items, problems)
    validate_model_stop_lines(problems)
    if problems:
        print("Questbook relation validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] questbook relations validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
