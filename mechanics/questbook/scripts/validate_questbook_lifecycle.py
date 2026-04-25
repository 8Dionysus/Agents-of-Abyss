#!/usr/bin/env python3
"""Validate Questbook lifecycle board placement."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - exercised by release env
    yaml = None


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


REPO_ROOT = _repo_root()
QUESTS_DIR = REPO_ROOT / "quests"
LIFECYCLE_STATES = (
    "captured",
    "triaged",
    "ready",
    "active",
    "blocked",
    "reanchor",
    "done",
    "dropped",
)
CLOSED_STATES = {"done", "dropped"}


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def fail(problems: list[str], message: str) -> None:
    problems.append(message)


def state_from_yaml(path: Path, problems: list[str]) -> str | None:
    if yaml is None:
        fail(problems, "PyYAML is required to validate YAML quest lifecycle state")
        return None
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report validation context
        fail(problems, f"{rel(path)}: cannot parse YAML quest: {exc}")
        return None
    if not isinstance(payload, dict):
        fail(problems, f"{rel(path)}: YAML quest must be an object")
        return None
    quest_id = payload.get("id")
    if quest_id != path.stem:
        fail(problems, f"{rel(path)}: id must match filename stem")
    state = payload.get("state")
    if state not in LIFECYCLE_STATES:
        fail(problems, f"{rel(path)}: unsupported quest state {state!r}")
        return None
    if payload.get("public_safe") is not True:
        fail(problems, f"{rel(path)}: public_safe must be true")
    return str(state)


def validate_lifecycle_dirs(problems: list[str]) -> None:
    for state in LIFECYCLE_STATES:
        state_dir = QUESTS_DIR / state
        if not state_dir.is_dir():
            fail(problems, f"{rel(state_dir)}: missing lifecycle directory")
            continue
        readme = state_dir / "README.md"
        if not readme.is_file():
            fail(problems, f"{rel(readme)}: lifecycle directory needs a README gate")


def validate_root_entries_absent(problems: list[str]) -> None:
    for path in sorted(QUESTS_DIR.glob("AOA-Q-*")):
        fail(problems, f"{rel(path)}: root quest aliases are not allowed; use quests/<lifecycle-state>/{path.name}")


def validate_source_items(problems: list[str]) -> None:
    source_names: set[str] = set()
    for state in LIFECYCLE_STATES:
        state_dir = QUESTS_DIR / state
        if not state_dir.is_dir():
            continue
        for path in sorted(state_dir.glob("AOA-Q-*")):
            if path.suffix not in {".md", ".yaml"}:
                fail(problems, f"{rel(path)}: quest source must be markdown or YAML")
                continue
            if path.name in source_names:
                fail(problems, f"{rel(path)}: duplicate quest source filename")
            source_names.add(path.name)
            if path.suffix == ".yaml":
                payload_state = state_from_yaml(path, problems)
                if payload_state is not None and payload_state != state:
                    fail(
                        problems,
                        f"{rel(path)}: YAML state {payload_state!r} must match lifecycle directory {state!r}",
                    )


def validate_public_index(problems: list[str]) -> None:
    questbook = (REPO_ROOT / "QUESTBOOK.md").read_text(encoding="utf-8")
    required_phrases = (
        "lifecycle directories under [`quests/`](quests/)",
        "Top-level `quests/AOA-Q-*` aliases are intentionally absent",
    )
    for phrase in required_phrases:
        if phrase not in questbook:
            fail(problems, f"QUESTBOOK.md must say: {phrase}")


def main() -> int:
    problems: list[str] = []
    validate_lifecycle_dirs(problems)
    validate_root_entries_absent(problems)
    validate_source_items(problems)
    validate_public_index(problems)
    if problems:
        print("Questbook lifecycle validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] questbook lifecycle board validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
