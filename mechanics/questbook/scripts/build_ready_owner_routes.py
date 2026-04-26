#!/usr/bin/env python3
"""Build lane ready owner-route Markdown projections from route registries."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
LANE_OWNER_ROUTES_DIR = REPO_ROOT / "mechanics" / "questbook" / "parts" / "lane-owner-routes"
DEFAULT_REGISTRY = LANE_OWNER_ROUTES_DIR / "experience-ready-owner-routes.json"
DEFAULT_OUTPUT = LANE_OWNER_ROUTES_DIR / "experience-ready-owner-routes.md"


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def load_registry(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{rel(path)} must contain a JSON object")
    return payload


def title_for_lane(lane: str) -> str:
    return lane.replace("-", " ").title()


def link_from_output(output: Path, target_ref: str) -> str:
    target = REPO_ROOT / target_ref
    return Path(os.path.relpath(target, output.parent)).as_posix()


def render_markdown(registry: dict[str, Any], output: Path = DEFAULT_OUTPUT) -> str:
    lane = str(registry.get("lane", "experience"))
    title = str(registry.get("title") or f"{title_for_lane(lane)} Ready Owner Routes")
    source_registry = str(registry.get("source_registry") or rel(DEFAULT_REGISTRY))
    ready_dir = str(registry.get("source_ready_dir") or f"quests/{lane}/ready")
    routes = registry.get("routes")
    if not isinstance(routes, list):
        routes = []
    stop_lines = registry.get("stop_lines")
    if not isinstance(stop_lines, list):
        stop_lines = []

    lines = [
        f"# {title}",
        "",
        f"This is the AoA-side route index for `{ready_dir}/`.",
        "",
        f"Source registry: [`{Path(source_registry).name}`]({Path(source_registry).name}).",
        "",
        "This Markdown table is generated from the registry. Do not edit route rows by hand.",
        "",
        "It maps each ready quest to explicit center-side owner-request packets.",
        "It is not owner acceptance, owner landing, proof, runtime activation,",
        "or a replacement for `mechanics/experience/OWNER_REQUESTS.md`.",
        "",
        "## Route Table",
        "",
        "| Quest | Owner request routes | Route note |",
        "|---|---|---|",
    ]
    for item in routes:
        if not isinstance(item, dict):
            continue
        quest_id = str(item.get("quest_id", ""))
        quest_path = str(item.get("quest_path", ""))
        owner_request_ids = item.get("owner_request_ids")
        if not isinstance(owner_request_ids, list):
            owner_request_ids = []
        route_note = str(item.get("route_note", ""))
        route_text = ", ".join(f"`{request_id}`" for request_id in owner_request_ids)
        quest_link = link_from_output(output, quest_path)
        lines.append(f"| [{quest_id}]({quest_link}) | {route_text} | {route_note} |")

    lines.extend(["", "## Stop-lines", ""])
    for line in stop_lines:
        lines.append(f"- {line}")

    lines.extend(
        [
            "",
            "## Validation",
            "",
            "Use the central Questbook validation matrix in "
            "[Questbook AGENTS](../../AGENTS.md#validation).",
            "",
        ]
    )
    return "\n".join(lines)


def write_or_check(output: Path, text: str, check: bool) -> int:
    if check:
        current = output.read_text(encoding="utf-8") if output.exists() else ""
        if current != text:
            print(f"{rel(output)} is stale; run mechanics/questbook/scripts/build_ready_owner_routes.py")
            return 1
        print(f"[ok] ready owner route projection current: {rel(output)}")
        return 0
    output.write_text(text, encoding="utf-8")
    print(f"wrote {rel(output)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    registry_path = Path(args.registry)
    output_path = Path(args.output)
    registry = load_registry(registry_path)
    text = render_markdown(registry, output_path)
    return write_or_check(output_path, text, args.check)


if __name__ == "__main__":
    sys.exit(main())
