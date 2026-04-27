#!/usr/bin/env python3
"""Validate owner-request protocol, central queue doc, and package-local request docs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = REPO_ROOT / "mechanics" / "owner-request-queue.json"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
CANONICAL_SLUGS = (
    "method-growth",
    "recurrence",
    "checkpoint",
    "experience",
    "agon",
    "antifragility",
    "questbook",
    "rpg",
    "boundary-bridge",
    "release-support",
)
CENTRAL_DOCS = {
    "mechanics/OWNER_REQUEST_PROTOCOL.md": ("## Request anatomy", "## Request status vocabulary", "## Advancement rules", "## Stop-lines", "## Validation"),
    "mechanics/OWNER_REQUEST_QUEUE.md": ("## Queue grammar", "## Request status vocabulary", "## How agents use the queue", "## Request index", "## Stop-lines", "## Validation"),
}
PACKAGE_HEADINGS = ("## Owner request packet", "## Requests", "## Center sources", "## Stop-lines", "## Validation", "## Next route")


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_docs(selected: set[str] | None = None) -> list[str]:
    problems: list[str] = []
    queue = load_json(QUEUE_PATH)
    registry = load_json(REGISTRY_PATH)
    requests_by_slug: dict[str, list[str]] = {slug: [] for slug in CANONICAL_SLUGS}
    for req in queue.get("requests", []):
        requests_by_slug.setdefault(str(req.get("mechanic")), []).append(str(req.get("id")))
    for rel, headings in CENTRAL_DOCS.items():
        path = REPO_ROOT / rel
        if not path.exists():
            problems.append(f"{rel}: missing")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            problems.append(f"{rel}: missing final newline")
        for heading in headings:
            if heading not in text:
                problems.append(f"{rel}: missing heading {heading}")
    for entry in registry.get("mechanics", []):
        slug = str(entry.get("slug"))
        if selected and slug not in selected:
            continue
        rel = str(entry.get("owner_request_doc_ref", ""))
        path = REPO_ROOT / rel
        if not path.exists():
            problems.append(f"{slug}: owner request doc missing: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            problems.append(f"{rel}: missing final newline")
        for heading in PACKAGE_HEADINGS:
            if heading not in text:
                problems.append(f"{rel}: missing heading {heading}")
        for rid in requests_by_slug.get(slug, []):
            if rid not in text:
                problems.append(f"{rel}: missing request id {rid}")
        if "A request packet is not owner acceptance" not in text and "not owner acceptance" not in text:
            problems.append(f"{rel}: missing owner-acceptance stop-line")
    return problems


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate owner request docs.")
    parser.add_argument("--mechanic", choices=CANONICAL_SLUGS, action="append", help="Mechanic slug to validate; may be repeated.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = set(args.mechanic) if args.mechanic else None
    problems = validate_docs(selected)
    if problems:
        print("Owner request docs validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    scope = ", ".join(sorted(selected)) if selected else "all mechanics"
    print(f"[ok] owner request docs validated: {scope}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
