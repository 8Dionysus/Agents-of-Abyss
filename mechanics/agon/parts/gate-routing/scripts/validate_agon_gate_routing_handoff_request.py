#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
REQUEST_PATH = ROOT / "mechanics" / "agon" / "parts" / "gate-routing" / "generated" / "agon_gate_routing_handoff_request.min.json"
REQUIRED_ROUTING_STOP_LINES = {
    "create_arena_session",
    "perform_sealed_commit",
    "issue_verdict",
    "write_scar",
    "schedule_retention",
    "mutate_rank",
    "grant_closure",
    "grant_summon_authority",
    "promote_to_tree_of_sophia",
    "author_agon_law",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "mechanics" / "agon" / "parts" / "gate-routing" / "scripts" / "build_agon_gate_routing_handoff_request.py"), "--check"],
        check=True,
    )
    request = load_json(REQUEST_PATH)

    require(request["schema_version"] == "agon_gate_routing_handoff_request.v1", "wrong schema version")
    require(request["owner_repo"] == "Agents-of-Abyss", "request must be center-owned")
    require(request["routing_repo"] == "aoa-routing", "routing repo mismatch")
    require("agon_gate_candidate" in request["routing_may_emit"], "gate candidate output missing")
    missing = sorted(REQUIRED_ROUTING_STOP_LINES - set(request["routing_must_not"]))
    require(not missing, f"missing routing stop-lines: {missing}")
    require(request["required_stop_line"] == "routing hint is not arena activation", "missing required stop-line")

    expected = ROOT.parent / "aoa-routing" / "generated" / "agon_gate_routing_registry.min.json"
    if expected.exists():
        print("found aoa-routing gate registry")
    else:
        print("optional aoa-routing gate registry not found")
    print("Agon gate routing handoff request validation passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
