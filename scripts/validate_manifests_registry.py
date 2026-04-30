#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "manifests" / "registry.json"
MANIFESTS_ROOT = ROOT / "manifests"


def fail(message: str) -> int:
    print(f"manifest registry validation failed: {message}", file=sys.stderr)
    return 1


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if not REGISTRY.exists():
        return fail("missing manifests/registry.json")

    data = load_json(REGISTRY)
    if data.get("schema_version") != "aoa_manifests_registry_v1":
        return fail("schema_version must be aoa_manifests_registry_v1")
    if data.get("authority_ref") != "manifests/README.md":
        return fail("authority_ref must be manifests/README.md")

    root_json = {path.name for path in MANIFESTS_ROOT.glob("*.json")}
    allowed_root_json = set(data.get("root_policy", {}).get("root_json_files", []))
    if root_json != allowed_root_json:
        return fail(f"root manifests JSON mismatch: {sorted(root_json)} != {sorted(allowed_root_json)}")

    homes = data.get("manifest_homes")
    if not isinstance(homes, list) or not homes:
        return fail("manifest_homes must be a non-empty list")

    refs: set[str] = set()
    for home in homes:
        home_ref = home.get("home_ref")
        if not isinstance(home_ref, str) or not home_ref:
            return fail("home missing home_ref")
        if home_ref in refs:
            return fail(f"duplicate home_ref: {home_ref}")
        refs.add(home_ref)

        for key in (
            "path",
            "owner_repo",
            "owner_mechanic",
            "owner_part",
            "publication_scope",
            "component_glob",
            "hook_glob",
            "validator",
        ):
            if not isinstance(home.get(key), str) or not home[key]:
                return fail(f"{home_ref} missing {key}")

        home_path = ROOT / home["path"]
        if not home_path.is_dir():
            return fail(f"{home_ref} path does not exist: {home['path']}")
        for local_doc in ("README.md", "AGENTS.md"):
            if not (home_path / local_doc).is_file():
                return fail(f"{home_ref} missing local {local_doc}")

        validator = ROOT / home["validator"]
        if not validator.is_file():
            return fail(f"{home_ref} validator does not exist: {home['validator']}")

        components = sorted(ROOT.glob(home["component_glob"]))
        hooks = sorted(ROOT.glob(home["hook_glob"]))
        if not components:
            return fail(f"{home_ref} has no component manifests")
        if len(components) != len(hooks):
            return fail(f"{home_ref} component/hook count mismatch")

        component_stems = {path.name.removesuffix(".json") for path in components}
        hook_stems = {path.name.removesuffix(".hooks.json") for path in hooks}
        if component_stems != hook_stems:
            return fail(f"{home_ref} component/hook names do not match")

    print("manifest registry validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
