#!/usr/bin/env python3
"""Validate the Boundary Bridge mechanic package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "boundary-bridge"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
QUEUE_PATH = REPO_ROOT / "mechanics" / "owner-request-queue.json"

PARTS = (
    "boundary-contract",
    "non-identity-guard",
    "counterpart-edge",
    "tos-support",
    "witness-compost",
    "derived-projection",
    "owner-handoff",
    "proof-review-route",
    "compatibility-route",
)

TOP_LEVEL_FILES = (
    "AGENTS.md",
    "README.md",
    "DIRECTION.md",
    "PARTS.md",
    "OWNER_MAP.md",
    "PROVENANCE.md",
    "OWNER_REQUESTS.md",
    "ROADMAP.md",
    "LANDING_LOG.md",
    "docs/AGENTS.md",
    "docs/COUNTERPART_BRIDGE.md",
    "docs/WITNESS_COMPOST.md",
    "docs/TOS_GROWTH_SUPPORT.md",
    "docs/TOS_TEMPLATE_SUPPORT.md",
    "docs/TOS_LINEAGE_PILOT_SUPPORT.md",
    "docs/TOS_SOIL_PREP_SUPPORT.md",
    "docs/TOS_BRIDGE_OWNER_REPO_REQUESTS.md",
    "parts/AGENTS.md",
    "parts/README.md",
    "legacy/AGENTS.md",
    "legacy/README.md",
    "legacy/raw/README.md",
)

PART_FILES = ("README.md", "CONTRACT.md", "VALIDATION.md")
PART_README_HEADINGS = (
    "## Function",
    "## Inputs",
    "## Outputs",
    "## Stop-lines",
    "## Validation",
)

OWNER_REQUEST_IDS = (
    "ORQ-BRIDGE-TOS-001",
    "ORQ-BRIDGE-KAG-001",
    "ORQ-BRIDGE-ROUTING-001",
    "ORQ-BRIDGE-MEMO-001",
    "ORQ-BRIDGE-EVALS-001",
    "ORQ-BRIDGE-PLAYBOOKS-001",
)

MUST_NOT_CLAIM = (
    "owner acceptance without owner-local receipt",
    "identity between bridged surfaces",
    "AoA-authored ToS canon",
    "derived projection as source truth",
    "routing, SDK, memory, runtime, or public projection as authority",
)

ALLOWED_STALE_SLUG_PATHS = {
    "mechanics/boundary-bridge/PROVENANCE.md",
    "mechanics/boundary-bridge/docs/TOS_BRIDGE_OWNER_REPO_REQUESTS.md",
}


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def contains_phrase(text: str, phrase: str) -> bool:
    compact_text = re.sub(r"\s+", " ", text).casefold()
    compact_phrase = re.sub(r"\s+", " ", phrase).casefold()
    return compact_phrase in compact_text


def validate_required_files(problems: list[str]) -> None:
    for item in TOP_LEVEL_FILES:
        path = PACKAGE_ROOT / item
        if not path.is_file():
            problems.append(f"missing required boundary-bridge surface: {rel(path)}")
        elif not read(path).endswith("\n"):
            problems.append(f"{rel(path)}: missing final newline")


def validate_card(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "README.md")
    required_phrases = (
        "Boundary bridge is a center mechanic package",
        "without turning support, analogy, translation, projection, proof, routing, runtime, or public wording into an authority transfer",
        "ToS Support",
        "A request packet is not owner acceptance",
        "Do not make `boundary-bridge` a universal connector",
    )
    for phrase in required_phrases:
        if not contains_phrase(text, phrase):
            problems.append(f"mechanics/boundary-bridge/README.md: missing phrase {phrase!r}")
    for stop_line in MUST_NOT_CLAIM:
        if not contains_phrase(text, stop_line):
            problems.append(f"mechanics/boundary-bridge/README.md: missing must-not-claim {stop_line!r}")


def validate_parts(problems: list[str]) -> None:
    parts_text = read(PACKAGE_ROOT / "PARTS.md")
    parts_readme = read(PACKAGE_ROOT / "parts" / "README.md")
    parts_agents = read(PACKAGE_ROOT / "parts" / "AGENTS.md")
    for part in PARTS:
        if f"parts/{part}/README.md" not in parts_text:
            problems.append(f"mechanics/boundary-bridge/PARTS.md: missing part link for {part}")
        if f"{part}/README.md" not in parts_readme:
            problems.append(f"mechanics/boundary-bridge/parts/README.md: missing part link for {part}")
        part_dir = PACKAGE_ROOT / "parts" / part
        if not part_dir.is_dir():
            problems.append(f"missing boundary-bridge part directory: {rel(part_dir)}")
            continue
        for file_name in PART_FILES:
            path = part_dir / file_name
            if not path.is_file():
                problems.append(f"missing boundary-bridge part file: {rel(path)}")
                continue
            text = read(path)
            if not text.endswith("\n"):
                problems.append(f"{rel(path)}: missing final newline")
            if file_name == "README.md":
                for heading in PART_README_HEADINGS:
                    if heading not in text:
                        problems.append(f"{rel(path)}: missing heading {heading}")
            if file_name == "VALIDATION.md" and "validate_boundary_bridge_distillation.py" not in text:
                problems.append(f"{rel(path)}: missing package validator route")
    if "validate_boundary_bridge_distillation.py" not in parts_agents:
        problems.append("mechanics/boundary-bridge/parts/AGENTS.md: missing package validator command")


def validate_owner_requests(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "OWNER_REQUESTS.md")
    if "A request packet is not owner acceptance" not in text:
        problems.append("mechanics/boundary-bridge/OWNER_REQUESTS.md: missing owner-acceptance stop-line")
    for request_id in OWNER_REQUEST_IDS:
        if request_id not in text:
            problems.append(f"mechanics/boundary-bridge/OWNER_REQUESTS.md: missing request id {request_id}")
    compat = read(PACKAGE_ROOT / "docs" / "TOS_BRIDGE_OWNER_REPO_REQUESTS.md")
    if "../OWNER_REQUESTS.md" not in compat:
        problems.append("mechanics/boundary-bridge/docs/TOS_BRIDGE_OWNER_REPO_REQUESTS.md: must route to ../OWNER_REQUESTS.md")


def validate_provenance_boundary(problems: list[str]) -> None:
    provenance = read(PACKAGE_ROOT / "PROVENANCE.md")
    for phrase in (
        "Historical slug",
        "boundary-bridge",
        "Tree-of-Sophia",
        "COUNTERPART_BRIDGE.md",
        "WITNESS_COMPOST.md",
    ):
        if not contains_phrase(provenance, phrase):
            problems.append(f"mechanics/boundary-bridge/PROVENANCE.md: missing provenance phrase {phrase!r}")

    for path in PACKAGE_ROOT.rglob("*.md"):
        path_ref = rel(path)
        if path_ref in ALLOWED_STALE_SLUG_PATHS:
            continue
        text = read(path)
        if "tos-bridge" in text:
            problems.append(f"{path_ref}: stale slug `tos-bridge` must route through PROVENANCE only")


def validate_registry_and_queue(problems: list[str]) -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    bridge = next(
        (entry for entry in registry.get("mechanics", []) if entry.get("slug") == "boundary-bridge"),
        None,
    )
    if not isinstance(bridge, dict):
        problems.append("mechanics/registry.json: missing boundary-bridge entry")
    else:
        if bridge.get("owner_request_doc_ref") != "mechanics/boundary-bridge/OWNER_REQUESTS.md":
            problems.append("mechanics/registry.json: boundary-bridge owner_request_doc_ref must point to root OWNER_REQUESTS.md")
        canonical_docs = set(bridge.get("canonical_docs", []))
        for rel_path in (
            "mechanics/boundary-bridge/DIRECTION.md",
            "mechanics/boundary-bridge/PARTS.md",
            "mechanics/boundary-bridge/OWNER_MAP.md",
            "mechanics/boundary-bridge/PROVENANCE.md",
            "mechanics/boundary-bridge/OWNER_REQUESTS.md",
            "mechanics/boundary-bridge/parts/tos-support/README.md",
            "mechanics/boundary-bridge/parts/owner-handoff/README.md",
        ):
            if rel_path not in canonical_docs:
                problems.append(f"mechanics/registry.json: boundary-bridge canonical_docs missing {rel_path}")

    queue = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    queue_ids = {entry.get("id") for entry in queue.get("requests", []) if entry.get("mechanic") == "boundary-bridge"}
    for request_id in OWNER_REQUEST_IDS:
        if request_id not in queue_ids:
            problems.append(f"mechanics/owner-request-queue.json: missing boundary-bridge request {request_id}")


def validate_landing_log(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "LANDING_LOG.md")
    for field in ("Status:", "Owner boundary:", "Surfaces:", "Validation:", "Stop-lines:", "Next route:"):
        if field not in text:
            problems.append(f"mechanics/boundary-bridge/LANDING_LOG.md: missing {field}")
    for phrase in (
        "Boundary-bridge rename and ToS-support distillation",
        "bridge law, non-identity guardrails",
        "no identity claim",
        "no owner acceptance without owner-local",
        "carry owner-local packets",
    ):
        if not contains_phrase(text, phrase):
            problems.append(f"mechanics/boundary-bridge/LANDING_LOG.md: missing phrase {phrase!r}")


def validate() -> list[str]:
    problems: list[str] = []
    validate_required_files(problems)
    if problems:
        return problems
    validate_card(problems)
    validate_parts(problems)
    validate_owner_requests(problems)
    validate_provenance_boundary(problems)
    validate_registry_and_queue(problems)
    validate_landing_log(problems)
    return problems


def main() -> int:
    problems = validate()
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1
    print("[ok] validated Boundary-bridge distillation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
