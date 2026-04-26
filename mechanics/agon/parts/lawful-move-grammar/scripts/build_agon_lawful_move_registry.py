#!/usr/bin/env python3
"""Build the compact Agon lawful move registry.

This script intentionally uses only the Python standard library.
It validates the Wave III pre-protocol vocabulary without claiming live arena runtime.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
SOURCE = ROOT / "mechanics" / "agon" / "parts" / "lawful-move-grammar" / "config" / "agon_lawful_moves.seed.json"
OUTPUT = ROOT / "mechanics" / "agon" / "parts" / "lawful-move-grammar" / "generated" / "agon_lawful_move_registry.min.json"

MOVE_CLASSES = {
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

ACTOR_FORMS = {
    "agonic_contestant_candidate",
    "agonic_witness_candidate",
    "agonic_judge_candidate",
    "assistant_service_actor",
}

SEATS = {
    "contestant",
    "witness",
    "judge_candidate",
    "service_actor",
}

NON_GOALS = [
    "live arena sessions",
    "sealed commits",
    "runtime packets",
    "contradiction ledger storage",
    "verdict logic",
    "scar writes",
    "retention scheduling",
    "Tree-of-Sophia canonization",
]

EXPECTED_MOVE_KEYS = {
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


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing required file: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from exc


def fail(message: str) -> None:
    raise SystemExit(message)


def require_string(move: dict[str, Any], key: str) -> str:
    value = move.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{move.get('move_id', '<unknown>')}: {key} must be a non-empty string")
    return value


def require_string_list(move: dict[str, Any], key: str, allowed: set[str] | None = None) -> list[str]:
    value = move.get(key)
    if not isinstance(value, list) or not value:
        fail(f"{move.get('move_id', '<unknown>')}: {key} must be a non-empty list")
    if len(value) != len(set(value)):
        fail(f"{move.get('move_id', '<unknown>')}: {key} must not contain duplicates")
    for item in value:
        if not isinstance(item, str) or not item.strip():
            fail(f"{move.get('move_id', '<unknown>')}: {key} items must be non-empty strings")
        if allowed is not None and item not in allowed:
            fail(f"{move.get('move_id', '<unknown>')}: invalid {key} item {item!r}")
    return value


def validate_move(move: dict[str, Any]) -> None:
    move_id = require_string(move, "move_id")
    if not re.match(r"^agon\.move\.[a-z_]+\.[a-z0-9_]+$", move_id):
        fail(f"{move_id}: move_id must match agon.move.<class>.<slug>")
    unexpected_keys = sorted(set(move) - EXPECTED_MOVE_KEYS)
    if unexpected_keys:
        fail(f"{move_id}: unexpected keys present: {unexpected_keys}")

    name = require_string(move, "name")
    move_class = require_string(move, "move_class")
    if move_class not in MOVE_CLASSES:
        fail(f"{move_id}: invalid move_class {move_class!r}")

    expected_prefix = f"agon.move.{move_class}."
    if not move_id.startswith(expected_prefix):
        fail(f"{move_id}: move_id class segment must match move_class {move_class!r}")

    if name != move_id.rsplit(".", 1)[-1]:
        fail(f"{move_id}: name must match final move_id segment")

    require_string(move, "intent")
    actor_forms = require_string_list(move, "allowed_actor_forms", ACTOR_FORMS)
    seats = require_string_list(move, "allowed_seats", SEATS)
    require_string_list(move, "preconditions")
    must_not = require_string_list(move, "must_not")
    require_string_list(move, "produces")
    require_string_list(move, "center_owns")
    not_owned_here = require_string_list(move, "not_owned_here")

    if move.get("status") != "seeded_pre_protocol":
        fail(f"{move_id}: status must be seeded_pre_protocol")
    if move.get("wave") != "III":
        fail(f"{move_id}: wave must be III")
    if move.get("live_protocol") is not False:
        fail(f"{move_id}: live_protocol must be false")
    if move.get("runtime_effect") != "none":
        fail(f"{move_id}: runtime_effect must be none")

    handoffs = move.get("future_owner_handoffs")
    if not isinstance(handoffs, dict) or not handoffs:
        fail(f"{move_id}: future_owner_handoffs must be a non-empty object")
    for owner, notes in handoffs.items():
        if not isinstance(owner, str) or not owner.strip():
            fail(f"{move_id}: owner handoff keys must be non-empty strings")
        if not isinstance(notes, list) or not notes:
            fail(f"{move_id}: future_owner_handoffs[{owner!r}] must be a non-empty list")
        for note in notes:
            if not isinstance(note, str) or not note.strip():
                fail(f"{move_id}: owner handoff notes must be non-empty strings")

    forbidden_runtime_claims = {
        "runtime packet",
        "verdict",
        "scar",
        "retention",
        "Tree-of-Sophia",
        "canonization",
    }
    joined_not_owned = " ".join(not_owned_here)
    for claim in forbidden_runtime_claims:
        if claim.lower() not in joined_not_owned.lower():
            fail(f"{move_id}: not_owned_here must explicitly exclude {claim!r}")

    if "assistant_service_actor" in actor_forms:
        forbidden_assistant_seats = {"judge_candidate"}
        overlap = forbidden_assistant_seats.intersection(seats)
        if overlap:
            fail(f"{move_id}: assistant_service_actor must not receive seats {sorted(overlap)}")
        if move_class in {"summon"}:
            fail(f"{move_id}: assistant_service_actor must not participate in summon moves")

    if move_class == "summon":
        if actor_forms != ["agonic_contestant_candidate"] or seats != ["contestant"]:
            fail(f"{move_id}: summon vocabulary is contestant-only in Wave III")
        if "hidden summon" not in " ".join(must_not).lower():
            fail(f"{move_id}: summon moves must explicitly forbid hidden summon")

    if move_class == "closure":
        if not any("closure" in item.lower() for item in must_not + move.get("preconditions", [])):
            fail(f"{move_id}: closure moves must mention closure stop-lines")

    if move_class == "contradiction":
        if not any("contradiction" in item.lower() for item in must_not + move.get("preconditions", [])):
            fail(f"{move_id}: contradiction moves must mention contradiction stop-lines")


def validate_source(source: dict[str, Any]) -> list[dict[str, Any]]:
    if source.get("wave") != "III":
        fail("source wave must be III")
    if source.get("status") != "pre_protocol_language_seed":
        fail("source status must be pre_protocol_language_seed")
    moves = source.get("moves")
    if not isinstance(moves, list) or not moves:
        fail("source moves must be a non-empty list")

    seen: set[str] = set()
    for move in moves:
        if not isinstance(move, dict):
            fail("each move must be an object")
        validate_move(move)
        move_id = move["move_id"]
        if move_id in seen:
            fail(f"duplicate move_id: {move_id}")
        seen.add(move_id)

    return sorted(moves, key=lambda item: item["move_id"])


def build_registry() -> dict[str, Any]:
    source = load_json(SOURCE)
    moves = validate_source(source)

    by_class = Counter(move["move_class"] for move in moves)
    by_actor_form: Counter[str] = Counter()
    by_seat: Counter[str] = Counter()
    for move in moves:
        by_actor_form.update(move["allowed_actor_forms"])
        by_seat.update(move["allowed_seats"])

    return {
        "schema_version": "agon-lawful-move-registry/0.1",
        "generated_by": "mechanics/agon/parts/lawful-move-grammar/scripts/build_agon_lawful_move_registry.py",
        "source": "mechanics/agon/parts/lawful-move-grammar/config/agon_lawful_moves.seed.json",
        "wave": "III",
        "status": "pre_protocol_lawful_move_language",
        "counts": {
            "total": len(moves),
            "by_class": dict(sorted(by_class.items())),
            "by_actor_form": dict(sorted(by_actor_form.items())),
            "by_seat": dict(sorted(by_seat.items())),
        },
        "non_goals": NON_GOALS,
        "moves": moves,
    }


def dumps_min(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated registry is stale")
    args = parser.parse_args(argv)

    registry = build_registry()
    rendered = dumps_min(registry)

    if args.check:
        if not OUTPUT.exists():
            fail(f"missing generated registry: {OUTPUT}")
        existing = OUTPUT.read_text(encoding="utf-8")
        if existing != rendered:
            fail(f"generated registry is stale: {OUTPUT}")
        print(f"ok: {OUTPUT.relative_to(ROOT)} is current")
        return 0

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
