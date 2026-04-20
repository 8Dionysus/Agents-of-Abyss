from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_agon_move_owner_binding_registry_is_current() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/build_agon_move_owner_binding_registry.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_agon_move_owner_binding_registry_shape() -> None:
    data = json.loads((ROOT / "generated" / "agon_move_owner_binding_registry.min.json").read_text())
    assert data["wave"] == "IV"
    assert data["status"] == "pre_protocol_owner_binding"
    assert data["total_bindings"] == 18
    assert data["owner_counts"]["Agents-of-Abyss"] == 18
    assert all(binding["live_protocol"] is False for binding in data["bindings"])
    assert all(binding["runtime_effect"] == "none" for binding in data["bindings"])
    assert any("aoa-techniques" in binding["owner_repos"] for binding in data["bindings"])
    assert any("aoa-skills" in binding["owner_repos"] for binding in data["bindings"])
