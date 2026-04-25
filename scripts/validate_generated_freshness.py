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


def validate(root: Path) -> list[str]:
    config = load_config(root)
    problems: list[str] = []
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
        cmd = [sys.executable, str(builder), *entry.get("check_args", ["--check"])]
        result = subprocess.run(cmd, cwd=root, text=True, capture_output=True)
        if result.returncode != 0:
            detail = (result.stdout + result.stderr).strip()
            problems.append(f"{entry['output']}: freshness check failed via {entry['builder']}: {detail}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    problems = validate(root)
    if problems:
        print("Generated freshness validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("generated surfaces freshness validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
