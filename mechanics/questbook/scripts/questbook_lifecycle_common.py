"""Shared Questbook lane/lifecycle helpers."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - exercised by release env
    yaml = None


def repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


REPO_ROOT = repo_root()
QUESTS_DIR = REPO_ROOT / "quests"
GENERATED_INDEX_PATH = REPO_ROOT / "generated" / "questbook_index.min.json"
GENERATED_FRONTIER_PATH = REPO_ROOT / "generated" / "questbook_frontier.min.json"
GENERATED_RELATIONS_PATH = REPO_ROOT / "generated" / "questbook_relations.min.json"

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
OPEN_STATES = tuple(state for state in LIFECYCLE_STATES if state not in CLOSED_STATES)

QUEST_LANES = (
    "center",
    "agon",
    "experience",
    "rpg",
    "recurrence",
    "checkpoint",
    "questbook",
    "antifragility",
    "method-growth",
    "release-support",
    "boundary-bridge",
)

ID_PREFIX_LANES = {
    "AOA-Q-AGON-": "agon",
    "AOA-Q-EXP-": "experience",
    "AOA-Q-RPG-": "rpg",
    "AOA-Q-RECURRENCE-": "recurrence",
    "AOA-Q-CHECKPOINT-": "checkpoint",
    "AOA-Q-QUESTBOOK-": "questbook",
    "AOA-Q-ANTIFRAGILITY-": "antifragility",
    "AOA-Q-METHOD-": "method-growth",
    "AOA-Q-RELEASE-": "release-support",
    "AOA-Q-BRIDGE-": "boundary-bridge",
    "AOA-Q-TOS-": "boundary-bridge",
}

RELATION_TYPES = (
    "parent",
    "sidequest",
    "related",
    "blocks",
    "blocked_by",
    "reanchors_to",
    "supersedes",
    "superseded_by",
)

QUEST_ID_PATTERN = re.compile(r"\bAOA-Q(?:-[A-Za-z0-9]+)+\b")


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def lane_for_quest_id(quest_id: str) -> str:
    for prefix, lane in ID_PREFIX_LANES.items():
        if quest_id.startswith(prefix):
            return lane
    return "center"


def read_yaml(path: Path) -> dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML is required to read YAML quest sources")
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("YAML quest must be an object")
    return payload


def markdown_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return path.stem


def normalize_relation_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        stripped = value.strip()
        return [stripped] if stripped else []
    if isinstance(value, (list, tuple)):
        refs: list[str] = []
        for item in value:
            refs.extend(normalize_relation_value(item))
        return refs
    raise ValueError(f"relation value must be a string or list, got {type(value).__name__}")


def add_relation(relations: dict[str, list[str]], relation_type: str, refs: list[str]) -> None:
    if not refs:
        return
    bucket = relations.setdefault(relation_type, [])
    for ref in refs:
        if ref not in bucket:
            bucket.append(ref)


def read_yaml_relations(payload: dict[str, Any]) -> dict[str, list[str]]:
    relations: dict[str, list[str]] = {}
    declared = payload.get("relations")
    if declared is not None:
        if not isinstance(declared, dict):
            raise ValueError("relations must be an object")
        for relation_type, value in declared.items():
            add_relation(relations, str(relation_type), normalize_relation_value(value))

    add_relation(relations, "parent", normalize_relation_value(payload.get("parent")))
    add_relation(relations, "blocked_by", normalize_relation_value(payload.get("depends_on")))
    return {key: value for key, value in relations.items() if value}


def read_markdown_relations(path: Path) -> dict[str, list[str]]:
    relations: dict[str, list[str]] = {}
    in_section = False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "## Relations":
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if not in_section:
            continue
        match = re.match(r"^\s*[-*]\s*([a-z_]+):\s*(.+?)\s*$", line)
        if not match:
            continue
        relation_type, value = match.groups()
        refs = QUEST_ID_PATTERN.findall(value)
        add_relation(relations, relation_type, refs)
    return {key: value for key, value in relations.items() if value}


def read_quest_relations(path: Path, payload: dict[str, Any] | None = None) -> dict[str, list[str]]:
    if path.suffix == ".yaml":
        if payload is None:
            payload = read_yaml(path)
        return read_yaml_relations(payload)
    if path.suffix == ".md":
        return read_markdown_relations(path)
    return {}


def iter_quest_sources() -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for lane in QUEST_LANES:
        lane_dir = QUESTS_DIR / lane
        if not lane_dir.is_dir():
            continue
        for state in LIFECYCLE_STATES:
            state_dir = lane_dir / state
            if not state_dir.exists():
                continue
            for path in sorted(state_dir.glob("AOA-Q-*")):
                if not path.is_file():
                    continue
                quest_id = path.stem
                title = markdown_title(path)
                band = None
                relations: dict[str, list[str]] = {}
                if path.suffix == ".yaml":
                    payload = read_yaml(path)
                    title = str(payload.get("title") or title)
                    band_value = payload.get("band")
                    if isinstance(band_value, str):
                        band = band_value
                    relations = read_quest_relations(path, payload)
                elif path.suffix == ".md":
                    relations = read_quest_relations(path)
                item = {
                    "id": quest_id,
                    "title": title,
                    "lane": lane,
                    "state": state,
                    "path": rel(path),
                    "format": path.suffix.removeprefix("."),
                    "band": band,
                    "closed": state in CLOSED_STATES,
                }
                if relations:
                    item["relations"] = relations
                items.append(item)
    return items
