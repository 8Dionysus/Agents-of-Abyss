#!/usr/bin/env python3
"""Shared builder helpers for the AoA center entry capsule."""
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]
CENTER_ENTRY_MAP_PATH = REPO_ROOT / "generated" / "center_entry_map.min.json"
SCHEMA_REF = "schemas/center-entry-map.schema.json"
ROUTE_CONTRACT_REF = "docs/START_HERE_ROUTE_CONTRACT.md"

ROUTE_MODE_ORDER = (
    "first-reading",
    "root-editing",
    "direction-change",
    "ownership-routing",
    "mechanic-change",
    "public-claim-validation",
    "low-context-agent",
    "district-work",
)
REQUIRED_ROUTE_MODES = ROUTE_MODE_ORDER

ENTRY_SURFACE_REFS = (
    "README.md",
    "AGENTS.md",
    "docs/README.md",
    "docs/START_HERE_ROUTE_CONTRACT.md",
    "CONTRIBUTING.md",
    "mechanics/README.md",
    "mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md",
    "generated/center_entry_map.min.json",
)

MACHINE_CONTRACT_REFS = (
    "generated/center_entry_map.min.json",
    "schemas/center-entry-map.schema.json",
    "scripts/center_entry_map_common.py",
    "scripts/validate_center_entry_map.py",
    "scripts/validate_entry_surface_sync.py",
    "tests/test_center_entry_map.py",
    "tests/test_entry_surface_sync.py",
)

BASELINE_VALIDATION_COMMANDS = (
    "python scripts/repair_known_link_drifts.py --check",
    "python scripts/validate_links.py",
    "python scripts/validate_markdown_shape.py",
    "python scripts/validate_status_vocabulary.py",
    "python scripts/build_link_shape_hygiene_index.py --check",
    "python scripts/validate_link_shape_hygiene_index.py",
    "python scripts/validate_agents_md_shape.py",
    "python scripts/validate_agents_mesh.py",
    "python scripts/build_agents_mesh_index.py --check",
    "python scripts/validate_agents_mesh_index.py",
    "python scripts/validate_entry_surface_sync.py",
    "python scripts/build_center_entry_map.py --check",
    "python scripts/validate_center_entry_map.py",
    "python scripts/validate_mechanics_topology.py",
    "python scripts/validate_mechanic_landing_logs.py",
    "python scripts/validate_generated_freshness.py",
    "python scripts/validate_hygiene_suite.py",
    "python scripts/validate_ecosystem.py",
    "python -m pytest -q",
)

VALIDATION_REFS = (
    "scripts/repair_known_link_drifts.py",
    "scripts/validate_links.py",
    "scripts/validate_markdown_shape.py",
    "scripts/validate_status_vocabulary.py",
    "scripts/build_link_shape_hygiene_index.py",
    "scripts/validate_link_shape_hygiene_index.py",
    "scripts/validate_agents_md_shape.py",
    "scripts/validate_agents_mesh.py",
    "scripts/build_agents_mesh_index.py",
    "scripts/validate_agents_mesh_index.py",
    "scripts/validate_entry_surface_sync.py",
    "scripts/build_center_entry_map.py",
    "scripts/validate_center_entry_map.py",
    "scripts/validate_mechanics_topology.py",
    "scripts/validate_mechanic_landing_logs.py",
    "scripts/validate_generated_freshness.py",
    "scripts/validate_hygiene_suite.py",
    "scripts/validate_ecosystem.py",
    "tests/test_center_entry_map.py",
    "tests/test_entry_surface_sync.py",
)

FORBIDDEN_LOW_CONTEXT_PREFIXES = ("src/", "scripts/")

