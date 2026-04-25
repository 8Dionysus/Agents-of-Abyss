from __future__ import annotations

import copy
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


def load_validator():
    path = ROOT / "scripts" / "validate_experience_wave1.py"
    spec = importlib.util.spec_from_file_location("experience_wave1_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads((ROOT / "examples" / "experience_wave1_flow.example.json").read_text(encoding="utf-8"))


def test_experience_wave1_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_experience_wave1.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_wave1_rejects_out_of_order_flow() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    bad_events = bad_flow["events"]
    assert isinstance(bad_events, list)
    bad_events[0], bad_events[1] = bad_events[1], bad_events[0]

    with pytest.raises(validator.ValidationError, match="ordered spine"):
        validator.validate_flow(bad_flow)


def test_experience_wave1_rejects_projection_runtime_fields() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    projection = bad_flow["projection"]
    assert isinstance(projection, dict)
    projection["runtime_endpoint"] = "https://example.invalid/run"

    with pytest.raises(validator.ValidationError, match="runtime fields"):
        validator.validate_flow(bad_flow)


def test_experience_wave1_rejects_memory_write_by_center() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    memory_gate = bad_flow["memory_gate"]
    assert isinstance(memory_gate, dict)
    memory_gate["write_performed"] = True

    with pytest.raises(validator.ValidationError, match="write_performed"):
        validator.validate_flow(bad_flow)
