#!/usr/bin/env python3
"""Validate shape of human-facing Markdown entrypoints.

This guardrail catches the failure mode where civic docs keep their semantic
content but collapse into a few extremely long lines. It is intentionally narrow:
it protects key entry surfaces and district README gates without pretending to
lint the whole repository.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

DEFAULT_TARGETS = {
    "README.md": {"min_lines": 90, "max_line_length": 700},
    "CHARTER.md": {"min_lines": 45, "max_line_length": 700},
    "ECOSYSTEM_MAP.md": {"min_lines": 50, "max_line_length": 700},
    "CONTRIBUTING.md": {"min_lines": 80, "max_line_length": 700},
    "GLOSSARY.md": {"min_lines": 180, "max_line_length": 700},
    "QUESTBOOK.md": {"min_lines": 30, "max_line_length": 700},
    "FRAGILITY_BLACKLIST.md": {"min_lines": 10, "max_line_length": 700},
    "ECOSYSTEM_AUDIT_INDEX.md": {"min_lines": 90, "max_line_length": 750},
    ".github/PULL_REQUEST_TEMPLATE.md": {"min_lines": 60, "max_line_length": 700},
    "docs/README.md": {"min_lines": 100, "max_line_length": 700},
    "docs/MECHANICS.md": {"min_lines": 15, "max_line_length": 700},
    "docs/START_HERE_ROUTE_CONTRACT.md": {"min_lines": 120, "max_line_length": 700},
    "mechanics/README.md": {"min_lines": 200, "max_line_length": 700},
    "mechanics/AGENTS.md": {"min_lines": 40, "max_line_length": 700},
    "mechanics/agon/LANDING_LOG.md": {"min_lines": 180, "max_line_length": 700},
    "mechanics/experience/LANDING_LOG.md": {"min_lines": 250, "max_line_length": 700},
    "mechanics/agon/README.md": {"min_lines": 25, "max_line_length": 700},
    "mechanics/experience/README.md": {"min_lines": 25, "max_line_length": 700},
    "mechanics/method-growth/README.md": {"min_lines": 20, "max_line_length": 700},
    "mechanics/recurrence/README.md": {"min_lines": 20, "max_line_length": 700},
    "mechanics/antifragility/README.md": {"min_lines": 20, "max_line_length": 700},
    "mechanics/questbook/README.md": {"min_lines": 20, "max_line_length": 700},
    "mechanics/rpg/README.md": {"min_lines": 20, "max_line_length": 700},
    "mechanics/tos-bridge/README.md": {"min_lines": 20, "max_line_length": 700},
    "mechanics/release-support/README.md": {"min_lines": 20, "max_line_length": 700},
    "docs/ROOT_SURFACE_LAW.md": {"min_lines": 70, "max_line_length": 700},
    "docs/THEMATIC_DISTRICT_PROTOCOL.md": {"min_lines": 30, "max_line_length": 700},
    "docs/CURRENT_SURFACE_INDEX.md": {"min_lines": 25, "max_line_length": 700},
    "docs/agent-lane/README.md": {"min_lines": 20, "max_line_length": 700},
    "docs/audits/README.md": {"min_lines": 18, "max_line_length": 700},
    "docs/decisions/README.md": {"min_lines": 20, "max_line_length": 700},
    "docs/postmortems/README.md": {"min_lines": 20, "max_line_length": 700},
    "docs/traces/README.md": {"min_lines": 20, "max_line_length": 700},
    "docs/agon/README.md": {"min_lines": 20, "max_line_length": 700},
    "docs/experience/README.md": {"min_lines": 20, "max_line_length": 700},
    "docs/legacy/README.md": {"min_lines": 20, "max_line_length": 700},
    "docs/registry/README.md": {"min_lines": 20, "max_line_length": 700},
    "docs/landings/README.md": {"min_lines": 14, "max_line_length": 700},
    "generated/README.md": {"min_lines": 25, "max_line_length": 700},
    "scripts/README.md": {"min_lines": 30, "max_line_length": 700},
    "schemas/README.md": {"min_lines": 30, "max_line_length": 700},
    "tests/README.md": {"min_lines": 20, "max_line_length": 700},
    "config/README.md": {"min_lines": 15, "max_line_length": 700},
    "examples/README.md": {"min_lines": 15, "max_line_length": 700},
    "manifests/README.md": {"min_lines": 20, "max_line_length": 700},
    "manifests/recurrence/README.md": {"min_lines": 20, "max_line_length": 700},
    "quests/README.md": {"min_lines": 30, "max_line_length": 700},
}


def has_heading(lines: list[str], level: str) -> bool:
    return any(line.startswith(level) for line in lines)


def check_file(root: Path, rel: str, min_lines: int, max_line_length: int) -> list[str]:
    path = root / rel
    problems: list[str] = []

    if not path.exists():
        problems.append(f"{rel}: missing")
        return problems

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if len(lines) < min_lines:
        problems.append(f"{rel}: only {len(lines)} lines, expected at least {min_lines}")

    if not text.endswith("\n"):
        problems.append(f"{rel}: missing final newline")

    if rel != ".github/PULL_REQUEST_TEMPLATE.md" and not has_heading(lines, "# "):
        problems.append(f"{rel}: missing top-level heading")

    if rel.endswith(".md") and rel != ".github/PULL_REQUEST_TEMPLATE.md" and not has_heading(lines, "## "):
        problems.append(f"{rel}: missing second-level headings")

    for number, line in enumerate(lines, start=1):
        if len(line) > max_line_length:
            problems.append(
                f"{rel}:{number}: line length {len(line)} exceeds {max_line_length}"
            )

    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo-root",
        default=".",
        help="repository root to inspect",
    )
    parser.add_argument(
        "--target",
        action="append",
        help="specific Markdown file to check; may be passed multiple times",
    )
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    targets = args.target or list(DEFAULT_TARGETS)

    problems: list[str] = []
    for rel in targets:
        spec = DEFAULT_TARGETS.get(rel, {"min_lines": 1, "max_line_length": 700})
        problems.extend(check_file(root, rel, spec["min_lines"], spec["max_line_length"]))

    if problems:
        print("Markdown shape validation failed:")
        for problem in problems:
            print(f"  - {problem}")
        return 1

    print(f"Markdown shape validation passed for {len(targets)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
