#!/usr/bin/env python3
"""Validate Agon active route surfaces and source-doc bridge."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


REPO_ROOT = _repo_root()
AGON_ROOT = REPO_ROOT / "mechanics" / "agon"
PARTS_ROOT = AGON_ROOT / "parts"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"

PART_SLUGS = (
    "imposition-readiness",
    "lawful-move-grammar",
    "owner-binding",
    "gate-routing",
    "trial-handoff",
    "recurrence-adapter",
    "packet-arena",
    "duel-kernel",
    "verdict-retention-rank",
    "epistemic-kag",
    "sophian-threshold",
    "compatibility-bridges",
)

ROOT_SURFACES = (
    "README.md",
    "DIRECTION.md",
    "PARTS.md",
    "PROVENANCE.md",
    "LANDING_LOG.md",
    "ROADMAP.md",
    "OWNER_REQUESTS.md",
    "AGENTS.md",
)

PART_SURFACES = ("README.md", "CONTRACT.md", "VALIDATION.md")

ACTIVE_TEXT_SURFACES = ROOT_SURFACES + ("parts/README.md", "parts/AGENTS.md")

ACTIVE_ROUTE_POLLUTION_PATTERNS = (
    "low-context",
    "small enough",
    "Legacy raw",
    "raw source",
    "raw sources",
    "archival sources consulted",
)

OWNER_REQUEST_IDS = (
    "ORQ-AGON-PLAYBOOKS-001",
    "ORQ-AGON-EVALS-001",
    "ORQ-AGON-MEMO-001",
    "ORQ-AGON-STATS-001",
    "ORQ-AGON-ROUTING-001",
    "ORQ-AGON-AGENTS-001",
    "ORQ-AGON-STACK-001",
    "ORQ-AGON-KAG-001",
    "ORQ-AGON-TOS-001",
)


def read_text(rel: str) -> str:
    return (AGON_ROOT / rel).read_text(encoding="utf-8")


def validate() -> list[str]:
    problems: list[str] = []

    for rel in ROOT_SURFACES:
        path = AGON_ROOT / rel
        if not path.is_file():
            problems.append(f"missing Agon root surface: {rel}")
        elif not path.read_text(encoding="utf-8").endswith("\n"):
            problems.append(f"{rel}: missing final newline")

    for slug in PART_SLUGS:
        part_dir = PARTS_ROOT / slug
        if not part_dir.is_dir():
            problems.append(f"missing Agon part: {slug}")
            continue
        for rel in PART_SURFACES:
            path = part_dir / rel
            if not path.is_file():
                problems.append(f"{slug}: missing {rel}")
            elif not path.read_text(encoding="utf-8").endswith("\n"):
                problems.append(f"{slug}/{rel}: missing final newline")

    readme = read_text("README.md")
    direction = read_text("DIRECTION.md")
    parts = read_text("PARTS.md")
    provenance = read_text("PROVENANCE.md")
    owner_requests = read_text("OWNER_REQUESTS.md")
    compatibility = read_text("docs/AGON_OWNER_REPO_REQUESTS.md")

    for rel in ("DIRECTION.md", "PARTS.md", "OWNER_REQUESTS.md", "PROVENANCE.md"):
        if f"({rel})" not in readme:
            problems.append(f"README.md: missing active route link to {rel}")

    for slug in PART_SLUGS:
        if f"parts/{slug}/README.md" not in readme:
            problems.append(f"README.md: missing part route for {slug}")
        if f"parts/{slug}/README.md" not in parts:
            problems.append(f"PARTS.md: missing part route for {slug}")
        if f"`{slug}`" not in direction:
            problems.append(f"DIRECTION.md: missing active order entry for {slug}")
        if f"`{slug}`" not in provenance:
            problems.append(f"PROVENANCE.md: missing source-doc map entry for {slug}")

    for rid in OWNER_REQUEST_IDS:
        if rid not in owner_requests:
            problems.append(f"OWNER_REQUESTS.md: missing request id {rid}")

    if "../OWNER_REQUESTS.md" not in compatibility:
        problems.append("docs/AGON_OWNER_REPO_REQUESTS.md: must route to OWNER_REQUESTS.md")

    active_texts = {
        rel: (AGON_ROOT / rel).read_text(encoding="utf-8")
        for rel in ACTIVE_TEXT_SURFACES
        if (AGON_ROOT / rel).exists()
    }
    for slug in PART_SLUGS:
        for rel in PART_SURFACES:
            path = PARTS_ROOT / slug / rel
            if path.exists():
                active_texts[f"parts/{slug}/{rel}"] = path.read_text(encoding="utf-8")

    for rel, text in active_texts.items():
        for pattern in ACTIVE_ROUTE_POLLUTION_PATTERNS:
            if pattern in text:
                problems.append(f"{rel}: active route pollution pattern: {pattern}")

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    agon_entry = next((entry for entry in registry.get("mechanics", []) if entry.get("slug") == "agon"), None)
    if not agon_entry:
        problems.append("mechanics/registry.json: missing Agon entry")
    else:
        if agon_entry.get("owner_request_doc_ref") != "mechanics/agon/OWNER_REQUESTS.md":
            problems.append("mechanics/registry.json: Agon owner_request_doc_ref must point to OWNER_REQUESTS.md")
        refs = set(agon_entry.get("validation_refs", []))
        if "mechanics/agon/scripts/validate_agon_distillation.py" not in refs:
            problems.append("mechanics/registry.json: missing Agon distillation validator ref")
        canonical_docs = set(agon_entry.get("canonical_docs", []))
        for rel in ("DIRECTION.md", "PARTS.md", "PROVENANCE.md", "OWNER_REQUESTS.md"):
            expected = f"mechanics/agon/{rel}"
            if expected not in canonical_docs:
                problems.append(f"mechanics/registry.json: missing canonical doc {expected}")
        for slug in PART_SLUGS:
            expected = f"mechanics/agon/parts/{slug}/README.md"
            if expected not in canonical_docs:
                problems.append(f"mechanics/registry.json: missing canonical part {expected}")

    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("Agon distillation validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] Agon distillation validated: active route and parts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
