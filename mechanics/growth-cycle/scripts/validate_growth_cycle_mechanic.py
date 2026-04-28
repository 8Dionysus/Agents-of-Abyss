#!/usr/bin/env python3
"""Validate the Growth Cycle mechanic package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "growth-cycle"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
QUEUE_PATH = REPO_ROOT / "mechanics" / "owner-request-queue.json"

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
    "docs/GROWTH_CYCLE_LAW.md",
    "docs/GROWTH_CYCLE_OWNER_REPO_REQUESTS.md",
    "parts/README.md",
)

PARTS = (
    "checkpoint-intake",
    "reviewed-closeout-chain",
    "donor-harvest",
    "progression-lift",
    "route-forks",
    "automation-opportunity",
    "diagnosis-gate",
    "repair-cycle",
    "quest-promotion",
    "owner-followthrough",
)

PART_README_HEADINGS = (
    "## Use When",
    "## Do Not Use When",
    "## Route Check",
    "## Active Outputs",
    "## Next Route",
)

OWNER_REQUEST_IDS = (
    "ORQ-GROWTHCYCLE-SDK-001",
    "ORQ-GROWTHCYCLE-SKILLS-001",
    "ORQ-GROWTHCYCLE-AGENTS-001",
    "ORQ-GROWTHCYCLE-EVALS-001",
    "ORQ-GROWTHCYCLE-MEMO-001",
    "ORQ-GROWTHCYCLE-PLAYBOOKS-001",
    "ORQ-GROWTHCYCLE-STATS-001",
    "ORQ-GROWTHCYCLE-ROUTING-001",
    "ORQ-GROWTHCYCLE-DIONYSUS-001",
    "ORQ-GROWTHCYCLE-STACK-001",
)

OWNER_REPOS = (
    "aoa-sdk",
    "aoa-skills",
    "aoa-agents",
    "aoa-evals",
    "aoa-memo",
    "aoa-playbooks",
    "aoa-stats",
    "aoa-routing",
    "Dionysus",
    "abyss-stack",
)

MUST_NOT_CLAIM = (
    "hook implementation authority",
    "executable skill truth",
    "proof verdict",
    "memory canon",
    "runtime activation",
    "owner acceptance",
    "hidden scheduler or autonomous self-repair",
    "universal progression score",
    "quest promotion authority without reviewed evidence",
    "method-growth final object truth",
)

ACTIVE_NOISE_TERMS = (
    "low-context model",
    "4b model",
    "raw source list",
    "sibling implementation history",
)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def contains_phrase(text: str, phrase: str) -> bool:
    compact_text = re.sub(r"\s+", " ", text).casefold()
    compact_phrase = re.sub(r"\s+", " ", phrase).casefold()
    return compact_phrase in compact_text


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_required_files(problems: list[str]) -> None:
    for item in REQUIRED_TOP_LEVEL:
        path = PACKAGE_ROOT / item
        if not path.exists():
            problems.append(f"missing required Growth Cycle surface: {rel(path)}")
        elif path.is_file() and not read(path).endswith("\n"):
            problems.append(f"{rel(path)}: missing final newline")


def validate_card(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "README.md")
    required_phrases = (
        "Status: `landed`",
        "Center growth-cycle law, stage order, stop-lines",
        "AoA owns the law and route grammar for Growth Cycle.",
        "Generated surfaces may reflect Growth Cycle cards",
    )
    for phrase in required_phrases:
        if not contains_phrase(text, phrase):
            problems.append(f"mechanics/growth-cycle/README.md: missing card phrase {phrase!r}")
    for stop_line in MUST_NOT_CLAIM:
        if not contains_phrase(text, stop_line):
            problems.append(f"mechanics/growth-cycle/README.md: missing must-not-claim {stop_line!r}")
    for owner in OWNER_REPOS:
        if owner not in text:
            problems.append(f"mechanics/growth-cycle/README.md: missing owner route {owner!r}")


def validate_parts(problems: list[str]) -> None:
    parts_text = read(PACKAGE_ROOT / "PARTS.md")
    parts_index = read(PACKAGE_ROOT / "parts" / "README.md")
    for part in PARTS:
        if f"parts/{part}/README.md" not in parts_text:
            problems.append(f"mechanics/growth-cycle/PARTS.md: missing part link for {part}")
        if f"{part}/README.md" not in parts_index:
            problems.append(f"mechanics/growth-cycle/parts/README.md: missing part link for {part}")
        path = PACKAGE_ROOT / "parts" / part / "README.md"
        if not path.is_file():
            problems.append(f"missing Growth Cycle part file: {rel(path)}")
            continue
        text = read(path)
        if not text.endswith("\n"):
            problems.append(f"{rel(path)}: missing final newline")
        for heading in PART_README_HEADINGS:
            if heading not in text:
                problems.append(f"{rel(path)}: missing heading {heading}")


def validate_owner_surfaces(problems: list[str]) -> None:
    owner_map = read(PACKAGE_ROOT / "OWNER_MAP.md")
    owner_requests = read(PACKAGE_ROOT / "OWNER_REQUESTS.md")
    if "A request packet is not owner acceptance" not in owner_requests:
        problems.append("mechanics/growth-cycle/OWNER_REQUESTS.md: missing owner-acceptance stop-line")
    for owner in OWNER_REPOS:
        if owner not in owner_map:
            problems.append(f"mechanics/growth-cycle/OWNER_MAP.md: missing owner {owner!r}")
    for request_id in OWNER_REQUEST_IDS:
        if request_id not in owner_requests:
            problems.append(f"mechanics/growth-cycle/OWNER_REQUESTS.md: missing request id {request_id}")
    compat = read(PACKAGE_ROOT / "docs" / "GROWTH_CYCLE_OWNER_REPO_REQUESTS.md")
    if "../OWNER_REQUESTS.md" not in compat:
        problems.append("mechanics/growth-cycle/docs/GROWTH_CYCLE_OWNER_REPO_REQUESTS.md: must route to ../OWNER_REQUESTS.md")


def validate_active_route_cleanliness(problems: list[str]) -> None:
    allowed = {
        "mechanics/growth-cycle/AGENTS.md",
        "mechanics/growth-cycle/PROVENANCE.md",
        "mechanics/growth-cycle/LANDING_LOG.md",
    }
    for path in PACKAGE_ROOT.rglob("*.md"):
        path_ref = rel(path)
        if path_ref in allowed:
            continue
        text = read(path)
        for term in ACTIVE_NOISE_TERMS:
            if term in text.casefold():
                problems.append(f"{path_ref}: active route must avoid noisy term {term!r}")


def validate_registry_and_queue(problems: list[str]) -> None:
    registry = load_json(REGISTRY_PATH)
    entry = next((item for item in registry.get("mechanics", []) if item.get("slug") == "growth-cycle"), None)  # type: ignore[union-attr]
    if not isinstance(entry, dict):
        problems.append("mechanics/registry.json: missing growth-cycle entry")
        return
    if entry.get("owner_request_ids") != list(OWNER_REQUEST_IDS):
        problems.append("mechanics/registry.json: growth-cycle owner_request_ids mismatch")
    if "mechanics/growth-cycle/scripts/validate_growth_cycle_mechanic.py" not in entry.get("validation_refs", []):
        problems.append("mechanics/registry.json: growth-cycle validation_refs missing package validator")
    for part in PARTS:
        expected = f"mechanics/growth-cycle/parts/{part}/README.md"
        if expected not in entry.get("canonical_docs", []):
            problems.append(f"mechanics/registry.json: growth-cycle canonical_docs missing {expected}")

    queue = load_json(QUEUE_PATH)
    queue_ids = [req.get("id") for req in queue.get("requests", []) if req.get("mechanic") == "growth-cycle"]  # type: ignore[union-attr]
    if queue_ids != list(OWNER_REQUEST_IDS):
        problems.append("mechanics/owner-request-queue.json: growth-cycle request order mismatch")


def validate_landing_log(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "LANDING_LOG.md")
    required_fields = ("Status:", "Owner boundary:", "Surfaces:", "Validation:", "Stop-lines:", "Next route:")
    for field in required_fields:
        if field not in text:
            problems.append(f"mechanics/growth-cycle/LANDING_LOG.md: missing {field}")
    if not re.search(r"^### .+", text, re.MULTILINE):
        problems.append("mechanics/growth-cycle/LANDING_LOG.md: missing landing entry")


def validate() -> list[str]:
    problems: list[str] = []
    validate_required_files(problems)
    if problems:
        return problems
    validate_card(problems)
    validate_parts(problems)
    validate_owner_surfaces(problems)
    validate_active_route_cleanliness(problems)
    validate_registry_and_queue(problems)
    validate_landing_log(problems)
    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("Growth Cycle mechanic validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] growth-cycle mechanic validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
