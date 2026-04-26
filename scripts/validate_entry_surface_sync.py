#!/usr/bin/env python3
"""Validate route-mode sync across center entry surfaces."""

from __future__ import annotations

from pathlib import Path

from center_entry_map_common import (
    BASELINE_VALIDATION_COMMANDS,
    CENTER_ENTRY_MAP_PATH,
    ENTRY_SURFACE_REFS,
    REQUIRED_ROUTE_MODES,
    ROUTE_CONTRACT_REF,
    VALIDATION_REFS,
    build_payload,
    resolve_local_ref,
)

HUMAN_ENTRY_SURFACES = tuple(
    ref for ref in ENTRY_SURFACE_REFS if ref != "generated/center_entry_map.min.json"
)

SURFACE_ROUTE_MODE_EXEMPTIONS = {
    "mechanics/README.md": {"low-context-agent"},
}

SURFACE_VALIDATION_AUTHORITY_REFS = {
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


def collect_problems() -> list[str]:
    problems: list[str] = []

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
        text = validation_text_for(ref)
        for command in BASELINE_VALIDATION_COMMANDS:
            if command not in text:
                problems.append(f"{ref}: missing baseline validation command '{command}'")

    payload = build_payload()
    for ref in VALIDATION_REFS:
        if ref not in payload["validation_refs"]:
            problems.append(f"generated payload: missing validation ref '{ref}'")

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
