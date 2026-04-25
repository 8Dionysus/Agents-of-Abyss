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
    path = ROOT / "scripts" / "validate_experience_v1_7_affective_economy_honor_treasury.py"
    spec = importlib.util.spec_from_file_location("experience_v17_affective_honor_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads(
        (
            ROOT
            / "examples"
            / "experience_v1_7_affective_economy_honor_treasury.example.json"
        ).read_text(encoding="utf-8")
    )


def load_schema() -> dict[str, object]:
    return json.loads(
        (
            ROOT
            / "schemas"
            / "experience-v1-7-affective-economy-honor-treasury.schema.json"
        ).read_text(encoding="utf-8")
    )


def test_experience_v17_affective_honor_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_experience_v1_7_affective_economy_honor_treasury.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_v17_affective_honor_requires_source_archive() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["archive_name"] = "aoa-experience-epistemic-memory-rank-reputation-engine-seed-v1_6.zip"

    with pytest.raises(validator.ValidationError, match="source_seed|archive|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v17_affective_honor_rejects_live_affect_governance() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_affect_governance"] = True

    with pytest.raises(validator.ValidationError, match="schema|live_affect_governance"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v17_affective_honor_rejects_live_honor_treasury_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_honor_treasury_activation"] = True

    with pytest.raises(validator.ValidationError, match="schema|live_honor_treasury_activation"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v17_affective_honor_requires_v16_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/experience/legacy/raw/EXPERIENCE_V1_6_EPISTEMIC_MEMORY_RANK_REPUTATION_ENGINE.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|bridge spine|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v17_affective_honor_requires_wave7_handoff_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/agon/docs/AGON_WAVE7_CENTER_HANDOFF.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|bridge spine|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v17_affective_honor_requires_eval_owned_rights_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["affective_flow"]
    assert isinstance(flow, list)
    flow[8]["owner"] = "aoa-agents"

    with pytest.raises(validator.ValidationError, match="affective_flow owners|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "guard",
    [
        "no_affect_without_evidence",
        "no_affect_to_rights_direct_grant",
        "no_honor_as_vanity_score",
        "no_codex_honor_decision",
        "no_assistant_agonic_pride",
        "no_assistant_persistent_affect_rewrite",
        "no_consciousness_claim_from_affect_signal",
        "no_stats_as_authority",
        "no_routing_as_verdict",
        "no_direct_tree_of_sophia_or_kag_canon",
    ],
)
def test_experience_v17_affective_honor_requires_hard_guards(guard: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    guards = bad_payload["hard_guards"]
    assert isinstance(guards, list)
    guards.remove(guard)

    with pytest.raises(validator.ValidationError, match="hard_guards|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v17_affective_honor_rejects_active_landing_state() -> None:
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
        "durable_consequence_without_evidence_allowed",
        "consciousness_claim_allowed",
        "affect_manipulation_allowed",
        "direct_rights_grant_allowed",
    ],
)
def test_experience_v17_affective_honor_blocks_affect_evidence_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    evidence = bad_payload["blocking_contracts"]["affect_evidence"]
    assert isinstance(evidence, dict)
    evidence[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "permanent_shame_allowed",
        "treasury_seal_allowed",
        "direct_rights_revocation_allowed",
    ],
)
def test_experience_v17_affective_honor_blocks_honor_debt_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    debt = bad_payload["blocking_contracts"]["honor_debt_boundary"]
    assert isinstance(debt, dict)
    debt[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "assistant_agonic_pride_allowed",
        "persistent_self_rewrite_allowed",
        "persona_lock_in_allowed",
        "assistant_verdict_authority_allowed",
    ],
)
def test_experience_v17_affective_honor_blocks_assistant_affect_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["assistant_affect_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "route_as_verdict_allowed",
        "automatic_escalation_allowed",
        "stats_as_authority_allowed",
        "dashboard_as_verdict_allowed",
    ],
)
def test_experience_v17_affective_honor_blocks_routing_and_stats_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["routing_and_observability_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "durable_memory_write_allowed",
        "retention_execution_allowed",
        "scheduler_loop_allowed",
        "hidden_ledger_allowed",
    ],
)
def test_experience_v17_affective_honor_blocks_memory_and_runtime_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["memory_retention_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "runtime_write_allowed",
        "direct_node_path_allowed",
        "tos_canon_write_allowed",
        "kag_promotion_allowed",
        "kag_canonization_allowed",
    ],
)
def test_experience_v17_affective_honor_blocks_tos_and_kag_authority(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["tos_kag_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "forbidden_grant",
    [
        "make honor decision",
        "seal treasury",
        "grant rights directly from affect",
        "claim consciousness proof",
        "write durable memory",
        "start hidden scheduler",
        "promote KAG canon",
    ],
)
def test_experience_v17_affective_honor_rejects_codex_authority_leaks(
    forbidden_grant: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    may = bad_payload["authority"]["codex_may"]
    assert isinstance(may, list)
    may.append(forbidden_grant)

    with pytest.raises(validator.ValidationError, match="codex_may|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v17_affective_honor_requires_assistant_rewrite_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    denied = bad_payload["authority"]["assistant_must_not"]
    assert isinstance(denied, list)
    denied.remove("perform persistent affect self-rewrite")

    with pytest.raises(validator.ValidationError, match="assistant_must_not"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v17_affective_honor_requires_eval_rights_gate_human_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    gates = bad_payload["authority"]["human_gates_required"]
    assert isinstance(gates, list)
    gates.remove("owner-local eval approval before affect-to-rights gate use")

    with pytest.raises(validator.ValidationError, match="human_gates_required"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "derived_denial",
    [
        "stats_as_authority",
        "routing_as_verdict",
        "evals_as_live_verdict_authority",
        "honor_as_sovereign_score",
    ],
)
def test_experience_v17_affective_honor_requires_derived_layer_denials(
    derived_denial: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    derived = bad_payload["authority"]["derived_layers_must_not"]
    assert isinstance(derived, list)
    derived.remove(derived_denial)

    with pytest.raises(validator.ValidationError, match="derived_layers_must_not"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "authority_note",
    [
        "affect proves consciousness here",
        "treasury may seal rights directly",
        "assistant persistent rewrite allowed",
        "routing decides the verdict",
        "dashboard becomes authority",
        "ToS write follows this packet",
        "generated output becomes truth",
    ],
)
def test_experience_v17_affective_honor_rejects_flow_authority_note_leaks(
    authority_note: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["affective_flow"]
    assert isinstance(flow, list)
    flow[3]["authority_note"] = authority_note

    with pytest.raises(validator.ValidationError, match="authority_note|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v17_affective_honor_schema_rejects_law_drift() -> None:
    payload = load_example()
    schema = load_schema()
    payload["affective_honor_law"][0] = "allow_affect_to_grant_rights"

    errors = list(Draft202012Validator(schema).iter_errors(payload))

    assert errors


def test_experience_v17_affective_honor_schema_rejects_predecessor_drift() -> None:
    payload = load_example()
    schema = load_schema()
    predecessors = payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors[0] = "docs/WRONG_PREDECESSOR.md"

    errors = list(Draft202012Validator(schema).iter_errors(payload))

    assert errors


def test_experience_v17_affective_honor_schema_rejects_flow_authority_note_drift() -> None:
    payload = load_example()
    schema = load_schema()
    flow = payload["affective_flow"]
    assert isinstance(flow, list)
    flow[7]["authority_note"] = "routing may decide rights here"

    errors = list(Draft202012Validator(schema).iter_errors(payload))

    assert errors


def test_experience_v17_affective_honor_schema_rejects_owner_split_drift() -> None:
    payload = load_example()
    schema = load_schema()
    owner_split = payload["owner_split"]
    assert isinstance(owner_split, list)
    owner_split[0]["repo"] = "wrong-owner"

    errors = list(Draft202012Validator(schema).iter_errors(payload))

    assert errors


def test_experience_v17_affective_honor_schema_rejects_quarantine_drift() -> None:
    payload = load_example()
    schema = load_schema()
    quarantined = payload["quarantined_surfaces"]
    assert isinstance(quarantined, list)
    quarantined[0] = "non_quarantined_surface"

    errors = list(Draft202012Validator(schema).iter_errors(payload))

    assert errors
