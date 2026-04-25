#!/usr/bin/env python3
"""Validate the Experience Wave 5 sovereign office center surfaces."""

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

DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_WAVE5_SOVEREIGN_OFFICE.md"
V10_DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V1_0_INSTALLATION_SOVEREIGN_RELEASE.md"
V11_DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V1_1_LIVE_OFFICE_EXPANSION.md"
SCHEMA_PATH = ROOT / "mechanics" / "experience" / "parts" / "office-operations" / "schemas" / "experience-wave5-sovereign-office.schema.json"
EXAMPLE_PATH = ROOT / "mechanics" / "experience" / "parts" / "office-operations" / "examples" / "experience_wave5_sovereign_office.example.json"

EXPECTED_SOURCE_SEEDS = [
    "aoa-experience-installation-sovereign-release-seed-v1_0.zip",
    "aoa-experience-live-office-expansion-seed-v1_1.zip",
]
INSTALLATION_ORDER = [
    "seed_prepared",
    "landing_order_declared",
    "migration_backed_up",
    "smoke_gates_passed",
    "operator_review_completed",
    "sovereign_release_sealed",
    "rollback_drill_passed",
    "post_release_watch_scheduled",
]
OFFICE_TRAIN_ORDER = [
    "notary_office_anchor_confirmed",
    "office_registry_declared",
    "bootstrap_order_notary_first",
    "handoff_graph_receipts_required",
    "compatibility_matrix_passed",
    "train_smoke_gates_passed",
    "rollback_plan_declared",
    "operator_go_no_go_recorded",
    "train_seal_recorded",
    "replay_and_watch_scheduled",
]
REQUIRED_DOC_TOKENS = [
    "Codex may not certify",
    "`notary.assistant` remains the first receipt-bearing office anchor",
    "allow direct runtime writes into `Tree-of-Sophia`",
    "Stats summarizes. Memo remembers. Evals judges. Routing points.",
]
REQUIRED_CODEX_DENIALS = {
    "certify releases",
    "seal releases",
    "approve release trains",
    "self-release",
    "suppress material evidence",
    "write directly to Tree-of-Sophia",
    "force owner adoption",
    "author routing meaning",
}
REQUIRED_ASSISTANT_DENIALS = {
    "self-release",
    "self-enroll",
    "self-certify",
    "self-recharter",
    "hide durable behavior adoption",
    "launder service revisions into agonic scars",
}
REQUIRED_HUMAN_AUTHORITIES = {
    "operator release seal",
    "operator train approval",
    "Tree-of-Sophia intake review",
    "owner-local activation",
    "rollback or hold override",
}
REQUIRED_OWNER_REPOS = {
    "Agents-of-Abyss",
    "Tree-of-Sophia",
    "abyss-stack",
    "aoa-agents",
    "aoa-evals",
    "aoa-kag",
    "aoa-memo",
    "aoa-playbooks",
    "aoa-routing",
    "aoa-sdk",
    "aoa-skills",
    "aoa-stats",
    "aoa-techniques",
}
REQUIRED_PRIMARY_OFFICES = {
    "notary.assistant",
    "concierge.assistant",
    "courier.assistant",
    "monitor.assistant",
}
NON_PRIMARY_UNTIL_PROMOTED = {
    "librarian.assistant",
    "steward.assistant",
    "scheduler.assistant",
}


class ValidationError(RuntimeError):
    """Raised when an Experience Wave 5 surface drifts."""


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
        for path in (DOC_PATH, V10_DOC_PATH, V11_DOC_PATH, SCHEMA_PATH, EXAMPLE_PATH)
        if not path.exists()
    ]
    if missing:
        fail("missing Experience Wave 5 files: " + ", ".join(missing))


def validate_schema(schema: dict[str, Any], example: dict[str, Any]) -> None:
    if schema.get("title") != "experience_wave5_sovereign_office_v1":
        fail("Wave 5 schema title must be experience_wave5_sovereign_office_v1")
    if schema.get("additionalProperties") is not False:
        fail("Wave 5 schema must reject additional top-level properties")
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(example), key=lambda error: list(error.path))
    if errors:
        fail(f"Wave 5 example does not match schema: {errors[0].message}")


def validate_flow_order(flow: dict[str, Any], key: str, expected: list[str]) -> None:
    raw_steps = require_list(flow.get(key), key)
    kinds = [require_dict(step, f"{key}[{index}]").get("kind") for index, step in enumerate(raw_steps)]
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


