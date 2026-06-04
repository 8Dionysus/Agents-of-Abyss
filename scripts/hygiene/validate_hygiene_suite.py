#!/usr/bin/env python3
"""Run the link and shape hygiene suite in a stable order."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

COMMANDS = [
    ["scripts/hygiene/repair_known_link_drifts.py", "--check"],
    ["scripts/hygiene/validate_links.py"],
    ["scripts/hygiene/validate_markdown_shape.py"],
    ["scripts/hygiene/validate_status_vocabulary.py"],
    ["scripts/hygiene/build_link_shape_hygiene_index.py", "--check"],
    ["scripts/hygiene/validate_link_shape_hygiene_index.py"],
    ["scripts/hygiene/validate_generated_freshness.py"],
]


def main() -> int:
    root = Path(".").resolve()
    failures = []
    for cmd in COMMANDS:
        result = subprocess.run([sys.executable, *cmd], cwd=root, text=True, capture_output=True)
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        if result.returncode != 0:
            failures.append(" ".join(cmd))
    if failures:
        print("Link and shape hygiene suite failed:")
        for failure in failures:
            print(f" - {failure}")
        return 1
    print("Link and shape hygiene suite passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
