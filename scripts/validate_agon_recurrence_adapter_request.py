#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "generated" / "agon_recurrence_adapter_request.min.json"

REQUIRED_STOP_LINES = {
    "no_arena_session_creation",
    "no_sealed_commit_creation",
    "no_live_move_execution",
    "no_verdict_authority",
    "no_scar_write",
    "no_retention_scheduling",
    "no_rank_mutation",
    "no_tree_of_sophia_promotion",
    "no_hidden_scheduler",
    "no_auto_owner_mutation",
    "no_assistant_contestant_drift",
    "no_source_meaning_rewrite",
}

def fail(msg: str) -> int:
    print(f"agon recurrence adapter request validation failed: {msg}", file=sys.stderr)
    return 1

def main() -> int:
    builder = ROOT / "scripts" / "build_agon_recurrence_adapter_request.py"
    result = subprocess.run([sys.executable, str(builder), "--check"], cwd=ROOT)
    if result.returncode != 0:
        return result.returncode

    data = json.loads(REQ.read_text(encoding="utf-8"))
    if data.get("interlude") != "R4":
        return fail("interlude must be R4")
    if data.get("owner_repo") != "Agents-of-Abyss":
        return fail("owner_repo must be Agents-of-Abyss")
    if data.get("target_primary_repo") != "aoa-sdk":
        return fail("target_primary_repo must be aoa-sdk")
    if data.get("live_protocol") is not False:
        return fail("live_protocol must be false")
    if data.get("runtime_effect") != "none":
        return fail("runtime_effect must be none")
    missing = REQUIRED_STOP_LINES - set(data.get("stop_lines", []))
    if missing:
        return fail(f"missing stop-lines: {sorted(missing)}")
    comps = data.get("requested_components", [])
    if len(comps) < 6:
        return fail("expected at least six requested components")
    refs = [c.get("component_ref") for c in comps]
    if len(refs) != len(set(refs)):
        return fail("duplicate component refs")
    repos = {c.get("target_repo") for c in comps}
    required_repos = {"Agents-of-Abyss", "aoa-agents", "aoa-routing", "aoa-playbooks", "aoa-techniques", "aoa-skills"}
    if not required_repos.issubset(repos):
        return fail(f"missing target repos: {sorted(required_repos - repos)}")
    for comp in comps:
        if not comp.get("observed_surfaces"):
            return fail(f"component missing observed surfaces: {comp.get('component_ref')}")
        if "aoa-memo" in comp.get("target_repo", "") or "Tree-of-Sophia" in comp.get("target_repo", ""):
            return fail("adapter request must not target memo or ToS directly")
    print("agon recurrence adapter request validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
