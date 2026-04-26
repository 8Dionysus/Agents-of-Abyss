from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


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
        / "certification-proof"
        / "scripts"
        / "validate_certification_proof.py"
    )
    spec = importlib.util.spec_from_file_location(
        "experience_certification_watchtower_validator_test", path
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
            / "certification-proof"
            / "examples"
            / "experience_certification_watchtower.example.json"
        ).read_text()
    )


def test_experience_certification_watchtower_validator_passes() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "mechanics/experience/parts/certification-proof/scripts/validate_certification_proof.py",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_certification_watchtower_rejects_codex_certification() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    may = authority["codex_may"]
    assert isinstance(may, list)
    may.append("certify")

    with pytest.raises(validator.ValidationError, match="denied authority"):
        validator.validate_example(bad_flow)


def test_experience_certification_watchtower_rejects_codex_ring_promotion() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    denied = authority["codex_must_not"]
    assert isinstance(denied, list)
    denied.remove("promote rollout rings")

    with pytest.raises(validator.ValidationError, match="codex_must_not"):
        validator.validate_example(bad_flow)


def test_experience_certification_watchtower_rejects_out_of_order_watchtower() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    deployment_flow = bad_flow["deployment_flow"]
    assert isinstance(deployment_flow, list)
    deployment_flow[1], deployment_flow[2] = deployment_flow[2], deployment_flow[1]

    with pytest.raises(validator.ValidationError, match="ordered spine"):
        validator.validate_example(bad_flow)


def test_seeded_center_examples_validate_against_schemas() -> None:
    stems = [
        example.name.removesuffix(".example.json")
        for example in sorted(
            (
                ROOT
                / "mechanics"
                / "experience"
                / "parts"
                / "certification-proof"
                / "examples"
            ).glob("experience_*.example.json")
        )
    ]
    paired = []
    for stem in stems:
        schema_path = (
            ROOT
            / "mechanics"
            / "experience"
            / "parts"
            / "certification-proof"
            / "schemas"
            / f"{stem}_v1.json"
        )
        example_path = (
            ROOT
            / "mechanics"
            / "experience"
            / "parts"
            / "certification-proof"
            / "examples"
            / f"{stem}.example.json"
        )
        if schema_path.exists():
            paired.append((schema_path, example_path))
    assert paired
    for schema_path, example_path in paired:
        schema = json.loads(schema_path.read_text())
        example = json.loads(example_path.read_text())
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema).iter_errors(example),
            key=lambda error: list(error.path),
        )
        assert not errors, f"{example_path.name}: {errors[0].message if errors else ''}"
