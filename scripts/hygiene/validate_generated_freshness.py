#!/usr/bin/env python3
"""Run configured generated-surface freshness checks."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from hygiene_common import load_config  # noqa: E402


def validate(root: Path, *, run_builders: bool = True) -> list[str]:
    config = load_config(root)
    problems: list[str] = []
    checks: dict[tuple[str, ...], tuple[str, list[str]]] = {}
    for entry in config.get("generated_freshness", []):
        output = root / entry["output"]
        builder = root / entry["builder"]
        required = bool(entry.get("required", False))
        if not output.exists() or not builder.exists():
            if required:
                missing = []
                if not output.exists():
                    missing.append(entry["output"])
                if not builder.exists():
                    missing.append(entry["builder"])
                problems.append(f"required generated freshness input missing: {', '.join(missing)}")
            continue
        command = (sys.executable, str(builder), *entry.get("check_args", ["--check"]))
        if command not in checks:
            checks[command] = (entry["builder"], [])
        checks[command][1].append(entry["output"])

    if not run_builders:
        return problems

    for command, (builder, outputs) in checks.items():
        result = subprocess.run(command, cwd=root, text=True, capture_output=True)
        if result.returncode != 0:
            detail = (result.stdout + result.stderr).strip()
            problems.append(f"{', '.join(outputs)}: freshness check failed via {builder}: {detail}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--inputs-only",
        action="store_true",
        help="Validate configured required outputs and builders without rerunning builders.",
    )
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    problems = validate(root, run_builders=not args.inputs_only)
    if problems:
        print("Generated freshness validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("generated surfaces freshness validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
