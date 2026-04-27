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
    "USAGE.md",
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
RPG_QUEST_CAMPAIGN_SURFACES = (
    "PLAYABLE_OBLIGATION.md",
)
WORKED_ROUTE_EXAMPLE = "parts/quest-campaign/examples/playable-obligation-route.md"
ACTIVE_DOC_ALLOWLIST = {"PROVENANCE.md", "LANDING_LOG.md", "AGENTS.md"}
PART_README_REQUIRED_HEADINGS = (
    "## Use When",
    "## Do Not Use When",
    "## Route Check",
    "## Active Outputs",
    "## Next Route",
)
PART_CONTRACT_REQUIRED_HEADINGS = (
    "## Center Owns",
    "## Must Not Claim",
    "## Allowed Outputs",
    "## Required Before Output",
)
USAGE_REQUIRED_HEADINGS = (
    "## Use RPG When",
    "## Use Plain Repo Language When",
    "## Decision Table",
    "## Application Sequence",
    "## Stop-lines",
    "## Post-change Route Review",
    "## Next Route",
)
USAGE_REQUIRED_ROUTES = (
    "mechanics/questbook/",
    "aoa-playbooks",
    "aoa-agents",
    "aoa-skills",
    "aoa-techniques",
    "aoa-evals",
    "aoa-memo",
    "aoa-stats",
    "abyss-stack",
)
PLAYABLE_OBLIGATION_REQUIRED_PHRASES = (
    "Questbook owns source quest object truth.",
    "RPG may add a derived reading only",
    "`quest_ref`",
    "`owner_route`",
    "`proof_route`",
    "`unlock_question`",
    "RPG does not own quest lifecycle.",
    "RPG does not close quests.",
    "mechanics/questbook/parts/model-spine/RPG_PLAYABLE_READING.md",
)
WORKED_ROUTE_REQUIRED_HEADINGS = (
    "## Ordinary Task",
    "## Quest Route",
    "## RPG Reading",
    "## Proof Route",
    "## Owner Handoff",
    "## Stop-lines",
)
WORKED_ROUTE_REQUIRED_PHRASES = (
    "Worked route, not a template. Do not copy this into every quest.",
    "`quests/center/triaged/AOA-Q-0008.yaml`",
    "`mechanics/rpg/parts/runtime-projection/README.md`",
    "`abyss-stack`",
    "Questbook still owns lifecycle state",
    "runtime projection remains an owner handoff, not center activation",
    "Do not claim quest closure, proof completion, runtime activation, owner acceptance, reward authority, or memory ownership from this example.",
)
OWNER_REQUEST_PACKETS = (
    ("ORQ-RPG-AGENTS-001", "aoa-agents"),
    ("ORQ-RPG-SKILLS-001", "aoa-skills"),
    ("ORQ-RPG-PLAYBOOKS-001", "aoa-playbooks"),
    ("ORQ-RPG-EVALS-001", "aoa-evals"),
    ("ORQ-RPG-STACK-001", "abyss-stack"),
    ("ORQ-RPG-STATS-001", "aoa-stats"),
)
OWNER_REQUEST_PACKET_REQUIRED_FIELDS = (
    "Carry to:",
    "Status:",
    "Center asks for:",
    "Why this owner:",
    "Center sources:",
    "Owner landing should decide:",
    "Acceptance signal:",
    "Proof route:",
    "Stop-lines:",
    "Do not carry as:",
    "Return receipt:",
)
ACTIVE_LEGACY_LANGUAGE_PATTERNS = (
    (re.compile(r"\bwave\b", re.IGNORECASE), "should not use wave-era language in active route"),
    (re.compile(r"first body-facing rollout", re.IGNORECASE), "should not keep rollout-era prose in active route"),
    (re.compile(r"rewrite the soul", re.IGNORECASE), "should not keep poetic runtime-projection slogans in active route"),
    (re.compile(r"\bthrone\b", re.IGNORECASE), "should not keep bridge-wave slogans in active route"),
)


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
    for surface in RPG_QUEST_CAMPAIGN_SURFACES:
        require(RPG_ROOT / "parts" / "quest-campaign" / surface, problems)
    require(RPG_ROOT / WORKED_ROUTE_EXAMPLE, problems)
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
    raw_name_pattern = re.compile(
        r"\b(?:" + "|".join(re.escape(raw) for raw in RAW_SOURCES) + r")\b"
    )
    for path in RPG_ROOT.glob("*.md"):
        if path.name in ACTIVE_DOC_ALLOWLIST:
            continue
        text = read_text(path)
        if "legacy/raw" in text:
            problems.append(f"{rel(path)} should route through PROVENANCE.md instead of legacy/raw")
        if raw_name_pattern.search(text):
            problems.append(f"{rel(path)} should not expose raw RPG_* filenames in active route")
        for pattern, message in ACTIVE_LEGACY_LANGUAGE_PATTERNS:
            if pattern.search(text):
                problems.append(f"{rel(path)} {message}")
    for path in (RPG_ROOT / "parts").rglob("*.md"):
        text = read_text(path)
        if "legacy/raw" in text or raw_name_pattern.search(text):
            problems.append(f"{rel(path)} should stay active and not expose raw legacy source names")
        for pattern, message in ACTIVE_LEGACY_LANGUAGE_PATTERNS:
            if pattern.search(text):
                problems.append(f"{rel(path)} {message}")


