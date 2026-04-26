#!/usr/bin/env python3
"""Validate RPG active parts and legacy provenance split."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
RPG_ROOT = REPO_ROOT / "mechanics" / "rpg"
PART_SLUGS = (
    "world-grammar",
    "source-boundary",
    "vocabulary-overlay",
    "quest-campaign",
    "progression-unlocks",
    "runtime-projection",
    "owner-handoffs",
)
ROOT_SURFACES = (
    "AGENTS.md",
    "README.md",
    "DIRECTION.md",
    "PARTS.md",
    "PROVENANCE.md",
    "ROADMAP.md",
    "LANDING_LOG.md",
    "OWNER_REQUESTS.md",
)
LEGACY_SURFACES = (
    "legacy/AGENTS.md",
    "legacy/README.md",
    "legacy/INDEX.md",
    "legacy/DISTILLATION_LOG.md",
    "legacy/raw/README.md",
    "legacy/artifacts/README.md",
)
RAW_SOURCES = (
    "RPG_LAYER_MODEL.md",
    "RPG_ARCHITECTURE_RFC.md",
    "RPG_BOUNDARY_MAP.md",
    "RPG_FIRST_WAVE.md",
    "RPG_SECOND_WAVE.md",
    "RPG_SKILLS_AND_FEATS.md",
    "RPG_BRIDGE_WAVE.md",
    "RPG_RUNTIME_PROJECTION_WAVE.md",
)
VOCAB_ARTIFACTS = (
    "TERMINOLOGY.md",
    "schemas/dual_vocabulary_overlay.schema.json",
    "examples/dual_vocabulary_overlay.example.json",
    "generated/dual_vocabulary_overlay.json",
    "scripts/validate_vocabulary_overlay.py",
    "tests/test_vocabulary_overlay.py",
)
ACTIVE_DOC_ALLOWLIST = {"PROVENANCE.md", "LANDING_LOG.md", "AGENTS.md"}


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(path: Path, problems: list[str]) -> None:
    if not path.exists():
        problems.append(f"missing required RPG surface: {rel(path)}")


def validate_paths(problems: list[str]) -> None:
    for name in ROOT_SURFACES:
        require(RPG_ROOT / name, problems)
    for name in LEGACY_SURFACES:
        require(RPG_ROOT / name, problems)
    for raw in RAW_SOURCES:
        require(RPG_ROOT / "legacy" / "raw" / raw, problems)
    require(RPG_ROOT / "parts" / "README.md", problems)
    require(RPG_ROOT / "parts" / "AGENTS.md", problems)
    require(RPG_ROOT / "docs" / "README.md", problems)
    require(RPG_ROOT / "docs" / "AGENTS.md", problems)

    for slug in PART_SLUGS:
        part = RPG_ROOT / "parts" / slug
        require(part / "README.md", problems)
        require(part / "CONTRACT.md", problems)
        require(part / "VALIDATION.md", problems)
    for artifact in VOCAB_ARTIFACTS:
        require(RPG_ROOT / "parts" / "vocabulary-overlay" / artifact, problems)

    for old_dir in ("schemas", "examples", "generated"):
        if (RPG_ROOT / old_dir).exists():
            problems.append(f"flat RPG artifact directory remains: {rel(RPG_ROOT / old_dir)}")
    for old in (RPG_ROOT / "scripts" / "validate_rpg_dual_vocabulary_overlay.py", RPG_ROOT / "tests" / "test_rpg_dual_vocabulary_overlay.py"):
        if old.exists():
            problems.append(f"old flat RPG vocabulary artifact remains: {rel(old)}")
    for old_doc in (RPG_ROOT / "docs").glob("RPG_*.md"):
        problems.append(f"old active RPG doc remains outside legacy: {rel(old_doc)}")


def validate_provenance(problems: list[str]) -> None:
    provenance = read_text(RPG_ROOT / "PROVENANCE.md")
    legacy_index = read_text(RPG_ROOT / "legacy" / "INDEX.md")
    distillation_log = read_text(RPG_ROOT / "legacy" / "DISTILLATION_LOG.md")
    for raw in RAW_SOURCES:
        for label, text in (
            ("legacy/INDEX.md", legacy_index),
            ("legacy/DISTILLATION_LOG.md", distillation_log),
        ):
            if raw not in text:
                problems.append(f"mechanics/rpg/{label}: missing raw source {raw}")
    for bridge_ref in ("legacy/INDEX.md", "legacy/DISTILLATION_LOG.md", "legacy/raw/"):
        if bridge_ref not in provenance:
            problems.append(f"mechanics/rpg/PROVENANCE.md: missing legacy bridge {bridge_ref}")
    for slug in PART_SLUGS:
        for label, text in (
            ("PARTS.md", read_text(RPG_ROOT / "PARTS.md")),
            ("PROVENANCE.md", provenance),
            ("legacy/INDEX.md", legacy_index),
            ("legacy/DISTILLATION_LOG.md", distillation_log),
        ):
            if slug not in text:
                problems.append(f"mechanics/rpg/{label}: missing part slug {slug}")


def validate_active_docs_are_clean(problems: list[str]) -> None:
    raw_name_pattern = re.compile(r"RPG_[A-Z0-9_]+\.md")
    for path in RPG_ROOT.glob("*.md"):
        if path.name in ACTIVE_DOC_ALLOWLIST:
            continue
        text = read_text(path)
        if "legacy/raw" in text:
            problems.append(f"{rel(path)} should route through PROVENANCE.md instead of legacy/raw")
        if raw_name_pattern.search(text):
            problems.append(f"{rel(path)} should not expose raw RPG_* filenames in active route")
    for path in (RPG_ROOT / "parts").rglob("*.md"):
        text = read_text(path)
        if "legacy/raw" in text or raw_name_pattern.search(text):
            problems.append(f"{rel(path)} should stay active and not expose raw legacy source names")


def validate_registry(problems: list[str]) -> None:
    registry = json.loads((REPO_ROOT / "mechanics" / "registry.json").read_text(encoding="utf-8"))
    entry = next((item for item in registry.get("mechanics", []) if item.get("slug") == "rpg"), None)
    if not isinstance(entry, dict):
        problems.append("mechanics/registry.json: missing RPG entry")
        return
    if entry.get("owner_request_doc_ref") != "mechanics/rpg/OWNER_REQUESTS.md":
        problems.append("mechanics/registry.json: RPG owner_request_doc_ref must point to mechanics/rpg/OWNER_REQUESTS.md")
    canonical_docs = set(entry.get("canonical_docs", []))
    required_docs = {
        "mechanics/rpg/DIRECTION.md",
        "mechanics/rpg/PARTS.md",
        "mechanics/rpg/PROVENANCE.md",
        "mechanics/rpg/OWNER_REQUESTS.md",
    }
    required_docs.update(
        f"mechanics/rpg/parts/{slug}/README.md"
        for slug in PART_SLUGS
    )
    required_docs.add("mechanics/rpg/parts/vocabulary-overlay/TERMINOLOGY.md")
    missing = sorted(required_docs - canonical_docs)
    for path_ref in missing:
        problems.append(f"mechanics/registry.json: RPG canonical_docs missing {path_ref}")
    for path_ref in canonical_docs:
        if "/legacy/raw/" in path_ref or "/docs/RPG_" in path_ref:
            problems.append(f"mechanics/registry.json: RPG canonical_docs points to legacy/raw source: {path_ref}")
    validation_refs = set(entry.get("validation_refs", []))
    for path_ref in (
        "mechanics/rpg/scripts/validate_rpg_distillation.py",
        "mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py",
    ):
        if path_ref not in validation_refs:
            problems.append(f"mechanics/registry.json: RPG validation_refs missing {path_ref}")


def validate_vocabulary_overlay(problems: list[str]) -> None:
    validator_path = RPG_ROOT / "parts" / "vocabulary-overlay" / "scripts" / "validate_vocabulary_overlay.py"
    spec = importlib.util.spec_from_file_location("validate_vocabulary_overlay", validator_path)
    if spec is None or spec.loader is None:
        problems.append(f"cannot load {rel(validator_path)}")
        return
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    problems.extend(module.validate())


def validate() -> list[str]:
    problems: list[str] = []
    validate_paths(problems)
    if problems:
        return problems
    validate_provenance(problems)
    validate_active_docs_are_clean(problems)
    validate_registry(problems)
    validate_vocabulary_overlay(problems)
    return problems


def parse_args() -> argparse.Namespace:
    return argparse.ArgumentParser(description=__doc__).parse_args()


def main() -> int:
    parse_args()
    problems = validate()
    if problems:
        print("RPG distillation validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] RPG distillation validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
