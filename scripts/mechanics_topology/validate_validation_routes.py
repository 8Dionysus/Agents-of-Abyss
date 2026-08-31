#!/usr/bin/env python3
"""Validate the source manifest for routed mechanics child checks."""

from __future__ import annotations

import argparse
import re
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


DEAD_AGENT_ROUTE_RE = re.compile(
    r"(?:commands?\s+live\s+in|route(?:d|s)?\s+(?:through|to)|use)\b[^\n]*AGENTS\.md(?:#(?:validation|verify))?",
    re.IGNORECASE,
)

ACTIVE_ROUTE_ANCHOR_RE = re.compile(
    r"AGENTS\.md#(?:validation|verify)|"
    r"(?:commands?|command\s+lists?)\s+(?:live|are\s+centralized|remain)\s+in[^\n]*AGENTS|"
    r"(?:validation\s+(?:commands?|lane|matrix|route)|executable\s+validation)[^\n]*AGENTS|"
    r"AGENTS[^\n]*(?:validation\s+commands?|command\s+authority|--show)",
    re.IGNORECASE,
)


def _historical_route_surface(relative: str) -> bool:
    return (
        relative.startswith(("docs/decisions/", "generated/"))
        or "/legacy/" in relative
        or "/raw/" in relative
        or (relative.startswith("quests/") and "/done/" in relative)
        or relative == "CHANGELOG.md"
        or relative.endswith("LANDING_LOG.md")
    )


def validate_active_route_residue(repo_root: Path) -> list[str]:
    """Reject present-tense AGENTS command authority in active route surfaces."""
    problems: list[str] = []
    for path in sorted(repo_root.rglob("*.md")):
        relative = path.relative_to(repo_root).as_posix()
        if _historical_route_surface(relative) or path.name == "VALIDATION.md":
            continue
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if ACTIVE_ROUTE_ANCHOR_RE.search(line):
                problems.append(
                    f"{relative}:{line_number}: active route must not assign executable validation authority to AGENTS.md"
                )
    return problems


def validate_validation_surfaces(repo_root: Path, data: dict) -> list[str]:
    """Require manifest-keyed VALIDATION.md files to name the direct runner route."""
    problems: list[str] = []
    routes = data.get("routes", {})
    if not isinstance(routes, dict):
        return problems
    for surface, route in routes.items():
        if not surface.endswith("VALIDATION.md"):
            continue
        path = repo_root / surface
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        show_route = (
            "python scripts/mechanics_topology/run_validation_route.py "
            f"--surface {surface} --show"
        )
        execute_route = (
            "python scripts/mechanics_topology/run_validation_route.py "
            f"--surface {surface}"
        )
        if "mechanics/validation-routes.json" not in text:
            problems.append(f"{surface}: must name mechanics/validation-routes.json")
        if show_route not in text:
            problems.append(f"{surface}: missing inspect route: {show_route}")
        if execute_route not in text:
            problems.append(f"{surface}: missing execute route: {execute_route}")
        if DEAD_AGENT_ROUTE_RE.search(text) or "AGENTS.md#validation" in text or "AGENTS.md#verify" in text:
            problems.append(f"{surface}: validation route must not delegate executable authority to AGENTS.md")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=None)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()
    repo_root = args.repo_root.resolve() if args.repo_root else repo_root_from()
    data = load_manifest(repo_root, args.manifest)
    problems = validate_manifest(repo_root, data)
    problems.extend(validate_validation_surfaces(repo_root, data))
    problems.extend(validate_active_route_residue(repo_root))
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
