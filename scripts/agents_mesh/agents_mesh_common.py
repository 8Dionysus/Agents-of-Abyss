from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

ROOT_MARKERS = ("CHARTER.md", "ECOSYSTEM_MAP.md", "README.md")
DEFAULT_CONFIG = Path("config/agents_mesh.json")
DEFAULT_GENERATED = Path("generated/agents_mesh.min.json")


def repo_root_from(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    for candidate in [cur, *cur.parents]:
        if all((candidate / marker).exists() for marker in ROOT_MARKERS[:2]):
            return candidate
    return cur


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_min_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def markdown_headings(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.startswith("#")]


def relative_agent_paths(config: dict[str, Any]) -> list[Path]:
    return [Path(entry["path"]) for entry in config.get("entries", []) if entry.get("status") == "required"]


def read_config(repo_root: Path) -> dict[str, Any]:
    path = repo_root / DEFAULT_CONFIG
    if not path.exists():
        raise SystemExit(f"missing AGENTS mesh config: {path}")
    return load_json(path)


def card_summary(repo_root: Path, rel: Path) -> dict[str, Any]:
    path = repo_root / rel
    text = path.read_text(encoding="utf-8")
    headings = markdown_headings(text)
    return {
        "path": rel.as_posix(),
        "sha256": sha256_text(text),
        "line_count": len(text.splitlines()),
        "heading_count": len(headings),
        "headings": headings[:12],
    }


def build_index(repo_root: Path) -> dict[str, Any]:
    config = read_config(repo_root)
    cards = []
    missing = []
    for rel in relative_agent_paths(config):
        if (repo_root / rel).exists():
            cards.append(card_summary(repo_root, rel))
        else:
            missing.append(rel.as_posix())
    return {
        "schema_version": "aoa_agents_mesh_index_v1",
        "source_ref": DEFAULT_CONFIG.as_posix(),
        "authority_ref": config.get("authority_ref"),
        "root_agents_ref": config.get("root_agents_ref"),
        "route_contract_ref": config.get("route_contract_ref"),
        "validation_commands": config.get("validation_commands", []),
        "card_count": len(cards),
        "missing_cards": missing,
        "cards": cards,
    }


def is_binary_like(path: Path) -> bool:
    try:
        raw = path.read_bytes()[:2048]
    except OSError:
        return True
    return b"\0" in raw
