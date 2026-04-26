#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import validate_nested_agents

try:
    import yaml
except ModuleNotFoundError:
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "generated" / "ecosystem_registry.min.json"
SCHEMA_PATH = REPO_ROOT / "schemas" / "ecosystem-registry.schema.json"
SUPPORTING_INVENTORY_PATH = REPO_ROOT / "generated" / "federation_supporting_inventory.min.json"
SUPPORTING_SCHEMA_PATH = REPO_ROOT / "schemas" / "federation-supporting-inventory.schema.json"
QUESTBOOK_PATH = REPO_ROOT / "QUESTBOOK.md"
QUESTBOOK_MODEL_PATH = REPO_ROOT / "mechanics" / "questbook" / "parts" / "model-spine" / "README.md"
QUESTBOOK_FIRST_WAVE_PATH = REPO_ROOT / "mechanics" / "questbook" / "legacy" / "raw" / "QUESTBOOK_FIRST_WAVE.md"
QUESTS_PATH = REPO_ROOT / "quests"
REQUIRED_QUEST_IDS = ("AOA-Q-0001", "AOA-Q-0002", "AOA-Q-0003")
CLOSED_QUEST_STATES = {"done", "dropped"}
RPG_ARCHITECTURE_RFC_PATH = REPO_ROOT / "mechanics" / "rpg" / "docs" / "RPG_ARCHITECTURE_RFC.md"
RPG_CANONICAL_TERMINOLOGY_PATH = REPO_ROOT / "mechanics" / "rpg" / "docs" / "RPG_CANONICAL_TERMINOLOGY.md"
RPG_BOUNDARY_MAP_PATH = REPO_ROOT / "mechanics" / "rpg" / "docs" / "RPG_BOUNDARY_MAP.md"
DUAL_VOCABULARY_SCHEMA_PATH = REPO_ROOT / "mechanics" / "rpg" / "schemas" / "dual_vocabulary_overlay.schema.json"
DUAL_VOCABULARY_EXAMPLE_PATH = REPO_ROOT / "mechanics" / "rpg" / "examples" / "dual_vocabulary_overlay.example.json"
DUAL_VOCABULARY_GENERATED_PATH = REPO_ROOT / "mechanics" / "rpg" / "generated" / "dual_vocabulary_overlay.json"
RPG_BRIDGE_WAVE_PATH = REPO_ROOT / "mechanics" / "rpg" / "docs" / "RPG_BRIDGE_WAVE.md"
RPG_RUNTIME_PROJECTION_WAVE_PATH = REPO_ROOT / "mechanics" / "rpg" / "docs" / "RPG_RUNTIME_PROJECTION_WAVE.md"
QUESTBOOK_SECTION_TO_BAND = {
    "Frontier": "frontier",
    "Near": "near",
}
QUEST_ID_RE = re.compile(r"`(AOA-Q-\d{4})`")
MARKDOWN_BULLET_RE = re.compile(r"^[*+-]\s+")
QUEST_LANES = {
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
}
QUEST_LIFECYCLE_STATES = {
    "captured",
    "triaged",
    "ready",
    "active",
    "blocked",
    "reanchor",
    "done",
    "dropped",
}

ALLOWED_STATUS = {
    "active",
    "bootstrap",
    "planned",
    "active-private",
    "active-conceptual",
    "related",
    "experimental",
    "deprecated",
}
ALLOWED_SHARED_MATURITY = {"seed", "proven", "promoted", "canonical", "deprecated"}
ALLOWED_KIND = {"meta", "source", "derived", "related"}
DOCUMENTED_REGISTRY_V1 = {
    "Agents-of-Abyss": {"role": "ecosystem-center", "kind": "meta"},
    "aoa-techniques": {"role": "practice-canon", "kind": "source"},
    "aoa-skills": {"role": "execution-canon", "kind": "source"},
    "aoa-evals": {"role": "proof-canon", "kind": "source"},
    "aoa-memo": {"role": "memory-layer", "kind": "source"},
    "aoa-agents": {"role": "agent-layer", "kind": "source"},
    "aoa-playbooks": {"role": "scenario-composition-layer", "kind": "source"},
    "aoa-stats": {"role": "derived-observability-layer", "kind": "derived"},
    "aoa-routing": {"role": "navigation-layer", "kind": "derived"},
    "aoa-kag": {"role": "derived-knowledge-substrate", "kind": "derived"},
    "Tree-of-Sophia": {"role": "knowledge-architecture-counterpart", "kind": "related"},
    "abyss-stack": {"role": "infrastructure-substrate", "kind": "related"},
}
DOCUMENTED_SUPPORTING_SURFACES = {
    "aoa-sdk": {
        "role": "typed-consumer-and-control-plane",
        "kind": "supporting-consumer",
    }
}


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(REPO_ROOT).as_posix()}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(REPO_ROOT).as_posix()}: {exc}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(REPO_ROOT).as_posix()}")


