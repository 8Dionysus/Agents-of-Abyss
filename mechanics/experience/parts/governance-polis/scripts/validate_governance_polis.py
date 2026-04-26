#!/usr/bin/env python3
"""Validate the Experience polis/constitution center surfaces."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


ROOT = _repo_root()

SCHEMA_PATH = (
    ROOT
    / "mechanics"
    / "experience"
    / "parts"
    / "governance-polis"
    / "schemas"
    / "experience-polis-constitution.schema.json"
)
EXAMPLE_PATH = (
    ROOT
    / "mechanics"
    / "experience"
    / "parts"
    / "governance-polis"
    / "examples"
    / "experience_polis_constitution.example.json"
)

EXPECTED_SOURCE_SEEDS = [
    "experience.seed.polis-governance",
    "experience.seed.constitution-runtime",
]
POLIS_ORDER = [
    "governance_case_opened",
    "authority_checked",
    "council_or_sovereign_review_selected",
    "vote_veto_stay_appeal_or_amendment_resolved",
    "decision_logged",
    "owner_local_route_declared",
    "precedent_or_release_hold_recorded",
    "retention_and_audit_scheduled",
]
RUNTIME_ORDER = [
    "runtime_case_queued",
    "authority_resolved",
    "council_scheduled_with_quorum",
    "vote_sealed_before_reveal",
    "reveal_checked_against_hash",
    "stay_hold_or_appeal_enforced",
    "decision_history_replayed",
    "precedent_indexed_from_sealed_decision",
    "dashboard_and_owner_dispatch_recorded",
]
REQUIRED_CODEX_DENIALS = {
    "vote",
    "resolve sovereign authority",
    "seal final decisions",
    "suppress material stays",
    "certify appeals",
    "amend charters",
    "write directly to Tree-of-Sophia",
    "force owner adoption",
    "author routing meaning",
    "promote policy precedent",
}
REQUIRED_ASSISTANT_DENIALS = {
    "self-recharter",
    "self-certify",
    "vote on own release",
    "bypass release holds",
    "hide durable behavior adoption",
}
REQUIRED_HUMAN_AUTHORITIES = {
    "council vote",
    "sovereign operator stop",
    "charter amendment",
    "veto or stay order",
    "appeal certification",
    "final policy precedent",
    "Tree-of-Sophia intake review",
}
REQUIRED_OWNER_REPOS = {
    "Agents-of-Abyss",
    "Tree-of-Sophia",
    "aoa-evals",
    "aoa-playbooks",
    "aoa-stats",
    "aoa-memo",
    "aoa-routing",
    "aoa-agents",
    "aoa-sdk",
    "aoa-kag",
    "aoa-skills",
    "aoa-techniques",
    "abyss-stack",
}


class ValidationError(RuntimeError):
    """Raised when an Experience polis/constitution surface drifts."""


def fail(message: str) -> None:
    raise ValidationError(message)


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        fail(f"missing JSON file: {path.relative_to(ROOT).as_posix()}")
        raise AssertionError from exc
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT).as_posix()}: {exc}")
        raise AssertionError from exc


def require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    return value


def require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{label} must be a list")
    return value


def require_files() -> None:
    missing = [
        path.relative_to(ROOT).as_posix()
        for path in (SCHEMA_PATH, EXAMPLE_PATH)
        if not path.exists()
    ]
    if missing:
        fail("missing Experience polis/constitution files: " + ", ".join(missing))


def validate_schema(schema: dict[str, Any], example: dict[str, Any]) -> None:
    if schema.get("title") != "experience_polis_constitution_v1":
        fail("polis/constitution schema title must be experience_polis_constitution_v1")
    if schema.get("additionalProperties") is not False:
        fail("polis/constitution schema must reject additional top-level properties")
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(example),
        key=lambda error: list(error.path),
    )
    if errors:
        fail(f"polis/constitution example does not match schema: {errors[0].message}")


def validate_flow_order(flow: dict[str, Any], key: str, expected: list[str]) -> None:
    raw_steps = require_list(flow.get(key), key)
    kinds = [
        require_dict(step, f"{key}[{index}]").get("kind")
        for index, step in enumerate(raw_steps)
    ]
    if kinds != expected:
        fail(f"{key} must preserve the expected ordered spine")
    if len(set(kinds)) != len(kinds):
        fail(f"{key} must not repeat step kinds")
    for index, raw_step in enumerate(raw_steps):
        step = require_dict(raw_step, f"{key}[{index}]")
        owner_repo = step.get("owner_repo")
        authority_note = step.get("authority_note")
        if not isinstance(owner_repo, str) or not owner_repo:
            fail(f"{key}[{index}].owner_repo must be non-empty")
        if not isinstance(authority_note, str) or not authority_note:
            fail(f"{key}[{index}].authority_note must be non-empty")


def validate_example(flow: dict[str, Any]) -> None:
    if flow.get("schema_version") != "experience_polis_constitution_v1":
        fail("example schema_version must be experience_polis_constitution_v1")
    if flow.get("contract_ref") != "experience_polis_constitution":
        fail("example contract_ref must be experience_polis_constitution")
    if flow.get("status") != "polis_governance_constitution_runtime_contract_gated":
        fail("example status must keep polis/constitution contract-gated")
    if flow.get("source_receipt_refs") != EXPECTED_SOURCE_SEEDS:
        fail("example source_receipt_refs must preserve v0.8 before v0.9")

    validate_flow_order(flow, "polis_flow", POLIS_ORDER)
    validate_flow_order(flow, "runtime_flow", RUNTIME_ORDER)

    authority = require_dict(flow.get("authority"), "authority")
    if authority.get("runtime_effect") != "contract_only":
        fail("authority.runtime_effect must remain contract_only")

    may = set(
        str(item)
        for item in require_list(authority.get("codex_may"), "authority.codex_may")
    )
    codex_denied = set(
        str(item)
        for item in require_list(
            authority.get("codex_must_not"), "authority.codex_must_not"
        )
    )
    assistant_denied = set(
        str(item)
        for item in require_list(
            authority.get("assistant_must_not"), "authority.assistant_must_not"
        )
    )
    human_required = set(
        str(item)
        for item in require_list(
            authority.get("human_authority_required"),
            "authority.human_authority_required",
        )
    )

    leaked = may.intersection(REQUIRED_CODEX_DENIALS)
    if leaked:
        fail(
            "authority.codex_may must not include denied authority: "
            + ", ".join(sorted(leaked))
        )

    missing_codex = REQUIRED_CODEX_DENIALS.difference(codex_denied)
    if missing_codex:
        fail("authority.codex_must_not is missing: " + ", ".join(sorted(missing_codex)))

    missing_assistant = REQUIRED_ASSISTANT_DENIALS.difference(assistant_denied)
    if missing_assistant:
        fail(
            "authority.assistant_must_not is missing: "
            + ", ".join(sorted(missing_assistant))
        )

    missing_human = REQUIRED_HUMAN_AUTHORITIES.difference(human_required)
    if missing_human:
        fail(
            "authority.human_authority_required is missing: "
            + ", ".join(sorted(missing_human))
        )

    owner_split = require_list(flow.get("owner_split"), "owner_split")
    repos = {
        require_dict(item, f"owner_split[{index}]").get("repo")
        for index, item in enumerate(owner_split)
    }
    missing_repos = REQUIRED_OWNER_REPOS.difference(repos)
    if missing_repos:
        fail("owner_split is missing: " + ", ".join(sorted(missing_repos)))


def run_validation() -> list[str]:
    try:
        require_files()
        schema = require_dict(read_json(SCHEMA_PATH), "schema")
        example = require_dict(read_json(EXAMPLE_PATH), "example")
        validate_schema(schema, example)
        validate_example(example)
    except ValidationError as exc:
        return [str(exc)]
    return []


def main() -> int:
    errors = run_validation()
    if errors:
        for error in errors:
            print(f"[error] {error}", file=sys.stderr)
        return 1
    print("ok: Experience polis/constitution center is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
