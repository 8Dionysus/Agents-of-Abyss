#!/usr/bin/env python3
"""Validate the Experience Wave 2 certification/watchtower center surfaces."""

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

DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_WAVE2_CERTIFICATION_WATCHTOWER.md"
V04_DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V0_4_CERTIFICATION_FORGE.md"
V05_DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V0_5_DEPLOYMENT_WATCHTOWER.md"
SCHEMA_PATH = ROOT / "mechanics" / "experience" / "parts" / "certification-proof" / "schemas" / "experience-wave2-certification-watchtower.schema.json"
EXAMPLE_PATH = ROOT / "mechanics" / "experience" / "parts" / "certification-proof" / "examples" / "experience_wave2_certification_watchtower.example.json"

EXPECTED_SOURCE_SEEDS = [
    "aoa-experience-certification-forge-seed-v0_4.zip",
    "aoa-experience-deployment-watchtower-seed-v0_5.zip",
]
CERTIFICATION_ORDER = [
    "experience_patch_proposal",
    "release_candidate_built",
    "regression_pack_bound",
    "certification_gate_evaluated",
    "rollback_drill_proved",
    "operator_review_recorded",
    "versioned_assistant_release_declared",
    "post_release_retention_watch_started",
]
DEPLOYMENT_ORDER = [
    "certified_release_received",
    "deployment_plan_declared",
    "rollout_ring_activated",
    "canary_watch_recorded",
    "drift_or_health_verdict_recorded",
    "ring_promotion_or_rollback_decided",
    "incident_reentry_routed",
    "post_release_retention_result_recorded",
]
REQUIRED_DOC_TOKENS = [
    "Codex may not certify",
    "No Codex ring promotion",
    "No assistant self-deployment",
    "release is not done at activation",
    "contract-only",
    "no live service activation",
]
REQUIRED_CODEX_DENIALS = {
    "certify",
    "approve release",
    "promote rollout rings",
    "execute durable rollback",
    "self-deploy assistants",
    "suppress material alarms",
}
REQUIRED_HUMAN_AUTHORITIES = {
    "certification",
    "release approval",
    "ring promotion",
    "durable rollback",
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
    "aoa-stats",
}


class ValidationError(RuntimeError):
    """Raised when an Experience Wave 2 surface drifts."""


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
        for path in (DOC_PATH, V04_DOC_PATH, V05_DOC_PATH, SCHEMA_PATH, EXAMPLE_PATH)
        if not path.exists()
    ]
    if missing:
        fail("missing Experience Wave 2 files: " + ", ".join(missing))


def validate_schema(schema: dict[str, Any], example: dict[str, Any]) -> None:
    if schema.get("title") != "experience_wave2_certification_watchtower_v1":
        fail("Wave 2 schema title must be experience_wave2_certification_watchtower_v1")
    if schema.get("additionalProperties") is not False:
        fail("Wave 2 schema must reject additional top-level properties")
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(example), key=lambda error: list(error.path))
    if errors:
        fail(f"Wave 2 example does not match schema: {errors[0].message}")


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
    if flow.get("schema_version") != "experience_wave2_certification_watchtower_v1":
        fail("example schema_version must be experience_wave2_certification_watchtower_v1")
    if flow.get("wave") != "experience_wave2":
        fail("example wave must be experience_wave2")
    if flow.get("status") != "certification_active_watchtower_contract_only":
        fail("example status must keep v0.5 contract-only until v0.4 is green")
    if flow.get("source_seeds") != EXPECTED_SOURCE_SEEDS:
        fail("example source_seeds must preserve v0.4 before v0.5")

    validate_flow_order(flow, "certification_flow", CERTIFICATION_ORDER)
    validate_flow_order(flow, "deployment_flow", DEPLOYMENT_ORDER)

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
            fail(f"mechanics/experience/legacy/raw/EXPERIENCE_WAVE2_CERTIFICATION_WATCHTOWER.md must mention {token!r}")


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
    print("ok: Experience Wave 2 certification/watchtower center is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
