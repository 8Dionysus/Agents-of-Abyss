#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "generated" / "agon_trial_playbook_request.min.json"
REQUIRED_STOP_LINES = {
    "no_arena_session_creation", "no_live_move_execution", "no_verdict_authority",
    "no_scar_write", "no_retention_schedule", "no_rank_mutation",
    "no_tos_promotion", "no_hidden_assistant_contestant",
}

def fail(msg: str) -> int:
    print(f"agon trial playbook request validation failed: {msg}", file=sys.stderr)
    return 1

def main() -> int:
    builder = ROOT / "scripts" / "build_agon_trial_playbook_request.py"
    result = subprocess.run([sys.executable, str(builder), "--check"], cwd=ROOT)
    if result.returncode != 0:
        return result.returncode
    data = json.loads(REQ.read_text(encoding="utf-8"))
    if data.get("wave") != "VI":
        return fail("wave must be VI")
    if data.get("target_repo") != "aoa-playbooks":
        return fail("target_repo must be aoa-playbooks")
    if data.get("live_protocol") is not False:
        return fail("live_protocol must be false")
    if data.get("runtime_effect") != "none":
        return fail("runtime_effect must be none")
    missing = REQUIRED_STOP_LINES - set(data.get("stop_lines", []))
    if missing:
        return fail(f"missing stop-lines: {sorted(missing)}")
    trials = data.get("requested_trial_playbooks", [])
    if len(trials) < 5:
        return fail("expected at least five requested trials")
    ids = [t.get("id") for t in trials]
    if len(ids) != len(set(ids)):
        return fail("duplicate playbook ids")
    for trial in trials:
        if not trial.get("trial_id", "").startswith("agon.trial."):
            return fail(f"bad trial_id: {trial.get('trial_id')}")
        if not trial.get("lawful_moves"):
            return fail(f"trial missing lawful_moves: {trial.get('id')}")
        if not trial.get("gate_triggers"):
            return fail(f"trial missing gate_triggers: {trial.get('id')}")
    print("agon trial playbook request validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