SURFACE_PAYLOAD: dict[str, object] = {
    "schema_version": "aoa_center_entry_map_v2",
    "schema_ref": SCHEMA_REF,
    "owner_repo": "Agents-of-Abyss",
    "surface_kind": "center_entry_map",
    "authority_ref": "CHARTER.md",
    "public_root_ref": "README.md",
    "route_contract_ref": ROUTE_CONTRACT_REF,
    "registry_ref": "generated/ecosystem_registry.min.json",
    "supporting_inventory_ref": "generated/federation_supporting_inventory.min.json",
    "validation_refs": list(VALIDATION_REFS),
}

ROUTES: tuple[dict[str, object], ...] = (
    {
        "route_id": "first-reading",
        "route_mode": "first-reading",
        "priority": 1,
        "audience": ["human", "new-agent", "outside-reader"],
        "need": "understand the center without entering every district",
        "surface_ref": "README.md",
        "human_path": [
            "README.md",
            "CHARTER.md",
            "ECOSYSTEM_MAP.md",
            "docs/FEDERATION_RULES.md",
        ],
        "machine_surface_refs": [
            "generated/center_entry_map.min.json",
            "generated/ecosystem_registry.min.json",
        ],
        "verification_refs": [
            "CHARTER.md",
            "mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md",
        ],
        "must_not_claim": [
            "the first-reading route replaces owner-local docs",
            "the center owns every object it names",
        ],
    },
    {
        "route_id": "root-editing",
        "route_mode": "root-editing",
        "priority": 2,
        "audience": ["contributor", "coding-agent", "maintainer"],
        "need": "change root surfaces without making the root a warehouse",
        "surface_ref": "docs/ROOT_SURFACE_LAW.md",
        "human_path": [
            "README.md",
            "CHARTER.md",
            "ECOSYSTEM_MAP.md",
            "docs/FEDERATION_RULES.md",
            "CONTRIBUTING.md",
            "docs/ROOT_SURFACE_LAW.md",
        ],
        "machine_surface_refs": ["generated/center_entry_map.min.json"],
        "verification_refs": [
            "ECOSYSTEM_AUDIT_INDEX.md",
            "mechanics/audit/PROVENANCE.md",
        ],
        "must_not_claim": [
            "a root file belongs in root because it was created during a wave",
            "audit artifacts are constitutional law",
        ],
    },
    {
        "route_id": "direction-change",
        "route_mode": "direction-change",
        "priority": 3,
        "audience": ["maintainer", "release-agent", "roadmap-editor"],
        "need": "update current phase, roadmap, maturity, or release contour",
        "surface_ref": "ROADMAP.md",
        "human_path": [
            "README.md",
            "CHARTER.md",
            "ECOSYSTEM_MAP.md",
            "docs/FEDERATION_RULES.md",
            "ROADMAP.md",
            "mechanics/release-support/DIRECTION.md",
            "mechanics/release-support/docs/DIRECTION_SURFACES.md",
            "CHANGELOG.md",
        ],
        "machine_surface_refs": ["generated/center_entry_map.min.json"],
        "verification_refs": [
            "mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md",
            "mechanics/release-support/docs/FEDERATION_RELEASE_PROTOCOL.md",
        ],
        "must_not_claim": [
            "future direction is already landed implementation",
            "roadmap history replaces changelog or landing receipts",
        ],
    },
    {
        "route_id": "ownership-routing",
        "route_mode": "ownership-routing",
        "priority": 4,
        "audience": ["human", "agent", "reviewer"],
        "need": "decide which repository owns a change",
        "surface_ref": "docs/REPO_ROLES.md",
        "human_path": [
            "README.md",
            "CHARTER.md",
            "ECOSYSTEM_MAP.md",
            "docs/FEDERATION_RULES.md",
            "docs/LAYERS.md",
            "docs/REPO_ROLES.md",
        ],
        "machine_surface_refs": [
            "generated/ecosystem_registry.min.json",
            "generated/federation_supporting_inventory.min.json",
        ],
        "verification_refs": [
            "docs/FEDERATION_RULES.md",
            "ECOSYSTEM_MAP.md",
        ],
        "must_not_claim": [
            "convenient routing transfers owner truth to the center",
            "derived layers own source-authored meaning",
        ],
    },
    {
        "route_id": "mechanic-change",
        "route_mode": "mechanic-change",
        "priority": 5,
        "audience": ["mechanic-author", "coding-agent", "reviewer"],
        "need": "edit Agon, Experience, recurrence, method/growth, distillation, growth-cycle, audit, antifragility, quest/RPG, release-support, or boundary bridge without stealing owner truth",
        "surface_ref": "mechanics/README.md",
        "human_path": [
            "README.md",
            "CHARTER.md",
            "ECOSYSTEM_MAP.md",
            "docs/FEDERATION_RULES.md",
            "mechanics/README.md",
        ],
        "machine_surface_refs": [
            "generated/center_entry_map.min.json",
            "mechanics/registry.json",
        ],
        "verification_refs": [
            "docs/START_HERE_ROUTE_CONTRACT.md",
            "docs/REPO_ROLES.md",
            "mechanics/registry.json",
        ],
        "must_not_claim": [
            "center mechanics activate live runtime",
            "center mechanics land sibling-repo implementation",
        ],
    },
    {
        "route_id": "public-claim-validation",
        "route_mode": "public-claim-validation",
        "priority": 6,
        "audience": ["release-agent", "public-docs-editor", "reviewer"],
        "need": "decide whether the center may honestly claim something publicly or move an internal transition into public view",
        "surface_ref": "mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md",
        "human_path": [
            "mechanics/release-support/README.md",
            "mechanics/release-support/PARTS.md",
            "mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md",
            "CHARTER.md",
            "ECOSYSTEM_MAP.md",
            "docs/FEDERATION_RULES.md",
        ],
        "machine_surface_refs": [
            "generated/center_entry_map.min.json",
            "generated/ecosystem_registry.min.json",
            "generated/federation_supporting_inventory.min.json",
        ],
        "verification_refs": [
            "mechanics/release-support/docs/FEDERATION_RELEASE_PROTOCOL.md",
            "mechanics/release-support/docs/RELEASING.md",
        ],
        "must_not_claim": [
            "passing center checks proves downstream implementation",
            "public support means owner truth has moved to the center",
        ],
    },
    {
        "route_id": "low-context-agent",
        "route_mode": "low-context-agent",
        "priority": 7,
        "audience": ["small-model", "retrieval-system", "capsule-first-agent"],
        "need": "get a compact route before reading full docs",
        "surface_ref": "generated/center_entry_map.min.json",
        "human_path": [
            "README.md",
            "docs/START_HERE_ROUTE_CONTRACT.md",
        ],
        "machine_surface_refs": [
            "generated/center_entry_map.min.json",
            "schemas/center-entry-map.schema.json",
        ],
        "verification_refs": [
            "CHARTER.md",
            "mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md",
        ],
        "must_not_claim": [
            "the machine capsule replaces human docs",
            "route selection is owner approval",
        ],
    },
    {
        "route_id": "district-work",
        "route_mode": "district-work",
        "priority": 8,
        "audience": ["coding-agent", "district-editor", "reviewer"],
        "need": "work inside generated, scripts, schemas, tests, quests, manifests, config, or examples without confusing local gates with constitutional law",
        "surface_ref": "docs/README.md",
        "human_path": [
            "README.md",
            "docs/README.md",
            "generated/README.md",
            "scripts/README.md",
            "schemas/README.md",
            "tests/README.md",
            "quests/README.md",
        ],
        "machine_surface_refs": ["generated/center_entry_map.min.json"],
        "verification_refs": [
            "docs/START_HERE_ROUTE_CONTRACT.md",
            "docs/ROOT_SURFACE_LAW.md",
        ],
        "must_not_claim": [
            "local district guidance overrides center law",
            "generated or executable artifacts author source meaning",
        ],
    },
)


