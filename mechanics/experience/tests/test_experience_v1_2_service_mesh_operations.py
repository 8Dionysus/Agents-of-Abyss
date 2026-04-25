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
    path = ROOT / "mechanics" / "experience" / "scripts" / "validate_experience_v1_2_service_mesh_operations.py"
    spec = importlib.util.spec_from_file_location("experience_v12_service_mesh_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads(
        (ROOT / "mechanics" / "experience" / "examples" / "experience_v1_2_service_mesh_operations.example.json").read_text(
            encoding="utf-8"
        )
    )


def load_schema() -> dict[str, object]:
    return json.loads(
        (ROOT / "mechanics" / "experience" / "schemas" / "experience-v1-2-service-mesh-operations.schema.json").read_text(
            encoding="utf-8"
        )
    )


def test_experience_v12_service_mesh_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/experience/scripts/validate_experience_v1_2_service_mesh_operations.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_v12_service_mesh_requires_source_archive() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["archive_name"] = "aoa-experience-office-foundry-role-pairs-seed-v1_3.zip"

    with pytest.raises(validator.ValidationError, match="archive_name|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_rejects_runtime_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_service_activation"] = True

    with pytest.raises(validator.ValidationError, match="schema|live_service_activation"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_rejects_codex_drill_pass_authority() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    may = authority["codex_may"]
    assert isinstance(may, list)
    may.append("certify drill passed")

    with pytest.raises(validator.ValidationError, match="codex_may"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_rejects_codex_worker_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    may = authority["codex_may"]
    assert isinstance(may, list)
    may.append("activate worker")

    with pytest.raises(validator.ValidationError, match="codex_may"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_rejects_codex_scheduler_loop() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    may = authority["codex_may"]
    assert isinstance(may, list)
    may.append("open scheduler loop")

    with pytest.raises(validator.ValidationError, match="codex_may"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "forbidden_grant",
    [
        "write directly to Tree-of-Sophia",
        "mutate trust",
        "execute retention",
        "runtime execution is allowed",
        "execute live drill",
        "run live service",
        "start runtime job",
    ],
)
def test_experience_v12_service_mesh_rejects_codex_authority_leaks(
    forbidden_grant: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    may = authority["codex_may"]
    assert isinstance(may, list)
    may.append(forbidden_grant)

    with pytest.raises(validator.ValidationError, match="codex_may|forbidden service authority"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_requires_assistant_self_heal_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    denied = authority["assistant_must_not"]
    assert isinstance(denied, list)
    denied.remove("self-heal persistent mandate")

    with pytest.raises(validator.ValidationError, match="assistant_must_not"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_requires_failure_law_order() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    laws = bad_payload["failure_laws"]
    assert isinstance(laws, list)
    laws.reverse()

    with pytest.raises(validator.ValidationError, match="failure_laws"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_requires_flow_order() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["operations_flow"]
    assert isinstance(flow, list)
    flow[2], flow[3] = flow[3], flow[2]

    with pytest.raises(validator.ValidationError, match="contiguous|spine"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_requires_flow_owner_routing() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["operations_flow"]
    assert isinstance(flow, list)
    flow[1]["owner"] = "abyss-stack"

    with pytest.raises(validator.ValidationError, match="owners"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_requires_flow_stop_lines() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["operations_flow"]
    assert isinstance(flow, list)
    flow[1]["stop_lines"] = []

    with pytest.raises(validator.ValidationError, match="stop_lines"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_requires_flow_stop_lines_in_schema() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["operations_flow"]
    assert isinstance(flow, list)
    del flow[1]["stop_lines"]

    with pytest.raises(validator.ValidationError, match="schema|stop_lines"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "authority_note",
    [
        "runtime executes scheduler loop",
        "scheduler loop may run for this drill",
        "runtime execution is allowed for this step",
    ],
)
def test_experience_v12_service_mesh_rejects_flow_runtime_authority_note(
    authority_note: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["operations_flow"]
    assert isinstance(flow, list)
    flow[1]["authority_note"] = authority_note

    with pytest.raises(validator.ValidationError, match="authority_note"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_requires_runtime_owner_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "abyss-stack":
            entry["owns"] = "runtime jobs workers storage and drill substrate"

    with pytest.raises(validator.ValidationError, match="runtime-owner gate"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_requires_runtime_doctrine_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    derived = authority["derived_layers_must_not"]
    assert isinstance(derived, list)
    derived.remove("runtime_as_doctrine")

    with pytest.raises(validator.ValidationError, match="derived_layers_must_not"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_requires_sdk_authority_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    derived = authority["derived_layers_must_not"]
    assert isinstance(derived, list)
    derived.remove("sdk_as_authority")

    with pytest.raises(validator.ValidationError, match="derived_layers_must_not"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v12_service_mesh_requires_all_owner_repos() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    owner_split[:] = [entry for entry in owner_split if entry.get("repo") != "aoa-routing"]

    with pytest.raises(validator.ValidationError, match="owner_split|schema"):
        validator.validate_payload(bad_payload, schema)
