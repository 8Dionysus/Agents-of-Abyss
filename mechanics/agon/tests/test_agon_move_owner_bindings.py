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
    path = ROOT / "mechanics" / "agon" / "scripts" / "build_agon_move_owner_binding_registry.py"
    spec = importlib.util.spec_from_file_location("agon_move_owner_binding_builder_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_agon_move_owner_binding_registry_is_current() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/agon/scripts/build_agon_move_owner_binding_registry.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_agon_move_owner_binding_registry_shape() -> None:
    data = json.loads((ROOT / "mechanics" / "agon" / "generated" / "agon_move_owner_binding_registry.min.json").read_text())
    assert data["wave"] == "IV"
    assert data["status"] == "pre_protocol_owner_binding"
    assert data["total_bindings"] == 18
    assert data["owner_counts"]["Agents-of-Abyss"] == 18
    assert all(binding["live_protocol"] is False for binding in data["bindings"])
    assert all(binding["runtime_effect"] == "none" for binding in data["bindings"])
    assert any("aoa-techniques" in binding["owner_repos"] for binding in data["bindings"])
    assert any("aoa-skills" in binding["owner_repos"] for binding in data["bindings"])


def test_owner_binding_validator_rejects_non_list_fields() -> None:
    builder = load_builder()
    config = json.loads((ROOT / "mechanics" / "agon" / "config" / "agon_move_owner_bindings.seed.json").read_text(encoding="utf-8"))
    config["bindings"][0]["owner_bindings"][0]["candidate_refs"] = "center:broken"
    with pytest.raises(builder.ValidationError, match="candidate_refs must be a non-empty list of strings"):
        builder.validate_config(config)


def test_owner_binding_validator_rejects_move_class_drift() -> None:
    builder = load_builder()
    config = json.loads((ROOT / "mechanics" / "agon" / "config" / "agon_move_owner_bindings.seed.json").read_text(encoding="utf-8"))
    config["bindings"][0]["move_class"] = "typo"
    with pytest.raises(builder.ValidationError, match="invalid move_class"):
        builder.validate_config(config)
