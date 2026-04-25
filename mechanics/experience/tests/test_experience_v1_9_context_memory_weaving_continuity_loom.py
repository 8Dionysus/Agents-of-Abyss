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
    path = ROOT / "mechanics" / "experience" / "scripts" / "validate_experience_v1_9_context_memory_weaving_continuity_loom.py"
    spec = importlib.util.spec_from_file_location("experience_v19_continuity_loom_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads(
        (ROOT / "mechanics" / "experience" / "examples" / "experience_v1_9_context_memory_weaving_continuity_loom.example.json").read_text(
            encoding="utf-8"
        )
    )


def load_schema() -> dict[str, object]:
    return json.loads(
        (ROOT / "mechanics" / "experience" / "schemas" / "experience-v1-9-context-memory-weaving-continuity-loom.schema.json").read_text(
            encoding="utf-8"
        )
    )


def validate_schema_only(payload: dict[str, object], schema: dict[str, object]) -> None:
    Draft202012Validator(schema).validate(payload)


def test_experience_v19_continuity_loom_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/experience/scripts/validate_experience_v1_9_context_memory_weaving_continuity_loom.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_v19_continuity_loom_requires_source_archive() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["archive_name"] = "aoa-experience-context-routing-nervous-system-seed-v1_8.zip"

    with pytest.raises(validator.ValidationError, match="source_seed|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v19_continuity_loom_schema_rejects_wrong_source_archive() -> None:
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["archive_name"] = "aoa-experience-context-routing-nervous-system-seed-v1_8.zip"

    with pytest.raises(JSONSchemaValidationError):
        validate_schema_only(bad_payload, schema)


def test_experience_v19_continuity_loom_rejects_live_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_continuity_loom_activation"] = True

    with pytest.raises(validator.ValidationError, match="live_continuity_loom_activation|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v19_continuity_loom_rejects_private_memory_sovereignty() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_private_memory_sovereignty"] = True

    with pytest.raises(validator.ValidationError, match="live_private_memory_sovereignty|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v19_continuity_loom_requires_v18_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/experience/legacy/raw/EXPERIENCE_V1_8_CONTEXT_ROUTING_NERVOUS_SYSTEM.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v19_continuity_loom_requires_agon_state_packet_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/agon/docs/AGON_STATE_PACKET_MODEL.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v19_continuity_loom_requires_memo_owned_thread_candidate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    requests = bad_payload["continuity_requests"]
    assert isinstance(requests, list)
    requests[0]["owner"] = "aoa-routing"

    with pytest.raises(validator.ValidationError, match="continuity_requests|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v19_continuity_loom_schema_rejects_wrong_request_owner() -> None:
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    requests = bad_payload["continuity_requests"]
    assert isinstance(requests, list)
    requests[0]["owner"] = "aoa-routing"

    with pytest.raises(JSONSchemaValidationError):
        validate_schema_only(bad_payload, schema)


def test_experience_v19_continuity_loom_requires_routing_owned_reentry_review() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    requests = bad_payload["continuity_requests"]
    assert isinstance(requests, list)
    requests[3]["owner"] = "aoa-memo"

    with pytest.raises(validator.ValidationError, match="continuity_requests|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v19_continuity_loom_requires_tos_owned_canonical_boundary() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["continuity_flow"]
    assert isinstance(flow, list)
    flow[9]["owner"] = "aoa-memo"

    with pytest.raises(validator.ValidationError, match="continuity_flow|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v19_continuity_loom_schema_rejects_wrong_flow_owner() -> None:
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["continuity_flow"]
    assert isinstance(flow, list)
    flow[9]["owner"] = "aoa-memo"

    with pytest.raises(JSONSchemaValidationError):
        validate_schema_only(bad_payload, schema)


def test_experience_v19_continuity_loom_requires_replay_integrity_human_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    gates = authority["human_gates_required"]
    assert isinstance(gates, list)
    gates.remove("owner-local eval approval before merge split or replay integrity use")

    with pytest.raises(validator.ValidationError, match="authority|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "guard",
    [
        "no_live_continuity_loom_activation",
        "no_live_runtime_activation",
        "no_private_memory_sovereignty",
        "no_continuity_without_purpose_evidence_freshness_and_budget",
        "no_false_continuity",
        "no_assistant_private_memory_expansion",
        "no_codex_continuity_approval",
        "no_memory_owner_theft",
        "no_personal_context_overreach",
        "no_symbolic_anchor_evidence_replacement",
        "no_stale_context_dominance",
        "no_continuity_as_consciousness_claim",
        "no_direct_tree_of_sophia_write",
        "no_runtime_continuity_installation",
        "no_dashboard_or_packet_sovereignty",
    ],
)
def test_experience_v19_continuity_loom_requires_hard_guards(guard: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    guards = bad_payload["hard_guards"]
    assert isinstance(guards, list)
    guards.remove(guard)

    with pytest.raises(validator.ValidationError, match="hard_guards|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v19_continuity_loom_rejects_active_landing_state() -> None:
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


def test_experience_v19_continuity_loom_schema_rejects_missing_hard_guard() -> None:
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    guards = bad_payload["hard_guards"]
    assert isinstance(guards, list)
    guards.remove("no_codex_continuity_approval")

    with pytest.raises(JSONSchemaValidationError):
        validate_schema_only(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "continuity_without_evidence_allowed",
        "false_continuity_allowed",
        "codex_continuity_approval_allowed",
        "consciousness_claim_allowed",
        "replay_hash_break_ignored_allowed",
    ],
)
def test_experience_v19_continuity_loom_blocks_evidence_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["evidence_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "assistant_private_memory_allowed",
        "memory_owner_theft_allowed",
        "personal_context_overreach_allowed",
        "symbolic_anchor_overreach_allowed",
        "direct_tos_write_allowed",
    ],
)
def test_experience_v19_continuity_loom_blocks_privacy_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["privacy_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "reentry_without_receipt_allowed",
        "reentry_without_budget_allowed",
        "stale_context_dominance_allowed",
        "context_flood_allowed",
        "merge_without_boundary_review_allowed",
    ],
)
def test_experience_v19_continuity_loom_blocks_continuity_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["continuity_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "durable_memory_write_allowed",
        "retention_execution_allowed",
        "runtime_continuity_install_allowed",
        "hidden_scheduler_allowed",
        "worker_or_daemon_activation_allowed",
    ],
)
def test_experience_v19_continuity_loom_blocks_runtime_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["runtime_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)
