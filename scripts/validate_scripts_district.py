#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REGISTRY_PATH = Path("scripts/registry.json")
SCHEMA_VERSION = "aoa_scripts_registry_v1"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require_string(problems: list[str], where: str, value: object) -> None:
    if not isinstance(value, str) or not value.strip():
        problems.append(f"{where} must be a non-empty string")


def require_string_list(problems: list[str], where: str, value: object) -> None:
    if not isinstance(value, list) or not value:
        problems.append(f"{where} must be a non-empty list")
        return
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            problems.append(f"{where}[{index}] must be a non-empty string")


def rel_exists(root: Path, rel: str) -> bool:
    return (root / rel).exists()


def validate_family(root: Path, family: dict[str, Any], seen_paths: dict[str, str]) -> list[str]:
    problems: list[str] = []
    family_id = family.get("family_id")
    where = f"script_families[{family_id or '?'}]"

    require_string(problems, f"{where}.family_id", family_id)
    require_string(problems, f"{where}.role", family.get("role"))
    require_string(problems, f"{where}.source_ref", family.get("source_ref"))
    require_string_list(problems, f"{where}.paths", family.get("paths"))
    require_string_list(problems, f"{where}.must_not_claim", family.get("must_not_claim"))

    source_ref = family.get("source_ref")
    if isinstance(source_ref, str) and not rel_exists(root, source_ref):
        problems.append(f"{where}.source_ref does not exist: {source_ref}")

    paths = family.get("paths", [])
    if isinstance(paths, list):
        for rel in paths:
            if not isinstance(rel, str):
                continue
            if not rel.startswith("scripts/") or not rel.endswith(".py"):
                problems.append(f"{where}.paths entry must be a root scripts Python file: {rel}")
                continue
            if rel in seen_paths:
                problems.append(f"{rel} appears in both {seen_paths[rel]} and {family_id}")
            else:
                seen_paths[rel] = str(family_id)
            if not (root / rel).is_file():
                problems.append(f"{where}.paths entry does not exist: {rel}")

    return problems


def validate(root: Path) -> list[str]:
    problems: list[str] = []
    registry_path = root / REGISTRY_PATH
    if not registry_path.exists():
        return [f"missing scripts registry: {REGISTRY_PATH}"]

    try:
        registry = load_json(registry_path)
    except json.JSONDecodeError as exc:
        return [f"{REGISTRY_PATH} is not valid JSON: {exc}"]

    if not isinstance(registry, dict):
        return [f"{REGISTRY_PATH} must be a JSON object"]

    if registry.get("schema_version") != SCHEMA_VERSION:
        problems.append(f"schema_version must be {SCHEMA_VERSION}")
    if registry.get("authority_ref") != "scripts/README.md":
        problems.append("authority_ref must be scripts/README.md")
    if registry.get("agents_ref") != "scripts/AGENTS.md":
        problems.append("agents_ref must be scripts/AGENTS.md")

    for rel in ("authority_ref", "agents_ref"):
        value = registry.get(rel)
        if isinstance(value, str) and not rel_exists(root, value):
            problems.append(f"{rel} does not exist: {value}")

    root_policy = registry.get("root_policy")
    if not isinstance(root_policy, dict):
        problems.append("root_policy must be an object")
        root_policy = {}
    if root_policy.get("root_python_glob") != "scripts/*.py":
        problems.append("root_policy.root_python_glob must be scripts/*.py")
    require_string(problems, "root_policy.root_role", root_policy.get("root_role"))

    families = registry.get("script_families")
    if not isinstance(families, list) or not families:
        problems.append("script_families must be a non-empty list")
        families = []

    family_ids: set[str] = set()
    seen_paths: dict[str, str] = {}
    for family in families:
        if not isinstance(family, dict):
            problems.append("script_families entries must be objects")
            continue
        family_id = family.get("family_id")
        if isinstance(family_id, str):
            if family_id in family_ids:
                problems.append(f"duplicate family_id: {family_id}")
            family_ids.add(family_id)
        problems.extend(validate_family(root, family, seen_paths))

    discovered = {
        path.relative_to(root).as_posix()
        for path in (root / "scripts").glob("*.py")
        if path.name != "__init__.py"
    }
    registered = set(seen_paths)
    if registered != discovered:
        missing = sorted(discovered - registered)
        stale = sorted(registered - discovered)
        if missing:
            problems.append(f"root scripts missing from registry: {', '.join(missing)}")
        if stale:
            problems.append(f"registry paths missing from scripts/: {', '.join(stale)}")

    homes = registry.get("script_home_globs")
    if not isinstance(homes, list) or not homes:
        problems.append("script_home_globs must be a non-empty list")
        homes = []
    home_refs: set[str] = set()
    for home in homes:
        if not isinstance(home, dict):
            problems.append("script_home_globs entries must be objects")
            continue
        home_ref = home.get("home_ref")
        where = f"script_home_globs[{home_ref or '?'}]"
        require_string(problems, f"{where}.home_ref", home_ref)
        require_string(problems, f"{where}.owner_scope", home.get("owner_scope"))
        require_string(problems, f"{where}.path_glob", home.get("path_glob"))
        if isinstance(home_ref, str):
            if home_ref in home_refs:
                problems.append(f"duplicate home_ref: {home_ref}")
            home_refs.add(home_ref)
        path_glob = home.get("path_glob")
        if isinstance(path_glob, str) and not [path for path in root.glob(path_glob) if path.is_dir()]:
            problems.append(f"{where}.path_glob matches no script homes: {path_glob}")

    require_string_list(problems, "validation_commands", registry.get("validation_commands"))

    readme = root / "scripts/README.md"
    agents = root / "scripts/AGENTS.md"
    if readme.exists():
        readme_text = readme.read_text(encoding="utf-8")
        for family_id in sorted(family_ids):
            if family_id not in readme_text:
                problems.append(f"scripts/README.md does not mention family: {family_id}")
    if agents.exists():
        agents_text = agents.read_text(encoding="utf-8")
        for required in (
            "scripts/registry.json",
            "python scripts/validate_scripts_district.py",
            "requirements-dev.txt",
            "Python 3.12",
        ):
            if required not in agents_text:
                problems.append(f"scripts/AGENTS.md does not mention {required}")

    release_check = root / "scripts/release_check.py"
    if release_check.exists():
        release_text = release_check.read_text(encoding="utf-8")
        if "scripts/validate_scripts_district.py" not in release_text:
            problems.append("release_check.py does not run scripts/validate_scripts_district.py")

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the root scripts district registry.")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()

    problems = validate(root)
    if problems:
        print("Scripts district validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("scripts district validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
