"""Shared Questbook lane/lifecycle helpers."""

from __future__ import annotations

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
    "questbook",
    "antifragility",
    "method-growth",
    "release-support",
    "tos-bridge",
)

ID_PREFIX_LANES = {
    "AOA-Q-AGON-": "agon",
    "AOA-Q-EXP-": "experience",
    "AOA-Q-RPG-": "rpg",
    "AOA-Q-RECURRENCE-": "recurrence",
    "AOA-Q-QUESTBOOK-": "questbook",
    "AOA-Q-ANTIFRAGILITY-": "antifragility",
    "AOA-Q-METHOD-": "method-growth",
    "AOA-Q-RELEASE-": "release-support",
    "AOA-Q-TOS-": "tos-bridge",
}


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
                if path.suffix == ".yaml":
                    payload = read_yaml(path)
                    title = str(payload.get("title") or title)
                    band_value = payload.get("band")
                    if isinstance(band_value, str):
                        band = band_value
                items.append(
                    {
                        "id": quest_id,
                        "title": title,
                        "lane": lane,
                        "state": state,
                        "path": rel(path),
                        "format": path.suffix.removeprefix("."),
                        "band": band,
                        "closed": state in CLOSED_STATES,
                    }
                )
    return items
