import json
import subprocess
import sys
from pathlib import Path

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()

def test_agon_trial_playbook_request_build_check():
    result = subprocess.run(
        [sys.executable, str(ROOT / "mechanics" / "agon" / "parts" / "trial-handoff" / "scripts" / "build_agon_trial_playbook_request.py"), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout

def test_agon_trial_playbook_request_shape():
    data = json.loads((ROOT / "mechanics" / "agon" / "parts" / "trial-handoff" / "generated" / "agon_trial_playbook_request.min.json").read_text(encoding="utf-8"))
    assert data["schema_version"] == "agon-trial-playbook-request-v1"
    assert data["wave"] == "VI"
    assert data["live_protocol"] is False
    assert data["runtime_effect"] == "none"
    assert data["trial_count"] == len(data["requested_trial_playbooks"])
    assert "no_arena_session_creation" in data["stop_lines"]
    assert "no_sealed_commit_runtime" in data["stop_lines"]
    assert "no_runtime_substrate_claim" in data["stop_lines"]
    assert all(t["handoff_status"] == "requested_for_playbook_owner_landing" for t in data["requested_trial_playbooks"])
