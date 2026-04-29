#!/usr/bin/env python3
"""Validate the Audit mechanic package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "audit"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
QUEUE_PATH = REPO_ROOT / "mechanics" / "owner-request-queue.json"

PARTS = (
    "source-map",
    "evidence-ledger",
    "risk-signal",
    "finding-lifecycle",
    "owner-routing",
    "validation-gate",
    "campaign-route",
    "audit-event-bridge",
)

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
    "docs/AGENTS.md",
    "docs/AUDIT_LAW.md",
    "docs/AUDIT_OWNER_REPO_REQUESTS.md",
    "parts/AGENTS.md",
    "parts/README.md",
    "legacy/AGENTS.md",
    "legacy/README.md",
    "legacy/INDEX.md",
    "legacy/raw/README.md",
)

PART_FILES = ("README.md", "CONTRACT.md", "VALIDATION.md")
PART_README_HEADINGS = ("## Use When", "## Do Not Use When", "## Route Check", "## Active Outputs", "## Next Route")
LEGACY_RAW = (
    "CODEX_AUDIT_PROTOCOL.md",
    "CODEX_SKILL_PROOF_AUDIT_BRIDGE.md",
    "DELETION_CANDIDATES.json",
    "DOCS_AUDITS_AGENTS.md",
    "DOCS_AUDITS_README.md",
    "DOCUMENTATION_SURFACE_AUDIT_2026_04_24.md",
    "ROOT_SURFACE_AUDIT_2026_04_24.md",
)
OWNER_REQUEST_IDS = (
    "ORQ-AUDIT-EVALS-001",
    "ORQ-AUDIT-MEMO-001",
    "ORQ-AUDIT-PLAYBOOKS-001",
    "ORQ-AUDIT-SKILLS-001",
    "ORQ-AUDIT-AGENTS-001",
    "ORQ-AUDIT-STATS-001",
)
MUST_NOT_CLAIM = (
    "proof verdict",
    "owner-local remediation",
    "runtime authority",
    "memory truth",
    "release support authority",
    "generated authority",
    "archive evidence as active law",
    "private scratch notes as public audit evidence",
    "cleanup candidate as deletion approval",
)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def contains_phrase(text: str, phrase: str) -> bool:
    compact_text = re.sub(r"\s+", " ", text).casefold()
    compact_phrase = re.sub(r"\s+", " ", phrase).casefold()
    return compact_phrase in compact_text


def active_markdown_paths() -> list[Path]:
    paths: list[Path] = []
    for path in PACKAGE_ROOT.rglob("*.md"):
        rel_parts = path.relative_to(PACKAGE_ROOT).parts
        if "legacy" in rel_parts:
            continue
        paths.append(path)
    return paths


def validate_required_files(problems: list[str]) -> None:
    for item in REQUIRED_TOP_LEVEL:
        path = PACKAGE_ROOT / item
        if not path.exists():
            problems.append(f"missing required audit surface: {rel(path)}")
        elif path.is_file() and not read(path).endswith("\n"):
            problems.append(f"{rel(path)}: missing final newline")
    for part in PARTS:
        for filename in PART_FILES:
            path = PACKAGE_ROOT / "parts" / part / filename
            if not path.exists():
                problems.append(f"missing audit part surface: {rel(path)}")
            elif not read(path).endswith("\n"):
                problems.append(f"{rel(path)}: missing final newline")


def validate_parts(problems: list[str]) -> None:
    parts_text = read(PACKAGE_ROOT / "PARTS.md")
    index_text = read(PACKAGE_ROOT / "parts" / "README.md")
    for part in PARTS:
        if f"parts/{part}/README.md" not in parts_text:
            problems.append(f"mechanics/audit/PARTS.md: missing part link for {part}")
        if f"{part}/README.md" not in index_text:
            problems.append(f"mechanics/audit/parts/README.md: missing part link for {part}")
        part_readme = PACKAGE_ROOT / "parts" / part / "README.md"
        if not part_readme.exists():
            continue
        text = read(part_readme)
        for heading in PART_README_HEADINGS:
            if heading not in text:
                problems.append(f"{rel(part_readme)}: missing heading {heading}")


def validate_card(problems: list[str]) -> None:
    text = read(PACKAGE_ROOT / "README.md")
    required_phrases = (
        "Status: `planted`",
        "Audit grammar, finding lifecycle, evidence-ledger posture",
        "Use when a surface, claim, route, owner boundary, evidence trail, or change result must be seen clearly enough",
        "Generated surfaces do not author meaning.",
    )
    for phrase in required_phrases:
        if not contains_phrase(text, phrase):
            problems.append(f"mechanics/audit/README.md: missing card phrase {phrase!r}")
    for claim in MUST_NOT_CLAIM:
        if not contains_phrase(text, claim):
            problems.append(f"mechanics/audit/README.md: missing must-not-claim {claim!r}")


def validate_legacy_bridge(problems: list[str]) -> None:
    provenance = read(PACKAGE_ROOT / "PROVENANCE.md")
    legacy_index = read(PACKAGE_ROOT / "legacy" / "INDEX.md")
    raw_readme = read(PACKAGE_ROOT / "legacy" / "raw" / "README.md")
    for item in LEGACY_RAW:
        path = PACKAGE_ROOT / "legacy" / "raw" / item
        if not path.exists():
            problems.append(f"missing audit raw source: {rel(path)}")
        for label, text in (("PROVENANCE.md", provenance), ("legacy/INDEX.md", legacy_index), ("legacy/raw/README.md", raw_readme)):
            if item not in text:
                problems.append(f"mechanics/audit/{label}: missing raw source {item}")
    if (REPO_ROOT / "docs" / "audits").exists():
        problems.append("docs/audits must not exist after audit mechanic landing")


def validate_active_cleanliness(problems: list[str]) -> None:
    for path in active_markdown_paths():
        path_ref = rel(path)
        text = read(path)
        if re.search(r"\baudit\s+is\s+not\b", text, re.IGNORECASE):
            problems.append(f"{path_ref}: use positive audit grammar instead of 'audit is not' phrasing")
        if path.name != "AGENTS.md" and "```bash" in text:
            problems.append(f"{path_ref}: executable command blocks belong in AGENTS.md")
        if path.name != "AGENTS.md" and re.search(r"(?:^|`)python (?:scripts|mechanics)/", text, re.MULTILINE):
            problems.append(f"{path_ref}: executable validation commands belong in AGENTS.md")


def validate_registry_and_queue(problems: list[str]) -> None:
    registry = load_json(REGISTRY_PATH)
    entry = next((item for item in registry.get("mechanics", []) if item.get("slug") == "audit"), None)  # type: ignore[union-attr]
    if not isinstance(entry, dict):
        problems.append("mechanics/registry.json: missing audit entry")
        return
    if entry.get("owner_request_ids") != list(OWNER_REQUEST_IDS):
        problems.append("mechanics/registry.json: audit owner_request_ids mismatch")
    if "mechanics/audit/scripts/validate_audit_distillation.py" not in entry.get("validation_refs", []):
        problems.append("mechanics/registry.json: audit validation_refs missing package validator")
    for part in PARTS:
        expected = f"mechanics/audit/parts/{part}/README.md"
        if expected not in entry.get("canonical_docs", []):
            problems.append(f"mechanics/registry.json: audit canonical_docs missing {expected}")

    queue = load_json(QUEUE_PATH)
    queue_ids = [req.get("id") for req in queue.get("requests", []) if req.get("mechanic") == "audit"]  # type: ignore[union-attr]
    if queue_ids != list(OWNER_REQUEST_IDS):
        problems.append("mechanics/owner-request-queue.json: audit request order mismatch")


def main() -> int:
    problems: list[str] = []
    validate_required_files(problems)
    if not problems:
        validate_parts(problems)
        validate_card(problems)
        validate_legacy_bridge(problems)
        validate_active_cleanliness(problems)
        validate_registry_and_queue(problems)
    if problems:
        print("Audit mechanic validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] audit mechanic validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
