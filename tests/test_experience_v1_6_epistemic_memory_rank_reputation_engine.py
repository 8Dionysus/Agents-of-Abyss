from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


def load_validator():
    path = ROOT / "scripts" / "validate_experience_v1_6_epistemic_memory_rank_reputation_engine.py"
    spec = importlib.util.spec_from_file_location("experience_v16_rank_reputation_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads(
        (
            ROOT
            / "examples"
            / "experience_v1_6_epistemic_memory_rank_reputation_engine.example.json"
        ).read_text(encoding="utf-8")
    )


def load_schema() -> dict[str, object]:
    return json.loads(
        (
            ROOT
            / "schemas"
            / "experience-v1-6-epistemic-memory-rank-reputation-engine.schema.json"
        ).read_text(encoding="utf-8")
    )


def test_experience_v16_rank_reputation_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_experience_v1_6_epistemic_memory_rank_reputation_engine.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_v16_rank_reputation_requires_source_archive() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["archive_name"] = "aoa-experience-epistemic-duel-model-of-other-forge-seed-v1_5.zip"

    with pytest.raises(validator.ValidationError, match="source_seed|archive|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v16_rank_reputation_rejects_live_rank_mutation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_rank_mutation"] = True

    with pytest.raises(validator.ValidationError, match="schema|live_rank_mutation"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v16_rank_reputation_rejects_live_rights_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_rights_activation"] = True

    with pytest.raises(validator.ValidationError, match="schema|live_rights_activation"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v16_rank_reputation_requires_v15_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/experience/docs/EXPERIENCE_V1_5_EPISTEMIC_DUEL_MODEL_OF_OTHER_FORGE.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|bridge spine|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v16_rank_reputation_requires_rank_jurisdiction_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/agon/docs/AGON_RANK_JURISDICTION_MODEL.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|bridge spine|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "guard",
    [
        "no_codex_rank_assignment",
        "no_assistant_agonic_rank",
        "no_reputation_without_evidence",
        "no_rank_delta_without_retention_and_review",
        "no_single_event_standing",
        "no_memory_or_model_history_as_truth",
        "no_stats_as_proof",
        "no_routing_as_owner",
        "no_direct_tree_of_sophia_or_kag_canon",
    ],
)
def test_experience_v16_rank_reputation_requires_hard_guards(guard: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    guards = bad_payload["hard_guards"]
    assert isinstance(guards, list)
    guards.remove(guard)

    with pytest.raises(validator.ValidationError, match="hard_guards|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v16_rank_reputation_rejects_active_landing_state() -> None:
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
        "missing_evidence_allowed",
        "direct_rights_grant_allowed",
        "one_event_promotion_allowed",
    ],
)
def test_experience_v16_rank_reputation_blocks_reputation_evidence_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    evidence = bad_payload["blocking_contracts"]["reputation_evidence"]
    assert isinstance(evidence, dict)
    evidence[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "automatic_decay_execution_allowed",
        "scheduler_loop_allowed",
        "retention_result_may_mutate_standing",
    ],
)
def test_experience_v16_rank_reputation_blocks_retention_runtime_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    retention = bad_payload["blocking_contracts"]["retention_boundary"]
    assert isinstance(retention, dict)
    retention[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "rank_jump_without_review_allowed",
        "closure_without_trace_allowed",
        "summon_without_visible_cost_allowed",
    ],
)
def test_experience_v16_rank_reputation_blocks_jurisdiction_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    standing = bad_payload["blocking_contracts"]["standing_and_jurisdiction"]
    assert isinstance(standing, dict)
    standing[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "assistant_rank_assignment_allowed",
        "assistant_jurisdiction_grant_allowed",
        "assistant_judge_allowed",
        "codex_rank_assignment_allowed",
        "codex_rights_grant_allowed",
        "codex_memory_write_allowed",
    ],
)
def test_experience_v16_rank_reputation_blocks_actor_authority(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    actors = bad_payload["blocking_contracts"]["actor_boundary"]
    assert isinstance(actors, dict)
    actors[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "durable_memory_write_allowed",
        "durable_identity_claim_allowed",
        "hidden_memory_thread_allowed",
        "pairing_lock_in_allowed",
    ],
)
def test_experience_v16_rank_reputation_blocks_memory_history_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    memory = bad_payload["blocking_contracts"]["memory_history_boundary"]
    assert isinstance(memory, dict)
    memory[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "stats_as_proof_allowed",
        "routing_as_owner_allowed",
        "memo_as_truth_allowed",
        "eval_live_verdict_authority_allowed",
        "dashboard_as_verdict_allowed",
    ],
)
def test_experience_v16_rank_reputation_blocks_derived_layer_leaks(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    derived = bad_payload["blocking_contracts"]["derived_layer_boundary"]
    assert isinstance(derived, dict)
    derived[field] = True

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
def test_experience_v16_rank_reputation_blocks_tos_and_kag_authority(field: str) -> None:
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
    "field",
    [
        "runtime_worker_activation_allowed",
        "host_port_open_allowed",
        "scheduler_loop_allowed",
        "scoring_job_allowed",
        "deployment_daemon_allowed",
    ],
)
def test_experience_v16_rank_reputation_blocks_runtime_storage(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    runtime = bad_payload["blocking_contracts"]["runtime_storage"]
    assert isinstance(runtime, dict)
    runtime[field] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v16_rank_reputation_blocks_raw_generated_output_as_truth() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    archive = bad_payload["blocking_contracts"]["archive_consistency"]
    assert isinstance(archive, dict)
    archive["raw_generated_output_copied_as_truth"] = True

    with pytest.raises(validator.ValidationError, match="blocking_contracts|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "forbidden_grant",
    [
        "assign rank",
        "grant summon right",
        "grant closure right",
        "issue reputation verdict",
        "write durable memory",
        "start decay scheduler",
        "promote KAG canon",
    ],
)
def test_experience_v16_rank_reputation_rejects_codex_authority_leaks(
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


def test_experience_v16_rank_reputation_requires_assistant_rank_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    denied = bad_payload["authority"]["assistant_must_not"]
    assert isinstance(denied, list)
    denied.remove("become primary rank authority")

    with pytest.raises(validator.ValidationError, match="assistant_must_not"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "derived_denial",
    [
        "stats_as_proof",
        "memo_as_truth",
        "routing_as_owner",
        "evals_as_live_verdict_authority",
        "reputation_as_live_score",
    ],
)
def test_experience_v16_rank_reputation_requires_derived_layer_denials(
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


def test_experience_v16_rank_reputation_requires_runtime_owner_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    gates = bad_payload["authority"]["human_gates_required"]
    assert isinstance(gates, list)
    gates.remove("runtime-owner gate before ledger scheduler workers ports services or daemons")

    with pytest.raises(validator.ValidationError, match="human_gates_required"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "authority_note",
    [
        "live rank may run after this gate",
        "Codex rank assignment allowed",
        "assistant rank authority allowed",
        "rights may be granted automatically",
        "durable memory write follows this packet",
        "dashboard becomes proof",
        "generated output becomes truth",
    ],
)
def test_experience_v16_rank_reputation_rejects_flow_authority_note_leaks(
    authority_note: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["consequence_flow"]
    assert isinstance(flow, list)
    flow[3]["authority_note"] = authority_note

    with pytest.raises(validator.ValidationError, match="authority_note"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v16_rank_reputation_requires_all_owner_repos() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    owner_split.pop()

    with pytest.raises(validator.ValidationError, match="owner_split|repo set|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v16_rank_reputation_requires_seed_evidence_exactness() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    evidence = bad_payload["seed_dry_run_evidence"]
    assert isinstance(evidence, dict)
    evidence["schema_example_pairs"] = 52

    with pytest.raises(validator.ValidationError, match="seed_dry_run_evidence|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v16_rank_reputation_schema_rejects_law_drift() -> None:
    payload = load_example()
    schema = load_schema()
    payload["rank_reputation_law"][0] = "allow_live_rank_from_single_blaze"

    errors = list(Draft202012Validator(schema).iter_errors(payload))

    assert errors


def test_experience_v16_rank_reputation_schema_rejects_flow_authority_note_drift() -> None:
    payload = load_example()
    schema = load_schema()
    flow = payload["consequence_flow"]
    assert isinstance(flow, list)
    flow[7]["authority_note"] = "owner review can assign standing directly in this packet"

    errors = list(Draft202012Validator(schema).iter_errors(payload))

    assert errors


def test_experience_v16_rank_reputation_schema_rejects_predecessor_drift() -> None:
    payload = load_example()
    schema = load_schema()
    predecessors = payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors[0] = "docs/WRONG_PREDECESSOR.md"

    errors = list(Draft202012Validator(schema).iter_errors(payload))

    assert errors


def test_experience_v16_rank_reputation_schema_rejects_owner_split_drift() -> None:
    payload = load_example()
    schema = load_schema()
    owner_split = payload["owner_split"]
    assert isinstance(owner_split, list)
    owner_split[0]["repo"] = "wrong-owner"

    errors = list(Draft202012Validator(schema).iter_errors(payload))

    assert errors


def test_experience_v16_rank_reputation_schema_rejects_quarantine_drift() -> None:
    payload = load_example()
    schema = load_schema()
    quarantined = payload["quarantined_surfaces"]
    assert isinstance(quarantined, list)
    quarantined[0] = "non_quarantined_surface"

    errors = list(Draft202012Validator(schema).iter_errors(payload))

    assert errors
