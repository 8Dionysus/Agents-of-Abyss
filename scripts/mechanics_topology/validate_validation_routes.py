#!/usr/bin/env python3
"""Validate the source manifest for routed mechanics child checks."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from validation_routes_common import DEFAULT_MANIFEST, load_manifest, repo_root_from, validate_manifest
except ModuleNotFoundError:  # pragma: no cover - package import route
    from scripts.mechanics_topology.validation_routes_common import (
        DEFAULT_MANIFEST,
        load_manifest,
        repo_root_from,
        validate_manifest,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=None)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()
    repo_root = args.repo_root.resolve() if args.repo_root else repo_root_from()
    data = load_manifest(repo_root, args.manifest)
    problems = validate_manifest(repo_root, data)
    if problems:
        print("Mechanics validation-route manifest failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    routes = data["routes"]
    command_count = sum(len(route["commands"]) for route in routes.values())
    print(f"[ok] validated {len(routes)} mechanics validation routes and {command_count} commands")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
