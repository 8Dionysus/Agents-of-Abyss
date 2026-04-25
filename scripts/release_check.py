#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

COMMANDS = [
    ("check docs thematic cleanup plan", [sys.executable, "scripts/plan_docs_thematic_cleanup.py", "--check"]),
    ("validate docs thematic districts", [sys.executable, "scripts/validate_docs_thematic_districts.py"]),
    ("validate docs migration map", [sys.executable, "scripts/validate_docs_migration_map.py"]),
    ("check docs thematic index", [sys.executable, "scripts/build_docs_thematic_index.py", "--check"]),
    ("validate docs thematic index", [sys.executable, "scripts/validate_docs_thematic_index.py"]),
    ("validate markdown shape", [sys.executable, "scripts/validate_markdown_shape.py"]),
    ("validate entry surface sync", [sys.executable, "scripts/validate_entry_surface_sync.py"]),
    ("check center entry map", [sys.executable, "scripts/build_center_entry_map.py", "--check"]),
    ("validate center entry map", [sys.executable, "scripts/validate_center_entry_map.py"]),
    ("validate mechanics topology", [sys.executable, "scripts/validate_mechanics_topology.py"]),
    ("check mechanic card index", [sys.executable, "scripts/build_mechanic_card_index.py", "--check"]),
    ("validate mechanic card index", [sys.executable, "scripts/validate_mechanic_card_index.py"]),
    ("check owner request queue", [sys.executable, "scripts/build_owner_request_queue.py", "--check"]),
    ("validate generated owner request queue", [sys.executable, "scripts/validate_generated_owner_request_queue.py"]),
    ("validate mechanic landing logs", [sys.executable, "scripts/validate_mechanic_landing_logs.py"]),
    ("validate ecosystem", [sys.executable, "scripts/validate_ecosystem.py"]),
    ("run tests", [sys.executable, "-m", "pytest", "-q"]),
]


def run_step(label: str, command: list[str]) -> int:
    print(f"[run] {label}: {subprocess.list2cmdline(command)}", flush=True)
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        env=os.environ.copy(),
        check=False,
    )
    if completed.returncode != 0:
        print(f"[error] {label} failed with exit code {completed.returncode}", flush=True)
        return completed.returncode
    print(f"[ok] {label}", flush=True)
    return 0


def main() -> int:
    for label, command in COMMANDS:
        exit_code = run_step(label, command)
        if exit_code != 0:
            return exit_code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
