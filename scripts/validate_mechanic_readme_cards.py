#!/usr/bin/env python3
"""Validate mechanic package README cards against mechanics/registry.json."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
DEFAULT_HEADINGS = (
    "## Mechanic card",
    "### Trigger",
    "### Center owns",
    "### Stronger owner split",
    "### Inputs",
    "### Outputs",
    "### Must not claim",
    "### Validation",
    "### Next route",
)
CARD_KEYS = (
    "trigger",
    "center_owns",
    "stronger_owner_split",
    "inputs",
    "outputs",
    "next_route",
)


def load_registry() -> dict[str, Any]:
    with REGISTRY_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def normalize(value: str) -> str:
    value = value.replace("`", "")
    value = value.replace("[", "").replace("]", "")
    value = value.replace("(", " ").replace(")", " ")
    return re.sub(r"\s+", " ", value.casefold()).strip()


def contains_phrase(text: str, phrase: str) -> bool:
    return normalize(phrase) in normalize(text)


def line_number(text: str, needle: str) -> int:
    index = text.find(needle)
    if index < 0:
        return -1
    return text[:index].count("\n") + 1


def validate_card(entry: dict[str, Any], required_headings: tuple[str, ...]) -> list[str]:
    problems: list[str] = []
    slug = str(entry.get("slug", ""))
    rel = str(entry.get("entry_ref", f"mechanics/{slug}/README.md"))
    path = REPO_ROOT / rel
    if not path.exists():
        return [f"{slug}: entry_ref missing: {rel}"]
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        problems.append(f"{rel}: missing final newline")

    last_line = 0
    for heading in required_headings:
        current = line_number(text, heading)
        if current < 0:
            problems.append(f"{rel}: missing heading {heading}")
            continue
        if current < last_line:
            problems.append(f"{rel}: heading out of order: {heading}")
        last_line = max(last_line, current)

    status = str(entry.get("status", "")).strip()
    if status and f"Status: `{status}`" not in text and f"Status: {status}" not in text:
        problems.append(f"{rel}: mechanic card must include Status: `{status}`")

    card = entry.get("card")
    if not isinstance(card, dict):
        problems.append(f"mechanics/registry.json:{slug}: card must be an object")
        return problems

    for key in CARD_KEYS:
        value = card.get(key)
        if value is None or value == "" or value == []:
            problems.append(f"mechanics/registry.json:{slug}: card.{key} is empty")
            continue
        values = value if isinstance(value, list) else [value]
        for item in values:
            if not contains_phrase(text, str(item)):
                problems.append(f"{rel}: missing card.{key} phrase: {item}")

    for claim in entry.get("must_not_claim", []):
        if not contains_phrase(text, str(claim)):
            problems.append(f"{rel}: missing must_not_claim phrase: {claim}")

    for doc in entry.get("canonical_docs", []):
        doc = str(doc)
        local_doc = doc
        package = str(entry.get("package_path", "")) + "/"
        if doc.startswith(package):
            local_doc = doc[len(package):]
        if doc not in text and local_doc not in text and Path(doc).name not in text:
            problems.append(f"{rel}: canonical doc not linked or named: {doc}")

    for ref in entry.get("validation_refs", []):
        ref = str(ref)
        if ref not in text and Path(ref).name not in text:
            problems.append(f"{rel}: validation ref not named: {ref}")

    if "docs/FEDERATION_RULES.md" not in text:
        problems.append(f"{rel}: Next route must preserve docs/FEDERATION_RULES.md fallback")
    if "generated" in text and "do not author" not in normalize(text):
        problems.append(f"{rel}: generated surfaces must not author meaning")
    return problems


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate mechanics README card contract.")
    parser.add_argument(
        "--mechanic",
        action="append",
        help="Mechanic slug to validate; may be passed more than once. Defaults to all.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    registry = load_registry()
    selected = set(args.mechanic or [])
    known = {str(entry.get("slug")) for entry in registry.get("mechanics", []) if isinstance(entry, dict)}
    unknown = selected - known
    if unknown:
        print("Unknown mechanic slug(s): " + ", ".join(sorted(unknown)))
        return 2
    required_headings = tuple(registry.get("mechanic_card_required_headings") or DEFAULT_HEADINGS)
    problems: list[str] = []
    for entry in registry.get("mechanics", []):
        if not isinstance(entry, dict):
            problems.append("mechanics/registry.json: mechanic entry is not an object")
            continue
        slug = str(entry.get("slug", ""))
        if selected and slug not in selected:
            continue
        problems.extend(validate_card(entry, required_headings))
    if problems:
        print("Mechanic README card validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    scope = ", ".join(sorted(selected)) if selected else "all mechanics"
    print(f"[ok] validated mechanic README cards: {scope}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