def validate_authority(flow: dict[str, Any]) -> None:
    authority = require_dict(flow.get("authority"), "authority")
    if authority.get("runtime_effect") != "contract_only":
        fail("authority.runtime_effect must remain contract_only")
    may = set(str(item) for item in require_list(authority.get("codex_may"), "authority.codex_may"))
    codex_denied = set(str(item) for item in require_list(authority.get("codex_must_not"), "authority.codex_must_not"))
    assistant_denied = set(
        str(item) for item in require_list(authority.get("assistant_must_not"), "authority.assistant_must_not")
    )
    human_required = set(
        str(item)
        for item in require_list(authority.get("human_authority_required"), "authority.human_authority_required")
    )
    leaked = may.intersection(REQUIRED_CODEX_DENIALS)
    if leaked:
        fail("authority.codex_may must not include denied authority: " + ", ".join(sorted(leaked)))
    missing_codex = REQUIRED_CODEX_DENIALS.difference(codex_denied)
    if missing_codex:
        fail("authority.codex_must_not is missing: " + ", ".join(sorted(missing_codex)))
    missing_assistant = REQUIRED_ASSISTANT_DENIALS.difference(assistant_denied)
    if missing_assistant:
        fail("authority.assistant_must_not is missing: " + ", ".join(sorted(missing_assistant)))
    missing_human = REQUIRED_HUMAN_AUTHORITIES.difference(human_required)
    if missing_human:
        fail("authority.human_authority_required is missing: " + ", ".join(sorted(missing_human)))


def validate_office_contract(flow: dict[str, Any]) -> None:
    office = require_dict(flow.get("office_contract"), "office_contract")
    if office.get("first_office") != "notary.assistant":
        fail("office_contract.first_office must remain notary.assistant")
    if office.get("office_kind") != "assistant":
        fail("office_contract.office_kind must remain assistant")
    if office.get("evolution_mode") != "exogenous_reactive":
        fail("office_contract.evolution_mode must remain exogenous_reactive")
    if office.get("self_modification_allowed") is not False:
        fail("office_contract.self_modification_allowed must stay false")
    if office.get("direct_tos_runtime_write_allowed") is not False:
        fail("office_contract.direct_tos_runtime_write_allowed must stay false")

    primary = set(str(item) for item in require_list(office.get("required_primary_offices"), "required_primary_offices"))
    missing_primary = REQUIRED_PRIMARY_OFFICES.difference(primary)
    if missing_primary:
        fail("office_contract.required_primary_offices is missing: " + ", ".join(sorted(missing_primary)))
    non_primary = set(str(item) for item in require_list(office.get("non_primary_until_promoted"), "non_primary_until_promoted"))
    missing_non_primary = NON_PRIMARY_UNTIL_PROMOTED.difference(non_primary)
    if missing_non_primary:
        fail("office_contract.non_primary_until_promoted is missing: " + ", ".join(sorted(missing_non_primary)))


def validate_example(flow: dict[str, Any]) -> None:
    if flow.get("schema_version") != "experience_wave5_sovereign_office_v1":
        fail("example schema_version must be experience_wave5_sovereign_office_v1")
    if flow.get("wave") != "experience_wave5":
        fail("example wave must be experience_wave5")
    if flow.get("status") != "sovereign_release_live_office_expansion_contract_gated":
        fail("example status must keep Wave 5 contract-gated")
    if flow.get("source_seeds") != EXPECTED_SOURCE_SEEDS:
        fail("example source_seeds must preserve v1.0 before v1.1")

    validate_flow_order(flow, "installation_flow", INSTALLATION_ORDER)
    validate_flow_order(flow, "office_train_flow", OFFICE_TRAIN_ORDER)
    validate_authority(flow)
    validate_office_contract(flow)

    owner_split = require_list(flow.get("owner_split"), "owner_split")
    repos = {require_dict(item, f"owner_split[{index}]").get("repo") for index, item in enumerate(owner_split)}
    missing_repos = REQUIRED_OWNER_REPOS.difference(repos)
    if missing_repos:
        fail("owner_split is missing: " + ", ".join(sorted(missing_repos)))


def validate_doc(text: str) -> None:
    for token in REQUIRED_DOC_TOKENS:
        if token not in text:
            fail(f"mechanics/experience/legacy/raw/EXPERIENCE_WAVE5_SOVEREIGN_OFFICE.md must mention {token!r}")


def run_validation() -> list[str]:
    try:
        require_files()
        validate_doc(DOC_PATH.read_text(encoding="utf-8"))
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
    print("ok: Experience Wave 5 sovereign office center is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