def validate_part_readme_shape(problems: list[str]) -> None:
    for slug in PART_SLUGS:
        path = RPG_ROOT / "parts" / slug / "README.md"
        text = read_text(path)
        for heading in PART_README_REQUIRED_HEADINGS:
            if heading not in text:
                problems.append(f"{rel(path)}: missing active-route heading {heading}")


def validate_part_contract_shape(problems: list[str]) -> None:
    for slug in PART_SLUGS:
        path = RPG_ROOT / "parts" / slug / "CONTRACT.md"
        text = read_text(path)
        for heading in PART_CONTRACT_REQUIRED_HEADINGS:
            if heading not in text:
                problems.append(f"{rel(path)}: missing contract heading {heading}")


def validate_usage_contract(problems: list[str]) -> None:
    path = RPG_ROOT / "USAGE.md"
    text = read_text(path)
    for heading in USAGE_REQUIRED_HEADINGS:
        if heading not in text:
            problems.append(f"{rel(path)}: missing usage heading {heading}")
    for route in USAGE_REQUIRED_ROUTES:
        if route not in text:
            problems.append(f"{rel(path)}: missing owner route {route}")
    for phrase in (
        "Plain repository language wins when it is clearer.",
        "Do not create a universal power score.",
        "What is the source object?",
        "Who owns the source truth?",
    ):
        if phrase not in text:
            problems.append(f"{rel(path)}: missing usage rule {phrase!r}")


def validate_playable_obligation_route(problems: list[str]) -> None:
    path = RPG_ROOT / "parts" / "quest-campaign" / "PLAYABLE_OBLIGATION.md"
    text = read_text(path)
    for phrase in PLAYABLE_OBLIGATION_REQUIRED_PHRASES:
        if phrase not in text:
            problems.append(f"{rel(path)}: missing playable obligation rule {phrase!r}")


def validate_worked_route_example(problems: list[str]) -> None:
    example_dir = RPG_ROOT / "parts" / "quest-campaign" / "examples"
    path = RPG_ROOT / WORKED_ROUTE_EXAMPLE
    examples = sorted(example_dir.glob("*.md"))
    if examples != [path]:
        refs = ", ".join(rel(example) for example in examples) or "none"
        problems.append(f"{rel(example_dir)} must contain exactly one worked route example, found: {refs}")
        return
    text = read_text(path)
    normalized = " ".join(text.split())
    for heading in WORKED_ROUTE_REQUIRED_HEADINGS:
        if heading not in text:
            problems.append(f"{rel(path)}: missing worked route heading {heading}")
    for phrase in WORKED_ROUTE_REQUIRED_PHRASES:
        if " ".join(phrase.split()) not in normalized:
            problems.append(f"{rel(path)}: missing worked route rule {phrase!r}")
    if "```" in text:
        problems.append(f"{rel(path)} should not carry copy-paste command blocks")


def validate_owner_request_packets(problems: list[str]) -> None:
    path = RPG_ROOT / "OWNER_REQUESTS.md"
    text = read_text(path)
    if "## Ready-to-carry packets" not in text:
        problems.append(f"{rel(path)}: missing ready-to-carry packets section")
        return
    if "They do not mark the request accepted, landed, proved, or activated." not in text:
        problems.append(f"{rel(path)}: missing no-acceptance rule for ready-to-carry packets")
    for request_id, owner_repo in OWNER_REQUEST_PACKETS:
        match = re.search(
            rf"^### {re.escape(request_id)}\n(?P<body>.*?)(?=^### |\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if match is None:
            problems.append(f"{rel(path)}: missing ready-to-carry packet {request_id}")
            continue
        body = match.group("body")
        for field in OWNER_REQUEST_PACKET_REQUIRED_FIELDS:
            if field not in body:
                problems.append(f"{rel(path)}: {request_id} missing packet field {field}")
        if f"Carry to: `{owner_repo}`" not in body:
            problems.append(f"{rel(path)}: {request_id} does not carry to `{owner_repo}`")
        if "Status: `requested`, not accepted." not in body:
            problems.append(f"{rel(path)}: {request_id} must remain requested, not accepted")
        if "owner_landing_ref" not in body or "owner_proof_ref" not in body:
            problems.append(f"{rel(path)}: {request_id} return receipt must name owner landing/proof refs")
        if "generated/owner_request_queue.min.json" not in body:
            problems.append(f"{rel(path)}: {request_id} return receipt must route generated queue rebuild")


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
        "mechanics/rpg/USAGE.md",
        "mechanics/rpg/PARTS.md",
        "mechanics/rpg/PROVENANCE.md",
        "mechanics/rpg/OWNER_REQUESTS.md",
    }
    required_docs.update(
        f"mechanics/rpg/parts/{slug}/README.md"
        for slug in PART_SLUGS
    )
    required_docs.add("mechanics/rpg/parts/vocabulary-overlay/TERMINOLOGY.md")
    required_docs.add("mechanics/rpg/parts/quest-campaign/PLAYABLE_OBLIGATION.md")
    required_docs.add("mechanics/rpg/parts/quest-campaign/examples/playable-obligation-route.md")
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
    validate_part_readme_shape(problems)
    validate_part_contract_shape(problems)
    validate_usage_contract(problems)
    validate_playable_obligation_route(problems)
    validate_worked_route_example(problems)
    validate_owner_request_packets(problems)
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
