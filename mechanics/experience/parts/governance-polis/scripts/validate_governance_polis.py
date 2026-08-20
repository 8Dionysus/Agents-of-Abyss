#!/usr/bin/env python3
"""Validate the Experience polis/constitution center surfaces."""

from __future__ import annotations

import copy
from datetime import datetime
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


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
OPERATOR_PACKET_SCHEMA_PATH = (
    ROOT
    / "mechanics"
    / "experience"
    / "parts"
    / "governance-polis"
    / "schemas"
    / "operator_decision_packet_v1.json"
)
OPERATOR_PACKET_EXAMPLE_PATH = (
    ROOT
    / "mechanics"
    / "experience"
    / "parts"
    / "governance-polis"
    / "examples"
    / "operator_decision_packet.example.json"
)
OPERATOR_PACKET_NEGATIVE_PATH = (
    ROOT
    / "mechanics"
    / "experience"
    / "parts"
    / "governance-polis"
    / "examples"
    / "operator_decision_packet.negative-examples.json"
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
    "aoa-sdk",
    "aoa-agents",
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
        for path in (
            SCHEMA_PATH,
            EXAMPLE_PATH,
            OPERATOR_PACKET_SCHEMA_PATH,
            OPERATOR_PACKET_EXAMPLE_PATH,
            OPERATOR_PACKET_NEGATIVE_PATH,
        )
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


def _schema_error(
    schema: dict[str, Any],
    payload: dict[str, Any],
) -> str | None:
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        ).iter_errors(payload),
        key=lambda error: [str(part) for part in error.absolute_path],
    )
    if not errors:
        return None
    error = errors[0]
    path = "/".join(str(part) for part in error.absolute_path) or "<root>"
    return f"{path}: {error.message}"


def _parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def validate_operator_decision_packet(
    packet: dict[str, Any],
    *,
    resolved_manifest_sha256: str | None,
    resolved_artifact_set_id: str | None,
    schema: dict[str, Any] | None = None,
) -> None:
    active_schema = schema or require_dict(
        read_json(OPERATOR_PACKET_SCHEMA_PATH),
        "operator decision packet schema",
    )
    schema_problem = _schema_error(active_schema, packet)
    if schema_problem:
        fail(schema_problem)

    if resolved_manifest_sha256 is None:
        fail(
            "artifact_manifest_sha256 is unresolved; missing owner resolution "
            "means no decision"
        )
    if packet["artifact_manifest_sha256"] != resolved_manifest_sha256:
        fail(
            "artifact_manifest_sha256 does not match owner-resolved exact bytes; "
            "outcome is no decision"
        )
    if resolved_artifact_set_id is None:
        fail(
            "artifact_set_id is unresolved; missing owner resolution means "
            "no decision"
        )
    if packet["artifact_set_id"] != resolved_artifact_set_id:
        fail(
            "artifact_set_id does not match the owner-resolved manifest; "
            "outcome is no decision"
        )

    created_at = _parse_timestamp(packet["created_at"])
    decided_at = _parse_timestamp(packet["operator_decided_at"])
    if decided_at < created_at:
        fail("operator_decided_at must not precede created_at")

    review = require_dict(packet["review_funnel"], "review_funnel")
    if review["evidence_review_ref"] == review["authority_review_ref"]:
        fail("review_funnel requires distinct evidence and authority AI runs")

    narrowed_items = require_list(packet["narrowed_items"], "narrowed_items")
    artifact_refs = [
        require_dict(item, f"narrowed_items[{index}]").get("artifact_ref")
        for index, item in enumerate(narrowed_items)
    ]
    if len(artifact_refs) != len(set(artifact_refs)):
        fail("narrowed_items artifact_ref values must be unique")

    payload_owner = require_dict(packet["payload_owner"], "payload_owner")
    followup = require_dict(packet["followup"], "followup")
    if followup["next_owner_ref"] != payload_owner["effect_owner_ref"]:
        fail("followup/next_owner_ref must equal payload_owner/effect_owner_ref")


