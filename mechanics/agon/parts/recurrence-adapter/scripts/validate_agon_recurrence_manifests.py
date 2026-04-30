#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


ROOT = _repo_root()
HOME = ROOT / "mechanics" / "agon" / "parts" / "recurrence-adapter" / "manifests"
HOOKS = HOME / "hooks"
REQUEST = (
    ROOT
    / "mechanics"
    / "agon"
    / "parts"
    / "recurrence-adapter"
    / "generated"
    / "agon_recurrence_adapter_request.min.json"
)

COMPONENT_SCHEMA = "aoa_agon_recurrence_component_manifest_v1"
HOOK_SCHEMA = "aoa_agon_recurrence_hook_manifest_v1"
OLD_SERIES_WORD = "wa" + "ve"
OLD_RAW_PATH = "legacy" + "/raw"
OLD_SERIES_FILE_TOKEN = "AGON_" + "WA" + "VE"
OLD_ROOT_MANIFEST_PATH = "manifests" + "/recurrence"
OLD_FLAT_GENERATED_GLOB = "generated/" + "agon_*.min.json"
PRE_NORMALIZED_PREFIX = "legacy" + "_"


def fail(message: str) -> int:
    print(f"agon recurrence manifest validation failed: {message}", file=sys.stderr)
    return 1


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def payload_text(data: dict) -> str:
    return json.dumps(data, sort_keys=True)


def validate_payload_hygiene(path: Path, data: dict) -> int:
    text = payload_text(data)
    if OLD_RAW_PATH in text:
        return fail(f"{path} still references raw source archive paths")
    if OLD_SERIES_FILE_TOKEN in text:
        return fail(f"{path} still references old series source file tokens")
    if re.search(rf"\b{OLD_SERIES_WORD}\b", text, re.IGNORECASE):
        return fail(f"{path} still uses old series wording in active manifest payload")
    if PRE_NORMALIZED_PREFIX in text:
        return fail(f"{path} still uses pre-normalization field names or statuses")
    return 0


def component_files() -> list[Path]:
    return sorted(HOME.glob("component.*.json"))


def hook_files() -> list[Path]:
    return sorted(HOOKS.glob("component.*.hooks.json"))


def validate_component(path: Path, data: dict) -> int:
    if data.get("schema_version") != COMPONENT_SCHEMA:
        return fail(f"{path} schema_version must be {COMPONENT_SCHEMA}")
    if data.get("manifest_class") != "agon_recurrence_component":
        return fail(f"{path} manifest_class must be agon_recurrence_component")
    if not str(data.get("component_ref", "")).startswith("component:agon:"):
        return fail(f"{path} component_ref must start with component:agon:")
    if data.get("owner_part") != "mechanics/agon/parts/recurrence-adapter":
        return fail(f"{path} owner_part must be recurrence adapter")
    if data.get("runtime_effect") != "none":
        return fail(f"{path} runtime_effect must be none")
    if data.get("live_protocol") is not False:
        return fail(f"{path} live_protocol must be false")
    if not isinstance(data.get("source_refs"), list):
        return fail(f"{path} source_refs must be a list")
    if not isinstance(data.get("observed_surfaces"), list):
        return fail(f"{path} observed_surfaces must be a list")
    if not isinstance(data.get("stop_lines"), list):
        return fail(f"{path} stop_lines must be a list")
    text = payload_text(data)
    if OLD_ROOT_MANIFEST_PATH in text:
        return fail(f"{path} still references old root recurrence manifest path")
    if OLD_FLAT_GENERATED_GLOB in text:
        return fail(f"{path} still references old flat root Agon generated glob")
    result = validate_payload_hygiene(path, data)
    if result:
        return result
    return 0


def validate_hook(path: Path, data: dict) -> int:
    if data.get("schema_version") != HOOK_SCHEMA:
        return fail(f"{path} schema_version must be {HOOK_SCHEMA}")
    if data.get("manifest_class") != "agon_recurrence_hook_binding":
        return fail(f"{path} manifest_class must be agon_recurrence_hook_binding")
    if not str(data.get("component_ref", "")).startswith("component:agon:"):
        return fail(f"{path} component_ref must start with component:agon:")
    if data.get("owner_part") != "mechanics/agon/parts/recurrence-adapter":
        return fail(f"{path} owner_part must be recurrence adapter")
    if data.get("runtime_effect") != "none":
        return fail(f"{path} runtime_effect must be none")
    if data.get("live_protocol") is not False:
        return fail(f"{path} live_protocol must be false")
    if not isinstance(data.get("bindings"), list):
        return fail(f"{path} bindings must be a list")
    if not isinstance(data.get("must_not_emit"), list):
        return fail(f"{path} must_not_emit must be a list")
    text = payload_text(data)
    if OLD_ROOT_MANIFEST_PATH in text:
        return fail(f"{path} still references old root recurrence manifest path")
    if OLD_FLAT_GENERATED_GLOB in text:
        return fail(f"{path} still references old flat root Agon generated glob")
    result = validate_payload_hygiene(path, data)
    if result:
        return result
    return 0


def validate_adapter_request_paths() -> int:
    request = load_json(REQUEST)
    for component in request.get("requested_components", []):
        target_repo = component.get("target_repo")
        manifest_path = component.get("manifest_path", "")
        hook_manifest_path = component.get("hook_manifest_path", "")
        if target_repo == "Agents-of-Abyss":
            for key, value in (
                ("manifest_path", manifest_path),
                ("hook_manifest_path", hook_manifest_path),
            ):
                local_path = ROOT / value
                if not local_path.is_file():
                    return fail(f"local {key} does not exist for {component.get('component_ref')}: {value}")
        else:
            expected_prefix = f"owner-local://{target_repo}/"
            if not manifest_path.startswith(expected_prefix):
                return fail(f"external manifest_path must start with {expected_prefix}")
            if not hook_manifest_path.startswith(expected_prefix):
                return fail(f"external hook_manifest_path must start with {expected_prefix}")
    return 0


def main() -> int:
    components = component_files()
    hooks = hook_files()
    if not components:
        return fail("no component manifests found")

    component_stems = {path.name.removesuffix(".json") for path in components}
    hook_stems = {path.name.removesuffix(".hooks.json") for path in hooks}
    if component_stems != hook_stems:
        return fail("component and hook manifest names differ")

    component_refs: set[str] = set()
    for component in components:
        data = load_json(component)
        result = validate_component(component, data)
        if result:
            return result
        component_refs.add(data["component_ref"])

    for hook in hooks:
        data = load_json(hook)
        result = validate_hook(hook, data)
        if result:
            return result
        if data["component_ref"] not in component_refs:
            return fail(f"hook references unknown component: {hook}")

    result = validate_adapter_request_paths()
    if result:
        return result

    print("agon recurrence manifests validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
