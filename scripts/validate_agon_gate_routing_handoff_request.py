#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUEST_PATH = ROOT / "generated" / "agon_gate_routing_handoff_request.min.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_agon_gate_routing_handoff_request.py"), "--check"],
        check=True,
    )
    request = load_json(REQUEST_PATH)

    require(request["schema_version"] == "agon_gate_routing_handoff_request.v1", "wrong schema version")
    require(request["owner_repo"] == "Agents-of-Abyss", "request must be center-owned")
    require(request["routing_repo"] == "aoa-routing", "routing repo mismatch")
    require("agon_gate_candidate" in request["routing_may_emit"], "gate candidate output missing")
    require("create_arena_session" in request["routing_must_not"], "missing arena stop-line")
    require("issue_verdict" in request["routing_must_not"], "missing verdict stop-line")
    require("write_scar" in request["routing_must_not"], "missing scar stop-line")
    require("promote_to_tree_of_sophia" in request["routing_must_not"], "missing ToS stop-line")
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
