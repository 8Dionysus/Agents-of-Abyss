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
    path = ROOT / "mechanics" / "experience" / "parts" / "governance-polis" / "scripts" / "validate_governance_polis.py"
    spec = importlib.util.spec_from_file_location("experience_wave4_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads((ROOT / "mechanics" / "experience" / "parts" / "governance-polis" / "examples" / "experience_wave4_polis_constitution.example.json").read_text())


def test_experience_wave4_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/experience/parts/governance-polis/scripts/validate_governance_polis.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_wave4_requires_v08_before_v09() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    seeds = bad_flow["source_seeds"]
    assert isinstance(seeds, list)
    seeds.reverse()

    with pytest.raises(validator.ValidationError, match="v0.8 before v0.9"):
        validator.validate_example(bad_flow)


def test_experience_wave4_rejects_codex_vote_authority() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    may = authority["codex_may"]
    assert isinstance(may, list)
    may.append("vote")

    with pytest.raises(validator.ValidationError, match="denied authority"):
        validator.validate_example(bad_flow)


def test_experience_wave4_rejects_missing_assistant_recharter_block() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    denied = authority["assistant_must_not"]
    assert isinstance(denied, list)
    denied.remove("self-recharter")

    with pytest.raises(validator.ValidationError, match="assistant_must_not"):
        validator.validate_example(bad_flow)


def test_experience_wave4_requires_ordered_runtime_seal_before_reveal() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    runtime_flow = bad_flow["runtime_flow"]
    assert isinstance(runtime_flow, list)
    runtime_flow[3], runtime_flow[4] = runtime_flow[4], runtime_flow[3]

    with pytest.raises(validator.ValidationError, match="ordered spine"):
        validator.validate_example(bad_flow)


def test_experience_wave4_requires_all_owner_repos() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    owner_split = bad_flow["owner_split"]
    assert isinstance(owner_split, list)
    owner_split[:] = [item for item in owner_split if item.get("repo") != "Tree-of-Sophia"]

    with pytest.raises(validator.ValidationError, match="owner_split is missing"):
        validator.validate_example(bad_flow)
