from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError as JSONSchemaValidationError


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()


def load_validator():
    path = ROOT / "mechanics" / "experience" / "parts" / "continuity-context" / "scripts" / "validate_living_workspace_continuity.py"
    spec = importlib.util.spec_from_file_location("experience_v20_living_workspace_runtime_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads(
        (ROOT / "mechanics" / "experience" / "parts" / "continuity-context" / "examples" / "experience_v2_0_living_workspace_continuity_runtime.example.json").read_text(
            encoding="utf-8"
        )
    )


def load_schema() -> dict[str, object]:
    return json.loads(
        (ROOT / "mechanics" / "experience" / "parts" / "continuity-context" / "schemas" / "experience-v2-0-living-workspace-continuity-runtime.schema.json").read_text(
            encoding="utf-8"
        )
    )


def validate_schema_only(payload: dict[str, object], schema: dict[str, object]) -> None:
    Draft202012Validator(schema).validate(payload)


def test_experience_v20_living_workspace_runtime_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/experience/parts/continuity-context/scripts/validate_living_workspace_continuity.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_v20_living_workspace_runtime_requires_source_archive() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["archive_name"] = "aoa-experience-context-memory-weaving-continuity-loom-seed-v1_9.zip"

    with pytest.raises(validator.ValidationError, match="source_seed|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_schema_rejects_wrong_runtime_seam() -> None:
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["runtime_seam"] = ".codex/session"

    with pytest.raises(JSONSchemaValidationError):
        validate_schema_only(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_rejects_live_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_workspace_runtime_activation"] = True

    with pytest.raises(validator.ValidationError, match="live_workspace_runtime_activation|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_rejects_live_codex_continuity_installation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_codex_continuity_installation"] = True

    with pytest.raises(validator.ValidationError, match="live_codex_continuity_installation|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_rejects_self_continuity_sovereignty() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_self_continuity_sovereignty"] = True

    with pytest.raises(validator.ValidationError, match="live_self_continuity_sovereignty|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_requires_wave9_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/experience/legacy/raw/EXPERIENCE_V1_9_CONTEXT_MEMORY_WEAVING_CONTINUITY_LOOM.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_requires_workspace_install_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("8Dionysus:docs/WORKSPACE_INSTALL.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_schema_rejects_wrong_projection_owner() -> None:
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    requests = bad_payload["runtime_requests"]
    assert isinstance(requests, list)
    requests[0]["owner"] = "Agents-of-Abyss"

    with pytest.raises(JSONSchemaValidationError):
        validate_schema_only(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_requires_tos_owned_runtime_boundary_review() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    requests = bad_payload["runtime_requests"]
    assert isinstance(requests, list)
    requests[7]["owner"] = "aoa-evals"

    with pytest.raises(validator.ValidationError, match="runtime_requests|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_requires_tos_owned_runtime_boundary_flow_step() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["runtime_flow"]
    assert isinstance(flow, list)
    flow[10]["owner"] = "aoa-memo"

    with pytest.raises(validator.ValidationError, match="runtime_flow|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_schema_rejects_wrong_integrity_flow_owner() -> None:
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["runtime_flow"]
    assert isinstance(flow, list)
    flow[9]["owner"] = "aoa-routing"

    with pytest.raises(JSONSchemaValidationError):
        validate_schema_only(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_requires_runtime_owner_human_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    gates = authority["human_gates_required"]
    assert isinstance(gates, list)
    gates.remove("runtime-owner gate before install storage cache worker scheduler daemon or background resume")

    with pytest.raises(validator.ValidationError, match="authority|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "guard",
    [
        "no_live_workspace_runtime_activation",
        "no_hidden_codex_continuity_installation",
        "no_self_continuity_sovereignty",
        "no_assistant_self_authorized_continuity",
        "no_codex_durable_continuity_approval",
        "no_checkpoint_export_without_budget_and_evidence",
        "no_memory_owner_theft",
        "no_personal_context_overreach",
        "no_stale_context_as_fresh_evidence",
        "no_replay_hash_break_bypass",
        "no_route_loop_runtime_escalation",
        "no_runtime_migration_without_backup_and_operator_gate",
        "no_worker_scheduler_or_daemon_activation",
        "no_direct_tree_of_sophia_runtime_write",
        "no_dashboard_or_state_machine_sovereignty",
        "no_continuity_as_consciousness_claim",
        "no_raw_archive_or_generated_runtime_promotion",
    ],
)
def test_experience_v20_living_workspace_runtime_requires_hard_guards(guard: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    guards = bad_payload["hard_guards"]
    assert isinstance(guards, list)
    guards.remove(guard)

    with pytest.raises(validator.ValidationError, match="hard_guards|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_schema_rejects_missing_hard_guard() -> None:
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    guards = bad_payload["hard_guards"]
    assert isinstance(guards, list)
    guards.remove("no_codex_durable_continuity_approval")

    with pytest.raises(JSONSchemaValidationError):
        validate_schema_only(bad_payload, schema)


def test_experience_v20_living_workspace_runtime_rejects_active_landing_state() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    activation = bad_payload["blocking_contracts"]["activation_state"]
    assert isinstance(activation, dict)
    states = activation["allowed_landing_states"]
    assert isinstance(states, list)
    states.append("active")

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "shared_root_projection_without_source_owner_allowed",
        "live_codex_continuity_path_write_allowed",
        "helper_seam_authority_theft_allowed",
        "missing_layout_promotion_allowed",
        "workspace_sovereignty_claim_allowed",
    ],
)
def test_experience_v20_living_workspace_runtime_blocks_projection_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["projection_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "assistant_self_continuity_allowed",
        "codex_durable_continuity_approval_allowed",
        "memory_owner_theft_allowed",
        "personal_context_overreach_allowed",
        "direct_tos_runtime_write_allowed",
    ],
)
def test_experience_v20_living_workspace_runtime_blocks_authority_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["authority_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "checkpoint_export_without_budget_allowed",
        "checkpoint_export_without_evidence_allowed",
        "stale_context_as_fresh_evidence_allowed",
        "replay_hash_break_ignored_allowed",
        "route_loop_ignored_allowed",
    ],
)
def test_experience_v20_living_workspace_runtime_blocks_integrity_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["integrity_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "migration_without_backup_allowed",
        "worker_or_daemon_activation_allowed",
        "hidden_scheduler_allowed",
        "auto_runtime_resume_allowed",
        "dashboard_or_state_machine_authority_allowed",
    ],
)
def test_experience_v20_living_workspace_runtime_blocks_runtime_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["runtime_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)