def _pointer_parts(pointer: str) -> list[str]:
    if not pointer.startswith("/"):
        fail(f"negative case pointer must start with '/': {pointer}")
    return [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.lstrip("/").split("/")
    ]


def _pointer_parent(payload: Any, pointer: str) -> tuple[Any, str]:
    parts = _pointer_parts(pointer)
    target = payload
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    return target, parts[-1]


def set_pointer(payload: Any, pointer: str, value: Any) -> None:
    target, leaf = _pointer_parent(payload, pointer)
    if isinstance(target, list):
        target[int(leaf)] = value
    else:
        target[leaf] = value


def delete_pointer(payload: Any, pointer: str) -> None:
    target, leaf = _pointer_parent(payload, pointer)
    if isinstance(target, list):
        del target[int(leaf)]
    else:
        del target[leaf]


def validate_operator_packet_negative_cases(
    schema: dict[str, Any],
    example: dict[str, Any],
) -> int:
    corpus = require_dict(
        read_json(OPERATOR_PACKET_NEGATIVE_PATH),
        "operator decision packet negative corpus",
    )
    cases = require_list(corpus.get("cases"), "negative cases")
    if not cases:
        fail("operator decision packet negative corpus must not be empty")
    seen: set[str] = set()
    for index, raw_case in enumerate(cases):
        case = require_dict(raw_case, f"negative cases[{index}]")
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            fail(f"negative cases[{index}].case_id must be non-empty")
        if case_id in seen:
            fail(f"duplicate operator decision negative case: {case_id}")
        seen.add(case_id)

        candidate = copy.deepcopy(example)
        for pointer, value in require_dict(
            case.get("set", {}),
            f"negative cases/{case_id}/set",
        ).items():
            set_pointer(candidate, pointer, value)
        for pointer in require_list(
            case.get("delete", []),
            f"negative cases/{case_id}/delete",
        ):
            delete_pointer(candidate, str(pointer))
        resolved_sha = case.get(
            "resolved_manifest_sha256",
            candidate.get("artifact_manifest_sha256"),
        )
        resolved_set_id = case.get(
            "resolved_artifact_set_id",
            candidate.get("artifact_set_id"),
        )
        try:
            validate_operator_decision_packet(
                candidate,
                resolved_manifest_sha256=(
                    str(resolved_sha) if resolved_sha is not None else None
                ),
                resolved_artifact_set_id=(
                    str(resolved_set_id) if resolved_set_id is not None else None
                ),
                schema=schema,
            )
        except ValidationError as exc:
            expected = case.get("expected_error")
            if not isinstance(expected, str) or expected not in str(exc):
                fail(
                    f"negative case {case_id} expected {expected!r}, "
                    f"got {str(exc)!r}"
                )
        else:
            fail(f"negative case {case_id} unexpectedly passed")
    return len(cases)


def run_validation() -> list[str]:
    try:
        require_files()
        schema = require_dict(read_json(SCHEMA_PATH), "schema")
        example = require_dict(read_json(EXAMPLE_PATH), "example")
        validate_schema(schema, example)
        validate_example(example)
        operator_schema = require_dict(
            read_json(OPERATOR_PACKET_SCHEMA_PATH),
            "operator decision packet schema",
        )
        operator_example = require_dict(
            read_json(OPERATOR_PACKET_EXAMPLE_PATH),
            "operator decision packet example",
        )
        validate_operator_decision_packet(
            operator_example,
            resolved_manifest_sha256=operator_example.get(
                "artifact_manifest_sha256"
            ),
            resolved_artifact_set_id=operator_example.get("artifact_set_id"),
            schema=operator_schema,
        )
        validate_operator_packet_negative_cases(operator_schema, operator_example)
    except ValidationError as exc:
        return [str(exc)]
    return []


def main() -> int:
    errors = run_validation()
    if errors:
        for error in errors:
            print(f"[error] {error}", file=sys.stderr)
        return 1
    print(
        "ok: Experience polis/constitution center and C25 operator decision "
        "packet are valid"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
