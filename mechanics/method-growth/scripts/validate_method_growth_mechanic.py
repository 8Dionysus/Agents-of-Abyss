#!/usr/bin/env python3
"""Validate the Method-growth mechanic package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "method-growth"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"

REQUIRED_TOP_LEVEL = (
    "AGENTS.md",
    "README.md",
    "DIRECTION.md",
    "PARTS.md",
    "OWNER_MAP.md",
    "PROVENANCE.md",
    "OWNER_REQUESTS.md",
    "ROADMAP.md",
    "LANDING_LOG.md",
    "docs/ROOTLINE.md",
    "docs/METHOD_SPINE.md",
    "docs/REVIEWABLE_GROWTH_REFINERY.md",
    "docs/CANDIDATE_LINEAGE_CROSSWALK.md",
    "docs/OWNER_LANDING_AND_PRUNING.md",
    "docs/METHOD_GROWTH_OWNER_REPO_REQUESTS.md",
    "parts/AGENTS.md",
    "parts/README.md",
)

PARTS = (
    "donor-refinery",
    "candidate-lineage",
    "owner-landing",
    "pruning",
    "proof-route",
    "method-promotion",
    "technique-skill-split",
    "memory-writeback",
    "maturity-ladder",
    "growth-closeout",
)

PART_FILES = ("README.md", "CONTRACT.md", "VALIDATION.md")
PART_README_HEADINGS = (
    "## Use When",
    "## Do Not Use When",
    "## Route Check",
    "## Active Outputs",
    "## Next Route",
)

OWNER_REQUEST_IDS = (
    "ORQ-METHOD-SKILLS-001",
    "ORQ-METHOD-SDK-001",
    "ORQ-METHOD-DIONYSUS-001",
    "ORQ-METHOD-EVALS-001",
    "ORQ-METHOD-PLAYBOOKS-001",
    "ORQ-METHOD-MEMO-001",
    "ORQ-METHOD-TECHNIQUES-001",
    "ORQ-METHOD-STATS-001",
)

OWNER_REPOS = (
    "aoa-sdk",
    "aoa-skills",
    "aoa-techniques",
    "Dionysus",
    "aoa-evals",
    "aoa-playbooks",
    "aoa-memo",
    "aoa-stats",
    "aoa-routing",
    "aoa-kag",
    "abyss-stack",
    "Tree-of-Sophia",
    "8Dionysus",
)

MUST_NOT_CLAIM = (
    "center-owned final object truth",
    "owner-local activation",
    "proof verdict",
    "memory canon",
    "candidate_ref minting in center",
    "seed_ref minting in center",
    "object_ref minting in center",
)

ACTIVE_PROVENANCE_TERMS = (
    "aoa-sdk/examples/checkpoint_lineage_hint.example.json",
    "aoa-skills/examples/session_growth_artifacts/",
    "Dionysus/examples/seed_lineage_entry.example.json",
    "aoa-playbooks/playbooks/reviewed-automation-followthrough/PLAYBOOK.md",
    "aoa-stats/generated/session_growth_branch_summary.min.json",
    "aoa-techniques/techniques/",
    "aoa-evals/",
    "aoa-memo/",
)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def contains_phrase(text: str, phrase: str) -> bool:
    compact_text = re.sub(r"\s+", " ", text).casefold()
    compact_phrase = re.sub(r"\s+", " ", phrase).casefold()
    return compact_phrase in compact_text


def validate_required_files(problems: list[str]) -> None:
    for item in REQUIRED_TOP_LEVEL:
        path = PACKAGE_ROOT / item
        if not path.exists():
            problems.append(f"missing required method-growth surface: {rel(path)}")
        elif path.is_file() and not read(path).endswith("\n"):
            problems.append(f"{rel(path)}: missing final newline")


def validate_card(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "README.md")
    required_phrases = (
        "Status: `landed`",
        "Center growth route, lineage vocabulary, reviewable-growth discipline",
        "Generated surfaces may reflect method-growth cards, queues, indexes, or manifests, but they do not author method-growth meaning.",
        "AoA owns growth-route law.",
        "`aoa-techniques` owns reusable practice.",
    )
    for phrase in required_phrases:
        if not contains_phrase(text, phrase):
            problems.append(f"mechanics/method-growth/README.md: missing card phrase {phrase!r}")
    for stop_line in MUST_NOT_CLAIM:
        if not contains_phrase(text, stop_line):
            problems.append(f"mechanics/method-growth/README.md: missing must-not-claim {stop_line!r}")
    for owner in OWNER_REPOS[:8]:
        if owner not in text:
            problems.append(f"mechanics/method-growth/README.md: missing owner route {owner!r}")


def validate_parts(problems: list[str]) -> None:
    parts_text = read(PACKAGE_ROOT / "PARTS.md")
    parts_readme = read(PACKAGE_ROOT / "parts" / "README.md")
    parts_agents = read(PACKAGE_ROOT / "parts" / "AGENTS.md")
    for part in PARTS:
        if f"parts/{part}/README.md" not in parts_text:
            problems.append(f"mechanics/method-growth/PARTS.md: missing part link for {part}")
        if f"{part}/README.md" not in parts_readme:
            problems.append(f"mechanics/method-growth/parts/README.md: missing part link for {part}")
        part_dir = PACKAGE_ROOT / "parts" / part
        if not part_dir.is_dir():
            problems.append(f"missing method-growth part directory: {rel(part_dir)}")
            continue
        for file_name in PART_FILES:
            path = part_dir / file_name
            if not path.is_file():
                problems.append(f"missing method-growth part file: {rel(path)}")
                continue
            text = read(path)
            if not text.endswith("\n"):
                problems.append(f"{rel(path)}: missing final newline")
            if file_name == "README.md":
                for heading in PART_README_HEADINGS:
                    if heading not in text:
                        problems.append(f"{rel(path)}: missing heading {heading}")
            if file_name == "VALIDATION.md" and "Method-growth parts AGENTS" not in text:
                problems.append(f"{rel(path)}: must route executable validation to Method-growth parts AGENTS")
    if "validate_method_growth_mechanic.py" not in parts_agents:
        problems.append("mechanics/method-growth/parts/AGENTS.md: missing package validator command")


def validate_owner_map(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "OWNER_MAP.md")
    for owner in OWNER_REPOS:
        if owner not in text:
            problems.append(f"mechanics/method-growth/OWNER_MAP.md: missing owner {owner!r}")
    for stop_line in (
        "A donor pattern is not canon.",
        "A `cluster_ref` is not reviewed candidate identity.",
        "A `candidate_ref` is not final owner truth.",
        "A `seed_ref` is not owner acceptance.",
        "A stats summary is not proof.",
    ):
        if stop_line not in text:
            problems.append(f"mechanics/method-growth/OWNER_MAP.md: missing stop-line {stop_line!r}")


def validate_owner_requests(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "OWNER_REQUESTS.md")
    if "A request packet is not owner acceptance" not in text:
        problems.append("mechanics/method-growth/OWNER_REQUESTS.md: missing owner-acceptance stop-line")
    for request_id in OWNER_REQUEST_IDS:
        if request_id not in text:
            problems.append(f"mechanics/method-growth/OWNER_REQUESTS.md: missing request id {request_id}")
    compat = read(PACKAGE_ROOT / "docs" / "METHOD_GROWTH_OWNER_REPO_REQUESTS.md")
    if "../OWNER_REQUESTS.md" not in compat:
        problems.append("mechanics/method-growth/docs/METHOD_GROWTH_OWNER_REPO_REQUESTS.md: must route to ../OWNER_REQUESTS.md")


def validate_provenance_boundary(problems: list[str]) -> None:
    provenance = read(PACKAGE_ROOT / "PROVENANCE.md")
    for term in ACTIVE_PROVENANCE_TERMS:
        if term not in provenance:
            problems.append(f"mechanics/method-growth/PROVENANCE.md: missing provenance term {term!r}")
    allowed = {
        "mechanics/method-growth/PROVENANCE.md",
        "mechanics/method-growth/docs/METHOD_GROWTH_OWNER_REPO_REQUESTS.md",
    }
    for path in [
        PACKAGE_ROOT / "README.md",
        PACKAGE_ROOT / "DIRECTION.md",
        PACKAGE_ROOT / "PARTS.md",
        PACKAGE_ROOT / "OWNER_MAP.md",
        PACKAGE_ROOT / "OWNER_REQUESTS.md",
        *sorted((PACKAGE_ROOT / "parts").rglob("*.md")),
    ]:
        path_ref = rel(path)
        if path_ref in allowed:
            continue
        text = read(path)
        for term in ACTIVE_PROVENANCE_TERMS:
            if term in text:
                problems.append(f"{path_ref}: sibling source path {term!r} must route through PROVENANCE")


def validate_registry(problems: list[str]) -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    method_growth = next(
        (entry for entry in registry.get("mechanics", []) if entry.get("slug") == "method-growth"),
        None,
    )
    if not isinstance(method_growth, dict):
        problems.append("mechanics/registry.json: missing method-growth entry")
        return
    if method_growth.get("owner_request_doc_ref") != "mechanics/method-growth/OWNER_REQUESTS.md":
        problems.append("mechanics/registry.json: method-growth owner_request_doc_ref must point to root OWNER_REQUESTS.md")
    if method_growth.get("owner_request_ids") != list(OWNER_REQUEST_IDS):
        problems.append("mechanics/registry.json: method-growth owner_request_ids mismatch")
    canonical_docs = set(method_growth.get("canonical_docs", []))
    for rel_path in (
        "mechanics/method-growth/DIRECTION.md",
        "mechanics/method-growth/PARTS.md",
        "mechanics/method-growth/OWNER_MAP.md",
        "mechanics/method-growth/PROVENANCE.md",
        "mechanics/method-growth/OWNER_REQUESTS.md",
        "mechanics/method-growth/parts/donor-refinery/README.md",
        "mechanics/method-growth/parts/candidate-lineage/README.md",
        "mechanics/method-growth/parts/growth-closeout/README.md",
    ):
        if rel_path not in canonical_docs:
            problems.append(f"mechanics/registry.json: method-growth canonical_docs missing {rel_path}")
    validation_refs = set(method_growth.get("validation_refs", []))
    if "mechanics/method-growth/scripts/validate_method_growth_mechanic.py" not in validation_refs:
        problems.append("mechanics/registry.json: method-growth validation_refs missing method-growth validator")


def validate_landing_log(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "LANDING_LOG.md")
    required_fields = ("Status:", "Owner boundary:", "Surfaces:", "Validation:", "Stop-lines:", "Next route:")
    for field in required_fields:
        if field not in text:
            problems.append(f"mechanics/method-growth/LANDING_LOG.md: missing {field}")
    if not re.search(r"^### .+", text, re.MULTILINE):
        problems.append("mechanics/method-growth/LANDING_LOG.md: missing landing entry")
    if "Method-growth active-part distillation" not in text:
        problems.append("mechanics/method-growth/LANDING_LOG.md: missing active-part distillation entry")


def validate() -> list[str]:
    problems: list[str] = []
    validate_required_files(problems)
    if problems:
        return problems
    validate_card(problems)
    validate_parts(problems)
    validate_owner_map(problems)
    validate_owner_requests(problems)
    validate_provenance_boundary(problems)
    validate_registry(problems)
    validate_landing_log(problems)
    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("Method-growth mechanic validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] method-growth mechanic validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
