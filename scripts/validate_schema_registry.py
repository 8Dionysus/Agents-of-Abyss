#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, SchemaError


def fail(message: str) -> int:
    print(f"schema registry validation failed: {message}", file=sys.stderr)
    return 1


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_path_list(repo_root: Path, label: str, paths: list[str], owner: str) -> str | None:
    if not isinstance(paths, list) or not paths:
        return f"{owner} {label} must be a non-empty list"
    for ref in paths:
        if not isinstance(ref, str) or not ref:
            return f"{owner} {label} contains an invalid path"
        if not (repo_root / ref).is_file():
            return f"{owner} {label} missing path: {ref}"
    return None


def validate_root_schema(repo_root: Path, item: dict[str, Any]) -> str | None:
    path_ref = item.get("path")
    if not isinstance(path_ref, str) or not path_ref.startswith("schemas/"):
        return "root schema entry has invalid path"
    path = repo_root / path_ref
    if not path.is_file():
        return f"registered root schema missing: {path_ref}"

    schema = load_json(path)
    for key in ("$schema", "$id", "title", "type"):
        if key not in schema:
            return f"{path_ref} missing schema key {key}"
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        return f"{path_ref} is not a valid Draft 2020-12 schema: {exc.message}"

    for key in ("owner_repo", "owner_surface", "publication_scope"):
        if not isinstance(item.get(key), str) or not item[key]:
            return f"{path_ref} missing registry key {key}"
    if item["owner_repo"] != "Agents-of-Abyss":
        return f"{path_ref} owner_repo must be Agents-of-Abyss"
    if not (repo_root / item["owner_surface"]).is_file():
        return f"{path_ref} owner_surface missing: {item['owner_surface']}"

    for label in ("source_refs", "generated_refs", "validator_refs", "test_refs"):
        problem = validate_path_list(repo_root, label, item.get(label), path_ref)
        if problem:
            return problem
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate root schema district registry.")
    parser.add_argument("--repo-root", default=None)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path(__file__).resolve().parents[1]
    schemas_root = repo_root / "schemas"
    registry_path = schemas_root / "registry.json"
    if not registry_path.is_file():
        return fail("missing schemas/registry.json")

    data = load_json(registry_path)
    if data.get("schema_version") != "aoa_schema_registry_v1":
        return fail("schema_version must be aoa_schema_registry_v1")
    if data.get("authority_ref") != "schemas/README.md":
        return fail("authority_ref must be schemas/README.md")

    root_json = {path.name for path in schemas_root.glob("*.json")}
    allowed_root_json = set(data.get("root_policy", {}).get("root_json_files", []))
    if root_json != allowed_root_json:
        return fail(f"root schemas JSON mismatch: {sorted(root_json)} != {sorted(allowed_root_json)}")

    root_schemas = data.get("root_schemas")
    if not isinstance(root_schemas, list) or not root_schemas:
        return fail("root_schemas must be a non-empty list")

    registered = {item.get("path") for item in root_schemas if isinstance(item, dict)}
    discovered = {
        path.relative_to(repo_root).as_posix()
        for path in schemas_root.glob("*.json")
        if path.name != "registry.json"
    }
    if registered != discovered:
        return fail(f"root schema registry mismatch: {sorted(registered)} != {sorted(discovered)}")

    seen: set[str] = set()
    for item in root_schemas:
        if not isinstance(item, dict):
            return fail("root_schemas entries must be objects")
        path_ref = str(item.get("path", ""))
        if path_ref in seen:
            return fail(f"duplicate root schema entry: {path_ref}")
        seen.add(path_ref)
        problem = validate_root_schema(repo_root, item)
        if problem:
            return fail(problem)

    homes = data.get("schema_home_globs")
    if not isinstance(homes, list) or not homes:
        return fail("schema_home_globs must be a non-empty list")
    home_refs: set[str] = set()
    for home in homes:
        if not isinstance(home, dict):
            return fail("schema_home_globs entries must be objects")
        home_ref = home.get("home_ref")
        path_glob = home.get("path_glob")
        if not isinstance(home_ref, str) or not home_ref:
            return fail("schema home missing home_ref")
        if home_ref in home_refs:
            return fail(f"duplicate schema home_ref: {home_ref}")
        home_refs.add(home_ref)
        if not isinstance(path_glob, str) or not path_glob:
            return fail(f"{home_ref} missing path_glob")
        matches = [path for path in repo_root.glob(path_glob) if path.is_dir()]
        if not matches:
            return fail(f"{home_ref} path_glob has no schema homes: {path_glob}")
        for match in matches:
            if not any(child.is_file() and child.suffix == ".json" for child in match.iterdir()):
                return fail(f"{home_ref} schema home has no JSON schemas: {match.relative_to(repo_root)}")

    print("schema registry validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
