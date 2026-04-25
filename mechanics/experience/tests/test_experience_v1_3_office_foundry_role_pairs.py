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
    path = ROOT / "mechanics" / "experience" / "scripts" / "validate_experience_v1_3_office_foundry_role_pairs.py"
    spec = importlib.util.spec_from_file_location("experience_v13_office_foundry_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads(
        (ROOT / "mechanics" / "experience" / "examples" / "experience_v1_3_office_foundry_role_pairs.example.json").read_text(
            encoding="utf-8"
        )
    )


def load_schema() -> dict[str, object]:
    return json.loads(
        (ROOT / "mechanics" / "experience" / "schemas" / "experience-v1-3-office-foundry-role-pairs.schema.json").read_text(
            encoding="utf-8"
        )
    )


def test_experience_v13_office_foundry_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/experience/scripts/validate_experience_v1_3_office_foundry_role_pairs.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_v13_office_foundry_requires_source_archive() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    source = bad_payload["source_seed"]
    assert isinstance(source, dict)
    source["archive_name"] = "aoa-experience-agonic-pair-trials-mechanical-arena-kernel-seed-v1_4.zip"

    with pytest.raises(validator.ValidationError, match="archive_name|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_rejects_runtime_activation() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    bad_payload["live_runtime_activation"] = True

    with pytest.raises(validator.ValidationError, match="schema|live_runtime_activation"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_expanded_offices_exactly() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    offices = bad_payload["expanded_service_offices"]
    assert isinstance(offices, list)
    offices.append("steward.agonic")

    with pytest.raises(validator.ValidationError, match="expanded_service_offices|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_rejects_hybrid_role_pair() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    role_pairs = bad_payload["role_pairs"]
    assert isinstance(role_pairs, list)
    role_pairs[0]["hybrid_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|role_pairs"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_role_pair_kind_split() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    role_pairs = bad_payload["role_pairs"]
    assert isinstance(role_pairs, list)
    role_pairs[1]["agonic"] = "chronicler.assistant"

    with pytest.raises(validator.ValidationError, match="role_pairs"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "forbidden_grant",
    [
        "approve office pair",
        "activate office pair",
        "certify release",
        "write scar",
        "mutate rank",
        "execute retention",
        "write directly to Tree-of-Sophia",
        "route meaning as owner",
        "promote KAG to canon",
        "start runtime worker",
        "allow hybrid actor",
    ],
)
def test_experience_v13_office_foundry_rejects_codex_authority_leaks(
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

    with pytest.raises(validator.ValidationError, match="codex_may|forbidden office foundry authority"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_hard_guard_order() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    guards = bad_payload["hard_guards"]
    assert isinstance(guards, list)
    guards.remove("no_hybrid_agent")

    with pytest.raises(validator.ValidationError, match="hard_guards|schema"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_blocks_same_actor_cross_kind() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    blocking = bad_payload["blocking_contracts"]
    assert isinstance(blocking, dict)
    actor_identity = blocking["actor_identity"]
    assert isinstance(actor_identity, dict)
    actor_identity["same_actor_id_cross_kind_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_rejects_active_landing_state() -> None:
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


@pytest.mark.parametrize(
    "requester",
    [
        "assistant",
        "codex",
        "runtime",
        "scheduler",
        "office",
        "derived_layer",
    ],
)
def test_experience_v13_office_foundry_recharter_blocks_forbidden_requesters(
    requester: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    blocking = bad_payload["blocking_contracts"]
    assert isinstance(blocking, dict)
    recharter = blocking["recharter"]
    assert isinstance(recharter, dict)
    allowed = recharter["allowed_requesters"]
    assert isinstance(allowed, list)
    allowed.append(requester)

    with pytest.raises(validator.ValidationError, match="blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_scar_candidate_only_no_durable_write() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    blocking = bad_payload["blocking_contracts"]
    assert isinstance(blocking, dict)
    scar = blocking["scar_rank_retention"]
    assert isinstance(scar, dict)
    scar["durable_write_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_rejects_direct_tos_runtime_boundary() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    blocking = bad_payload["blocking_contracts"]
    assert isinstance(blocking, dict)
    tos = blocking["tos_boundary"]
    assert isinstance(tos, dict)
    tos["runtime_write_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_rejects_routing_meaning_definition() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    blocking = bad_payload["blocking_contracts"]
    assert isinstance(blocking, dict)
    routing = blocking["routing_boundary"]
    assert isinstance(routing, dict)
    routing["meaning_definition_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_rejects_eval_scar_rank_closure_grant() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    blocking = bad_payload["blocking_contracts"]
    assert isinstance(blocking, dict)
    eval_boundary = blocking["eval_boundary"]
    assert isinstance(eval_boundary, dict)
    eval_boundary["may_grant_scar_rank_closure"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_archive_consistency_failure_on_disagreement() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    blocking = bad_payload["blocking_contracts"]
    assert isinstance(blocking, dict)
    consistency = blocking["archive_consistency"]
    assert isinstance(consistency, dict)
    consistency["fixture_generated_result_disagreement_allowed"] = True

    with pytest.raises(validator.ValidationError, match="schema|blocking_contracts"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_assistant_self_recharter_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    denied = authority["assistant_must_not"]
    assert isinstance(denied, list)
    denied.remove("self-recharter")

    with pytest.raises(validator.ValidationError, match="assistant_must_not"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_flow_owner_routing() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["foundry_flow"]
    assert isinstance(flow, list)
    flow[2]["owner"] = "abyss-stack"

    with pytest.raises(validator.ValidationError, match="owners"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_flow_stop_lines() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["foundry_flow"]
    assert isinstance(flow, list)
    flow[3]["stop_lines"] = []

    with pytest.raises(validator.ValidationError, match="stop_lines"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "authority_note",
    [
        "runtime activation is allowed for this pair",
        "scheduler loop may run for this foundry",
        "hybrid runtime allowed after review",
        "Codex approves office pair",
        "routing owns meaning for this office",
        "KAG canon follows from this pattern",
    ],
)
def test_experience_v13_office_foundry_rejects_flow_authority_note_leaks(
    authority_note: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    flow = bad_payload["foundry_flow"]
    assert isinstance(flow, list)
    flow[3]["authority_note"] = authority_note

    with pytest.raises(validator.ValidationError, match="authority_note"):
        validator.validate_payload(bad_payload, schema)


@pytest.mark.parametrize(
    "derived_denial",
    [
        "routing_as_owner",
        "kag_as_canon",
        "runtime_as_doctrine",
        "evals_as_certifier",
    ],
)
def test_experience_v13_office_foundry_requires_derived_layer_denials(
    derived_denial: str,
) -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    derived = authority["derived_layers_must_not"]
    assert isinstance(derived, list)
    derived.remove(derived_denial)

    with pytest.raises(validator.ValidationError, match="derived_layers_must_not"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_runtime_owner_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "abyss-stack":
            entry["owns"] = "runtime activation storage guard events and workers"

    with pytest.raises(validator.ValidationError, match="owner_split|runtime-owner gate"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_tos_runtime_write_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "Tree-of-Sophia":
            entry["must_not"] = "receive reviewed dossiers only"

    with pytest.raises(validator.ValidationError, match="owner_split|Tree-of-Sophia"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_agents_no_hybrid_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-agents":
            entry["must_not"] = "grant self-release self-enroll self-certify or scar authority"

    with pytest.raises(validator.ValidationError, match="owner_split|aoa-agents"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_kag_canon_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-kag":
            entry["must_not"] = "force uptake into Tree-of-Sophia"

    with pytest.raises(validator.ValidationError, match="owner_split"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_sdk_semantic_authority_denial() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "aoa-sdk":
            entry["must_not"] = "become runtime"

    with pytest.raises(validator.ValidationError, match="owner_split"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_human_runtime_gate() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    authority = bad_payload["authority"]
    assert isinstance(authority, dict)
    gates = authority["human_gates_required"]
    assert isinstance(gates, list)
    gates.remove("runtime-owner gate before any service scheduler pair or worker activation")

    with pytest.raises(validator.ValidationError, match="human_gates_required"):
        validator.validate_payload(bad_payload, schema)


def test_experience_v13_office_foundry_requires_all_owner_repos() -> None:
    validator = load_validator()
    payload = load_example()
    schema = load_schema()
    bad_payload = copy.deepcopy(payload)
    owner_split = bad_payload["owner_split"]
    assert isinstance(owner_split, list)
    owner_split[:] = [entry for entry in owner_split if entry.get("repo") != "aoa-agents"]

    with pytest.raises(validator.ValidationError, match="owner_split|schema"):
        validator.validate_payload(bad_payload, schema)
