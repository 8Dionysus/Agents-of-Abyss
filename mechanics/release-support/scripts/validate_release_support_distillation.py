#!/usr/bin/env python3
"""Validate the Release-support mechanic package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "release-support"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
QUEUE_PATH = REPO_ROOT / "mechanics" / "owner-request-queue.json"

REQUIRED_TOP_LEVEL = (
    "AGENTS.md",
    "README.md",
    "DIRECTION.md",
    "PARTS.md",
    "OWNER_MAP.md",
    "OWNER_REQUESTS.md",
    "PROVENANCE.md",
    "ROADMAP.md",
    "LANDING_LOG.md",
    "docs/PUBLIC_SUPPORT_POSTURE.md",
    "docs/FEDERATION_RELEASE_PROTOCOL.md",
    "docs/RELEASING.md",
    "docs/DIRECTION_SURFACES.md",
    "docs/RELEASE_SUPPORT_OWNER_REPO_REQUESTS.md",
    "parts/AGENTS.md",
    "parts/README.md",
    "legacy/AGENTS.md",
    "legacy/README.md",
    "legacy/raw/README.md",
)

PARTS = (
    "state-transition-gate",
    "public-claim-gate",
    "release-runbook",
    "changelog-roadmap-split",
    "landing-closeout",
    "owner-handoff-packet",
    "sibling-evidence-route",
    "rollback-return",
    "direction-surface-review",
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
    "ORQ-RELEASE-EVALS-001",
    "ORQ-RELEASE-STATS-001",
    "ORQ-RELEASE-ROUTING-001",
    "ORQ-RELEASE-SDK-001",
    "ORQ-RELEASE-PROFILE-001",
)

OWNER_REPOS = (
    "aoa-evals",
    "aoa-stats",
    "aoa-routing",
    "aoa-sdk",
    "8Dionysus",
    "abyss-stack",
)

MUST_NOT_CLAIM = (
    "GitHub-only definition of release",
    "unverified public claim",
    "sibling acceptance without receipt",
    "roadmap history as changelog",
    "generated or derived release authority",
    "hidden rollback safety",
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
            problems.append(f"missing required release-support surface: {rel(path)}")
        elif path.is_file() and not read(path).endswith("\n"):
            problems.append(f"{rel(path)}: missing final newline")


def validate_card(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "README.md")
    required_phrases = (
        "Release support is the center mechanic for honest state transitions.",
        "Status: `landed`",
        "Center state-transition vocabulary",
        "`aoa-evals` owns proof evidence",
        "`abyss-stack` owns runtime deployment and rollback truth.",
        "Generated surfaces reflect source truth but do not author release truth.",
    )
    for phrase in required_phrases:
        if not contains_phrase(text, phrase):
            problems.append(f"mechanics/release-support/README.md: missing card phrase {phrase!r}")
    for stop_line in MUST_NOT_CLAIM:
        if not contains_phrase(text, stop_line):
            problems.append(f"mechanics/release-support/README.md: missing must-not-claim {stop_line!r}")


def validate_direction(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "DIRECTION.md")
    for phrase in (
        "Release support treats release as a state transition, not only as a GitHub event.",
        "Internal landing",
        "Mechanic maturity",
        "Quest or checkpoint closeout",
        "Sibling adoption",
        "Rollback or return",
    ):
        if not contains_phrase(text, phrase):
            problems.append(f"mechanics/release-support/DIRECTION.md: missing direction phrase {phrase!r}")


def validate_parts(problems: list[str]) -> None:
    parts_text = read(PACKAGE_ROOT / "PARTS.md")
    parts_readme = read(PACKAGE_ROOT / "parts" / "README.md")
    parts_agents = read(PACKAGE_ROOT / "parts" / "AGENTS.md")
    for part in PARTS:
        if f"parts/{part}/README.md" not in parts_text:
            problems.append(f"mechanics/release-support/PARTS.md: missing part link for {part}")
        if f"{part}/README.md" not in parts_readme:
            problems.append(f"mechanics/release-support/parts/README.md: missing part link for {part}")
        part_dir = PACKAGE_ROOT / "parts" / part
        if not part_dir.is_dir():
            problems.append(f"missing release-support part directory: {rel(part_dir)}")
            continue
        for file_name in PART_FILES:
            path = part_dir / file_name
            if not path.is_file():
                problems.append(f"missing release-support part file: {rel(path)}")
                continue
            text = read(path)
            if not text.endswith("\n"):
                problems.append(f"{rel(path)}: missing final newline")
            if file_name == "README.md":
                for heading in PART_README_HEADINGS:
                    if heading not in text:
                        problems.append(f"{rel(path)}: missing heading {heading}")
            if file_name == "VALIDATION.md" and "Release-support parts AGENTS" not in text:
                problems.append(f"{rel(path)}: must route executable validation to Release-support parts AGENTS")
    if "validate_release_support_distillation.py" not in parts_agents:
        problems.append("mechanics/release-support/parts/AGENTS.md: missing package validator command")


def validate_owner_map(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "OWNER_MAP.md")
    for owner in OWNER_REPOS:
        if owner not in text:
            problems.append(f"mechanics/release-support/OWNER_MAP.md: missing owner {owner!r}")
    for stop_line in (
        "Wording change is not state change.",
        "The center must not publish unverified promises.",
        "Release support cannot become proof authority.",
        "Runtime state and deployment truth are runtime-owned.",
    ):
        if stop_line not in text:
            problems.append(f"mechanics/release-support/OWNER_MAP.md: missing stop-line {stop_line!r}")


def validate_owner_requests(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "OWNER_REQUESTS.md")
    if "A request packet is not owner acceptance" not in text:
        problems.append("mechanics/release-support/OWNER_REQUESTS.md: missing owner-acceptance stop-line")
    for request_id in OWNER_REQUEST_IDS:
        if request_id not in text:
            problems.append(f"mechanics/release-support/OWNER_REQUESTS.md: missing request id {request_id}")
    compat = read(PACKAGE_ROOT / "docs" / "RELEASE_SUPPORT_OWNER_REPO_REQUESTS.md")
    if "../OWNER_REQUESTS.md" not in compat:
        problems.append("mechanics/release-support/docs/RELEASE_SUPPORT_OWNER_REPO_REQUESTS.md: must route to ../OWNER_REQUESTS.md")


def validate_provenance_boundary(problems: list[str]) -> None:
    provenance = read(PACKAGE_ROOT / "PROVENANCE.md")
    for term in (
        "PUBLIC_SUPPORT_POSTURE",
        "FEDERATION_RELEASE_PROTOCOL",
        "DIRECTION_SURFACES",
        "No raw source file was moved during this landing.",
    ):
        if term not in provenance:
            problems.append(f"mechanics/release-support/PROVENANCE.md: missing provenance term {term!r}")
    active_forbidden = (
        "legacy/raw/",
        "raw source file",
    )
    allowed = {
        "mechanics/release-support/PROVENANCE.md",
        "mechanics/release-support/LANDING_LOG.md",
        "mechanics/release-support/legacy/README.md",
        "mechanics/release-support/legacy/raw/README.md",
    }
    for path in PACKAGE_ROOT.rglob("*.md"):
        if "legacy/raw" in path.as_posix():
            continue
        rel_path = rel(path)
        if rel_path in allowed:
            continue
        text = read(path)
        for term in active_forbidden:
            if term in text:
                problems.append(f"{rel_path}: active surface must route raw history through PROVENANCE.md")
                break


def validate_registry(problems: list[str]) -> None:
    registry = json.loads(read(REGISTRY_PATH))
    entry = next((item for item in registry.get("mechanics", []) if item.get("slug") == "release-support"), None)
    if not entry:
        problems.append("mechanics/registry.json: missing release-support entry")
        return
    if entry.get("owner_request_doc_ref") != "mechanics/release-support/OWNER_REQUESTS.md":
        problems.append("mechanics/registry.json: release-support owner_request_doc_ref must point to OWNER_REQUESTS.md")
    required_sources = (
        "mechanics/release-support/DIRECTION.md",
        "mechanics/release-support/PARTS.md",
        "mechanics/release-support/OWNER_MAP.md",
        "mechanics/release-support/PROVENANCE.md",
        "mechanics/release-support/OWNER_REQUESTS.md",
    )
    for source in required_sources:
        if source not in entry.get("canonical_docs", []):
            problems.append(f"mechanics/registry.json: release-support canonical_docs missing {source}")
    for part in PARTS:
        rel_path = f"mechanics/release-support/parts/{part}/README.md"
        if rel_path not in entry.get("canonical_docs", []):
            problems.append(f"mechanics/registry.json: release-support canonical_docs missing {rel_path}")
    if "mechanics/release-support/scripts/validate_release_support_distillation.py" not in entry.get("validation_refs", []):
        problems.append("mechanics/registry.json: release-support validation_refs missing package validator")
    if entry.get("owner_request_ids") != list(OWNER_REQUEST_IDS):
        problems.append("mechanics/registry.json: release-support owner_request_ids mismatch")


def validate_queue_sources(problems: list[str]) -> None:
    queue = json.loads(read(QUEUE_PATH))
    required_sources = {
        "mechanics/release-support/README.md",
        "mechanics/release-support/DIRECTION.md",
        "mechanics/release-support/PARTS.md",
        "mechanics/release-support/OWNER_MAP.md",
        "mechanics/release-support/OWNER_REQUESTS.md",
        "mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md",
        "mechanics/release-support/docs/FEDERATION_RELEASE_PROTOCOL.md",
        "mechanics/release-support/docs/DIRECTION_SURFACES.md",
    }
    seen: list[str] = []
    for request in queue.get("requests", []):
        if request.get("mechanic") != "release-support":
            continue
        seen.append(request.get("id"))
        sources = set(request.get("center_sources", []))
        missing = sorted(required_sources - sources)
        for source in missing:
            problems.append(f"{request.get('id')}: center_sources missing {source}")
    if seen != list(OWNER_REQUEST_IDS):
        problems.append("mechanics/owner-request-queue.json: release-support request order mismatch")


def main() -> int:
    problems: list[str] = []
    validate_required_files(problems)
    if not problems:
        validate_card(problems)
        validate_direction(problems)
        validate_parts(problems)
        validate_owner_map(problems)
        validate_owner_requests(problems)
        validate_provenance_boundary(problems)
        validate_registry(problems)
        validate_queue_sources(problems)
    if problems:
        print("Release-support distillation validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] Release-support distillation validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
