#!/usr/bin/env python3
"""Validate configured status fields against named vocabularies."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from hygiene_common import load_config, load_json, resolve_json_path  # noqa: E402


def validate(root: Path) -> list[str]:
    config = load_config(root)
    vocabularies = config.get("status_vocabulary", {})
    checks = config.get("status_checks", [])
    problems: list[str] = []
    for check in checks:
        rel = check["file"]
        path = root / rel
        required = bool(check.get("required", False))
        if not path.exists():
            if required:
                problems.append(f"{rel}: missing required status surface")
            continue
        data = load_json(path)
        vocabulary_name = check["vocabulary"]
        allowed = set(vocabularies.get(vocabulary_name, []))
        if not allowed:
            problems.append(f"{rel}: unknown or empty vocabulary {vocabulary_name}")
            continue
        values = resolve_json_path(data, check["json_path"])
        if not values and required:
            problems.append(f"{rel}: no values found for {check['json_path']}")
        for value in values:
            if not isinstance(value, str):
                problems.append(f"{rel}: non-string status at {check['json_path']}: {value!r}")
                continue
            if value not in allowed:
                problems.append(
                    f"{rel}: status {value!r} at {check['json_path']} not in {vocabulary_name}: {sorted(allowed)}"
                )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    problems = validate(root)
    if problems:
        print("Status vocabulary validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("Status vocabularies validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