def resolve_local_ref(value: str) -> Path:
    path_text = value.partition("#")[0]
    target_path = REPO_ROOT / path_text
    if not target_path.exists():
        if target_path == CENTER_ENTRY_MAP_PATH:
            return target_path
        raise ValueError(f"missing ref target '{value}'")
    return target_path


def validate_low_context_local_ref(value: str, location: str) -> Path:
    path_text, _, anchor = value.partition("#")
    for prefix in FORBIDDEN_LOW_CONTEXT_PREFIXES:
        if path_text.startswith(prefix) and not path_text.endswith("/README.md"):
            raise ValueError(f"{location} must not point to implementation path '{value}'")
    target_path = resolve_local_ref(path_text)
    if anchor and target_path.suffix.lower() != ".md":
        raise ValueError(f"{location} may only use anchors for markdown refs")
    return target_path


def load_schema() -> dict[str, object]:
    return json.loads(resolve_local_ref(SCHEMA_REF).read_text(encoding="utf-8"))


def validate_payload_schema(payload: dict[str, object]) -> None:
    validator = Draft202012Validator(load_schema())
    errors = sorted(validator.iter_errors(payload), key=lambda error: list(error.absolute_path))
    if not errors:
        return
    error = errors[0]
    path = "".join(
        f"[{item}]" if isinstance(item, int) else f".{item}"
        for item in error.absolute_path
    )
    if path.startswith("."):
        path = path[1:]
    if path:
        raise ValueError(f"schema violation at '{path}': {error.message}")
    raise ValueError(f"schema violation: {error.message}")


