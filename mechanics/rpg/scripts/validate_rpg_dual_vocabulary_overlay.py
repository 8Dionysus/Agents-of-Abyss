#!/usr/bin/env python3
"""Validate the RPG dual vocabulary overlay contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[3]
RPG_ROOT = REPO_ROOT / "mechanics" / "rpg"

TERMINOLOGY_PATH = RPG_ROOT / "docs" / "RPG_CANONICAL_TERMINOLOGY.md"
SCHEMA_PATH = RPG_ROOT / "schemas" / "dual_vocabulary_overlay.schema.json"
EXAMPLE_PATH = RPG_ROOT / "examples" / "dual_vocabulary_overlay.example.json"
GENERATED_PATH = RPG_ROOT / "generated" / "dual_vocabulary_overlay.json"

SCHEMA_VERSION = "dual_vocabulary_overlay_v1"
ACTION_KEYS = ("inspect", "expand", "handoff", "verify", "reanchor")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def markdown_section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group("body") if match else ""


def table_keys(section: str) -> list[str]:
    keys: list[str] = []
    for line in section.splitlines():
        match = re.match(r"\|\s*`([^`]+)`\s*\|", line)
        if match:
            keys.append(match.group(1))
    return keys


def first_frontend_minimum_keys(text: str) -> list[str]:
    keys: list[str] = []
    keys.extend(table_keys(markdown_section(text, "Identity terms")))
    keys.extend(table_keys(markdown_section(text, "Mastery axes")))
    keys.extend(table_keys(markdown_section(text, "Runtime resources")))
    keys.extend(ACTION_KEYS)
    keys.extend(table_keys(markdown_section(text, "Reputation axes")))
    return keys


def schema_required_keys(schema: dict[str, Any]) -> list[str]:
    keys: list[str] = []
    for item in schema.get("allOf", []):
        try:
            key = item["properties"]["entries"]["contains"]["properties"]["canonical_key"]["const"]
        except KeyError:
            continue
        keys.append(str(key))
    return keys


def entry_keys(payload: dict[str, Any]) -> list[str]:
    return [str(entry.get("canonical_key")) for entry in payload.get("entries", [])]


def validate_json_payload(
    *,
    label: str,
    payload: dict[str, Any],
    validator: Draft202012Validator,
    expected_keys: list[str],
    problems: list[str],
) -> None:
    errors = sorted(validator.iter_errors(payload), key=lambda error: list(error.path))
    for error in errors:
        location = "/".join(str(part) for part in error.path) or "<root>"
        problems.append(f"{label}: schema violation at {location}: {error.message}")

    keys = entry_keys(payload)
    if keys != expected_keys:
        problems.append(f"{label}: canonical_key order must match RPG first frontend minimum")
    if len(keys) != len(set(keys)):
        problems.append(f"{label}: duplicate canonical_key entries are not allowed")

    for entry in payload.get("entries", []):
        key = entry.get("canonical_key")
        if entry.get("canonical_label") != key:
            problems.append(f"{label}: canonical_label must equal canonical_key for {key!r}")

    if payload.get("schema_version") != SCHEMA_VERSION:
        problems.append(f"{label}: schema_version must be {SCHEMA_VERSION}")
    if payload.get("public_safe") is not True:
        problems.append(f"{label}: public_safe must be true")


def validate() -> list[str]:
    problems: list[str] = []

    for path in (TERMINOLOGY_PATH, SCHEMA_PATH, EXAMPLE_PATH, GENERATED_PATH):
        if not path.exists():
            problems.append(f"{path.relative_to(REPO_ROOT)}: missing")
            return problems

    terminology = read_text(TERMINOLOGY_PATH)
    schema = load_json(SCHEMA_PATH)
    example = load_json(EXAMPLE_PATH)
    generated = load_json(GENERATED_PATH)

    expected_keys = first_frontend_minimum_keys(terminology)
    if len(expected_keys) != 26:
        problems.append(
            "mechanics/rpg/docs/RPG_CANONICAL_TERMINOLOGY.md: first frontend minimum must resolve to 26 keys"
        )
    if len(expected_keys) != len(set(expected_keys)):
        problems.append(
            "mechanics/rpg/docs/RPG_CANONICAL_TERMINOLOGY.md: first frontend minimum has duplicate keys"
        )

    schema_keys = schema_required_keys(schema)
    if schema_keys != expected_keys:
        problems.append(
            "mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json: required canonical keys must match terminology order"
        )

    entries_schema = schema.get("properties", {}).get("entries", {})
    if entries_schema.get("minItems") != len(expected_keys):
        problems.append("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json: minItems must match required key count")
    if entries_schema.get("maxItems") != len(expected_keys):
        problems.append("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json: maxItems must match required key count")

    if schema.get("title") != SCHEMA_VERSION:
        problems.append("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json: title must match schema_version")

    validator = Draft202012Validator(schema)
    validate_json_payload(
        label="mechanics/rpg/examples/dual_vocabulary_overlay.example.json",
        payload=example,
        validator=validator,
        expected_keys=expected_keys,
        problems=problems,
    )
    validate_json_payload(
        label="mechanics/rpg/generated/dual_vocabulary_overlay.json",
        payload=generated,
        validator=validator,
        expected_keys=expected_keys,
        problems=problems,
    )

    comparable_example = {key: value for key, value in example.items() if key != "notes"}
    comparable_generated = {key: value for key, value in generated.items() if key != "notes"}
    if comparable_example != comparable_generated:
        problems.append("RPG example and generated overlay must match apart from notes")
    if "Generated twin" not in str(generated.get("notes", "")):
        problems.append("mechanics/rpg/generated/dual_vocabulary_overlay.json: notes must name generated twin posture")
    if "Example only" not in str(example.get("notes", "")):
        problems.append("mechanics/rpg/examples/dual_vocabulary_overlay.example.json: notes must name example posture")

    return problems


def parse_args() -> argparse.Namespace:
    return argparse.ArgumentParser(description=__doc__).parse_args()


def main() -> int:
    parse_args()
    problems = validate()
    if problems:
        print("RPG dual vocabulary overlay validation failed:")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("[ok] validated RPG dual vocabulary overlay")
    return 0


if __name__ == "__main__":
    sys.exit(main())
