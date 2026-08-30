#!/usr/bin/env python3
"""Inspect or execute one exact mechanics validation route without a shell."""

from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from pathlib import Path

try:
    from validation_routes_common import DEFAULT_MANIFEST, load_manifest, normalize_repo_ref, repo_root_from, validate_manifest
except ModuleNotFoundError:  # pragma: no cover - package import route
    from scripts.mechanics_topology.validation_routes_common import (
        DEFAULT_MANIFEST,
        load_manifest,
        normalize_repo_ref,
        repo_root_from,
        validate_manifest,
    )


def display_command(argv: list[str]) -> str:
    return shlex.join(argv)


def runtime_argv(argv: list[str]) -> list[str]:
    return [sys.executable, *argv[1:]] if argv and argv[0] == "python" else argv


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=None)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--surface", help="exact repository-relative child surface")
    parser.add_argument("--list", action="store_true", help="list available surface routes")
    parser.add_argument("--show", action="store_true", help="print commands without executing them")
    parser.add_argument("--keep-going", action="store_true", help="continue after a failed command")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve() if args.repo_root else repo_root_from()
    data = load_manifest(repo_root, args.manifest)
    problems = validate_manifest(repo_root, data)
    if problems:
        raise SystemExit("invalid validation-route manifest:\n" + "\n".join(f"- {item}" for item in problems))
    routes = data["routes"]

    if args.list:
        if args.surface:
            parser.error("--list cannot be combined with --surface")
        for surface, route in routes.items():
            print(f"{surface}\t{route['owner_card']}\t{len(route['commands'])}")
        return 0
    if not args.surface:
        parser.error("--surface is required unless --list is used")

    try:
        surface = normalize_repo_ref(args.surface)
    except ValueError as exc:
        parser.error(str(exc))
    if surface not in routes:
        raise SystemExit(f"no validation route for {surface}; use --list to inspect available routes")

    route = routes[surface]
    print(f"surface: {surface}")
    print(f"owner card: {route['owner_card']}")
    if args.show:
        for argv in route["commands"]:
            print(display_command(argv))
        return 0

    failures = 0
    for argv in route["commands"]:
        print(f"$ {display_command(argv)}", flush=True)
        result = subprocess.run(runtime_argv(argv), cwd=repo_root, check=False)
        if result.returncode:
            failures += 1
            if not args.keep_going:
                return result.returncode
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
