from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_lawful_move_registry_is_current() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/build_agon_lawful_move_registry.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_lawful_move_registry_pre_protocol_invariants() -> None:
    registry_path = ROOT / "generated" / "agon_lawful_move_registry.min.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))

    assert registry["wave"] == "III"
    assert registry["status"] == "pre_protocol_lawful_move_language"
    assert registry["counts"]["total"] == len(registry["moves"])
    assert registry["counts"]["total"] >= 10

    classes = {move["move_class"] for move in registry["moves"]}
    assert {
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
    }.issubset(classes)

    move_ids = [move["move_id"] for move in registry["moves"]]
    assert move_ids == sorted(move_ids)
    assert len(move_ids) == len(set(move_ids))

    for move in registry["moves"]:
        assert move["live_protocol"] is False
        assert move["runtime_effect"] == "none"
        assert "runtime packet shape" in move["not_owned_here"]
        assert "verdict logic" in move["not_owned_here"]
        assert "scar storage" in move["not_owned_here"]
        assert "retention check" in move["not_owned_here"]
        assert "Tree-of-Sophia canonization" in move["not_owned_here"]

        if "assistant_service_actor" in move["allowed_actor_forms"]:
            assert "judge_candidate" not in move["allowed_seats"]
            assert move["move_class"] != "summon"
