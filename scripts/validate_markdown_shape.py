#!/usr/bin/env python3
"""Validate protected Markdown files for readable shape."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from hygiene_common import load_config  # noqa: E402


def has_heading(lines: list[str], prefix: str) -> bool:
    return any(line.startswith(prefix) for line in lines)


def code_fences_balanced(lines: list[str]) -> bool:
    count = 0
    for line in lines:
        if line.strip().startswith("```"):
            count += 1
    return count % 2 == 0


def check_file(root: Path, target: dict[str, object], defaults: dict[str, object]) -> list[str]:
    rel = str(target["path"])
    path = root / rel
    required = bool(target.get("required", False))
    problems: list[str] = []
    if not path.exists():
        if required:
            problems.append(f"{rel}: missing required Markdown surface")
        return problems
    if not path.is_file():
        problems.append(f"{rel}: expected a file")
        return problems
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    min_lines = int(target.get("min_lines", defaults.get("default_min_lines", 1)))
    max_line_length = int(target.get("max_line_length", defaults.get("default_max_line_length", 900)))
    if len(lines) < min_lines:
        problems.append(f"{rel}: only {len(lines)} lines, expected at least {min_lines}")
    if bool(target.get("require_final_newline", defaults.get("default_require_final_newline", True))) and not text.endswith("\n"):
        problems.append(f"{rel}: missing final newline")
    if bool(target.get("require_h1", defaults.get("default_require_h1", False))) and not has_heading(lines, "# "):
        problems.append(f"{rel}: missing top-level heading")
    if bool(target.get("require_h2", defaults.get("default_require_h2", False))) and not has_heading(lines, "## "):
        problems.append(f"{rel}: missing second-level heading")
    if not code_fences_balanced(lines):
        problems.append(f"{rel}: unbalanced fenced code blocks")
    for number, line in enumerate(lines, start=1):
        if len(line) > max_line_length:
            problems.append(f"{rel}:{number}: line length {len(line)} exceeds {max_line_length}")
    return problems


def configured_targets(config: dict[str, object]) -> list[dict[str, object]]:
    shape = config.get("markdown_shape", {})
    targets = list(shape.get("targets", [])) + list(shape.get("directory_readme_gates", []))
    deduped: dict[str, dict[str, object]] = {}
    for target in targets:
        if isinstance(target, dict) and "path" in target:
            deduped[str(target["path"])] = target
    return [deduped[key] for key in sorted(deduped)]


def validate(root: Path, explicit_targets: list[str] | None = None) -> list[str]:
    config = load_config(root)
    shape = config.get("markdown_shape", {})
    targets = configured_targets(config)
    if explicit_targets:
        targets = [{"path": item, "required": True, "min_lines": 1} for item in explicit_targets]
    problems: list[str] = []
    for target in targets:
        problems.extend(check_file(root, target, shape))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--target", action="append", help="specific Markdown file to check; may be repeated")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    problems = validate(root, args.target)
    if problems:
        print("Markdown shape validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("Markdown shape validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
