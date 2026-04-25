#!/usr/bin/env python3
"""Validate the compact Wave E hygiene index."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from hygiene_common import GENERATED_PATH, load_json  # noqa: E402

REQUIRED_KEYS = {
    "schema",
    "wave",
    "purpose",
    "protocol_ref",
    "index_ref",
    "config_ref",
    "guardrails",
    "validation_commands",
}


def validate(root: Path) -> list[str]:
    path = root / GENERATED_PATH
    problems: list[str] = []
    if not path.exists():
        return [f"{GENERATED_PATH}: missing"]
    data = load_json(path)
    if not isinstance(data, dict):
        return [f"{GENERATED_PATH}: expected JSON object"]
    missing = REQUIRED_KEYS - set(data)
    for key in sorted(missing):
        problems.append(f"{GENERATED_PATH}: missing key {key}")
    if data.get("schema") != "aoa.link_shape_hygiene_index.v1":
        problems.append(f"{GENERATED_PATH}: unexpected schema {data.get('schema')!r}")
    if data.get("wave") != "E":
        problems.append(f"{GENERATED_PATH}: unexpected wave {data.get('wave')!r}")
    guardrails = data.get("guardrails")
    if not isinstance(guardrails, list) or not guardrails:
        problems.append(f"{GENERATED_PATH}: guardrails must be a non-empty list")
    else:
        seen: set[str] = set()
        for index, guard in enumerate(guardrails):
            if not isinstance(guard, dict):
                problems.append(f"{GENERATED_PATH}: guardrails[{index}] must be object")
                continue
            gid = guard.get("id")
            if not isinstance(gid, str) or not gid:
                problems.append(f"{GENERATED_PATH}: guardrails[{index}] missing id")
            elif gid in seen:
                problems.append(f"{GENERATED_PATH}: duplicate guardrail id {gid}")
            seen.add(gid)
            if guard.get("status") != "active":
                problems.append(f"{GENERATED_PATH}: guardrail {gid} must be active")
    for rel in (data.get("protocol_ref"), data.get("index_ref"), data.get("config_ref")):
        if isinstance(rel, str) and not (root / rel).exists():
            problems.append(f"{GENERATED_PATH}: referenced source missing: {rel}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    problems = validate(root)
    if problems:
        print("Generated hygiene index validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("generated hygiene index validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
