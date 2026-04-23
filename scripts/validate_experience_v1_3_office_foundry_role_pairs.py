#!/usr/bin/env python3
"""Validate the Experience v1.3 office foundry role-pairs center contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = ROOT / "docs" / "EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS.md"
SCHEMA_PATH = ROOT / "schemas" / "experience-v1-3-office-foundry-role-pairs.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "experience_v1_3_office_foundry_role_pairs.example.json"

SOURCE_ARCHIVE = "aoa-experience-office-foundry-role-pairs-seed-v1_3.zip"
SOURCE_SHA256 = "d7ccb771f742540fcee0becdbfc79de69c2f97b5704ac067029fec23fef90648"

EXPECTED_PREDECESSORS = [
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.md",
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.map.yaml",
    "docs/EXPERIENCE_WAVE5_SOVEREIGN_OFFICE.md",
    "docs/EXPERIENCE_V1_1_LIVE_OFFICE_EXPANSION.md",
    "docs/EXPERIENCE_SERVICE_MESH_LAW.md",
    "docs/EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md",
    "docs/EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md",
    "docs/EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md",
    "docs/AGON_PRE_PROTOCOL_STOP_LINES.md",
]

EXPECTED_EXISTING_SERVICE_OFFICES = [
    "notary.assistant",
    "concierge.assistant",
    "courier.assistant",
    "monitor.assistant",
]

EXPECTED_EXPANDED_SERVICE_OFFICES = [
    "librarian.assistant",
    "steward.assistant",
    "scheduler.assistant",
]

EXPECTED_ROLE_PAIRS = [
    {
        "office": "verifier",
        "assistant": "verifier.assistant",
        "agonic": "verifier.agonic",
        "hybrid_allowed": False,
        "handoff_contract_required": True,
        "scar_authority": "none_from_center",
    },
    {
        "office": "chronicler",
        "assistant": "chronicler.assistant",
        "agonic": "chronicler.agonic",
        "hybrid_allowed": False,
        "handoff_contract_required": True,
        "scar_authority": "none_from_center",
    },
    {
        "office": "librarian",
        "assistant": "librarian.assistant",
        "agonic": "librarian.agonic",
        "hybrid_allowed": False,
        "handoff_contract_required": True,
        "scar_authority": "none_from_center",
    },
]

EXPECTED_KIND_SPLIT_LAW = [
    "office_names_the_work",
    "kind_names_the_mode_of_becoming",
    "assistant_becomes_by_governed_release",
    "agonic_becomes_by_owner_local_trial_law",
    "no_artifact_may_launder_one_path_through_the_other",
]

EXPECTED_FLOW_KINDS = [
    "source_seed_received",
    "service_mesh_predecessor_checked",
    "office_cast_expansion_declared",
    "role_pair_kind_split_declared",
    "pair_handoff_contract_requested",
    "no_hybrid_guard_evaluated",
    "memory_and_lineage_gate_requested",
    "owner_landing_or_recharter_request_declared",
]

EXPECTED_FLOW_OWNERS = [
    "Agents-of-Abyss",
    "Agents-of-Abyss",
    "aoa-agents",
    "aoa-agents",
    "aoa-routing",
    "aoa-evals",
    "aoa-memo",
    "Agents-of-Abyss",
]

EXPECTED_FLOW_AUTHORITY_NOTES = [
    "Dionysus archive is transport evidence; center may name the contract only",
    "v1.2 service mesh operations remains the predecessor; no runtime activation follows from this check",
    "expanded service offices are owner-local posture requests, not hidden office promotion",
    "assistant and agonic embodiments stay separate; one actor may not hold both runtime kinds",
    "routing may request explicit pair handoff packets; routing does not define office meaning",
    "evals may record no-hybrid evidence; they do not approve pairs or certify release",
    "memory may preserve reviewed lineage candidates only after owner review",
    "material foundry changes return to owner-local landing or human recharter as requests",
]

EXPECTED_FLOW_STOP_LINES = [
    ["no raw archive replay", "no owner truth import"],
    ["no service activation", "no scheduler runtime loop"],
    ["no hidden office promotion", "no assistant self-enroll"],
    ["no hybrid runtime mask", "no cross-kind memory leak"],
    ["no routing meaning theft", "no live service-to-Agon summon"],
    ["no Codex pair approval", "no scar rank honor or retention mutation"],
    ["memo is not truth", "KAG is not canon"],
    ["no automatic recharter", "no direct Tree-of-Sophia runtime write"],
]

EXPECTED_HARD_GUARDS = [
    "no_hybrid_agent",
    "no_assistant_self_recharter",
    "no_assistant_scar_write",
    "no_agonic_release_disguised_as_assistant_version",
    "no_cross_kind_memory_leak",
    "no_direct_tree_of_sophia_runtime_write",
    "no_kag_forced_uptake",
    "no_routing_meaning_theft",
    "no_codex_pair_approval",
    "no_runtime_pair_activation",
]

EXPECTED_BLOCKING_CONTRACTS = {
    "actor_identity": {
        "same_actor_id_cross_kind_allowed": False,
        "kind_required_on_pair_seeds": True,
        "assistant_id_must_differ_from_agonic_id": True,
    },
    "activation_state": {
        "allowed_landing_states": [
            "draft",
            "proposed",
            "reviewed",
            "blocked",
            "quarantined",
            "candidate_only",
        ],
        "active_allowed_during_landing": False,
    },
    "recharter": {
        "allowed_requesters": [
            "operator",
            "council",
            "repo_owner",
        ],
        "blocked_requesters": [
            "assistant",
            "codex",
            "runtime",
            "scheduler",
            "office",
            "derived_layer",
        ],
        "review_required": True,
    },
    "scar_rank_retention": {
        "candidate_only_required": True,
        "durable_write_allowed": False,
        "scheduler_action_allowed": False,
    },
    "tos_boundary": {
        "runtime_write_allowed": False,
        "direct_node_path_allowed": False,
        "canon_write_allowed": False,
    },
    "routing_boundary": {
        "advisory_only": True,
        "meaning_definition_allowed": False,
        "live_agonic_activation_allowed": False,
    },
    "eval_boundary": {
        "bounded_verdict_only": True,
        "may_grant_scar_rank_closure": False,
    },
    "archive_consistency": {
        "fixture_generated_result_disagreement_allowed": False,
        "missing_handoff_contract_must_block": True,
    },
}

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

EXPECTED_OWNER_SPLIT = [
    {
        "repo": "Agents-of-Abyss",
        "owns": "center office foundry role-pair law source bridge foundry flow and authority stop-lines",
        "must_not": "replace owner-local repository truth",
    },
    {
        "repo": "aoa-agents",
        "owns": "assistant and agonic office posture no-hybrid actor contracts pair profiles and recharter runbooks after owner-local landing",
        "must_not": "grant hybrid actor masks assistant self-recharter self-release self-enroll self-certify or scar authority",
    },
    {
        "repo": "aoa-evals",
        "owns": "bounded pair verdict bundles no-hybrid checks regression checks and trial verdict models",
        "must_not": "certify release approve office pairs or become pair authority",
    },
    {
        "repo": "aoa-playbooks",
        "owns": "office foundry runbooks pair certification playbooks pair trial playbooks and recharter scenarios",
        "must_not": "execute runtime trials or scheduler loops",
    },
    {
        "repo": "aoa-memo",
        "owns": "reviewed lineage memories revision ledger candidates and retention readiness",
        "must_not": "make memory truth write scars or execute retention",
    },
    {
        "repo": "aoa-stats",
        "owns": "derived office foundry dashboards hybrid-risk summaries and pair handoff health views",
        "must_not": "become proof pair judgment or certification authority",
    },
    {
        "repo": "aoa-routing",
        "owns": "advisory pair routes explicit handoff candidates and service-to-Agon escalation hints",
        "must_not": "define office meaning become owner or grant live summon authority",
    },
    {
        "repo": "aoa-sdk",
        "owns": "typed helper calls kind-safe projections and pair lookup contracts",
        "must_not": "become runtime or semantic authority",
    },
    {
        "repo": "aoa-kag",
        "owns": "derived pair pattern candidates and lineage pattern nodes",
        "must_not": "become canon or force uptake into Tree-of-Sophia",
    },
    {
        "repo": "abyss-stack",
        "owns": "runtime activation storage guard events and workers only after a separate runtime-owner gate",
        "must_not": "activate runtime from this center landing",
    },
    {
        "repo": "Tree-of-Sophia",
        "owns": "canon and interpretive review through its own path",
        "must_not": "receive direct runtime writes",
    },
    {
        "repo": "Dionysus",
        "owns": "source lineage staged intake and later harvest trace",
        "must_not": "become runtime or owner doctrine",
    },
    {
        "repo": "8Dionysus",
        "owns": "shared-root projection law where workspace projection surfaces are affected",
        "must_not": "absorb office foundry truth",
    },
    {
        "repo": "aoa-skills",
        "owns": "bounded execution workflows extracted from owner-accepted patterns",
        "must_not": "grant pair approval release scar rank retention or runtime authority",
    },
    {
        "repo": "aoa-techniques",
        "owns": "reusable engineering practice extracted from owner-accepted patterns",
        "must_not": "grant runtime canon pair or scar authority",
    },
]

REQUIRED_DOC_TOKENS = [
    "It is Wave 3 of the current v1.2-v2.0 planting campaign",
    "It is not `Experience Wave 3`",
    "`aoa-experience-office-foundry-role-pairs-seed-v1_3.zip`",
    SOURCE_SHA256,
    "`EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md`",
    "`EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md`",
    "`AGON_PRE_PROTOCOL_STOP_LINES.md`",
    "office names the work",
    "kind names the mode of becoming",
    "`no_hybrid_agent`",
    "`no_assistant_self_recharter`",
    "`no_codex_pair_approval`",
    "hybrid runtime mask",
    "`active` is not a landing state",
    "durable writes are forbidden",
    "fixture/generated-result disagreement is a validation failure",
    "stats become proof",
    "memo become truth",
    "routing become owner",
    "KAG become canon",
    "SDK become authority",
    "evals become certification authority",
]

REQUIRED_CODEX_DENIALS = [
    "approve office pair",
    "activate office pair",
    "certify release or trial",
    "self-recharter assistant",
    "grant agonic scar write",
    "mutate rank trust honor or retention",
    "write directly to Tree-of-Sophia",
    "promote KAG patterns to canon",
    "route meaning as owner",
    "open runtime services ports schedulers workers or daemons",
    "copy raw archive proposals into owner truth",
]

EXPECTED_CODEX_MAY = [
    "simulate foundry checks",
    "collect evidence",
    "propose owner-local requests",
    "run validators",
    "prepare kind-split review packets",
]

REQUIRED_ASSISTANT_DENIALS = [
    "self-recharter",
    "self-release",
    "self-enroll",
    "self-certify",
    "hold assistant and agonic runtime kinds",
    "write scars",
    "mutate rank trust honor or retention",
    "leak memory across kinds",
    "write directly to Tree-of-Sophia",
]

EXPECTED_DERIVED_DENIALS = {
    "stats_as_proof",
    "memo_as_truth",
    "routing_as_owner",
    "kag_as_canon",
    "sdk_as_authority",
    "evals_as_certifier",
    "runtime_as_doctrine",
    "dionysus_as_runtime",
}

REQUIRED_HUMAN_GATES = [
    "operator office expansion acceptance",
    "owner-local assistant posture approval",
    "agonic owner trial approval before scars rank or retention",
    "runtime-owner gate before any service scheduler pair or worker activation",
    "Tree-of-Sophia review before canon or interpretive intake",
]


class ValidationError(RuntimeError):
    """Raised when the v1.3 office foundry role-pairs contract drifts."""


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
    if schema.get("title") != "experience_v1_3_office_foundry_role_pairs_v1":
        fail("schema title must remain experience_v1_3_office_foundry_role_pairs_v1")
    if schema.get("additionalProperties") is not False:
        fail("schema must reject additional top-level properties")
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(payload),
        key=lambda error: list(error.path),
    )
    if errors:
        path = ".".join(str(part) for part in errors[0].path) or "<root>"
        fail(f"office foundry example does not match schema at {path}: {errors[0].message}")


def validate_payload(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    validate_schema(schema, payload)

    if payload["runtime_effect"] != "none":
        fail("runtime_effect must remain none")
    if payload["live_runtime_activation"] is not False:
        fail("live_runtime_activation must remain false")

    source = payload["source_seed"]
    if source["archive_name"] != SOURCE_ARCHIVE:
        fail("source_seed.archive_name must preserve the v1.3 archive")
    if source["sha256"] != SOURCE_SHA256:
        fail("source_seed.sha256 must preserve the Dionysus intake checksum")
    if source["claim_limit"] != "archive_readable_not_owner_ready":
        fail("source_seed.claim_limit must deny owner readiness")

    if payload["predecessor_surfaces"] != EXPECTED_PREDECESSORS:
        fail("predecessor_surfaces must preserve Dionysus, v1.2, runtime, and Agon order")
    if payload["existing_service_offices"] != EXPECTED_EXISTING_SERVICE_OFFICES:
        fail("existing_service_offices must preserve the pre-v1.3 service offices")
    if payload["expanded_service_offices"] != EXPECTED_EXPANDED_SERVICE_OFFICES:
        fail("expanded_service_offices must preserve the first expanded service offices")
    if payload["role_pairs"] != EXPECTED_ROLE_PAIRS:
        fail("role_pairs must preserve exact no-hybrid role-pair contour")
    if payload["kind_split_law"] != EXPECTED_KIND_SPLIT_LAW:
        fail("kind_split_law must preserve exact office/kind split law")

    flow = payload["foundry_flow"]
    if [step["order"] for step in flow] != list(range(1, 9)):
        fail("foundry_flow orders must be contiguous from 1 to 8")
    if [step["kind"] for step in flow] != EXPECTED_FLOW_KINDS:
        fail("foundry_flow kinds must preserve the office foundry spine")
    if [step["owner"] for step in flow] != EXPECTED_FLOW_OWNERS:
        fail("foundry_flow owners must preserve center and downstream owner routing")
    if [step["authority_note"] for step in flow] != EXPECTED_FLOW_AUTHORITY_NOTES:
        fail("foundry_flow authority_note values must preserve the exact no-hybrid contract")
    for index, step in enumerate(flow):
        if step.get("stop_lines") != EXPECTED_FLOW_STOP_LINES[index]:
            fail(f"foundry_flow[{index}].stop_lines must preserve required stop-lines")
        authority_note = str(step["authority_note"]).lower()
        forbidden_note_tokens = [
            "runtime activation is allowed",
            "activate runtime",
            "activate service",
            "scheduler loop may run",
            "hybrid may run",
            "hybrid runtime allowed",
            "codex approves",
            "codex certifies",
            "grants scar",
            "write scar",
            "mutate rank",
            "mutate honor",
            "execute retention",
            "direct tree-of-sophia write",
            "routing owns meaning",
            "kag canon",
        ]
        leaked_note = [token for token in forbidden_note_tokens if token in authority_note]
        if leaked_note:
            fail(f"foundry_flow[{index}].authority_note grants forbidden authority: {leaked_note}")

    if payload["hard_guards"] != EXPECTED_HARD_GUARDS:
        fail("hard_guards must preserve the v1.3 non-negotiable guard order exactly")
    if payload["blocking_contracts"] != EXPECTED_BLOCKING_CONTRACTS:
        fail("blocking_contracts must preserve exact no-runtime, no-scar, no-hybrid guard contracts")

    authority = payload["authority"]
    if authority["contract_effect"] != "center_office_foundry_role_pairs_law_only":
        fail("authority.contract_effect must remain center_office_foundry_role_pairs_law_only")
    if authority["codex_may"] != EXPECTED_CODEX_MAY:
        fail("codex_may must remain the exact bounded allow-list")

    may_text = "\n".join(authority["codex_may"]).lower()
    forbidden_may_tokens = [
        "approve",
        "activate",
        "certify",
        "seal",
        "release",
        "trial",
        "scar",
        "rank",
        "trust",
        "honor",
        "retention",
        "tree-of-sophia",
        "kag canon",
        "routing meaning",
        "runtime",
        "port",
        "scheduler",
        "worker",
        "daemon",
        "hybrid",
        "self-recharter",
    ]
    leaked = [token for token in forbidden_may_tokens if token in may_text]
    if leaked:
        fail(f"codex_may grants forbidden office foundry authority: {leaked}")

    for phrase in REQUIRED_CODEX_DENIALS:
        assert_phrase_present(authority["codex_must_not"], phrase, "codex_must_not")
    for phrase in REQUIRED_ASSISTANT_DENIALS:
        assert_phrase_present(authority["assistant_must_not"], phrase, "assistant_must_not")

    derived = set(authority["derived_layers_must_not"])
    if derived != EXPECTED_DERIVED_DENIALS:
        fail("derived_layers_must_not must exactly deny stats, memo, routing, KAG, SDK, evals, runtime, and Dionysus drift")

    for phrase in REQUIRED_HUMAN_GATES:
        assert_phrase_present(authority["human_gates_required"], phrase, "human_gates_required")

    owners = {entry["repo"] for entry in payload["owner_split"]}
    if owners != EXPECTED_OWNER_REPOS:
        fail(f"owner_split repo set mismatch: {sorted(owners)}")
    if payload["owner_split"] != EXPECTED_OWNER_SPLIT:
        fail("owner_split must preserve exact owner responsibilities and authority denials")

    for entry in payload["owner_split"]:
        if entry["repo"] == "aoa-agents" and "hybrid actor masks" not in entry["must_not"]:
            fail("aoa-agents owner_split entry must deny hybrid actor masks")
        if entry["repo"] == "aoa-evals" and "certify release" not in entry["must_not"]:
            fail("aoa-evals owner_split entry must deny certification authority")
        if entry["repo"] == "aoa-routing" and "define office meaning" not in entry["must_not"]:
            fail("aoa-routing owner_split entry must deny meaning ownership")
        if entry["repo"] == "abyss-stack" and "separate runtime-owner gate" not in entry["owns"]:
            fail("abyss-stack owner_split entry must require a separate runtime-owner gate")
        if entry["repo"] == "Tree-of-Sophia" and "direct runtime writes" not in entry["must_not"]:
            fail("Tree-of-Sophia owner_split entry must deny direct runtime writes")


def validate_files() -> None:
    for path in (DOC_PATH, SCHEMA_PATH, EXAMPLE_PATH):
        if not path.exists():
            fail(f"missing office foundry role-pairs surface: {path.relative_to(ROOT).as_posix()}")

    doc_text = DOC_PATH.read_text(encoding="utf-8")
    assert_contains_all(doc_text, REQUIRED_DOC_TOKENS, "office foundry role-pairs doc")

    schema = read_json(SCHEMA_PATH)
    payload = read_json(EXAMPLE_PATH)
    validate_payload(payload, schema)


def main() -> int:
    validate_files()
    print("ok: Experience v1.3 office foundry role-pairs center contract is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