def route_modes(routes: list[dict[str, object]]) -> set[str]:
    return {str(route.get("route_mode")) for route in routes}


def build_payload() -> dict[str, object]:
    for key in (
        "schema_ref",
        "authority_ref",
        "public_root_ref",
        "route_contract_ref",
        "registry_ref",
        "supporting_inventory_ref",
    ):
        validate_low_context_local_ref(str(SURFACE_PAYLOAD[key]), f"surface.{key}")

    for ref in SURFACE_PAYLOAD["validation_refs"]:
        resolve_local_ref(str(ref))

    routes: list[dict[str, object]] = []
    seen_route_ids: set[str] = set()
    seen_priorities: set[int] = set()

    for route in ROUTES:
        route_id = str(route["route_id"])
        priority = int(route["priority"])
        if route_id in seen_route_ids:
            raise ValueError(f"duplicate route_id '{route_id}'")
        if priority in seen_priorities:
            raise ValueError(f"duplicate route priority '{priority}'")
        seen_route_ids.add(route_id)
        seen_priorities.add(priority)

        validate_low_context_local_ref(str(route["surface_ref"]), f"route:{route_id}.surface_ref")
        for field in ("human_path", "machine_surface_refs", "verification_refs"):
            values = route[field]
            if not isinstance(values, list):
                raise ValueError(f"route:{route_id}.{field} must be a list")
            for ref in values:
                validate_low_context_local_ref(str(ref), f"route:{route_id}.{field}")

        routes.append(
            {
                "route_id": route_id,
                "route_mode": route["route_mode"],
                "priority": priority,
                "audience": list(route["audience"]),
                "need": route["need"],
                "surface_ref": route["surface_ref"],
                "human_path": list(route["human_path"]),
                "machine_surface_refs": list(route["machine_surface_refs"]),
                "verification_refs": list(route["verification_refs"]),
                "must_not_claim": list(route["must_not_claim"]),
            }
        )

    missing_modes = set(REQUIRED_ROUTE_MODES) - route_modes(routes)
    if missing_modes:
        raise ValueError("missing center entry route modes: " + ", ".join(sorted(missing_modes)))

    payload = {**SURFACE_PAYLOAD, "routes": sorted(routes, key=lambda item: int(item["priority"]))}
    validate_payload_schema(payload)
    return payload


def render_payload(payload: dict[str, object]) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n"
