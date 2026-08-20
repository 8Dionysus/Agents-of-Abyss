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
        / "governance-polis"
        / "scripts"
        / "validate_governance_polis.py"
    )
    spec = importlib.util.spec_from_file_location(
        "experience_polis_constitution_validator_test", path
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
            / "governance-polis"
            / "examples"
            / "experience_polis_constitution.example.json"
        ).read_text()
    )


def load_operator_packet() -> dict[str, object]:
    return json.loads(
        (
            ROOT
            / "mechanics"
            / "experience"
            / "parts"
            / "governance-polis"
            / "examples"
            / "operator_decision_packet.example.json"
        ).read_text()
    )


def test_experience_polis_constitution_validator_passes() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "mechanics/experience/parts/governance-polis/scripts/validate_governance_polis.py",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_polis_constitution_requires_v08_before_v09() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    seeds = bad_flow["source_receipt_refs"]
    assert isinstance(seeds, list)
    seeds.reverse()

    with pytest.raises(validator.ValidationError, match="v0.8 before v0.9"):
        validator.validate_example(bad_flow)


def test_experience_polis_constitution_rejects_codex_vote_authority() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    may = authority["codex_may"]
    assert isinstance(may, list)
    may.append("vote")

    with pytest.raises(validator.ValidationError, match="denied authority"):
        validator.validate_example(bad_flow)


def test_experience_polis_constitution_rejects_missing_assistant_recharter_block() -> (
    None
):
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    denied = authority["assistant_must_not"]
    assert isinstance(denied, list)
    denied.remove("self-recharter")

    with pytest.raises(validator.ValidationError, match="assistant_must_not"):
        validator.validate_example(bad_flow)


def test_experience_polis_constitution_requires_ordered_runtime_seal_before_reveal() -> (
    None
):
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    runtime_flow = bad_flow["runtime_flow"]
    assert isinstance(runtime_flow, list)
    runtime_flow[3], runtime_flow[4] = runtime_flow[4], runtime_flow[3]

    with pytest.raises(validator.ValidationError, match="ordered spine"):
        validator.validate_example(bad_flow)


def test_experience_polis_constitution_requires_all_owner_repos() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    owner_split = bad_flow["owner_split"]
    assert isinstance(owner_split, list)
    owner_split[:] = [
        item for item in owner_split if item.get("repo") != "Tree-of-Sophia"
    ]

    with pytest.raises(validator.ValidationError, match="owner_split is missing"):
        validator.validate_example(bad_flow)


@pytest.mark.parametrize(
    "decision",
    ["approve", "reject", "defer", "narrow", "quarantine"],
)
def test_c25_supports_exact_operator_decisions(decision: str) -> None:
    validator = load_validator()
    packet = load_operator_packet()
    if decision != "narrow":
        packet["decision"] = decision
        packet["decision_scope"] = "artifact_set"
        packet["narrowed_items"] = []

    validator.validate_operator_decision_packet(
        packet,
        resolved_manifest_sha256=packet["artifact_manifest_sha256"],
        resolved_artifact_set_id=packet["artifact_set_id"],
    )


def test_c25_unresolved_or_mismatched_manifest_means_no_decision() -> None:
    validator = load_validator()
    packet = load_operator_packet()

    with pytest.raises(validator.ValidationError, match="unresolved"):
        validator.validate_operator_decision_packet(
            packet,
            resolved_manifest_sha256=None,
            resolved_artifact_set_id=packet["artifact_set_id"],
        )
    with pytest.raises(validator.ValidationError, match="exact bytes"):
        validator.validate_operator_decision_packet(
            packet,
            resolved_manifest_sha256="sha256:" + "9" * 64,
            resolved_artifact_set_id=packet["artifact_set_id"],
        )
    with pytest.raises(validator.ValidationError, match="owner-resolved manifest"):
        validator.validate_operator_decision_packet(
            packet,
            resolved_manifest_sha256=packet["artifact_manifest_sha256"],
            resolved_artifact_set_id="aoa-memo:active-organ:different-candidate-v1",
        )


def test_c25_requires_procedurally_separated_ai_review_runs() -> None:
    validator = load_validator()
    packet = load_operator_packet()
    review_funnel = packet["review_funnel"]
    assert isinstance(review_funnel, dict)
    review_funnel["authority_review_ref"] = review_funnel["evidence_review_ref"]

    with pytest.raises(validator.ValidationError, match="distinct"):
        validator.validate_operator_decision_packet(
            packet,
            resolved_manifest_sha256=packet["artifact_manifest_sha256"],
            resolved_artifact_set_id=packet["artifact_set_id"],
        )


def test_c25_cannot_apply_effect_or_absorb_payload_authority() -> None:
    validator = load_validator()
    packet = load_operator_packet()

    assert packet["followup"] == {
        "next_owner_ref": "aoa-sdk:active-organ-admission",
        "owner_revalidation_required": True,
        "automatic_effect": False,
        "packet_effect": "operator_decision_only",
    }
    authority = packet["authority"]
    assert isinstance(authority, dict)
    assert authority["sole_operator_decision"] is True
    assert authority["ai_final_decision_authority"] is False
    assert authority["ai_authority_widening"] is False
    assert authority["center_payload_meaning_authority"] is False
    assert authority["named_owner_payload_authority"] is True
    assert authority["production_authority"] == "none"

    validator.validate_operator_decision_packet(
        packet,
        resolved_manifest_sha256=packet["artifact_manifest_sha256"],
        resolved_artifact_set_id=packet["artifact_set_id"],
    )
