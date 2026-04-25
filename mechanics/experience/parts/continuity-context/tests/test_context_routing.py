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
    path = ROOT / "mechanics" / "experience" / "parts" / "continuity-context" / "scripts" / "validate_context_routing.py"
    spec = importlib.util.spec_from_file_location("experience_v18_context_routing_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads(
        (ROOT / "mechanics" / "experience" / "parts" / "continuity-context" / "examples" / "experience_v1_8_context_routing_nervous_system.example.json").read_text(
            encoding="utf-8"
        )
    )


def load_schema() -> dict[str, object]:
    return json.loads(
        (ROOT / "mechanics" / "experience" / "parts" / "continuity-context" / "schemas" / "experience-v1-8-context-routing-nervous-system.schema.json").read_text(
            encoding="utf-8"
        )
    )


def test_experience_v18_context_routing_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/experience/parts/continuity-context/scripts/validate_context_routing.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_v18_context_routing_requires_source_archive() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["archive_name"] = "aoa-experience-affective-economy-honor-treasury-seed-v1_7.zip"

    with pytest.raises(validator.ValidationError, match="source_seed|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v18_context_routing_rejects_live_context_routing_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_context_routing_activation"] = True

    with pytest.raises(validator.ValidationError, match="live_context_routing_activation|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v18_context_routing_rejects_live_owner_override() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_owner_override"] = True

    with pytest.raises(validator.ValidationError, match="live_owner_override|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v18_context_routing_requires_v17_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/experience/legacy/raw/EXPERIENCE_V1_7_AFFECTIVE_ECONOMY_HONOR_TREASURY.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v18_context_routing_requires_gate_routing_handoff_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/agon/docs/AGON_GATE_ROUTING_HANDOFF.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v18_context_routing_requires_eval_owned_service_to_agon_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["routing_flow"]
    assert isinstance(flow, list)
    flow[7]["owner"] = "aoa-routing"

    with pytest.raises(validator.ValidationError, match="routing_flow|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v18_context_routing_requires_tos_owned_dossier_boundary() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["routing_flow"]
    assert isinstance(flow, list)
    flow[9]["owner"] = "aoa-routing"

    with pytest.raises(validator.ValidationError, match="routing_flow|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v18_context_routing_requires_service_to_agon_human_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    gates = authority["human_gates_required"]
    assert isinstance(gates, list)
    gates.remove("owner-local eval approval before service-to-agon escalation")

    with pytest.raises(validator.ValidationError, match="authority|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "guard",
    [
        "no_live_context_routing_activation",
        "no_live_runtime_activation",
        "no_live_owner_override",
        "no_new_repo_creation",
        "no_routing_without_reason_budget_and_receipt",
        "no_salience_as_authority",
        "no_codex_context_override",
        "no_assistant_context_expansion",
        "no_personal_context_overreach",
        "no_affect_or_rank_direct_rights_route",
        "no_service_to_agon_without_lawful_trigger",
        "no_direct_tree_of_sophia_write",
        "no_durable_memory_write",
        "no_runtime_cache_worker_or_scheduler_activation",
        "no_stats_memo_or_routing_as_authority",
    ],
)
def test_experience_v18_context_routing_requires_hard_guards(guard: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    guards = bad_payload["hard_guards"]
    assert isinstance(guards, list)
    guards.remove(guard)

    with pytest.raises(validator.ValidationError, match="hard_guards|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v18_context_routing_rejects_active_landing_state() -> None:
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
        "routing_authorship_of_meaning_allowed",
        "owner_override_allowed",
        "codex_context_override_allowed",
        "assistant_context_expansion_allowed",
        "personal_context_overreach_allowed",
        "direct_tos_write_allowed",
    ],
)
def test_experience_v18_context_routing_blocks_authority_leaks(field: str) -> None:
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
        "route_without_reason_allowed",
        "route_without_budget_allowed",
        "route_without_receipt_allowed",
        "stale_context_reuse_allowed",
        "route_loop_allowed",
        "symbolic_overreach_allowed",
    ],
)
def test_experience_v18_context_routing_blocks_budget_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["budget_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "service_to_agon_without_trigger_allowed",
        "affect_to_rights_direct_route_allowed",
        "rank_or_closure_direct_rights_route_allowed",
        "canonical_risk_direct_write_allowed",
        "automatic_runtime_failover_allowed",
    ],
)
def test_experience_v18_context_routing_blocks_escalation_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["escalation_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "durable_memory_write_allowed",
        "retention_execution_allowed",
        "runtime_cache_activation_allowed",
        "worker_job_activation_allowed",
        "hidden_scheduler_allowed",
    ],
)
def test_experience_v18_context_routing_blocks_memory_runtime_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["memory_runtime_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)
