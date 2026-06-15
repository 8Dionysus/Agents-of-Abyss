#!/usr/bin/env python3
"""Validate owner-request protocol, central queue doc, and package-local request docs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
QUEUE_PATH = REPO_ROOT / "mechanics" / "owner-request-queue.json"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
CANONICAL_SLUGS = (
    "method-growth",
    "distillation",
    "growth-cycle",
    "recurrence",
    "checkpoint",
    "experience",
    "agon",
    "antifragility",
    "questbook",
    "rpg",
    "boundary-bridge",
    "audit",
    "release-support",
)
CENTRAL_DOCS = {
    "mechanics/OWNER_REQUEST_PROTOCOL.md": ("## Request anatomy", "## Request status vocabulary", "## Advancement rules", "## Stop-lines", "## Validation"),
    "mechanics/OWNER_REQUEST_QUEUE.md": ("## Queue grammar", "## Request status vocabulary", "## How agents use the queue", "## Request index", "## Stop-lines", "## Validation"),
}
PACKAGE_HEADINGS = ("## Owner request packet", "## Requests", "## Center sources", "## Stop-lines", "## Validation", "## Next route")
RECEIPT_BACKED_STATUSES = {"accepted", "landed"}


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def request_packet_body(text: str, request_id: str) -> str | None:
    match = re.search(
        rf"^### {re.escape(request_id)}\n(?P<body>.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group("body") if match else None


def receipt_backed_packet_section_problems(rel: str, text: str, requests: list[dict[str, Any]]) -> list[str]:
    problems: list[str] = []
    if not requests or "## Ready-to-carry packets" not in text:
        return problems
    for req in requests:
        request_id = str(req.get("id") or "")
        body = request_packet_body(text, request_id)
        if body is None:
            problems.append(f"{rel}: {request_id} must have its own ready-to-carry packet section")
            continue
        if "receipt-backed" not in body.lower():
            problems.append(f"{rel}: {request_id} must distinguish its receipt-backed status")
        if "owner_landing_ref" not in body:
            problems.append(f"{rel}: {request_id} must name owner_landing_ref in its packet")
        if req.get("queue_status") == "landed" and "owner_proof_ref" not in body:
            problems.append(f"{rel}: {request_id} must name owner_proof_ref in its packet")
    return problems


def validate_docs(selected: set[str] | None = None) -> list[str]:
    problems: list[str] = []
    queue = load_json(QUEUE_PATH)
    registry = load_json(REGISTRY_PATH)
    requests_by_slug: dict[str, list[str]] = {slug: [] for slug in CANONICAL_SLUGS}
    advanced_requests_by_slug: dict[str, list[dict[str, Any]]] = {slug: [] for slug in CANONICAL_SLUGS}
    for req in queue.get("requests", []):
        slug = str(req.get("mechanic"))
        requests_by_slug.setdefault(slug, []).append(str(req.get("id")))
        if req.get("queue_status") in RECEIPT_BACKED_STATUSES:
            advanced_requests_by_slug.setdefault(slug, []).append(req)
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
        advanced_requests = advanced_requests_by_slug.get(slug, [])
        problems.extend(receipt_backed_packet_section_problems(rel, text, advanced_requests))
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
