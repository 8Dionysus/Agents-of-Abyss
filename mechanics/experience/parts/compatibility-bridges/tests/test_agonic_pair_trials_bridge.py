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
        / "compatibility-bridges"
        / "scripts"
        / "validate_agonic_pair_trials_bridge.py"
    )
    spec = importlib.util.spec_from_file_location(
        "experience_agonic_arena_validator_test", path
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
            / "compatibility-bridges"
            / "examples"
            / "experience_agonic_pair_trials_arena_kernel.example.json"
        ).read_text(encoding="utf-8")
    )


def load_schema() -> dict[str, object]:
    return json.loads(
        (
            ROOT
            / "mechanics"
            / "experience"
            / "parts"
            / "compatibility-bridges"
            / "schemas"
            / "experience-agonic-pair-trials-arena-kernel.schema.json"
        ).read_text(encoding="utf-8")
    )


def test_experience_agonic_arena_validator_passes() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "mechanics/experience/parts/compatibility-bridges/scripts/validate_agonic_pair_trials_bridge.py",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_agonic_arena_requires_source_archive() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["receipt_ref"] = (
        "experience.seed.epistemic-duel-model-forge"
    )

    with pytest.raises(validator.ValidationError, match="receipt_ref|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_rejects_live_arena_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_arena_activation"] = True

    with pytest.raises(validator.ValidationError, match="schema|live_arena_activation"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_rejects_live_runtime_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_runtime_activation"] = True

    with pytest.raises(
        validator.ValidationError, match="schema|live_runtime_activation"
    ):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_current_agon_predecessors() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_receipt_refs"]
    assert isinstance(predecessors, list)
    predecessors.remove("agon.duel-kernel-model")

    with pytest.raises(validator.ValidationError, match="predecessor_receipt_refs|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_latest_agon_stop_lines() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    predecessors = bad_payload["predecessor_receipt_refs"]
    assert isinstance(predecessors, list)
    predecessors.remove("agon.arena-session-landing-stop-lines")

    with pytest.raises(validator.ValidationError, match="predecessor_receipt_refs|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_rejects_assistant_contestant_pair_trial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    trials = bad_payload["first_pair_trials"]
    assert isinstance(trials, list)
    trials[0]["agonic_form"] = "verifier.assistant"

    with pytest.raises(validator.ValidationError, match="first_pair_trials|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_rejects_live_pair_enrollment() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    trials = bad_payload["first_pair_trials"]
    assert isinstance(trials, list)
    trials[1]["live_enrollment"] = True

    with pytest.raises(validator.ValidationError, match="schema|first_pair_trials"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "guard",
    [
        "no_assistant_contestant",
        "no_hidden_summon",
        "no_codex_arena_verdict",
        "no_durable_scar_or_retention_write",
        "no_runtime_storage_or_worker_activation",
    ],
)
def test_experience_agonic_arena_requires_hard_guards(guard: str) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    guards = bad_payload["hard_guards"]
    assert isinstance(guards, list)
    guards.remove(guard)

    with pytest.raises(validator.ValidationError, match="hard_guards|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_rejects_active_landing_state() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    blocking = bad_payload["blocking_contracts"]
    assert isinstance(blocking, dict)
    activation = blocking["activation_state"]
    assert isinstance(activation, dict)
    states = activation["allowed_landing_states"]
    assert isinstance(states, list)
    states.append("active")

    with pytest.raises(validator.ValidationError, match="blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_blocks_assistant_primary_contestant() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    contestant = bad_payload["blocking_contracts"]["contestant_eligibility"]
    assert isinstance(contestant, dict)
    contestant["assistant_primary_contestant_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_witness_and_blocks_assistant_judge() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    witness = bad_payload["blocking_contracts"]["witness_contract"]
    assert isinstance(witness, dict)
    witness["assistant_judge_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_blocks_posthoc_commit_edit() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    stance = bad_payload["blocking_contracts"]["stance_integrity"]
    assert isinstance(stance, dict)
    stance["posthoc_commit_edit_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_blocks_open_material_contradiction_closure() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    closure = bad_payload["blocking_contracts"]["closure_contract"]
    assert isinstance(closure, dict)
    closure["material_open_contradiction_blocks_closure"] = False

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_blocks_hidden_summon() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    summon = bad_payload["blocking_contracts"]["summon_economy"]
    assert isinstance(summon, dict)
    summon["hidden_summon_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_blocks_codex_verdict() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    verdict = bad_payload["blocking_contracts"]["verdict_boundary"]
    assert isinstance(verdict, dict)
    verdict["codex_verdict_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_blocks_scar_grant_by_verdict() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    verdict = bad_payload["blocking_contracts"]["verdict_boundary"]
    assert isinstance(verdict, dict)
    verdict["verdict_may_grant_scar_rank_retention"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_blocks_durable_scar_and_retention_execution() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    scar = bad_payload["blocking_contracts"]["scar_retention"]
    assert isinstance(scar, dict)
    scar["durable_scar_write_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_blocks_direct_tos_write() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    tos = bad_payload["blocking_contracts"]["tos_boundary"]
    assert isinstance(tos, dict)
    tos["runtime_write_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_blocks_runtime_storage_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    runtime = bad_payload["blocking_contracts"]["runtime_storage"]
    assert isinstance(runtime, dict)
    runtime["runtime_worker_activation_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_blocks_archive_pycache_landing() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    archive = bad_payload["blocking_contracts"]["archive_consistency"]
    assert isinstance(archive, dict)
    archive["archive_pycache_allowed_in_owner_repo"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "forbidden_grant",
    [
        "activate live arena",
        "issue arena verdict",
        "write durable scar",
        "execute retention",
        "mutate rank",
        "start runtime worker",
        "grant summon authority",
    ],
)
def test_experience_agonic_arena_rejects_codex_authority_leaks(
    forbidden_grant: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    may = bad_payload["authority"]["codex_may"]
    assert isinstance(may, list)
    may.append(forbidden_grant)

    with pytest.raises(
        validator.ValidationError,
        match="codex_may|forbidden mechanical arena authority",
    ):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_assistant_contestant_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    denied = bad_payload["authority"]["assistant_must_not"]
    assert isinstance(denied, list)
    denied.remove("become primary contestant")

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
    ],
)
def test_experience_agonic_arena_requires_derived_layer_denials(
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


def test_experience_agonic_arena_requires_runtime_owner_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    gates = bad_payload["authority"]["human_gates_required"]
    assert isinstance(gates, list)
    gates.remove(
        "runtime-owner gate before storage workers ports schedulers services or daemons"
    )

    with pytest.raises(validator.ValidationError, match="human_gates_required"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_flow_owner_routing() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["kernel_flow"]
    assert isinstance(flow, list)
    flow[3]["owner"] = "abyss-stack"

    with pytest.raises(validator.ValidationError, match="owners"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "authority_note",
    [
        "live arena may run after this gate",
        "Codex verdict allowed for this trial",
        "assistant may judge when notary is present",
        "hidden summon allowed if useful",
        "durable scar write follows this verdict",
        "generated output becomes truth",
    ],
)
def test_experience_agonic_arena_rejects_flow_authority_note_leaks(
    authority_note: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["kernel_flow"]
    assert isinstance(flow, list)
    flow[8]["authority_note"] = authority_note

    with pytest.raises(validator.ValidationError, match="authority_note"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_all_owner_repos() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    owner_split[:] = [
        entry for entry in owner_split if entry.get("repo") != "aoa-agents"
    ]

    with pytest.raises(validator.ValidationError, match="owner_split|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_agents_assistant_contestant_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-agents":
            entry["must_not"] = (
                "grant judge scar writer retention executor hidden summon or hybrid mask authority"
            )

    with pytest.raises(validator.ValidationError, match="owner_split|aoa-agents"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_evals_no_live_verdict_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-evals":
            entry["must_not"] = (
                "certify trials grant scars mutate rank or execute retention"
            )

    with pytest.raises(validator.ValidationError, match="owner_split|aoa-evals"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_memo_no_durable_scar_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-memo":
            entry["must_not"] = (
                "make memory truth execute retention or grant future behavior rights"
            )

    with pytest.raises(validator.ValidationError, match="owner_split|aoa-memo"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_runtime_owner_split_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "abyss-stack":
            entry["owns"] = (
                "runtime storage workers deployment ports services and session persistence"
            )

    with pytest.raises(
        validator.ValidationError, match="owner_split|runtime-owner gate"
    ):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_tos_direct_write_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "Tree-of-Sophia":
            entry["must_not"] = "receive unreviewed arena dossiers"

    with pytest.raises(validator.ValidationError, match="owner_split|Tree-of-Sophia"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_requires_quarantine_of_generated_outputs() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    quarantine = bad_payload["quarantined_surfaces"]
    assert isinstance(quarantine, list)
    quarantine.remove(
        "archive-local generated scar_write and retention_schedule artifacts"
    )

    with pytest.raises(validator.ValidationError, match="quarantined_surfaces|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_agonic_arena_preserves_dry_run_only_evidence() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    evidence = bad_payload["seed_dry_run_evidence"]
    assert isinstance(evidence, dict)
    evidence["claim_limit"] = "owner_ready"

    with pytest.raises(validator.ValidationError, match="schema|seed_dry_run_evidence"):
        validator.validate_payload(bad_payload, schema)
