from __future__ import annotations

import json
from pathlib import Path

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump_min(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def test_agon_gate_handoff_request_is_current():
    config = load_json(ROOT / "config" / "agon_gate_routing_handoff_request.seed.json")
    current = (ROOT / "generated" / "agon_gate_routing_handoff_request.min.json").read_text(encoding="utf-8")
    assert current == dump_min(config)


def test_agon_gate_handoff_preserves_center_law():
    request = load_json(ROOT / "generated" / "agon_gate_routing_handoff_request.min.json")

    assert request["owner_repo"] == "Agents-of-Abyss"
    assert request["routing_repo"] == "aoa-routing"
    assert "agon_gate_candidate" in request["routing_may_emit"]
    assert "create_arena_session" in request["routing_must_not"]
    assert "issue_verdict" in request["routing_must_not"]
    assert "write_scar" in request["routing_must_not"]
    assert "grant_closure" in request["routing_must_not"]
    assert "grant_summon_authority" in request["routing_must_not"]
    assert "future_arena_session_model" in request["center_must_keep"]
    assert request["required_stop_line"] == "routing hint is not arena activation"
