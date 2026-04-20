#!/usr/bin/env python3
"""Validate Agon Wave III lawful move language landing."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = ROOT / "scripts" / "build_agon_lawful_move_registry.py"
GENERATED = ROOT / "generated" / "agon_lawful_move_registry.min.json"

REQUIRED_FILES = [
    "README.md",
    "CHARTER.md",
    "docs/LAYERS.md",
    "docs/AGON_PREPARATION_POSTURE.md",
    "docs/AGON_LAWFUL_MOVE_LANGUAGE.md",
    "docs/AGON_MOVE_REGISTRY_MODEL.md",
    "docs/AGON_MOVE_OWNER_HANDOFFS.md",
    "docs/AGON_WAVE3_LANDING.md",
    "schemas/agon-lawful-move.schema.json",
    "schemas/agon-lawful-move-registry.schema.json",
    "config/agon_lawful_moves.seed.json",
    "generated/agon_lawful_move_registry.min.json",
]

OPTIONAL_WAVE0_FILES = [
    "docs/AGON_IMPOSITION_POSTURE.md",
    "generated/agon_imposition_readiness.min.json",
]

REQUIRED_MOVE_KEYS = {
    "move_id",
    "name",
    "move_class",
    "intent",
    "allowed_actor_forms",
    "allowed_seats",
    "preconditions",
    "must_not",
    "produces",
    "future_owner_handoffs",
    "status",
    "wave",
    "live_protocol",
    "runtime_effect",
    "center_owns",
    "not_owned_here",
}


def load_builder():
    spec = importlib.util.spec_from_file_location("build_agon_lawful_move_registry", BUILDER_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import builder from {BUILDER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing JSON file: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from exc


def fail(message: str) -> None:
    raise SystemExit(message)


def validate_required_files() -> list[str]:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    if missing:
        fail("missing required Wave III files: " + ", ".join(missing))
    return [rel for rel in OPTIONAL_WAVE0_FILES if (ROOT / rel).exists()]


def validate_registry_shape(registry: dict[str, Any]) -> None:
    if registry.get("wave") != "III":
        fail("registry wave must be III")
    if registry.get("status") != "pre_protocol_lawful_move_language":
        fail("registry status must be pre_protocol_lawful_move_language")

    moves = registry.get("moves")
    if not isinstance(moves, list) or not moves:
        fail("registry moves must be non-empty")

    if registry.get("counts", {}).get("total") != len(moves):
        fail("registry counts.total does not match moves length")

    required_classes = {
        "stance",
        "evidence",
        "trace",
        "contradiction",
        "closure",
        "summon",
        "witness",
        "revision",
        "boundary",
        "escalation",
    }
    seen_classes = {move.get("move_class") for move in moves}
    missing_classes = required_classes - seen_classes
    if missing_classes:
        fail("registry missing move classes: " + ", ".join(sorted(missing_classes)))

    for move in moves:
        move_id = move.get("move_id", "<unknown>")
        unexpected_keys = sorted(set(move) - REQUIRED_MOVE_KEYS)
        if unexpected_keys:
            fail(f"{move_id}: unexpected move keys present: {unexpected_keys}")
        if move.get("live_protocol") is not False:
            fail(f"{move_id}: live_protocol must remain false")
        if move.get("runtime_effect") != "none":
            fail(f"{move_id}: runtime_effect must remain none")
        forbidden_fields = {
            "packet_schema",
            "verdict_schema",
            "scar_schema",
            "retention_schedule",
            "tos_promotion_path",
            "runtime_endpoint",
        }
        present_forbidden = sorted(forbidden_fields.intersection(move))
        if present_forbidden:
            fail(f"{move_id}: forbidden protocol/runtime fields present: {present_forbidden}")

        if "assistant_service_actor" in move.get("allowed_actor_forms", []):
            forbidden_seats = {"judge_candidate"}
            seat_overlap = forbidden_seats.intersection(move.get("allowed_seats", []))
            if seat_overlap:
                fail(f"{move_id}: assistant actor received forbidden seat(s): {sorted(seat_overlap)}")
        if move.get("move_class") == "summon":
            if move.get("allowed_actor_forms") != ["agonic_contestant_candidate"]:
                fail(f"{move_id}: summon allowed_actor_forms must remain contestant-only")
            if move.get("allowed_seats") != ["contestant"]:
                fail(f"{move_id}: summon allowed_seats must remain contestant-only")

    non_goals = " ".join(registry.get("non_goals", []))
    for phrase in ["live arena sessions", "verdict logic", "scar writes", "retention scheduling", "Tree-of-Sophia canonization"]:
        if phrase not in non_goals:
            fail(f"registry non_goals must include {phrase!r}")


def main() -> int:
    wave0_present = validate_required_files()

    builder = load_builder()
    expected = builder.dumps_min(builder.build_registry())
    existing = GENERATED.read_text(encoding="utf-8")
    if existing != expected:
        fail("generated/agon_lawful_move_registry.min.json is stale; run scripts/build_agon_lawful_move_registry.py")

    registry = read_json(GENERATED)
    validate_registry_shape(registry)

    print("ok: Wave III lawful move language is valid")
    if wave0_present:
        print("ok: optional Wave 0 imposition surfaces detected: " + ", ".join(wave0_present))
    else:
        print("note: Wave 0 imposition surfaces not detected by this validator; Wave III shape is still internally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
