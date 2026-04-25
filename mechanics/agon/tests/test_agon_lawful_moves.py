from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()


def load_builder():
    path = ROOT / "mechanics" / "agon" / "scripts" / "build_agon_lawful_move_registry.py"
    spec = importlib.util.spec_from_file_location("agon_lawful_move_builder_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_lawful_move_registry_is_current() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/agon/scripts/build_agon_lawful_move_registry.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_lawful_move_registry_pre_protocol_invariants() -> None:
    registry_path = ROOT / "mechanics" / "agon" / "generated" / "agon_lawful_move_registry.min.json"
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
        if move["move_class"] == "summon":
            assert move["allowed_actor_forms"] == ["agonic_contestant_candidate"]
            assert move["allowed_seats"] == ["contestant"]


def test_builder_rejects_unknown_move_keys() -> None:
    builder = load_builder()
    move = next(
        item
        for item in json.loads((ROOT / "mechanics" / "agon" / "config" / "agon_lawful_moves.seed.json").read_text(encoding="utf-8"))["moves"]
        if item["move_class"] == "summon"
    )
    bad_move = dict(move)
    bad_move["unexpected"] = "drift"

    with pytest.raises(SystemExit, match="unexpected keys present"):
        builder.validate_move(bad_move)


def test_builder_rejects_non_contestant_summon_semantics() -> None:
    builder = load_builder()
    move = next(
        item
        for item in json.loads((ROOT / "mechanics" / "agon" / "config" / "agon_lawful_moves.seed.json").read_text(encoding="utf-8"))["moves"]
        if item["move_class"] == "summon"
    )
    bad_seats = dict(move)
    bad_seats["allowed_seats"] = ["contestant", "witness"]
    with pytest.raises(SystemExit, match="summon vocabulary is contestant-only"):
        builder.validate_move(bad_seats)

    bad_actor_forms = dict(move)
    bad_actor_forms["allowed_actor_forms"] = ["agonic_contestant_candidate", "agonic_witness_candidate"]
    with pytest.raises(SystemExit, match="summon vocabulary is contestant-only"):
        builder.validate_move(bad_actor_forms)
