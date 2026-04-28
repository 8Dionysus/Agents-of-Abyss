#!/usr/bin/env python3
"""Validate the root config district registry."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REGISTRY_PATH = Path("config/registry.json")
SCHEMA_VERSION = "aoa_config_registry_v1"
VALID_STATUSES = {"active", "planned", "retired"}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def rel_exists(root: Path, rel: str) -> bool:
    return (root / rel).exists()


def require_string(problems: list[str], where: str, value: object) -> None:
    if not isinstance(value, str) or not value.strip():
        problems.append(f"{where} must be a non-empty string")


def require_string_list(problems: list[str], where: str, value: object, *, allow_empty: bool = False) -> None:
    if not isinstance(value, list):
        problems.append(f"{where} must be a list")
        return
    if not allow_empty and not value:
        problems.append(f"{where} must not be empty")
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            problems.append(f"{where}[{index}] must be a non-empty string")


def validate_entry(root: Path, entry: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    entry_id = entry.get("id")
    path_value = entry.get("path")
    where = f"configs[{entry_id or '?'}]"

    require_string(problems, f"{where}.id", entry_id)
    require_string(problems, f"{where}.path", path_value)
    require_string(problems, f"{where}.owner", entry.get("owner"))
    require_string(problems, f"{where}.role", entry.get("role"))
    require_string(problems, f"{where}.source_ref", entry.get("source_ref"))
    require_string_list(problems, f"{where}.generated_refs", entry.get("generated_refs"), allow_empty=True)
    require_string_list(problems, f"{where}.consumers", entry.get("consumers"))
    require_string_list(problems, f"{where}.validation_commands", entry.get("validation_commands"))
    require_string_list(problems, f"{where}.must_not_claim", entry.get("must_not_claim"))

    status = entry.get("status")
    if status not in VALID_STATUSES:
        problems.append(f"{where}.status must be one of {sorted(VALID_STATUSES)}")

    if isinstance(path_value, str):
        if not path_value.startswith("config/") or not path_value.endswith(".json"):
            problems.append(f"{where}.path must be a root config JSON path")
        path = root / path_value
        if not path.exists():
            problems.append(f"{where}.path does not exist: {path_value}")
        else:
            try:
                load_json(path)
            except json.JSONDecodeError as exc:
                problems.append(f"{where}.path is not valid JSON: {exc}")

    source_ref = entry.get("source_ref")
    if isinstance(source_ref, str) and not rel_exists(root, source_ref):
        problems.append(f"{where}.source_ref does not exist: {source_ref}")

    index_ref = entry.get("index_ref")
    if index_ref is not None:
        require_string(problems, f"{where}.index_ref", index_ref)
        if isinstance(index_ref, str) and not rel_exists(root, index_ref):
            problems.append(f"{where}.index_ref does not exist: {index_ref}")

    for rel in entry.get("generated_refs", []) if isinstance(entry.get("generated_refs"), list) else []:
        if not rel_exists(root, rel):
            problems.append(f"{where}.generated_refs entry does not exist: {rel}")

    for rel in entry.get("consumers", []) if isinstance(entry.get("consumers"), list) else []:
        if not rel_exists(root, rel):
            problems.append(f"{where}.consumers entry does not exist: {rel}")

    return problems


def validate(root: Path) -> list[str]:
    problems: list[str] = []
    registry_path = root / REGISTRY_PATH
    if not registry_path.exists():
        return [f"missing config registry: {REGISTRY_PATH}"]

    try:
        registry = load_json(registry_path)
    except json.JSONDecodeError as exc:
        return [f"{REGISTRY_PATH} is not valid JSON: {exc}"]

    if not isinstance(registry, dict):
        return [f"{REGISTRY_PATH} must be a JSON object"]

    if registry.get("schema_version") != SCHEMA_VERSION:
        problems.append(f"schema_version must be {SCHEMA_VERSION}")
    require_string(problems, "purpose", registry.get("purpose"))
    require_string(problems, "owner", registry.get("owner"))
    require_string(problems, "district_ref", registry.get("district_ref"))
    require_string(problems, "agents_ref", registry.get("agents_ref"))
    require_string_list(problems, "validation_commands", registry.get("validation_commands"))

    for rel in ("district_ref", "agents_ref"):
        value = registry.get(rel)
        if isinstance(value, str) and not rel_exists(root, value):
            problems.append(f"{rel} does not exist: {value}")

    configs = registry.get("configs")
    if not isinstance(configs, list) or not configs:
        problems.append("configs must be a non-empty list")
        configs = []

    ids: set[str] = set()
    paths: set[str] = set()
    for entry in configs:
        if not isinstance(entry, dict):
            problems.append("configs entries must be JSON objects")
            continue
        entry_id = entry.get("id")
        path_value = entry.get("path")
        if isinstance(entry_id, str):
            if entry_id in ids:
                problems.append(f"duplicate config id: {entry_id}")
            ids.add(entry_id)
        if isinstance(path_value, str):
            if path_value in paths:
                problems.append(f"duplicate config path: {path_value}")
            paths.add(path_value)
        problems.extend(validate_entry(root, entry))

    discovered = sorted(path.relative_to(root).as_posix() for path in (root / "config").glob("*.json"))
    if sorted(paths) != discovered:
        missing = sorted(set(discovered) - paths)
        stale = sorted(paths - set(discovered))
        if missing:
            problems.append(f"config JSON files missing from registry: {', '.join(missing)}")
        if stale:
            problems.append(f"registry paths missing from config/: {', '.join(stale)}")

    readme = root / "config/README.md"
    if readme.exists():
        readme_text = readme.read_text(encoding="utf-8")
        for rel in sorted(paths):
            if rel not in readme_text:
                problems.append(f"config/README.md does not mention registered config: {rel}")

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    problems = validate(root)
    if problems:
        print("Config registry validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] config registry validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
