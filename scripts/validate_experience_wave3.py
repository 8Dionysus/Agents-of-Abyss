#!/usr/bin/env python3
"""Validate the Experience Wave 3 federation/adoption center surfaces."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_WAVE3_FEDERATION_ADOPTION.md"
V06_DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V0_6_FEDERATION_HARVEST.md"
V07_DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V0_7_ADOPTION_FORGE.md"
SCHEMA_PATH = ROOT / "schemas" / "experience-wave3-federation-adoption.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "experience_wave3_federation_adoption.example.json"

EXPECTED_SOURCE_SEEDS = [
    "aoa-experience-federation-harvest-seed-v0_6.zip",
    "aoa-experience-adoption-forge-seed-v0_7.zip",
]
FEDERATION_ORDER = [
    "owner_local_signals_collected",
    "cross_repo_recurrence_detected",
    "federation_pattern_candidate_named",
    "harvest_gate_evaluated",
    "shared_pattern_registry_recorded",
    "kag_promotion_dossier_built",
    "tos_candidate_dossier_boundary_checked",
    "owner_local_adoption_quests_fanned_out",
]
ADOPTION_ORDER = [
    "shared_pattern_received",
    "adoption_request_opened",
    "owner_consent_recorded",
    "compatibility_matrix_checked",
    "projection_resolution_reviewed",
    "shadow_adoption_run_completed",
    "adoption_decision_recorded",
    "owner_local_patch_prepared",
    "runtime_activation_gate_checked",
    "rollback_or_quarantine_declared",
    "retention_check_scheduled",
]
REQUIRED_DOC_TOKENS = [
    "Harvest approval is not adoption authority",
    "no direct `Tree-of-Sophia` write",
    "no Codex approval of federation harvest",
    "no assistant hidden self-rewrite",
    "no runtime activation without owner-local approval",
]
REQUIRED_CODEX_DENIALS = {
    "approve federation harvest",
    "promote to KAG",
    "write directly to Tree-of-Sophia",
    "self-rewrite assistants",
    "force owner adoption",
    "activate runtime behavior",
    "author routing meaning",
    "bypass rollback or quarantine",
}
REQUIRED_HUMAN_AUTHORITIES = {
    "harvest approval",
    "owner adoption decision",
    "runtime activation",
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
    """Raised when an Experience Wave 3 surface drifts."""


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
        for path in (DOC_PATH, V06_DOC_PATH, V07_DOC_PATH, SCHEMA_PATH, EXAMPLE_PATH)
        if not path.exists()
    ]
    if missing:
        fail("missing Experience Wave 3 files: " + ", ".join(missing))


def validate_schema(schema: dict[str, Any], example: dict[str, Any]) -> None:
    if schema.get("title") != "experience_wave3_federation_adoption_v1":
        fail("Wave 3 schema title must be experience_wave3_federation_adoption_v1")
    if schema.get("additionalProperties") is not False:
        fail("Wave 3 schema must reject additional top-level properties")
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(example), key=lambda error: list(error.path))
    if errors:
        fail(f"Wave 3 example does not match schema: {errors[0].message}")


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


def validate_example(flow: dict[str, Any]) -> None:
    if flow.get("schema_version") != "experience_wave3_federation_adoption_v1":
        fail("example schema_version must be experience_wave3_federation_adoption_v1")
    if flow.get("wave") != "experience_wave3":
        fail("example wave must be experience_wave3")
    if flow.get("status") != "federation_harvest_active_adoption_forge_contract_gated":
        fail("example status must keep adoption owner-gated")
    if flow.get("source_seeds") != EXPECTED_SOURCE_SEEDS:
        fail("example source_seeds must preserve v0.6 before v0.7")

    validate_flow_order(flow, "federation_flow", FEDERATION_ORDER)
    validate_flow_order(flow, "adoption_flow", ADOPTION_ORDER)

    authority = require_dict(flow.get("authority"), "authority")
    if authority.get("runtime_effect") != "none":
        fail("authority.runtime_effect must remain none")

    may = set(str(item) for item in require_list(authority.get("codex_may"), "authority.codex_may"))
    denied = set(str(item) for item in require_list(authority.get("codex_must_not"), "authority.codex_must_not"))
    required = set(
        str(item)
        for item in require_list(authority.get("human_authority_required"), "authority.human_authority_required")
    )
    leaked = may.intersection(REQUIRED_CODEX_DENIALS)
    if leaked:
        fail("authority.codex_may must not include denied authority: " + ", ".join(sorted(leaked)))
    missing_denials = REQUIRED_CODEX_DENIALS.difference(denied)
    if missing_denials:
        fail("authority.codex_must_not is missing: " + ", ".join(sorted(missing_denials)))
    missing_human = REQUIRED_HUMAN_AUTHORITIES.difference(required)
    if missing_human:
        fail("authority.human_authority_required is missing: " + ", ".join(sorted(missing_human)))

    owner_split = require_list(flow.get("owner_split"), "owner_split")
    repos = {require_dict(item, f"owner_split[{index}]").get("repo") for index, item in enumerate(owner_split)}
    missing_repos = REQUIRED_OWNER_REPOS.difference(repos)
    if missing_repos:
        fail("owner_split is missing: " + ", ".join(sorted(missing_repos)))


def validate_doc(text: str) -> None:
    for token in REQUIRED_DOC_TOKENS:
        if token not in text:
            fail(f"mechanics/experience/legacy/raw/EXPERIENCE_WAVE3_FEDERATION_ADOPTION.md must mention {token!r}")


def run_validation() -> list[str]:
    try:
        require_files()
        doc_text = DOC_PATH.read_text(encoding="utf-8")
        validate_doc(doc_text)
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
    print("ok: Experience Wave 3 federation/adoption center is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
