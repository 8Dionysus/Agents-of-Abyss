#!/usr/bin/env python3
"""Validate the AoA-side Experience ready quest owner-route registry."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
LANE_OWNER_ROUTES_DIR = REPO_ROOT / "mechanics" / "questbook" / "parts" / "lane-owner-routes"
ROUTE_REGISTRY_PATH = LANE_OWNER_ROUTES_DIR / "experience-ready-owner-routes.json"
ROUTE_MAP_PATH = LANE_OWNER_ROUTES_DIR / "experience-ready-owner-routes.md"
READY_DIR = REPO_ROOT / "quests" / "experience" / "ready"
OWNER_QUEUE_PATH = REPO_ROOT / "mechanics" / "owner-request-queue.json"
OWNER_DOC_PATH = REPO_ROOT / "mechanics" / "experience" / "OWNER_REQUESTS.md"
BUILDER_PATH = REPO_ROOT / "mechanics" / "questbook" / "scripts" / "build_ready_owner_routes.py"


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def load_builder():
    spec = importlib.util.spec_from_file_location("build_ready_owner_routes", BUILDER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load build_ready_owner_routes.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path: Path, problems: list[str]) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
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


def load_experience_request_ids() -> set[str]:
    payload = json.loads(OWNER_QUEUE_PATH.read_text(encoding="utf-8"))
    return {
        str(item.get("id"))
        for item in payload.get("requests", [])
        if item.get("mechanic") == "experience"
    }


def validate_registry_shape(registry: dict[str, Any], problems: list[str]) -> None:
    if registry.get("schema_version") != "aoa_ready_owner_routes_v1":
        problems.append(f"{rel(ROUTE_REGISTRY_PATH)} schema_version must be aoa_ready_owner_routes_v1")
    if registry.get("lane") != "experience":
        problems.append(f"{rel(ROUTE_REGISTRY_PATH)} lane must be experience")
    if registry.get("source_ready_dir") != "quests/experience/ready":
        problems.append(f"{rel(ROUTE_REGISTRY_PATH)} source_ready_dir must be quests/experience/ready")
    for field in ("title", "source_registry"):
        if not isinstance(registry.get(field), str) or not registry.get(field):
            problems.append(f"{rel(ROUTE_REGISTRY_PATH)} {field} must be a non-empty string")
    stop_lines = registry.get("stop_lines")
    if not isinstance(stop_lines, list) or not all(isinstance(item, str) and item for item in stop_lines):
        problems.append(f"{rel(ROUTE_REGISTRY_PATH)} stop_lines must be a non-empty string list")
    routes = registry.get("routes")
    if not isinstance(routes, list):
        problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes must be a list")
        return
    for index, item in enumerate(routes, start=1):
        if not isinstance(item, dict):
            problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}] must be an object")
            continue
        for field in ("quest_id", "quest_path", "route_note"):
            if not isinstance(item.get(field), str) or not item.get(field):
                problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}].{field} must be a non-empty string")
        owner_request_ids = item.get("owner_request_ids")
        if not isinstance(owner_request_ids, list) or not owner_request_ids:
            problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}].owner_request_ids must be a non-empty list")
        elif not all(isinstance(request_id, str) and request_id for request_id in owner_request_ids):
            problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}].owner_request_ids must contain strings")


def validate_routes(registry: dict[str, Any], problems: list[str]) -> None:
    routes = registry.get("routes")
    if not isinstance(routes, list):
        return

    owner_doc = OWNER_DOC_PATH.read_text(encoding="utf-8")
    valid_request_ids = load_experience_request_ids()
    seen_paths: dict[str, list[str]] = {}
    seen_request_ids: set[str] = set()
    seen_quest_ids: set[str] = set()

    for index, item in enumerate(routes, start=1):
        if not isinstance(item, dict):
            continue
        quest_id = str(item.get("quest_id", ""))
        quest_path = str(item.get("quest_path", ""))
        if quest_id in seen_quest_ids:
            problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}] repeats quest_id {quest_id}")
        seen_quest_ids.add(quest_id)
        if not quest_path.startswith("quests/experience/ready/AOA-Q-EXP-"):
            problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}].quest_path must point to the ready directory")
            continue
        target = (REPO_ROOT / quest_path).resolve()
        if target.parent != READY_DIR.resolve():
            problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}].quest_path escapes ready directory")
            continue
        if not target.is_file():
            problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}] missing quest target {quest_path}")
        if target.stem != quest_id:
            problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}] quest_id must match target filename stem")
        seen_paths.setdefault(rel(target), []).append(f"routes[{index}]")

        owner_request_ids = item.get("owner_request_ids")
        if not isinstance(owner_request_ids, list):
            continue
        for request_id in owner_request_ids:
            request_id = str(request_id)
            if request_id not in valid_request_ids:
                problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}] unknown Experience owner request {request_id}")
            if request_id not in owner_doc:
                problems.append(f"{rel(ROUTE_REGISTRY_PATH)} routes[{index}] {request_id} missing from {rel(OWNER_DOC_PATH)}")
            seen_request_ids.add(request_id)

    ready_paths = {rel(path) for path in READY_DIR.glob("AOA-Q-EXP-*.md")}
    mapped_paths = set(seen_paths)
    missing = sorted(ready_paths - mapped_paths)
    extra = sorted(mapped_paths - ready_paths)
    duplicate = sorted(path for path, rows in seen_paths.items() if len(rows) > 1)
    if missing:
        problems.append(f"{rel(ROUTE_REGISTRY_PATH)} missing ready quests: {', '.join(missing)}")
    if extra:
        problems.append(f"{rel(ROUTE_REGISTRY_PATH)} maps non-ready quests: {', '.join(extra)}")
    if duplicate:
        problems.append(f"{rel(ROUTE_REGISTRY_PATH)} maps quests more than once: {', '.join(duplicate)}")

    unused_request_ids = sorted(valid_request_ids - seen_request_ids)
    if unused_request_ids:
        problems.append(f"{rel(ROUTE_REGISTRY_PATH)} does not route any ready quest to: {', '.join(unused_request_ids)}")


def validate_markdown_projection(registry: dict[str, Any], problems: list[str]) -> None:
    if not ROUTE_MAP_PATH.is_file():
        problems.append(f"{rel(ROUTE_MAP_PATH)}: missing route map")
        return
    text = ROUTE_MAP_PATH.read_text(encoding="utf-8")
    for phrase in (
        "It is not owner acceptance",
        "Do not update owner-request status from a route table.",
        "Do not close a ready quest until owner-local acceptance",
        "Do not edit route rows by hand.",
    ):
        if phrase not in text:
            problems.append(f"{rel(ROUTE_MAP_PATH)} must say: {phrase}")

    builder = load_builder()
    expected = builder.render_markdown(registry, ROUTE_MAP_PATH)
    if text != expected:
        problems.append(f"{rel(ROUTE_MAP_PATH)} is stale; run mechanics/questbook/scripts/build_ready_owner_routes.py")


def validate() -> list[str]:
    problems: list[str] = []
    registry = load_json(ROUTE_REGISTRY_PATH, problems)
    if registry:
        validate_registry_shape(registry, problems)
        validate_routes(registry, problems)
        validate_markdown_projection(registry, problems)
    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("Experience ready owner-route validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] Experience ready owner routes validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
