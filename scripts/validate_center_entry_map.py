#!/usr/bin/env python3
"""Validate the AoA center entry capsule against live center posture."""
from __future__ import annotations

import json

from center_entry_map_common import (
    CENTER_ENTRY_MAP_PATH,
    REQUIRED_ROUTE_MODES,
    ROUTES,
    SURFACE_PAYLOAD,
    build_payload,
    resolve_local_ref,
    route_modes,
    validate_low_context_local_ref,
    validate_payload_schema,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    expected_payload = build_payload()
    current_payload = json.loads(CENTER_ENTRY_MAP_PATH.read_text(encoding="utf-8"))

    validate_payload_schema(current_payload)

    if current_payload != expected_payload:
        raise SystemExit("generated/center_entry_map.min.json does not match the canonical rebuild")

    for key, expected in SURFACE_PAYLOAD.items():
        if current_payload.get(key) != expected:
            raise SystemExit(f"generated/center_entry_map.min.json must keep {key}={expected!r}")
        if key == "validation_refs":
            for ref in expected:
                resolve_local_ref(str(ref))
        elif key in {
            "schema_ref",
            "authority_ref",
            "public_root_ref",
            "route_contract_ref",
            "registry_ref",
            "supporting_inventory_ref",
        }:
            resolve_local_ref(str(expected))

    routes = current_payload.get("routes")
    require(isinstance(routes, list), "generated/center_entry_map.min.json routes must be a list")
    require(len(routes) == len(ROUTES), "generated/center_entry_map.min.json must publish the canonical route set")

    missing_modes = set(REQUIRED_ROUTE_MODES) - route_modes(routes)
    require(not missing_modes, "missing route modes: " + ", ".join(sorted(missing_modes)))

    seen_ids: set[str] = set()
    seen_priorities: set[int] = set()

    for route in routes:
        require(isinstance(route, dict), "generated/center_entry_map.min.json routes must be objects")
        for key in (
            "route_id",
            "route_mode",
            "priority",
            "audience",
            "need",
            "surface_ref",
            "human_path",
            "machine_surface_refs",
            "verification_refs",
            "must_not_claim",
        ):
            require(key in route, f"generated/center_entry_map.min.json is missing route field '{key}'")

        route_id = str(route["route_id"])
        priority = route["priority"]
        require(route_id not in seen_ids, f"duplicate route_id '{route_id}'")
        require(isinstance(priority, int), f"route:{route_id}.priority must be an integer")
        require(priority not in seen_priorities, f"duplicate route priority '{priority}'")
        seen_ids.add(route_id)
        seen_priorities.add(priority)

        validate_low_context_local_ref(str(route["surface_ref"]), f"route:{route_id}.surface_ref")

        for field in ("human_path", "machine_surface_refs", "verification_refs"):
            values = route[field]
            require(isinstance(values, list), f"route:{route_id}.{field} must be a list")
            if field != "machine_surface_refs":
                require(bool(values), f"route:{route_id}.{field} must not be empty")
            for ref in values:
                require(isinstance(ref, str) and ref.strip(), f"route:{route_id}.{field} must contain strings")
                validate_low_context_local_ref(ref, f"route:{route_id}.{field}")

        must_not_claim = route["must_not_claim"]
        require(
            isinstance(must_not_claim, list) and all(isinstance(item, str) and item.strip() for item in must_not_claim),
            f"route:{route_id}.must_not_claim must contain strings",
        )

    print("[ok] validated generated/center_entry_map.min.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
