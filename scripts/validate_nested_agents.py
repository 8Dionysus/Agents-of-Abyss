#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import TypeAlias

REPO_ROOT = Path(__file__).resolve().parents[1]
Issue: TypeAlias = tuple[str, str]

REQUIRED_AGENTS: dict[str, tuple[str, ...]] = {
    "docs/AGENTS.md": (
        "README.md",
        "LAYERS.md",
        "REPO_ROLES.md",
        "FEDERATION_RULES.md",
        "guardrails/",
        "mechanics/<slug>",
        "mechanic receipts",
        "Tree-of-Sophia",
        "python scripts/validate_ecosystem.py",
    ),
    "generated/AGENTS.md": (
        "ecosystem_registry.min.json",
        "machine-readable",
        "shared_maturity",
        "not a hidden second charter",
        "python scripts/validate_ecosystem.py",
    ),
    "schemas/AGENTS.md": (
        "ecosystem-registry.schema.json",
        "contract change",
        "shared-maturity",
        "validate_ecosystem.py",
        "$id",
    ),
    "scripts/AGENTS.md": (
        "validate_ecosystem.py",
        "validate_nested_agents.py",
        "requirements-dev.txt",
        "repo-relative",
        "Python 3.12",
        "python scripts/validate_ecosystem.py",
    ),
}


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def run_validation(repo_root: Path | None = None) -> list[Issue]:
    repo_root = repo_root or REPO_ROOT
    issues: list[Issue] = []

    for relative_path, required_phrases in REQUIRED_AGENTS.items():
        path = repo_root / relative_path
        if not path.is_file():
            issues.append((relative_path, "missing required nested AGENTS.md"))
            continue

        raw_text = path.read_text(encoding="utf-8")
        stripped = raw_text.strip()
        if not stripped.startswith("# AGENTS.md"):
            issues.append((relative_path, "missing '# AGENTS.md' heading"))

        text = normalize(raw_text)
        for phrase in required_phrases:
            if normalize(phrase) not in text:
                issues.append((relative_path, f"missing required phrase: {phrase}"))

    return issues


def main() -> int:
    issues = run_validation(REPO_ROOT)
    if issues:
        print("Nested AGENTS docs check failed.")
        for location, message in issues:
            print(f"- {location}: {message}")
        return 1

    print(f"Nested AGENTS docs check passed for {len(REQUIRED_AGENTS)} directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
