#!/usr/bin/env python3
"""Validate the Antifragility mechanic package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "antifragility"
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
    "FRAGILITY_BLACKLIST.md",
    "docs/ANTIFRAGILITY.md",
    "docs/VIA_NEGATIVA.md",
    "docs/ANTI_AUTHORITY_RULES.md",
    "docs/ONE_IN_ONE_OUT.md",
    "docs/ANTIFRAGILITY_OWNER_REPO_REQUESTS.md",
    "parts/AGENTS.md",
    "parts/README.md",
    "legacy/AGENTS.md",
    "legacy/README.md",
    "legacy/raw/README.md",
    "legacy/raw/ANTIFRAGILITY_FIRST_WAVE.md",
    "legacy/raw/VIA_NEGATIVA_CHECKLIST.md",
)

PARTS = (
    "stress-review",
    "via-negativa",
    "authority-boundary",
    "sprawl-control",
    "fragility-registry",
    "repair-proof",
    "memory-return",
    "owner-handoff",
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
    "ORQ-ANTIFRAGILITY-EVALS-001",
    "ORQ-ANTIFRAGILITY-MEMO-001",
    "ORQ-ANTIFRAGILITY-STATS-001",
    "ORQ-ANTIFRAGILITY-PLAYBOOKS-001",
)

OWNER_REPOS = (
    "aoa-evals",
    "aoa-memo",
    "aoa-stats",
    "aoa-playbooks",
    "aoa-techniques",
    "aoa-skills",
    "abyss-stack",
)

MUST_NOT_CLAIM = (
    "one-score health",
    "deletion theater",
    "owner-local cleanup authority",
)

LEGACY_TERMS = (
    "ANTIFRAGILITY_FIRST_WAVE",
    "VIA_NEGATIVA_CHECKLIST",
    "legacy/raw",
    "first-wave",
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
            problems.append(f"missing required antifragility surface: {rel(path)}")
        elif path.is_file() and not read(path).endswith("\n"):
            problems.append(f"{rel(path)}: missing final newline")


def validate_card(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "README.md")
    required_phrases = (
        "Status: `landed`",
        "Center stress doctrine, via negativa, anti-authority posture",
        "Generated surfaces may reflect antifragility cards, queues, indexes, or manifests, but they do not author antifragility meaning.",
        "AoA owns antifragility law",
        "`aoa-stats` owns derived fragility windows without one-score health.",
        "`aoa-playbooks` owns recurring cleanup and degraded-mode choreography.",
    )
    for phrase in required_phrases:
        if not contains_phrase(text, phrase):
            problems.append(f"mechanics/antifragility/README.md: missing card phrase {phrase!r}")
    for stop_line in MUST_NOT_CLAIM:
        if not contains_phrase(text, stop_line):
            problems.append(f"mechanics/antifragility/README.md: missing must-not-claim {stop_line!r}")


def validate_parts(problems: list[str]) -> None:
    parts_text = read(PACKAGE_ROOT / "PARTS.md")
    parts_readme = read(PACKAGE_ROOT / "parts" / "README.md")
    parts_agents = read(PACKAGE_ROOT / "parts" / "AGENTS.md")
    for part in PARTS:
        if f"parts/{part}/README.md" not in parts_text:
            problems.append(f"mechanics/antifragility/PARTS.md: missing part link for {part}")
        if f"{part}/README.md" not in parts_readme:
            problems.append(f"mechanics/antifragility/parts/README.md: missing part link for {part}")
        part_dir = PACKAGE_ROOT / "parts" / part
        if not part_dir.is_dir():
            problems.append(f"missing antifragility part directory: {rel(part_dir)}")
            continue
        for file_name in PART_FILES:
            path = part_dir / file_name
            if not path.is_file():
                problems.append(f"missing antifragility part file: {rel(path)}")
                continue
            text = read(path)
            if not text.endswith("\n"):
                problems.append(f"{rel(path)}: missing final newline")
            if file_name == "README.md":
                for heading in PART_README_HEADINGS:
                    if heading not in text:
                        problems.append(f"{rel(path)}: missing heading {heading}")
            if file_name == "VALIDATION.md" and "Antifragility parts AGENTS" not in text:
                problems.append(f"{rel(path)}: must route executable validation to Antifragility parts AGENTS")
    if "validate_antifragility_distillation.py" not in parts_agents:
        problems.append("mechanics/antifragility/parts/AGENTS.md: missing package validator command")


def validate_owner_map(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "OWNER_MAP.md")
    for owner in OWNER_REPOS:
        if owner not in text:
            problems.append(f"mechanics/antifragility/OWNER_MAP.md: missing owner {owner!r}")
    for stop_line in (
        "A stress note is not a repair receipt.",
        "Pattern presence is not a health score.",
        "A cleanup story is not proof.",
        "Memory is not proof or live truth.",
    ):
        if stop_line not in text:
            problems.append(f"mechanics/antifragility/OWNER_MAP.md: missing stop-line {stop_line!r}")


def validate_owner_requests(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "OWNER_REQUESTS.md")
    if "A request packet is not owner acceptance" not in text:
        problems.append("mechanics/antifragility/OWNER_REQUESTS.md: missing owner-acceptance stop-line")
    for request_id in OWNER_REQUEST_IDS:
        if request_id not in text:
            problems.append(f"mechanics/antifragility/OWNER_REQUESTS.md: missing request id {request_id}")
    compat = read(PACKAGE_ROOT / "docs" / "ANTIFRAGILITY_OWNER_REPO_REQUESTS.md")
    if "../OWNER_REQUESTS.md" not in compat:
        problems.append("mechanics/antifragility/docs/ANTIFRAGILITY_OWNER_REPO_REQUESTS.md: must route to ../OWNER_REQUESTS.md")


def validate_provenance_boundary(problems: list[str]) -> None:
    provenance = read(PACKAGE_ROOT / "PROVENANCE.md")
    for term in ("ANTIFRAGILITY_FIRST_WAVE", "VIA_NEGATIVA_CHECKLIST", "mechanics/audit/legacy/raw/DELETION_CANDIDATES.json"):
        if term not in provenance:
            problems.append(f"mechanics/antifragility/PROVENANCE.md: missing provenance term {term!r}")
    allowed = {
        "mechanics/antifragility/PROVENANCE.md",
        "mechanics/antifragility/LANDING_LOG.md",
        "mechanics/antifragility/legacy/README.md",
        "mechanics/antifragility/legacy/raw/README.md",
        "mechanics/antifragility/docs/ANTIFRAGILITY_OWNER_REPO_REQUESTS.md",
    }
    active_files = [
        path
        for path in PACKAGE_ROOT.rglob("*.md")
        if "legacy/raw" not in path.as_posix()
    ]
    for path in active_files:
        rel_path = rel(path)
        if rel_path in allowed:
            continue
        text = read(path)
        for term in LEGACY_TERMS:
            if term in text:
                problems.append(f"{rel_path}: active surface must not carry legacy/raw term {term!r}")
                break


def validate_registry(problems: list[str]) -> None:
    registry = json.loads(read(REGISTRY_PATH))
    entry = next((item for item in registry.get("mechanics", []) if item.get("slug") == "antifragility"), None)
    if not entry:
        problems.append("mechanics/registry.json: missing antifragility entry")
        return
    if entry.get("owner_request_doc_ref") != "mechanics/antifragility/OWNER_REQUESTS.md":
        problems.append("mechanics/registry.json: antifragility owner_request_doc_ref must point to OWNER_REQUESTS.md")
    for item in REQUIRED_TOP_LEVEL[:9]:
        rel_path = f"mechanics/antifragility/{item}"
        if rel_path not in entry.get("canonical_docs", []) and item not in {"AGENTS.md", "README.md", "ROADMAP.md", "LANDING_LOG.md"}:
            problems.append(f"mechanics/registry.json: antifragility canonical_docs missing {rel_path}")
    for part in PARTS:
        rel_path = f"mechanics/antifragility/parts/{part}/README.md"
        if rel_path not in entry.get("canonical_docs", []):
            problems.append(f"mechanics/registry.json: antifragility canonical_docs missing {rel_path}")
    if "mechanics/antifragility/scripts/validate_antifragility_distillation.py" not in entry.get("validation_refs", []):
        problems.append("mechanics/registry.json: antifragility validation_refs missing package validator")
    if entry.get("owner_request_ids") != list(OWNER_REQUEST_IDS):
        problems.append("mechanics/registry.json: antifragility owner_request_ids mismatch")


def validate_queue_sources(problems: list[str]) -> None:
    queue = json.loads(read(QUEUE_PATH))
    required_sources = {
        "mechanics/antifragility/README.md",
        "mechanics/antifragility/DIRECTION.md",
        "mechanics/antifragility/PARTS.md",
        "mechanics/antifragility/OWNER_MAP.md",
        "mechanics/antifragility/OWNER_REQUESTS.md",
    }
    seen = []
    for request in queue.get("requests", []):
        if request.get("mechanic") != "antifragility":
            continue
        seen.append(request.get("id"))
        sources = set(request.get("center_sources", []))
        missing = sorted(required_sources - sources)
        for source in missing:
            problems.append(f"{request.get('id')}: center_sources missing {source}")
    if seen != list(OWNER_REQUEST_IDS):
        problems.append("mechanics/owner-request-queue.json: antifragility request order mismatch")


def main() -> int:
    problems: list[str] = []
    validate_required_files(problems)
    if not problems:
        validate_card(problems)
        validate_parts(problems)
        validate_owner_map(problems)
        validate_owner_requests(problems)
        validate_provenance_boundary(problems)
        validate_registry(problems)
        validate_queue_sources(problems)
    if problems:
        print("Antifragility distillation validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] Antifragility distillation validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