def read_yaml(path: Path) -> dict[str, object]:
    if yaml is None:
        fail("PyYAML is required to validate QUESTBOOK surfaces")

    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(REPO_ROOT).as_posix()}")
    except yaml.YAMLError as exc:
        fail(f"invalid YAML in {path.relative_to(REPO_ROOT).as_posix()}: {exc}")

    if not isinstance(payload, dict):
        fail(f"{path.relative_to(REPO_ROOT).as_posix()} must contain a YAML object")

    return payload


def parse_questbook_bands(text: str) -> tuple[dict[str, str], set[str]]:
    current_band: str | None = None
    current_heading_seen = False
    current_heading_mapped = False
    bands_by_id: dict[str, str] = {}
    ids_in_unmapped_sections: set[str] = set()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            current_heading_seen = True
            current_band = QUESTBOOK_SECTION_TO_BAND.get(stripped[3:].strip())
            current_heading_mapped = current_band is not None
            continue
        match = QUEST_ID_RE.search(stripped)
        if match is None:
            continue
        if current_heading_mapped and current_band is not None:
            bands_by_id[match.group(1)] = current_band
        elif current_heading_seen and MARKDOWN_BULLET_RE.match(stripped):
            ids_in_unmapped_sections.add(match.group(1))
    return bands_by_id, ids_in_unmapped_sections


