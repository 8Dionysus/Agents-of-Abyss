from __future__ import annotations

import hashlib
import json
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


def inherited_chain_paths(rel: Path, registered_paths: Iterable[Path]) -> list[Path]:
    registered = {path.as_posix() for path in registered_paths}
    candidates = [Path("AGENTS.md")]
    current = Path()
    for part in rel.parent.parts:
        current /= part
        candidates.append(current / "AGENTS.md")
    return [candidate for candidate in candidates if candidate.as_posix() in registered]


def read_config(repo_root: Path) -> dict[str, Any]:
    path = repo_root / DEFAULT_CONFIG
    if not path.exists():
        raise SystemExit(f"missing AGENTS mesh config: {path}")
    return load_json(path)


def card_summary(
    repo_root: Path,
    rel: Path,
    registered_paths: Iterable[Path],
    chain_budget_bytes: int,
) -> dict[str, Any]:
    path = repo_root / rel
    text = path.read_text(encoding="utf-8")
    headings = markdown_headings(text)
    chain_paths = inherited_chain_paths(rel, registered_paths)
    chain_bytes = sum(len((repo_root / chain_path).read_bytes()) for chain_path in chain_paths)
    return {
        "path": rel.as_posix(),
        "sha256": sha256_text(text),
        "bytes": len(text.encode("utf-8")),
        "line_count": len(text.splitlines()),
        "heading_count": len(headings),
        "headings": headings[:12],
        "inherited_chain_paths": [item.as_posix() for item in chain_paths],
        "inherited_chain_bytes": chain_bytes,
        "inherited_chain_headroom_bytes": chain_budget_bytes - chain_bytes,
        "inherited_chain_over_budget": chain_bytes > chain_budget_bytes,
    }


def build_index(repo_root: Path) -> dict[str, Any]:
    config = read_config(repo_root)
    registered_paths = relative_agent_paths(config)
    chain_budget_bytes = int(config.get("chain_budget_bytes", 32768))
    cards = []
    missing = []
    for rel in registered_paths:
        if (repo_root / rel).exists():
            cards.append(card_summary(repo_root, rel, registered_paths, chain_budget_bytes))
        else:
            missing.append(rel.as_posix())
    chains_over_budget = [card["path"] for card in cards if card["inherited_chain_over_budget"]]
    return {
        "schema_version": "aoa_agents_mesh_index_v2",
        "source_ref": DEFAULT_CONFIG.as_posix(),
        "authority_ref": config.get("authority_ref"),
        "root_agents_ref": config.get("root_agents_ref"),
        "route_contract_ref": config.get("route_contract_ref"),
        "validation_commands": config.get("validation_commands", []),
        "chain_budget_bytes": chain_budget_bytes,
        "chain_max_bytes": max((card["inherited_chain_bytes"] for card in cards), default=0),
        "chains_over_budget": chains_over_budget,
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
