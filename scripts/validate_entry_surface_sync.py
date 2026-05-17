#!/usr/bin/env python3
"""Validate route-mode sync across center entry surfaces."""

from __future__ import annotations

import json
from pathlib import Path

from center_entry_map_common import (
    BASELINE_VALIDATION_COMMANDS,
    CENTER_ENTRY_MAP_PATH,
    ENTRY_SURFACE_REFS,
    REQUIRED_ROUTE_MODES,
    ROUTE_CONTRACT_REF,
    VALIDATION_BASELINE_REF,
    VALIDATION_REFS,
    resolve_local_ref,
)

HUMAN_ENTRY_SURFACES = tuple(
    ref for ref in ENTRY_SURFACE_REFS if ref != "generated/center_entry_map.min.json"
)

SURFACE_ROUTE_MODE_EXEMPTIONS = {
    "mechanics/README.md": {"low-context-agent"},
}

SURFACE_VALIDATION_AUTHORITY_REFS = {
    "docs/README.md": "docs/AGENTS.md",
    "mechanics/README.md": "mechanics/AGENTS.md",
    "mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md": "mechanics/release-support/docs/AGENTS.md",
}


def read_ref(ref: str) -> str:
    path = CENTER_ENTRY_MAP_PATH if ref == "generated/center_entry_map.min.json" else resolve_local_ref(ref)
    return path.read_text(encoding="utf-8")


def validation_text_for(ref: str) -> str:
    text = read_ref(ref)
    authority_ref = SURFACE_VALIDATION_AUTHORITY_REFS.get(ref)
    if authority_ref:
        text += "\n" + read_ref(authority_ref)
    return text


def has_contract_pointer(text: str) -> bool:
    return ROUTE_CONTRACT_REF in text or Path(ROUTE_CONTRACT_REF).name in text


def has_validation_baseline_pointer(text: str) -> bool:
    return VALIDATION_BASELINE_REF in text or Path(VALIDATION_BASELINE_REF).name in text


def collect_problems() -> list[str]:
    problems: list[str] = []

    try:
        baseline_text = read_ref(VALIDATION_BASELINE_REF)
    except Exception as exc:  # pragma: no cover - reported as data problem
        baseline_text = ""
        problems.append(f"{VALIDATION_BASELINE_REF}: cannot read validation baseline: {exc}")

    for command in BASELINE_VALIDATION_COMMANDS:
        if command not in baseline_text:
            problems.append(f"{VALIDATION_BASELINE_REF}: missing baseline validation command '{command}'")

    for ref in ENTRY_SURFACE_REFS:
        try:
            text = read_ref(ref)
        except Exception as exc:  # pragma: no cover - reported as data problem
            problems.append(f"{ref}: cannot read entry surface: {exc}")
            continue

        exempt = SURFACE_ROUTE_MODE_EXEMPTIONS.get(ref, set())
        for mode in REQUIRED_ROUTE_MODES:
            if mode in exempt:
                continue
            if mode not in text:
                problems.append(f"{ref}: missing route mode '{mode}'")

        if ref in HUMAN_ENTRY_SURFACES and not has_contract_pointer(text):
            problems.append(f"{ref}: missing pointer to {ROUTE_CONTRACT_REF}")

    for ref in HUMAN_ENTRY_SURFACES:
        try:
            text = validation_text_for(ref)
        except Exception as exc:  # pragma: no cover - reported as data problem
            problems.append(f"{ref}: cannot read validation authority surface: {exc}")
            continue
        if has_validation_baseline_pointer(text):
            continue
        for command in BASELINE_VALIDATION_COMMANDS:
            if command not in text:
                problems.append(
                    f"{ref}: missing baseline validation command '{command}' "
                    f"or pointer to {VALIDATION_BASELINE_REF}"
                )

    try:
        generated_payload = json.loads(CENTER_ENTRY_MAP_PATH.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - reported as data problem
        generated_payload = {}
        problems.append(f"generated/center_entry_map.min.json: cannot read generated map: {exc}")
    generated_refs = generated_payload.get("validation_refs") if isinstance(generated_payload, dict) else None
    if not isinstance(generated_refs, list):
        problems.append("generated/center_entry_map.min.json: validation_refs must be a list")
    else:
        for ref in VALIDATION_REFS:
            if ref not in generated_refs:
                problems.append(f"generated/center_entry_map.min.json: missing validation ref '{ref}'")

    return problems


def main() -> int:
    problems = collect_problems()
    if problems:
        print("Entry surface sync validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print(f"[ok] entry route modes synced across {len(ENTRY_SURFACE_REFS)} surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
