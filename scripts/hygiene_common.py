#!/usr/bin/env python3
"""Shared helpers for Wave E link and shape hygiene validators."""
from __future__ import annotations

import fnmatch
import json
from pathlib import Path
from typing import Any, Iterable

CONFIG_PATH = Path("config/link_shape_hygiene.json")
GENERATED_PATH = Path("generated/link_shape_hygiene.min.json")
DEFAULT_EXCLUDE_GLOBS = [
    ".git/**",
    ".mypy_cache/**",
    ".pytest_cache/**",
    ".ruff_cache/**",
    ".venv/**",
    "venv/**",
    "node_modules/**",
    "__pycache__/**",
    ".wave_*_backups/**",
]


def repo_path(root: Path, rel: str | Path) -> Path:
    return (root / rel).resolve()


def relpath(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dump_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def load_config(root: Path) -> dict[str, Any]:
    path = root / CONFIG_PATH
    if not path.exists():
        raise FileNotFoundError(f"missing hygiene config: {CONFIG_PATH}")
    data = load_json(path)
    if not isinstance(data, dict):
        raise ValueError(f"{CONFIG_PATH}: expected JSON object")
    return data


def matches_any(rel: str, patterns: Iterable[str]) -> bool:
    rel = rel.replace("\\", "/")
    return any(fnmatch.fnmatch(rel, pattern) for pattern in patterns)


def iter_markdown_files(root: Path, config: dict[str, Any] | None = None) -> list[Path]:
    config = config or {}
    link_cfg = config.get("link_validation", {}) if isinstance(config, dict) else {}
    scan_globs = link_cfg.get("scan_globs") or ["**/*.md"]
    exclude_globs = list(DEFAULT_EXCLUDE_GLOBS) + list(link_cfg.get("exclude_globs") or [])
    found: dict[str, Path] = {}
    for glob in scan_globs:
        for path in root.glob(glob):
            if not path.is_file():
                continue
            rel = relpath(root, path)
            if matches_any(rel, exclude_globs):
                continue
            found[rel] = path
    return [found[key] for key in sorted(found)]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text_if_changed(path: Path, text: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def resolve_json_path(data: Any, path_expr: str) -> list[Any]:
    """Resolve a small dotted JSON path language with * wildcards."""
    parts = [part for part in path_expr.split(".") if part]
    current = [data]
    for part in parts:
        next_values: list[Any] = []
        for item in current:
            if part == "*":
                if isinstance(item, dict):
                    next_values.extend(item.values())
                elif isinstance(item, list):
                    next_values.extend(item)
                continue
            if isinstance(item, dict) and part in item:
                next_values.append(item[part])
            elif isinstance(item, list):
                for element in item:
                    if isinstance(element, dict) and part in element:
                        next_values.append(element[part])
        current = next_values
    return current
