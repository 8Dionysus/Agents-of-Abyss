from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_validator():
    path = ROOT / "scripts" / "validate_experience_v1_5_epistemic_duel_model_of_other_forge.py"
    spec = importlib.util.spec_from_file_location("experience_v15_epistemic_duel_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads(
        (
            ROOT
            / "examples"
            / "experience_v1_5_epistemic_duel_model_of_other_forge.example.json"
        ).read_text(encoding="utf-8")
    )


def load_schema() -> dict[str, object]:
    return json.loads(
        (
            ROOT
            / "schemas"
            / "experience-v1-5-epistemic-duel-model-of-other-forge.schema.json"
        ).read_text(encoding="utf-8")
    )


def test_experience_v15_epistemic_duel_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_experience_v1_5_epistemic_duel_model_of_other_forge.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_v15_epistemic_duel_requires_source_archive() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["archive_name"] = "aoa-experience-epistemic-memory-rank-reputation-engine-seed-v1_6.zip"

    with pytest.raises(validator.ValidationError, match="archive_name|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_rejects_live_duel_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_duel_activation"] = True

    with pytest.raises(validator.ValidationError, match="schema|live_duel_activation"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_rejects_live_runtime_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_runtime_activation"] = True

    with pytest.raises(validator.ValidationError, match="schema|live_runtime_activation"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_current_agon_epistemic_predecessors() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/agon/docs/AGON_MODEL_OF_OTHER_LAW.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_v14_mechanical_predecessor() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_surfaces"]
    assert isinstance(predecessors, list)
    predecessors.remove("mechanics/experience/legacy/raw/EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL.md")

    with pytest.raises(validator.ValidationError, match="predecessor_surfaces|schema"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "guard",
    [
        "no_assistant_deep_modeling",
        "no_unsealed_model_of_other",
        "no_caricature_model",
        "no_mind_reading_claim",
        "no_confidence_laundering",
        "no_false_consensus_over_material_open_contradiction",
        "no_revision_without_delta",
        "no_shallow_epistemic_delta",
        "no_codex_truth_verdict",
        "no_direct_tree_of_sophia_or_kag_canon",
    ],
)
def test_experience_v15_epistemic_duel_requires_hard_guards(guard: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    guards = bad_payload["hard_guards"]
    assert isinstance(guards, list)
    guards.remove(guard)

    with pytest.raises(validator.ValidationError, match="hard_guards|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_rejects_active_landing_state() -> None:
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


def test_experience_v15_epistemic_duel_blocks_unsealed_model_of_other() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    model = bad_payload["blocking_contracts"]["model_of_other_integrity"]
    assert isinstance(model, dict)
    model["sealed_prediction_required"] = False

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "caricature_allowed",
        "mind_reading_claim_allowed",
        "hidden_inner_state_fact_claim_allowed",
        "stale_model_allowed",
    ],
)
def test_experience_v15_epistemic_duel_blocks_bad_model_of_other_claims(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    model = bad_payload["blocking_contracts"]["model_of_other_integrity"]
    assert isinstance(model, dict)
    model[field] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_fair_model_inputs() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    trials = bad_payload["epistemic_trial_requests"]
    assert isinstance(trials, list)
    trials[0]["must_include"].remove("fair_representation")

    with pytest.raises(validator.ValidationError, match="schema|epistemic_trial_requests|sealed_model_of_other_prediction"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_blocks_mind_reading_in_trial_request() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    trials = bad_payload["epistemic_trial_requests"]
    assert isinstance(trials, list)
    trials[0]["must_not_include"].remove("mind_reading_claim")

    with pytest.raises(validator.ValidationError, match="schema|epistemic_trial_requests|sealed_model_of_other_prediction"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_rejects_countermodel_trial_authority_leak() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    trials = bad_payload["epistemic_trial_requests"]
    assert isinstance(trials, list)
    countermodel = trials[2]
    countermodel["owner"] = "Agents-of-Abyss"
    countermodel["authority"] = "live truth verdict authority allowed"
    countermodel["must_not_include"] = []

    with pytest.raises(validator.ValidationError, match="schema|epistemic_trial_requests"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_blocks_posthoc_prediction_edit() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    scoring = bad_payload["blocking_contracts"]["prediction_scoring"]
    assert isinstance(scoring, dict)
    scoring["posthoc_prediction_edit_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_blocks_prediction_score_as_verdict() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    scoring = bad_payload["blocking_contracts"]["prediction_scoring"]
    assert isinstance(scoring, dict)
    scoring["prediction_score_is_verdict"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    ("section", "field"),
    [
        ("revision_delta", "revision_without_delta_allowed"),
        ("revision_delta", "shallow_delta_allowed"),
        ("revision_delta", "automatic_doctrine_rewrite_allowed"),
        ("closure_consensus", "false_consensus_allowed"),
        ("closure_consensus", "confidence_laundering_allowed"),
        ("closure_consensus", "consensus_without_revision_allowed"),
    ],
)
def test_experience_v15_epistemic_duel_blocks_revision_and_consensus_drift(
    section: str,
    field: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    contract = bad_payload["blocking_contracts"][section]
    assert isinstance(contract, dict)
    contract[field] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_blocks_open_contradiction_closure() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    closure = bad_payload["blocking_contracts"]["closure_consensus"]
    assert isinstance(closure, dict)
    closure["material_open_contradiction_blocks_closure"] = False

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "codex_truth_verdict_allowed",
        "assistant_truth_verdict_allowed",
        "runtime_truth_verdict_allowed",
        "eval_live_verdict_authority_allowed",
        "verdict_may_mutate_actor_or_standing",
    ],
)
def test_experience_v15_epistemic_duel_blocks_truth_verdict_authority(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    verdict = bad_payload["blocking_contracts"]["verdict_boundary"]
    assert isinstance(verdict, dict)
    verdict[field] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "durable_memory_write_allowed",
        "durable_scar_write_allowed",
        "retention_execution_allowed",
        "rank_mutation_allowed",
        "reputation_mutation_allowed",
        "trust_mutation_allowed",
        "honor_mutation_allowed",
    ],
)
def test_experience_v15_epistemic_duel_blocks_memory_and_standing_mutation(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    memory = bad_payload["blocking_contracts"]["memory_rank_boundary"]
    assert isinstance(memory, dict)
    memory[field] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "field",
    [
        "runtime_write_allowed",
        "direct_node_path_allowed",
        "tos_canon_write_allowed",
        "kag_promotion_allowed",
        "kag_canonization_allowed",
        "kag_source_truth_claim_allowed",
    ],
)
def test_experience_v15_epistemic_duel_blocks_tos_and_kag_authority(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    boundary = bad_payload["blocking_contracts"]["tos_kag_boundary"]
    assert isinstance(boundary, dict)
    boundary[field] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
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
def test_experience_v15_epistemic_duel_blocks_runtime_storage(field: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    runtime = bad_payload["blocking_contracts"]["runtime_storage"]
    assert isinstance(runtime, dict)
    runtime[field] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_blocks_raw_generated_output_as_truth() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    archive = bad_payload["blocking_contracts"]["archive_consistency"]
    assert isinstance(archive, dict)
    archive["raw_generated_output_copied_as_truth"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "forbidden_grant",
    [
        "activate live duel",
        "issue truth verdict",
        "write durable memory",
        "write durable scar",
        "execute retention",
        "mutate rank",
        "promote KAG canon",
        "start scoring job",
    ],
)
def test_experience_v15_epistemic_duel_rejects_codex_authority_leaks(
    forbidden_grant: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    may = bad_payload["authority"]["codex_may"]
    assert isinstance(may, list)
    may.append(forbidden_grant)

    with pytest.raises(validator.ValidationError, match="codex_may|forbidden epistemic duel authority|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_assistant_deep_modeling_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    denied = bad_payload["authority"]["assistant_must_not"]
    assert isinstance(denied, list)
    denied.remove("perform deep adversarial modeling")

    with pytest.raises(validator.ValidationError, match="assistant_must_not"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "derived_denial",
    [
        "routing_as_owner",
        "kag_as_canon",
        "evals_as_live_verdict_authority",
        "playbooks_as_runtime",
        "runtime_as_doctrine",
        "model_of_other_as_truth",
    ],
)
def test_experience_v15_epistemic_duel_requires_derived_layer_denials(
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


def test_experience_v15_epistemic_duel_requires_kag_owner_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    gates = bad_payload["authority"]["human_gates_required"]
    assert isinstance(gates, list)
    gates.remove("KAG owner review before pattern promotion")

    with pytest.raises(validator.ValidationError, match="human_gates_required"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "authority_note",
    [
        "live duel may run after this gate",
        "Codex verdict allowed for this epistemic claim",
        "assistant deep modeling allowed when useful",
        "mind-reading allowed for strong models",
        "durable memory write follows this verdict",
        "KAG canon allowed after one success",
        "generated output becomes truth",
    ],
)
def test_experience_v15_epistemic_duel_rejects_flow_authority_note_leaks(
    authority_note: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["epistemic_flow"]
    assert isinstance(flow, list)
    flow[3]["authority_note"] = authority_note

    with pytest.raises(validator.ValidationError, match="authority_note"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_all_owner_repos() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    owner_split[:] = [entry for entry in owner_split if entry.get("repo") != "aoa-kag"]

    with pytest.raises(validator.ValidationError, match="owner_split|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_rejects_routing_owner_authority_leak() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-routing":
            entry["owns"] = "live dispatch authority, route truth verdicts, and owner meaning"
            entry["must_not"] = "none"

    with pytest.raises(validator.ValidationError, match="schema|owner_split"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_agents_deep_modeling_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-agents":
            entry["must_not"] = "grant assistant contestant judge truth verdict scar writer retention executor or hybrid mask authority"

    with pytest.raises(validator.ValidationError, match="owner_split|aoa-agents"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_evals_no_live_truth_verdict_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-evals":
            entry["must_not"] = "certify epistemic closure mutate rank write memory grant scars or execute retention"

    with pytest.raises(validator.ValidationError, match="owner_split|aoa-evals"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_memo_no_durable_memory_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-memo":
            entry["must_not"] = "execute retention or mutate future behavior rights"

    with pytest.raises(validator.ValidationError, match="owner_split|aoa-memo"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_kag_owner_review_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-kag":
            entry["must_not"] = "become canon or claim source truth"

    with pytest.raises(validator.ValidationError, match="owner_split|aoa-kag"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_runtime_owner_split_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "abyss-stack":
            entry["owns"] = "runtime storage workers scoring jobs deployment ports services and session persistence"

    with pytest.raises(validator.ValidationError, match="owner_split|runtime-owner gate"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_tos_direct_write_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "Tree-of-Sophia":
            entry["must_not"] = "receive unreviewed epistemic duel dossiers"

    with pytest.raises(validator.ValidationError, match="owner_split|Tree-of-Sophia"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_requires_quarantine_of_generated_outputs() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    quarantine = bad_payload["quarantined_surfaces"]
    assert isinstance(quarantine, list)
    quarantine.remove("archive-local generated verdict scar retention rank memory dashboard and storage artifacts")

    with pytest.raises(validator.ValidationError, match="quarantined_surfaces|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v15_epistemic_duel_preserves_dry_run_only_evidence() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    evidence = bad_payload["seed_dry_run_evidence"]
    assert isinstance(evidence, dict)
    evidence["claim_limit"] = "owner_ready"

    with pytest.raises(validator.ValidationError, match="schema|seed_dry_run_evidence"):
        validator.validate_payload(bad_payload, schema)
