#!/usr/bin/env python3
"""Shared builder helpers for the AoA center entry capsule."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]
CENTER_ENTRY_MAP_PATH = REPO_ROOT / "generated" / "center_entry_map.min.json"
SCHEMA_REF = "schemas/center-entry-map.schema.json"
VALIDATION_REFS = (
    "scripts/build_center_entry_map.py",
    "scripts/validate_center_entry_map.py",
    "tests/test_center_entry_map.py",
)
FORBIDDEN_LOW_CONTEXT_PREFIXES = ("src/", "scripts/")

SURFACE_PAYLOAD = {
    "schema_version": "aoa_center_entry_map_v1",
    "schema_ref": SCHEMA_REF,
    "owner_repo": "Agents-of-Abyss",
    "surface_kind": "center_entry_map",
    "authority_ref": "CHARTER.md",
    "public_root_ref": "README.md",
    "registry_ref": "generated/ecosystem_registry.min.json",
    "supporting_inventory_ref": "generated/federation_supporting_inventory.min.json",
    "validation_refs": list(VALIDATION_REFS),
}

ROUTES = (
    {
        "route_id": "center-overview",
        "need": "get the shortest constitutional overview of AoA before branching into layer-owned repos",
        "surface_ref": "README.md",
        "verification_refs": ["CHARTER.md", "docs/PUBLIC_SUPPORT_POSTURE.md"],
    },
    {
        "route_id": "constitutional-boundary",
        "need": "check what the center owns and what must stay in owner-layer repositories",
        "surface_ref": "CHARTER.md",
        "verification_refs": ["docs/FEDERATION_RULES.md", "docs/PUBLIC_SUPPORT_POSTURE.md"],
    },
    {
        "route_id": "public-contour",
        "need": "inspect the current compact documented federation contour without mistaking it for layer-owned truth",
        "surface_ref": "generated/ecosystem_registry.min.json",
        "verification_refs": [
            "ECOSYSTEM_MAP.md",
            "generated/federation_supporting_inventory.min.json",
        ],
    },
    {
        "route_id": "source-of-truth-rules",
        "need": "restore source-of-truth discipline and routing law before following derived or supporting surfaces",
        "surface_ref": "docs/FEDERATION_RULES.md",
        "verification_refs": ["docs/LAYERS.md", "generated/ecosystem_registry.min.json"],
    },
)


def resolve_local_ref(value: str) -> Path:
    target_path = REPO_ROOT / value
    if not target_path.exists():
        raise ValueError(f"missing ref target '{value}'")
    return target_path


def validate_low_context_local_ref(value: str, location: str) -> Path:
    path_text, _, anchor = value.partition("#")
    for prefix in FORBIDDEN_LOW_CONTEXT_PREFIXES:
        if path_text.startswith(prefix):
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
    path = "".join(f"[{item}]" if isinstance(item, int) else f".{item}" for item in error.absolute_path)
    if path.startswith("."):
        path = path[1:]
    if path:
        raise ValueError(f"schema violation at '{path}': {error.message}")
    raise ValueError(f"schema violation: {error.message}")


def build_payload() -> dict[str, object]:
    for key in (
        "schema_ref",
        "authority_ref",
        "public_root_ref",
        "registry_ref",
        "supporting_inventory_ref",
    ):
        validate_low_context_local_ref(str(SURFACE_PAYLOAD[key]), f"surface.{key}")
    for ref in SURFACE_PAYLOAD["validation_refs"]:
        resolve_local_ref(ref)

    routes: list[dict[str, object]] = []
    for route in ROUTES:
        validate_low_context_local_ref(route["surface_ref"], f"route:{route['route_id']}.surface_ref")
        for ref in route["verification_refs"]:
            validate_low_context_local_ref(ref, f"route:{route['route_id']}.verification_refs")
        routes.append(
            {
                "route_id": route["route_id"],
                "need": route["need"],
                "surface_ref": route["surface_ref"],
                "verification_refs": list(route["verification_refs"]),
            }
        )

    payload = {
        **SURFACE_PAYLOAD,
        "routes": routes,
    }
    validate_payload_schema(payload)
    return payload


def render_payload(payload: dict[str, object]) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n"