def validate_schema_surface() -> None:
    schema = read_json(SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail("schema file must contain a JSON object")
    required_top_level = {"$schema", "$id", "title", "type", "properties", "required"}
    missing = sorted(required_top_level - set(schema))
    if missing:
        fail(f"schema is missing required top-level keys: {', '.join(missing)}")

    supporting_schema = read_json(SUPPORTING_SCHEMA_PATH)
    if not isinstance(supporting_schema, dict):
        fail("supporting inventory schema file must contain a JSON object")
    missing = sorted(required_top_level - set(supporting_schema))
    if missing:
        fail(
            "supporting inventory schema is missing required top-level keys: "
            + ", ".join(missing)
        )


def dual_vocabulary_required_canonical_keys(schema: dict[str, object]) -> set[str]:
    required_keys: set[str] = set()
    for rule in schema.get("allOf", []):
        if not isinstance(rule, dict):
            continue
        properties = rule.get("properties")
        if not isinstance(properties, dict):
            continue
        entries = properties.get("entries")
        if not isinstance(entries, dict):
            continue
        contains = entries.get("contains")
        if not isinstance(contains, dict):
            continue
        contains_properties = contains.get("properties")
        if not isinstance(contains_properties, dict):
            continue
        canonical_key = contains_properties.get("canonical_key")
        if not isinstance(canonical_key, dict):
            continue
        const_value = canonical_key.get("const")
        if isinstance(const_value, str):
            required_keys.add(const_value)
    return required_keys


def validate_dual_vocabulary_generated_payload(payload: object, schema: dict[str, object]) -> None:
    if not isinstance(payload, dict):
        fail("mechanics/rpg/generated/dual_vocabulary_overlay.json must be a JSON object")

    required_top_level = schema.get("required")
    if not isinstance(required_top_level, list):
        fail("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json must declare top-level required fields")
    missing_top_level = [key for key in required_top_level if key not in payload]
    if missing_top_level:
        fail(
            "mechanics/rpg/generated/dual_vocabulary_overlay.json is missing required keys: "
            + ", ".join(missing_top_level)
        )

    properties = schema.get("properties")
    if not isinstance(properties, dict):
        fail("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json must declare properties")
    entries_schema = properties.get("entries")
    if not isinstance(entries_schema, dict):
        fail("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json must define entries")

    for field_name in ("overlay_id", "theme_id", "language"):
        value = payload.get(field_name)
        if not isinstance(value, str) or not value:
            fail(f"mechanics/rpg/generated/dual_vocabulary_overlay.json {field_name} must be a non-empty string")

    if payload.get("schema_version") != "dual_vocabulary_overlay_v1":
        fail("mechanics/rpg/generated/dual_vocabulary_overlay.json schema_version must equal 'dual_vocabulary_overlay_v1'")
    if payload.get("public_safe") is not True:
        fail("mechanics/rpg/generated/dual_vocabulary_overlay.json public_safe must be true")

    entries = payload.get("entries")
    if not isinstance(entries, list):
        fail("mechanics/rpg/generated/dual_vocabulary_overlay.json entries must be a list")

    min_items = entries_schema.get("minItems")
    if isinstance(min_items, int) and len(entries) < min_items:
        fail(f"mechanics/rpg/generated/dual_vocabulary_overlay.json entries must contain at least {min_items} items")
    max_items = entries_schema.get("maxItems")
    if isinstance(max_items, int) and len(entries) > max_items:
        fail(f"mechanics/rpg/generated/dual_vocabulary_overlay.json entries must contain at most {max_items} items")

    item_schema = entries_schema.get("items")
    if not isinstance(item_schema, dict):
        fail("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json entries.items must be an object")
    required_entry_fields = item_schema.get("required")
    if not isinstance(required_entry_fields, list):
        fail("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json entries.items must declare required fields")
    item_properties = item_schema.get("properties")
    if not isinstance(item_properties, dict):
        fail("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json entries.items must declare properties")
    presentation_group_schema = item_properties.get("presentation_group")
    if not isinstance(presentation_group_schema, dict) or not isinstance(
        presentation_group_schema.get("enum"),
        list,
    ):
        fail("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json must constrain presentation_group")
    allowed_groups = {value for value in presentation_group_schema["enum"] if isinstance(value, str)}

    seen_canonical_keys: set[str] = set()
    duplicate_canonical_keys: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            fail(f"mechanics/rpg/generated/dual_vocabulary_overlay.json entries[{index}] must be an object")
        missing_entry_fields = [key for key in required_entry_fields if key not in entry]
        if missing_entry_fields:
            fail(
                "mechanics/rpg/generated/dual_vocabulary_overlay.json "
                f"entries[{index}] is missing required keys: {', '.join(missing_entry_fields)}"
            )
        for field_name in ("canonical_key", "canonical_label", "presentation_label"):
            value = entry.get(field_name)
            if not isinstance(value, str) or not value:
                fail(
                    "mechanics/rpg/generated/dual_vocabulary_overlay.json "
                    f"entries[{index}].{field_name} must be a non-empty string"
                )
        presentation_group = entry.get("presentation_group")
        if presentation_group not in allowed_groups:
            fail(
                "mechanics/rpg/generated/dual_vocabulary_overlay.json "
                f"entries[{index}].presentation_group must stay within the schema enum"
            )
        canonical_key = entry["canonical_key"]
        if canonical_key in seen_canonical_keys:
            duplicate_canonical_keys.append(canonical_key)
        seen_canonical_keys.add(canonical_key)

    if duplicate_canonical_keys:
        fail(
            "mechanics/rpg/generated/dual_vocabulary_overlay.json must not duplicate canonical_key values "
            f"(first duplicate: {duplicate_canonical_keys[0]})"
        )

    missing_canonical_keys = sorted(dual_vocabulary_required_canonical_keys(schema) - seen_canonical_keys)
    if missing_canonical_keys:
        fail(
            "mechanics/rpg/generated/dual_vocabulary_overlay.json is missing required canonical_key values: "
            + ", ".join(missing_canonical_keys)
        )


def validate_registry() -> None:
    payload = read_json(REGISTRY_PATH)
    if not isinstance(payload, dict):
        fail("ecosystem registry must be a JSON object")

    for key in ("version", "ecosystem", "repos"):
        if key not in payload:
            fail(f"ecosystem registry is missing required key '{key}'")

    if not isinstance(payload["version"], int) or payload["version"] < 1:
        fail("registry 'version' must be an integer >= 1")
    if payload["ecosystem"] != "AoA":
        fail("registry 'ecosystem' must equal 'AoA'")

    repos = payload["repos"]
    if not isinstance(repos, list) or not repos:
        fail("registry 'repos' must be a non-empty list")

    seen_names: set[str] = set()
    expected_names = set(DOCUMENTED_REGISTRY_V1)

    for index, repo in enumerate(repos):
        location = f"repos[{index}]"
        if not isinstance(repo, dict):
            fail(f"{location} must be an object")

        for key in ("name", "role", "status", "shared_maturity", "kind"):
            if key not in repo:
                fail(f"{location} is missing required key '{key}'")

        name = repo["name"]
        role = repo["role"]
        status = repo["status"]
        shared_maturity = repo["shared_maturity"]
        kind = repo["kind"]

        if not isinstance(name, str) or len(name) < 3:
            fail(f"{location}.name must be a string of length >= 3")
        if name in seen_names:
            fail(f"duplicate repository name in registry: '{name}'")
        seen_names.add(name)

        if not isinstance(role, str) or len(role) < 3:
            fail(f"{location}.role must be a string of length >= 3")
        if status not in ALLOWED_STATUS:
            fail(f"{location}.status '{status}' is not allowed")
        if shared_maturity not in ALLOWED_SHARED_MATURITY:
            fail(f"{location}.shared_maturity '{shared_maturity}' is not allowed")
        if kind not in ALLOWED_KIND:
            fail(f"{location}.kind '{kind}' is not allowed")

        expected_entry = DOCUMENTED_REGISTRY_V1.get(name)
        if expected_entry is not None:
            expected_role = expected_entry["role"]
            expected_kind = expected_entry["kind"]
            if role != expected_role:
                fail(
                    f"{location}.role for '{name}' must equal "
                    f"'{expected_role}'"
                )
            if kind != expected_kind:
                fail(
                    f"{location}.kind for '{name}' must equal "
                    f"'{expected_kind}'"
                )

    missing_expected = sorted(expected_names - seen_names)
    if missing_expected:
        fail(
            "ecosystem registry is missing documented v1 repos: "
            + ", ".join(missing_expected)
        )

    unexpected_repos = sorted(seen_names - expected_names)
    if unexpected_repos:
        fail(
            "ecosystem registry contains repos outside compact v1 scope: "
            + ", ".join(unexpected_repos)
        )


def validate_supporting_inventory() -> None:
    payload = read_json(SUPPORTING_INVENTORY_PATH)
    if not isinstance(payload, dict):
        fail("supporting inventory must be a JSON object")

    for key in ("version", "inventory", "center_registry_ref", "repos"):
        if key not in payload:
            fail(f"supporting inventory is missing required key '{key}'")

    if not isinstance(payload["version"], int) or payload["version"] < 1:
        fail("supporting inventory 'version' must be an integer >= 1")
    if payload["inventory"] != "AoA-supporting-surfaces":
        fail("supporting inventory 'inventory' must equal 'AoA-supporting-surfaces'")
    if payload["center_registry_ref"] != "generated/ecosystem_registry.min.json":
        fail(
            "supporting inventory 'center_registry_ref' must equal "
            "'generated/ecosystem_registry.min.json'"
        )

    repos = payload["repos"]
    if not isinstance(repos, list) or not repos:
        fail("supporting inventory 'repos' must be a non-empty list")

    seen_names: set[str] = set()
    expected_names = set(DOCUMENTED_SUPPORTING_SURFACES)

    for index, repo in enumerate(repos):
        location = f"supporting_inventory.repos[{index}]"
        if not isinstance(repo, dict):
            fail(f"{location} must be an object")

        for key in ("name", "role", "status", "shared_maturity", "kind", "boundary"):
            if key not in repo:
                fail(f"{location} is missing required key '{key}'")

        name = repo["name"]
        role = repo["role"]
        status = repo["status"]
        shared_maturity = repo["shared_maturity"]
        kind = repo["kind"]
        boundary = repo["boundary"]

        if not isinstance(name, str) or len(name) < 3:
            fail(f"{location}.name must be a string of length >= 3")
        if name in seen_names:
            fail(f"duplicate repository name in supporting inventory: '{name}'")
        seen_names.add(name)
        if not isinstance(role, str) or len(role) < 3:
            fail(f"{location}.role must be a string of length >= 3")
        if status not in ALLOWED_STATUS:
            fail(f"{location}.status '{status}' is not allowed")
        if shared_maturity not in ALLOWED_SHARED_MATURITY:
            fail(f"{location}.shared_maturity '{shared_maturity}' is not allowed")
        if not isinstance(boundary, str) or len(boundary) < 12:
            fail(f"{location}.boundary must be a string of length >= 12")

        expected_entry = DOCUMENTED_SUPPORTING_SURFACES.get(name)
        if expected_entry is None:
            fail(f"supporting inventory contains undocumented repo '{name}'")
        if role != expected_entry["role"]:
            fail(f"{location}.role for '{name}' must equal '{expected_entry['role']}'")
        if kind != expected_entry["kind"]:
            fail(f"{location}.kind for '{name}' must equal '{expected_entry['kind']}'")

    missing_expected = sorted(expected_names - seen_names)
    if missing_expected:
        fail(
            "supporting inventory is missing documented supporting repos: "
            + ", ".join(missing_expected)
        )


def validate_nested_agents_surface() -> None:
    issues = validate_nested_agents.run_validation(REPO_ROOT)
    if issues:
        formatted = "; ".join(
            f"{location}: {message}" for location, message in issues
        )
        fail(f"nested AGENTS docs check failed: {formatted}")


def collect_quest_paths() -> dict[str, Path]:
    root_quest_files = sorted(path for path in QUESTS_PATH.glob("AOA-Q-*.yaml") if path.is_file())
    if root_quest_files:
        listed = ", ".join(path.relative_to(REPO_ROOT).as_posix() for path in root_quest_files)
        fail(f"quest yaml files must live in lane-first lifecycle directories, not top-level quests: {listed}")
    old_lifecycle_dirs = sorted(path for path in QUESTS_PATH.iterdir() if path.is_dir() and path.name in QUEST_LIFECYCLE_STATES)
    if old_lifecycle_dirs:
        listed = ", ".join(path.relative_to(REPO_ROOT).as_posix() for path in old_lifecycle_dirs)
        fail(f"quest lifecycle directories must live under a lane, not directly under quests: {listed}")

    quest_paths: dict[str, Path] = {}
    for path in sorted(QUESTS_PATH.glob("*/*/AOA-Q-*.yaml")):
        if not path.is_file():
            continue
        lane = path.parent.parent.name
        state = path.parent.name
        if lane not in QUEST_LANES:
            fail(f"{path.relative_to(REPO_ROOT).as_posix()} uses unsupported quest lane '{lane}'")
        if state not in QUEST_LIFECYCLE_STATES:
            fail(f"{path.relative_to(REPO_ROOT).as_posix()} uses unsupported quest lifecycle state '{state}'")
        quest_id = path.stem
        previous = quest_paths.get(quest_id)
        if previous is not None:
            fail(
                f"duplicate quest id '{quest_id}' in "
                f"{previous.relative_to(REPO_ROOT).as_posix()} and {path.relative_to(REPO_ROOT).as_posix()}"
            )
        quest_paths[quest_id] = path
    return quest_paths


def validate_questbook_surface() -> None:
    questbook_text = read_text(QUESTBOOK_PATH)
    read_text(QUESTBOOK_MODEL_PATH)
    first_wave_text = read_text(QUESTBOOK_FIRST_WAVE_PATH)
    questbook_bands, ids_in_unmapped_sections = parse_questbook_bands(questbook_text)

    quest_paths = collect_quest_paths()
    actual_ids = set(quest_paths)
    expected_ids = set(REQUIRED_QUEST_IDS)
    missing = sorted(expected_ids - actual_ids)
    if missing:
        fail(f"foundation quest set must include required center quests (missing: {', '.join(missing)})")

    active_quest_ids: list[str] = []
    closed_quest_ids: list[str] = []
    for quest_id in sorted(quest_paths):
        path = quest_paths[quest_id]
        payload = read_yaml(path)

        schema_version = payload.get("schema_version")
        if schema_version != "work_quest_v1":
            fail(
                f"{path.relative_to(REPO_ROOT).as_posix()} has unsupported "
                f"schema_version '{schema_version}'"
            )

        repo = payload.get("repo")
        if repo != "Agents-of-Abyss":
            fail(
                f"{path.relative_to(REPO_ROOT).as_posix()} must target "
                "repo 'Agents-of-Abyss'"
            )
        lane = path.parent.parent.name
        if payload.get("lane") != lane:
            fail(
                f"{path.relative_to(REPO_ROOT).as_posix()} lane '{payload.get('lane')}' "
                f"does not match path lane '{lane}'"
            )
        state = path.parent.name
        if payload.get("state") != state:
            fail(
                f"{path.relative_to(REPO_ROOT).as_posix()} state '{payload.get('state')}' "
                f"does not match path state '{state}'"
            )

        payload_id = payload.get("id")
        if payload_id != quest_id:
            fail(
                f"{path.relative_to(REPO_ROOT).as_posix()} id '{payload_id}' "
                f"does not match filename '{quest_id}'"
            )
        quest_band = payload.get("band")
        listed_band = questbook_bands.get(quest_id)
        if isinstance(quest_band, str) and listed_band is None and quest_id in ids_in_unmapped_sections:
            fail(
                f"QUESTBOOK.md must list quest id '{quest_id}' under the section for band "
                f"'{quest_band}', not only under an unmapped section"
            )
        if isinstance(quest_band, str) and listed_band is not None and listed_band != quest_band:
            fail(
                f"QUESTBOOK.md must list quest id '{quest_id}' under the section for band "
                f"'{quest_band}', not '{listed_band}'"
            )

        if payload.get("public_safe") is not True:
            fail(f"{path.relative_to(REPO_ROOT).as_posix()} must set public_safe: true")
        if payload.get("state") in CLOSED_QUEST_STATES:
            closed_quest_ids.append(quest_id)
        else:
            active_quest_ids.append(quest_id)

    for quest_id in active_quest_ids:
        if quest_id not in questbook_text:
            fail(f"QUESTBOOK.md must reference active quest id '{quest_id}'")
    for quest_id in closed_quest_ids:
        if quest_id in questbook_text:
            fail(f"QUESTBOOK.md must not list closed quest id '{quest_id}'")

    if "AOA-Q-0006" in actual_ids:
        architecture_rfc_text = read_text(RPG_ARCHITECTURE_RFC_PATH)
        if "The RPG layer MUST remain a reflection and orchestration layer." not in architecture_rfc_text:
            fail("mechanics/rpg/docs/RPG_ARCHITECTURE_RFC.md must keep the reflection-layer core rule explicit")
        if "One universal power score MUST NOT become authoritative." not in architecture_rfc_text:
            fail("mechanics/rpg/docs/RPG_ARCHITECTURE_RFC.md must keep the anti-power-score law explicit")

        canonical_terms_text = read_text(RPG_CANONICAL_TERMINOLOGY_PATH)
        if "the machine vocabulary stays stable" not in canonical_terms_text:
            fail("mechanics/rpg/docs/RPG_CANONICAL_TERMINOLOGY.md must keep machine vocabulary stability explicit")
        if "dual_vocabulary_overlay_v1" not in canonical_terms_text:
            fail("mechanics/rpg/docs/RPG_CANONICAL_TERMINOLOGY.md must reference dual_vocabulary_overlay_v1")

        boundary_map_text = read_text(RPG_BOUNDARY_MAP_PATH)
        if "The repo that already owns meaning keeps owning meaning." not in boundary_map_text:
            fail("mechanics/rpg/docs/RPG_BOUNDARY_MAP.md must keep the ownership law explicit")
        if "1. source meaning wins" not in boundary_map_text:
            fail("mechanics/rpg/docs/RPG_BOUNDARY_MAP.md must keep the precedence rule explicit")

        schema_payload = read_json(DUAL_VOCABULARY_SCHEMA_PATH)
        if not isinstance(schema_payload, dict):
            fail("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json must be a JSON object")
        if schema_payload.get("title") != "dual_vocabulary_overlay_v1":
            fail("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json title must equal 'dual_vocabulary_overlay_v1'")

        example_payload = read_json(DUAL_VOCABULARY_EXAMPLE_PATH)
        if not isinstance(example_payload, dict):
            fail("mechanics/rpg/examples/dual_vocabulary_overlay.example.json must be a JSON object")
        if example_payload.get("schema_version") != "dual_vocabulary_overlay_v1":
            fail("mechanics/rpg/examples/dual_vocabulary_overlay.example.json schema_version must equal 'dual_vocabulary_overlay_v1'")
        if example_payload.get("public_safe") is not True:
            fail("mechanics/rpg/examples/dual_vocabulary_overlay.example.json public_safe must be true")

    if "AOA-Q-0007" in actual_ids:
        bridge_wave_text = read_text(RPG_BRIDGE_WAVE_PATH)
        if "What remained was the bridge that lets proof, composition, and navigation speak to one another without collapsing repo ownership." not in bridge_wave_text:
            fail("mechanics/rpg/docs/RPG_BRIDGE_WAVE.md must keep the bridge-purpose law explicit")
        if "`aoa-routing` may orient. It does not own proof, party doctrine, or quest meaning." not in bridge_wave_text:
            fail("mechanics/rpg/docs/RPG_BRIDGE_WAVE.md must keep routing non-authority explicit")
        if "do not create a universal rank or power score here" not in bridge_wave_text:
            fail("mechanics/rpg/docs/RPG_BRIDGE_WAVE.md must keep the anti-power-score bridge rule explicit")
        if "This wave is a bridge, not a throne." not in bridge_wave_text:
            fail("mechanics/rpg/docs/RPG_BRIDGE_WAVE.md must keep the anti-throne rule explicit")

    if "AOA-Q-0008" in actual_ids:
        runtime_projection_text = read_text(RPG_RUNTIME_PROJECTION_WAVE_PATH)
        if "This document defines the first body-facing rollout for the AoA RPG reflection contour." not in runtime_projection_text:
            fail("mechanics/rpg/docs/RPG_RUNTIME_PROJECTION_WAVE.md must keep the body-facing role explicit")
        if "It is the pass where the contour stops being only a federation of ideas and gains runtime-owned read models, generated transport collections, and a bounded projection seam." not in runtime_projection_text:
            fail("mechanics/rpg/docs/RPG_RUNTIME_PROJECTION_WAVE.md must keep the body-facing transition explicit")
        if "Let the body carry the contour." not in runtime_projection_text:
            fail("mechanics/rpg/docs/RPG_RUNTIME_PROJECTION_WAVE.md must keep the body-carries-the-contour rule explicit")
        if "Do not let it rewrite the soul." not in runtime_projection_text:
            fail("mechanics/rpg/docs/RPG_RUNTIME_PROJECTION_WAVE.md must keep the anti-rewrite rule explicit")

        generated_payload = read_json(DUAL_VOCABULARY_GENERATED_PATH)
        schema_payload = read_json(DUAL_VOCABULARY_SCHEMA_PATH)
        if not isinstance(schema_payload, dict):
            fail("mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json must be a JSON object")
        validate_dual_vocabulary_generated_payload(generated_payload, schema_payload)

    if "ATM10-Agent" in first_wave_text:
        fail("mechanics/questbook/legacy/raw/QUESTBOOK_FIRST_WAVE.md must not reference ATM10-Agent")

    required_phrase = "It is a foundation pass, not a new numbered AoA wave."
    if required_phrase not in first_wave_text:
        fail(
            "mechanics/questbook/legacy/raw/QUESTBOOK_FIRST_WAVE.md must state that the contour is not "
            "a new numbered AoA wave"
        )


def main() -> int:
    try:
        validate_schema_surface()
        validate_registry()
        validate_supporting_inventory()
        validate_questbook_surface()
        validate_nested_agents_surface()
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    print("[ok] validated ecosystem registry schema surface")
    print("[ok] validated generated/ecosystem_registry.min.json")
    print("[ok] validated generated/federation_supporting_inventory.min.json")
    print("[ok] validated questbook center surface")
    print("[ok] validated nested AGENTS directory guidance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
