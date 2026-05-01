#!/usr/bin/env python3
"""Validate the AbyssOS organ-contract docs district."""
from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DISTRICT = REPO_ROOT / "docs" / "organ-contract"

REQUIRED_SURFACES = (
    "AGENTS.md",
    "README.md",
    "ORGAN_CONTRACT.md",
    "SURFACE_STATES.md",
    "FIRST_CYCLE.md",
    "EVENTS.md",
)

README_HEADINGS = (
    "## District law",
    "## Current surfaces",
    "## Must not claim",
    "## Promotion path",
    "## Validation",
)

SURFACE_STATES = (
    "source",
    "generated",
    "trace",
    "legacy",
    "runtime",
    "public",
    "projection",
    "receipt",
    "cache",
)

FIRST_CYCLE_STEPS = (
    "intent",
    "route",
    "work",
    "proof",
    "record",
    "land",
    "handoff",
)

SYSTEM_EVENTS = (
    "landing",
    "distillation",
    "audit",
    "checkpoint",
    "decision",
    "quest",
    "release",
    "rollback",
    "handoff",
    "reanchor",
    "harvest",
    "owner-request",
)

STRONGER_OWNER_REFS = (
    "aoa-sdk",
    "aoa-routing",
    "aoa-agents",
    "aoa-playbooks",
    "aoa-evals",
    "aoa-memo",
    "aoa-kag",
    "aoa-stats",
    "abyss-stack",
    "Tree-of-Sophia",
)

ENTRY_SURFACES = (
    "AGENTS.md",
    "README.md",
    "CONTRIBUTING.md",
    "docs/README.md",
    "docs/START_HERE_ROUTE_CONTRACT.md",
    "mechanics/README.md",
    "mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md",
    "scripts/center_entry_map_common.py",
    "schemas/center-entry-map.schema.json",
)

NO_STUB_TOKENS = ("TODO", "TBD", "placeholder", "stub")


def read(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


def require_contains(problems: list[str], rel: str, needle: str) -> None:
    if needle not in read(rel):
        problems.append(f"{rel} missing {needle!r}")


def validate_required_surfaces(problems: list[str]) -> None:
    for name in REQUIRED_SURFACES:
        path = DISTRICT / name
        if not path.is_file():
            problems.append(f"missing docs/organ-contract/{name}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# "):
            problems.append(f"docs/organ-contract/{name} must start with an H1")
        for token in NO_STUB_TOKENS:
            if token in text:
                problems.append(f"docs/organ-contract/{name} contains stub token {token!r}")


def validate_readme(problems: list[str]) -> None:
    rel = "docs/organ-contract/README.md"
    text = read(rel)
    for heading in README_HEADINGS:
        if heading not in text:
            problems.append(f"{rel} missing heading {heading!r}")
    for name in REQUIRED_SURFACES:
        if name not in text:
            problems.append(f"{rel} does not index {name}")
    for owner in STRONGER_OWNER_REFS:
        if owner not in text:
            problems.append(f"{rel} missing stronger owner route {owner!r}")
    if "organ-alignment" not in text:
        problems.append(f"{rel} missing organ-alignment route mode")


def validate_contract(problems: list[str]) -> None:
    rel = "docs/organ-contract/ORGAN_CONTRACT.md"
    text = read(rel)
    for phrase in (
        "README.md",
        "AGENTS.md",
        "CHANGELOG.md",
        "decision record route",
        "validation route",
        "handoff route",
        "owns",
        "routes",
        "receives",
        "hands off",
    ):
        if phrase not in text:
            problems.append(f"{rel} missing contract phrase {phrase!r}")


def validate_surface_states(problems: list[str]) -> None:
    rel = "docs/organ-contract/SURFACE_STATES.md"
    text = read(rel)
    for state in SURFACE_STATES:
        if f"`{state}`" not in text:
            problems.append(f"{rel} missing surface state {state!r}")


def validate_first_cycle(problems: list[str]) -> None:
    rel = "docs/organ-contract/FIRST_CYCLE.md"
    text = read(rel)
    for step in FIRST_CYCLE_STEPS:
        if f"`{step}`" not in text:
            problems.append(f"{rel} missing first-cycle step {step!r}")
    for route in ("docs/decisions/", "QUESTBOOK.md", "CHANGELOG.md", "docs/traces/"):
        if route not in text:
            problems.append(f"{rel} missing record route {route!r}")


def validate_events(problems: list[str]) -> None:
    rel = "docs/organ-contract/EVENTS.md"
    text = read(rel)
    for event in SYSTEM_EVENTS:
        if f"`{event}`" not in text:
            problems.append(f"{rel} missing system event {event!r}")


def validate_entry_sync_refs(problems: list[str]) -> None:
    for rel in ENTRY_SURFACES:
        require_contains(problems, rel, "organ-alignment")
    for rel in (
        "docs/guardrails/ENTRY_SURFACE_VALIDATION_BASELINE.md",
        "docs/AGENTS.md",
        "scripts/release_check.py",
        "scripts/registry.json",
        "tests/registry.json",
    ):
        require_contains(problems, rel, "scripts/validate_organ_contract.py")


def main() -> int:
    problems: list[str] = []
    validate_required_surfaces(problems)
    if not problems:
        validate_readme(problems)
        validate_contract(problems)
        validate_surface_states(problems)
        validate_first_cycle(problems)
        validate_events(problems)
    validate_entry_sync_refs(problems)

    if problems:
        raise SystemExit("organ contract validation failed:\n- " + "\n- ".join(problems))
    print("organ contract validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
