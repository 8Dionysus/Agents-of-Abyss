#!/usr/bin/env python3
"""Validate the Experience v1.2 service mesh operations center contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md"
SCHEMA_PATH = ROOT / "mechanics" / "experience" / "parts" / "service-mesh" / "schemas" / "experience-v1-2-service-mesh-operations.schema.json"
EXAMPLE_PATH = ROOT / "mechanics" / "experience" / "parts" / "service-mesh" / "examples" / "experience_v1_2_service_mesh_operations.example.json"

SOURCE_ARCHIVE = "aoa-experience-service-mesh-operations-seed-v1_2.zip"
SOURCE_SHA256 = "df829241ac629770635290e5da2742b81e4d5575270c94a92c34a95f4bbacb85"

EXPECTED_PREDECESSORS = [
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.md",
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.map.yaml",
    "mechanics/experience/legacy/raw/EXPERIENCE_WAVE5_SOVEREIGN_OFFICE.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_1_LIVE_OFFICE_EXPANSION.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_SERVICE_MESH_LAW.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md",
    "mechanics/agon/docs/AGON_PRE_PROTOCOL_STOP_LINES.md",
]

EXPECTED_PRIMARY_OFFICES = [
    "notary.assistant",
    "concierge.assistant",
    "courier.assistant",
    "monitor.assistant",
]

EXPECTED_PREPARED_OFFICES = [
    "librarian.assistant",
    "steward.assistant",
    "scheduler.assistant",
]

EXPECTED_FLOW_KINDS = [
    "service_mesh_release_received",
    "drill_plan_declared",
    "scenario_injected",
    "office_integrity_checked",
    "bounded_verdict_recorded",
    "memory_gate_evaluated",
    "incident_reentry_routed",
    "retention_or_patch_proposal_declared",
]

EXPECTED_FLOW_OWNERS = [
    "Agents-of-Abyss",
    "aoa-playbooks",
    "aoa-playbooks",
    "aoa-agents",
    "aoa-evals",
    "aoa-memo",
    "aoa-routing",
    "Agents-of-Abyss",
]

EXPECTED_FLOW_STOP_LINES = [
    ["no new office promotion", "no release approval"],
    ["no runtime execution", "no scheduler loop"],
    ["no hidden failure injection", "no live service activation"],
    ["no assistant self-heal", "no assistant contestant drift"],
    ["no drill pass by Codex", "no live verdict authority"],
    ["memo is not truth", "no retention execution"],
    ["routing is not owner", "no live summon authority"],
    ["no automatic patch landing", "no rank trust or honor mutation"],
]

EXPECTED_FLOW_AUTHORITY_NOTES = [
    "v1.1 office mesh law is the predecessor; this step does not expand the mesh",
    "future owner-local playbooks may choreograph drills; center only names the contract",
    "scenario injection remains rehearsal input, not production incident creation",
    "office mandate, handoff, receipt, scope, alarm, rollback, and escalation checks remain assistant-boundary evidence",
    "evals may record bounded verdict evidence; they do not certify drill pass",
    "memory gate can admit reviewed lesson candidates only after owner review",
    "routing may suggest reentry and escalation paths; it does not own meaning",
    "material failures return to the experience loop as candidates, not automatic landings",
]

EXPECTED_FAILURE_LAWS = [
    "no_hidden_assistant_self_heal",
    "no_courier_meaning_edit",
    "no_concierge_scope_expansion",
    "no_notary_closure_without_receipt",
    "no_monitor_material_alarm_without_verdict_path",
    "no_service_to_agon_escalation_without_trigger",
    "no_drill_pass_by_codex",
    "no_direct_tree_of_sophia_runtime_write",
]

EXPECTED_OWNER_REPOS = {
    "8Dionysus",
    "Agents-of-Abyss",
    "Dionysus",
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

REQUIRED_DOC_TOKENS = [
    "It is Wave 2 of the current v1.2-v2.0 planting campaign",
    "It is not `Experience Wave 2`",
    "`aoa-experience-service-mesh-operations-seed-v1_2.zip`",
    SOURCE_SHA256,
    "`EXPERIENCE_V1_1_LIVE_OFFICE_EXPANSION.md`",
    "`EXPERIENCE_SERVICE_MESH_LAW.md`",
    "`EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md`",
    "`EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md`",
    "`AGON_PRE_PROTOCOL_STOP_LINES.md`",
    "`no_hidden_assistant_self_heal`",
    "`no_drill_pass_by_codex`",
    "activate live services",
    "service-to-Agon escalation into live summon authority",
    "stats become proof",
    "memo become truth",
    "routing become owner",
    "KAG become canon",
    "SDK become authority",
]

REQUIRED_CODEX_DENIALS = [
    "certify drill passed",
    "seal drill",
    "rewrite assistant policy",
    "activate live services ports schedulers workers or daemons",
    "approve release or train",
    "grant service-to-Agon live summon authority",
    "grant live verdict authority",
    "write scars",
    "mutate rank trust honor or retention",
    "write directly to Tree-of-Sophia",
    "promote KAG patterns to canon",
    "copy raw archive proposals into owner truth",
]

EXPECTED_CODEX_MAY = [
    "simulate service drills",
    "collect evidence",
    "propose drill results",
    "prepare owner-local requests",
    "run validators",
]

REQUIRED_ASSISTANT_DENIALS = [
    "self-heal persistent mandate",
    "self-release",
    "self-enroll",
    "self-certify",
    "become agonic contestant",
    "edit courier packet meaning",
    "expand concierge scope",
    "close notary work without receipt",
    "treat monitor alarm as material without verdict path",
]

EXPECTED_DERIVED_DENIALS = {
    "stats_as_proof",
    "memo_as_truth",
    "routing_as_owner",
    "kag_as_canon",
    "sdk_as_authority",
    "runtime_as_doctrine",
    "dionysus_as_runtime",
}

REQUIRED_HUMAN_GATES = [
    "operator drill pass acceptance",
    "owner-local assistant posture approval",
    "runtime-owner gate before any service or worker",
    "Tree-of-Sophia review before canon or interpretive intake",
]


class ValidationError(RuntimeError):
    """Raised when the v1.2 service mesh operations contract drifts."""


def fail(message: str) -> None:
    raise ValidationError(message)


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        fail(f"missing JSON file: {path.relative_to(ROOT).as_posix()}")
        raise AssertionError from exc
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT).as_posix()}: {exc}")
        raise AssertionError from exc


def assert_contains_all(text: str, tokens: list[str], surface: str) -> None:
    missing = [token for token in tokens if token not in text]
    if missing:
        fail(f"{surface} missing required tokens: {missing}")


def assert_phrase_present(items: list[str], phrase: str, surface: str) -> None:
    if not any(phrase in item for item in items):
        fail(f"{surface} missing required phrase: {phrase}")


def validate_schema(schema: dict[str, Any], payload: dict[str, Any]) -> None:
    if schema.get("title") != "experience_v1_2_service_mesh_operations_v1":
        fail("schema title must remain experience_v1_2_service_mesh_operations_v1")
    if schema.get("additionalProperties") is not False:
        fail("schema must reject additional top-level properties")
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(payload),
        key=lambda error: list(error.path),
    )
    if errors:
        path = ".".join(str(part) for part in errors[0].path) or "<root>"
        fail(f"service mesh example does not match schema at {path}: {errors[0].message}")


def validate_payload(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    validate_schema(schema, payload)

    if payload["runtime_effect"] != "none":
        fail("runtime_effect must remain none")
    if payload["live_service_activation"] is not False:
        fail("live_service_activation must remain false")

    source = payload["source_seed"]
    if source["archive_name"] != SOURCE_ARCHIVE:
        fail("source_seed.archive_name must preserve the v1.2 archive")
    if source["sha256"] != SOURCE_SHA256:
        fail("source_seed.sha256 must preserve the Dionysus intake checksum")
    if source["claim_limit"] != "archive_readable_not_runtime_ready":
        fail("source_seed.claim_limit must deny runtime readiness")

    if payload["predecessor_surfaces"] != EXPECTED_PREDECESSORS:
        fail("predecessor_surfaces must preserve Dionysus, v1.1, bridge, runtime, and Agon order")
    if payload["primary_offices"] != EXPECTED_PRIMARY_OFFICES:
        fail("primary_offices must preserve the v1.2 primary office contour")
    if payload["prepared_offices"] != EXPECTED_PREPARED_OFFICES:
        fail("prepared_offices must preserve prepared-not-primary offices")

    flow = payload["operations_flow"]
    if [step["order"] for step in flow] != list(range(1, 9)):
        fail("operations_flow orders must be contiguous from 1 to 8")
    if [step["kind"] for step in flow] != EXPECTED_FLOW_KINDS:
        fail("operations_flow kinds must preserve the service mesh operations spine")
    if [step["owner"] for step in flow] != EXPECTED_FLOW_OWNERS:
        fail("operations_flow owners must preserve center and downstream owner routing")
    if [step["authority_note"] for step in flow] != EXPECTED_FLOW_AUTHORITY_NOTES:
        fail("operations_flow authority_note values must preserve the exact no-runtime contract")
    for index, step in enumerate(flow):
        if step.get("stop_lines") != EXPECTED_FLOW_STOP_LINES[index]:
            fail(f"operations_flow[{index}].stop_lines must preserve required stop-lines")
        authority_note = str(step["authority_note"]).lower()
        forbidden_note_tokens = [
            "runtime executes",
            "execute scheduler",
            "activate worker",
            "activate service",
            "open port",
            "certifies drill",
            "passes drill",
            "grants live summon",
            "direct tree-of-sophia write",
            "mutate trust",
            "mutate rank",
            "mutate honor",
            "execute retention",
        ]
        leaked_note = [token for token in forbidden_note_tokens if token in authority_note]
        if leaked_note:
            fail(f"operations_flow[{index}].authority_note grants forbidden authority: {leaked_note}")

    if payload["failure_laws"] != EXPECTED_FAILURE_LAWS:
        fail("failure_laws must preserve the v1.2 non-negotiable laws exactly")

    authority = payload["authority"]
    if authority["contract_effect"] != "center_service_mesh_operations_law_only":
        fail("authority.contract_effect must remain center_service_mesh_operations_law_only")
    if authority["codex_may"] != EXPECTED_CODEX_MAY:
        fail("codex_may must remain the exact bounded allow-list")

    may_text = "\n".join(authority["codex_may"]).lower()
    forbidden_may_tokens = [
        "certify",
        "seal",
        "pass",
        "approve",
        "activate",
        "port",
        "scheduler",
        "worker",
        "daemon",
        "live summon",
        "live verdict",
        "scar",
        "rank",
        "trust",
        "honor",
        "retention",
        "direct tree-of-sophia",
        "write directly to tree-of-sophia",
        "tree-of-sophia",
        "kag canon",
        "tree-of-sophia write",
    ]
    leaked = [token for token in forbidden_may_tokens if token in may_text]
    if leaked:
        fail(f"codex_may grants forbidden service authority: {leaked}")

    for phrase in REQUIRED_CODEX_DENIALS:
        assert_phrase_present(authority["codex_must_not"], phrase, "codex_must_not")
    for phrase in REQUIRED_ASSISTANT_DENIALS:
        assert_phrase_present(authority["assistant_must_not"], phrase, "assistant_must_not")

    derived = set(authority["derived_layers_must_not"])
    if derived != EXPECTED_DERIVED_DENIALS:
        fail("derived_layers_must_not must exactly deny stats, memo, routing, KAG, SDK, runtime, and Dionysus drift")

    for phrase in REQUIRED_HUMAN_GATES:
        assert_phrase_present(authority["human_gates_required"], phrase, "human_gates_required")

    owners = {entry["repo"] for entry in payload["owner_split"]}
    if owners != EXPECTED_OWNER_REPOS:
        fail(f"owner_split repo set mismatch: {sorted(owners)}")

    for entry in payload["owner_split"]:
        if entry["repo"] == "abyss-stack" and "separate runtime-owner gate" not in entry["owns"]:
            fail("abyss-stack owner_split entry must require a separate runtime-owner gate")
        if entry["repo"] == "Tree-of-Sophia" and "direct runtime writes" not in entry["must_not"]:
            fail("Tree-of-Sophia owner_split entry must deny direct runtime writes")
        if entry["repo"] == "aoa-agents" and "self-heal" not in entry["must_not"]:
            fail("aoa-agents owner_split entry must deny assistant self-heal authority")


def validate_files() -> None:
    for path in (DOC_PATH, SCHEMA_PATH, EXAMPLE_PATH):
        if not path.exists():
            fail(f"missing service mesh operations surface: {path.relative_to(ROOT).as_posix()}")

    doc_text = DOC_PATH.read_text(encoding="utf-8")
    assert_contains_all(doc_text, REQUIRED_DOC_TOKENS, "service mesh operations doc")

    schema = read_json(SCHEMA_PATH)
    payload = read_json(EXAMPLE_PATH)
    validate_payload(payload, schema)


def main() -> int:
    validate_files()
    print("ok: Experience v1.2 service mesh operations center contract is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
