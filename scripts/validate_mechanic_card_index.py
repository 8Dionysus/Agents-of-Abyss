#!/usr/bin/env python3
"""Validate generated/mechanic_card_index.min.json against the registry."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
INDEX_PATH = REPO_ROOT / "generated" / "mechanic_card_index.min.json"
BUILDER_PATH = REPO_ROOT / "scripts" / "build_mechanic_card_index.py"


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_builder():
    spec = importlib.util.spec_from_file_location("build_mechanic_card_index", BUILDER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load build_mechanic_card_index.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    problems: list[str] = []
    if not INDEX_PATH.exists():
        print(f"Mechanic card index validation failed:\n - missing {INDEX_PATH.relative_to(REPO_ROOT)}")
        return 1
    registry = load_json(REGISTRY_PATH)
    index = load_json(INDEX_PATH)
    if index.get("schema_version") != "aoa_mechanic_card_index_v1":
        problems.append("schema_version must be aoa_mechanic_card_index_v1")
    if index.get("source_registry") != "mechanics/registry.json":
        problems.append("source_registry must be mechanics/registry.json")
    if index.get("card_contract_ref") != registry.get("card_contract_ref"):
        problems.append("card_contract_ref must match registry")
    registry_slugs = [entry.get("slug") for entry in registry.get("mechanics", [])]
    index_slugs = [entry.get("slug") for entry in index.get("mechanics", [])]
    if registry_slugs != index_slugs:
        problems.append("mechanic slug order must match registry")
    for item in index.get("mechanics", []):
        rel = item.get("entry_ref")
        if not isinstance(rel, str) or not (REPO_ROOT / rel).exists():
            problems.append(f"entry_ref missing in checkout: {rel}")
        for key in ("trigger", "center_owns", "owner_boundary"):
            if not str(item.get(key, "")).strip():
                problems.append(f"{item.get('slug')}: {key} is empty")
        for key in ("stronger_owner_split", "must_not_claim", "validation_refs", "next_route"):
            if not isinstance(item.get(key), list) or not item.get(key):
                problems.append(f"{item.get('slug')}: {key} must be a non-empty list")
    builder = load_builder()
    expected = builder.dump_compact(builder.build_index(registry))
    actual = INDEX_PATH.read_text(encoding="utf-8")
    if actual != expected:
        problems.append("generated index content does not match builder output")
    if problems:
        print("Mechanic card index validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print(f"[ok] validated {INDEX_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
