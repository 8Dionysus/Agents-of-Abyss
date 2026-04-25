#!/usr/bin/env python3
"""Validate the generated owner-request queue capsule shape."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATED_PATH = REPO_ROOT / "generated" / "owner_request_queue.min.json"
BUILDER_PATH = REPO_ROOT / "scripts" / "build_owner_request_queue.py"


def load_builder():
    spec = importlib.util.spec_from_file_location("build_owner_request_queue", BUILDER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load scripts/build_owner_request_queue.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_payload(payload: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    if payload.get("schema_version") != "aoa_generated_owner_request_queue_v1":
        problems.append("generated owner queue: schema_version mismatch")
    if payload.get("generated_from") != ["mechanics/owner-request-queue.json", "mechanics/registry.json"]:
        problems.append("generated owner queue: generated_from mismatch")
    requests = payload.get("requests")
    if not isinstance(requests, list) or not requests:
        problems.append("generated owner queue: requests must be a non-empty list")
        return problems
    if payload.get("request_count") != len(requests):
        problems.append("generated owner queue: request_count mismatch")
    if payload.get("mechanic_count") != len({item.get("mechanic") for item in requests}):
        problems.append("generated owner queue: mechanic_count mismatch")
    for item in requests:
        for field in ("id", "mechanic", "owner_repo", "queue_status", "priority", "slice", "owner_request_doc_ref", "required_owner_landing", "proof_route", "stop_line"):
            if item.get(field) in (None, "", []):
                problems.append(f"{item.get('id', '<missing id>')}: generated missing {field}")
    return problems


def main() -> int:
    if not GENERATED_PATH.exists():
        print("generated/owner_request_queue.min.json is missing")
        return 1
    builder = load_builder()
    expected = builder.dumps_min(builder.build_payload())
    actual = GENERATED_PATH.read_text(encoding="utf-8")
    problems: list[str] = []
    if actual != expected:
        problems.append("generated/owner_request_queue.min.json is stale")
    try:
        payload = json.loads(actual)
    except json.JSONDecodeError as exc:
        print(f"generated owner queue is invalid JSON: {exc}")
        return 1
    problems.extend(validate_payload(payload))
    if problems:
        print("Generated owner request queue validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] generated owner request queue validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
