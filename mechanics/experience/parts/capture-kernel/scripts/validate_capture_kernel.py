#!/usr/bin/env python3
"""Validate the Experience Wave 1 center kernel surfaces."""

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

DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_WAVE1_KERNEL.md"
SCHEMA_PATH = ROOT / "mechanics" / "experience" / "parts" / "capture-kernel" / "schemas" / "experience-wave1-flow.schema.json"
EXAMPLE_PATH = ROOT / "mechanics" / "experience" / "parts" / "capture-kernel" / "examples" / "experience_wave1_flow.example.json"

EXPECTED_SOURCE_SEEDS = [
    "aoa-experience-mechanic-seed-v0_1.zip",
    "aoa-experience-runtime-capture-seed-v0_2.zip",
    "aoa-experience-pilot-integration-seed-v0_3.zip",
]
EXPECTED_EVENT_ORDER = [
    "friction_observed",
    "recurrence_detected",
    "candidate_declared",
    "review_verdict_recorded",
    "memory_gate_decided",
    "owner_route_selected",
    "projection_proposed",
]
REQUIRED_NOT_OWNED_TOKENS = [
    "runtime activation",
    "durable memory write",
    "owner-repo landing",
    "derived observability truth",
    "projection execution",
]
FORBIDDEN_PROJECTION_FIELDS = {
    "runtime_endpoint",
    "memory_write",
    "stats_truth",
    "hidden_runner",
    "auto_projection",
    "live_operator_queue",
}


class ValidationError(RuntimeError):
    """Raised when an Experience Wave 1 surface drifts."""


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


def require_files() -> None:
    missing = [
        path.relative_to(ROOT).as_posix()
        for path in (DOC_PATH, SCHEMA_PATH, EXAMPLE_PATH)
        if not path.exists()
    ]
    if missing:
        fail("missing Experience Wave 1 files: " + ", ".join(missing))


def require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    return value


def require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{label} must be a list")
    return value


def validate_schema(schema: dict[str, Any]) -> None:
    if schema.get("title") != "experience_wave1_flow_v1":
        fail("mechanics/experience/parts/capture-kernel/schemas/experience-wave1-flow.schema.json title must be experience_wave1_flow_v1")
    if schema.get("additionalProperties") is not False:
        fail("experience Wave 1 schema must reject additional top-level properties")
    required = require_list(schema.get("required"), "schema.required")
    for key in (
        "schema_version",
        "wave",
        "source_seeds",
        "candidate",
        "events",
        "verdict",
        "memory_gate",
        "owner_route",
        "projection",
        "authority",
    ):
        if key not in required:
            fail(f"schema.required must include {key!r}")


def validate_example_matches_schema(schema: dict[str, Any], example: dict[str, Any]) -> None:
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(example), key=lambda error: list(error.path))
    if errors:
        fail(f"Experience Wave 1 example does not match schema: {errors[0].message}")


