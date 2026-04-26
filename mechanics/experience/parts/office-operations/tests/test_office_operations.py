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
    path = (
        ROOT
        / "mechanics"
        / "experience"
        / "parts"
        / "office-operations"
        / "scripts"
        / "validate_office_operations.py"
    )
    spec = importlib.util.spec_from_file_location(
        "experience_sovereign_office_validator_test", path
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads(
        (
            ROOT
            / "mechanics"
            / "experience"
            / "parts"
            / "office-operations"
            / "examples"
            / "experience_sovereign_office.example.json"
        ).read_text()
    )


def test_experience_sovereign_office_validator_passes() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "mechanics/experience/parts/office-operations/scripts/validate_office_operations.py",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_sovereign_office_requires_v10_before_v11() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    seeds = bad_flow["source_receipt_refs"]
    assert isinstance(seeds, list)
    seeds.reverse()

    with pytest.raises(validator.ValidationError, match="v1.0 before v1.1"):
        validator.validate_example(bad_flow)


def test_experience_sovereign_office_rejects_codex_train_approval_authority() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    may = authority["codex_may"]
    assert isinstance(may, list)
    may.append("approve release trains")

    with pytest.raises(validator.ValidationError, match="denied authority"):
        validator.validate_example(bad_flow)


def test_experience_sovereign_office_rejects_assistant_self_enroll_escape() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    denied = authority["assistant_must_not"]
    assert isinstance(denied, list)
    denied.remove("self-enroll")

    with pytest.raises(validator.ValidationError, match="assistant_must_not"):
        validator.validate_example(bad_flow)


def test_experience_sovereign_office_requires_notary_first_office() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    office = bad_flow["office_contract"]
    assert isinstance(office, dict)
    office["first_office"] = "concierge.assistant"

    with pytest.raises(validator.ValidationError, match="first_office"):
        validator.validate_example(bad_flow)


def test_experience_sovereign_office_blocks_direct_tos_runtime_write() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    office = bad_flow["office_contract"]
    assert isinstance(office, dict)
    office["direct_tos_runtime_write_allowed"] = True

    with pytest.raises(
        validator.ValidationError, match="direct_tos_runtime_write_allowed"
    ):
        validator.validate_example(bad_flow)


def test_experience_sovereign_office_requires_ordered_train_gate_before_seal() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    train_flow = bad_flow["office_train_flow"]
    assert isinstance(train_flow, list)
    train_flow[5], train_flow[8] = train_flow[8], train_flow[5]

    with pytest.raises(validator.ValidationError, match="ordered spine"):
        validator.validate_example(bad_flow)


def test_experience_sovereign_office_requires_all_owner_repos() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    owner_split = bad_flow["owner_split"]
    assert isinstance(owner_split, list)
    owner_split[:] = [
        item for item in owner_split if item.get("repo") != "Tree-of-Sophia"
    ]

    with pytest.raises(validator.ValidationError, match="owner_split is missing"):
        validator.validate_example(bad_flow)