def validate_flow(flow: dict[str, Any]) -> None:
    if flow.get("schema_version") != "experience_wave1_flow_v1":
        fail("example schema_version must be experience_wave1_flow_v1")
    if flow.get("wave") != "experience_wave1":
        fail("example wave must be experience_wave1")
    if flow.get("status") != "center_kernel_seeded":
        fail("example status must be center_kernel_seeded")
    if flow.get("source_seeds") != EXPECTED_SOURCE_SEEDS:
        fail("example source_seeds must preserve the v0.1-v0.3 Wave 1 order")

    candidate = require_dict(flow.get("candidate"), "candidate")
    candidate_ref = candidate.get("candidate_ref")
    if not isinstance(candidate_ref, str) or not candidate_ref.startswith("experience.candidate."):
        fail("candidate.candidate_ref must be an experience candidate ref")

    events = require_list(flow.get("events"), "events")
    kinds = [require_dict(event, f"events[{index}]").get("kind") for index, event in enumerate(events)]
    if kinds[: len(EXPECTED_EVENT_ORDER)] != EXPECTED_EVENT_ORDER:
        fail("events must preserve the Wave 1 ordered spine")
    if len(set(kinds)) != len(kinds):
        fail("events must not repeat Wave 1 event kinds in the center example")

    event_ids: list[str] = []
    for index, raw_event in enumerate(events):
        event = require_dict(raw_event, f"events[{index}]")
        event_id = event.get("event_id")
        if not isinstance(event_id, str) or not event_id:
            fail(f"events[{index}].event_id must be non-empty")
        event_ids.append(event_id)
        if event.get("candidate_ref") != candidate_ref:
            fail(f"events[{index}].candidate_ref must match candidate.candidate_ref")
        evidence_refs = require_list(event.get("evidence_refs"), f"events[{index}].evidence_refs")
        if not evidence_refs:
            fail(f"events[{index}].evidence_refs must not be empty")
    if len(event_ids) != len(set(event_ids)):
        fail("event_id values must be unique")

    verdict = require_dict(flow.get("verdict"), "verdict")
    if verdict.get("candidate_ref") != candidate_ref:
        fail("verdict.candidate_ref must match candidate.candidate_ref")
    if verdict.get("decision") != candidate.get("status"):
        fail("candidate.status must match verdict.decision")
    if verdict.get("decision") == "accepted_for_owner_landing":
        route = require_dict(flow.get("owner_route"), "owner_route")
        if route.get("routing_status") != "owner_review_required":
            fail("accepted candidates must still require owner review")

    memory_gate = require_dict(flow.get("memory_gate"), "memory_gate")
    if memory_gate.get("candidate_ref") != candidate_ref:
        fail("memory_gate.candidate_ref must match candidate.candidate_ref")
    if memory_gate.get("write_performed") is not False:
        fail("memory_gate.write_performed must remain false in the center kernel")

    owner_route = require_dict(flow.get("owner_route"), "owner_route")
    if owner_route.get("candidate_ref") != candidate_ref:
        fail("owner_route.candidate_ref must match candidate.candidate_ref")
    if owner_route.get("primary_repo") != candidate.get("intended_owner_repo"):
        fail("owner_route.primary_repo must match candidate.intended_owner_repo")
    non_authority_repos = require_list(owner_route.get("non_authority_repos"), "owner_route.non_authority_repos")
    for repo in ("Agents-of-Abyss", "aoa-stats", "aoa-routing", "aoa-sdk"):
        if repo not in non_authority_repos:
            fail(f"owner_route.non_authority_repos must include {repo}")

    projection = require_dict(flow.get("projection"), "projection")
    if projection.get("candidate_ref") != candidate_ref:
        fail("projection.candidate_ref must match candidate.candidate_ref")
    if projection.get("status") not in {"not_requested", "proposed_dry_run", "owner_local_only", "blocked"}:
        fail("projection.status is not a valid inert Wave 1 projection status")
    forbidden_present = sorted(FORBIDDEN_PROJECTION_FIELDS.intersection(projection))
    if forbidden_present:
        fail("projection must not contain runtime fields: " + ", ".join(forbidden_present))
    must_not = " ".join(str(item) for item in require_list(projection.get("must_not"), "projection.must_not"))
    for phrase in ("hidden runtime", "durable memory", "owner review"):
        if phrase not in must_not:
            fail(f"projection.must_not must mention {phrase!r}")

    authority = require_dict(flow.get("authority"), "authority")
    if authority.get("runtime_effect") != "none":
        fail("authority.runtime_effect must remain none")
    not_owned = require_list(authority.get("not_owned_here"), "authority.not_owned_here")
    not_owned_text = "\n".join(str(item) for item in not_owned)
    for token in REQUIRED_NOT_OWNED_TOKENS:
        if token not in not_owned_text:
            fail(f"authority.not_owned_here must include {token!r}")


def validate_doc(text: str) -> None:
    for token in (
        "friction_observed",
        "recurrence_detected",
        "candidate_declared",
        "review_verdict_recorded",
        "memory_gate_decided",
        "owner_route_selected",
        "projection_proposed",
        "hidden runtime execution",
        "automatic projection",
    ):
        if token not in text:
            fail(f"mechanics/experience/legacy/raw/EXPERIENCE_WAVE1_KERNEL.md must mention {token!r}")


def run_validation() -> list[str]:
    try:
        require_files()
        validate_doc(DOC_PATH.read_text(encoding="utf-8"))
        schema = require_dict(read_json(SCHEMA_PATH), "schema")
        example = require_dict(read_json(EXAMPLE_PATH), "example")
        validate_schema(schema)
        validate_example_matches_schema(schema, example)
        validate_flow(example)
    except ValidationError as exc:
        return [str(exc)]
    return []


def main() -> int:
    errors = run_validation()
    if errors:
        for error in errors:
            print(f"[error] {error}", file=sys.stderr)
        return 1
    print("ok: Experience Wave 1 center kernel is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
