#!/usr/bin/env python3
"""Validate the Experience v1.4 mechanical arena kernel center contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL.md"
SCHEMA_PATH = (
    ROOT
    / "schemas"
    / "experience-v1-4-agonic-pair-trials-mechanical-arena-kernel.schema.json"
)
EXAMPLE_PATH = (
    ROOT
    / "examples"
    / "experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.example.json"
)

SOURCE_ARCHIVE = "aoa-experience-agonic-pair-trials-mechanical-arena-kernel-seed-v1_4.zip"
SOURCE_SHA256 = "c62a9c38b662ad7c62405c7ca2ac75fe5ea7cc05f13e001a141ad60cf2f5f404"

EXPECTED_PREDECESSORS = [
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.md",
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.map.yaml",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS.md",
    "mechanics/agon/docs/AGON_ARENA_SESSION_MODEL.md",
    "mechanics/agon/docs/AGON_CHARTER_AND_SEAT_MODEL.md",
    "mechanics/agon/docs/AGON_SEALED_COMMIT_MODEL.md",
    "mechanics/agon/docs/AGON_STATE_PACKET_MODEL.md",
    "mechanics/agon/docs/AGON_CONTRADICTION_CLOSURE_SUMMON_LAW.md",
    "mechanics/agon/docs/AGON_VERDICT_DELTA_SCAR_BRIDGE.md",
    "mechanics/agon/docs/AGON_DUEL_KERNEL_MODEL.md",
    "mechanics/agon/docs/AGON_MECHANICAL_TRIALS_OVER_DUEL_KERNEL.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md",
    "mechanics/agon/docs/AGON_PRE_PROTOCOL_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE12_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE13_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE14_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE15_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE16_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE17_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE18_STOP_LINES.md",
]

EXPECTED_ARENA_KERNEL_LAW = [
    "no_arena_without_charter",
    "no_contestant_without_agonic_kind",
    "no_stance_without_sealed_commit",
    "no_closure_without_trace",
    "no_closure_over_material_open_contradiction",
    "no_summon_without_visible_request_and_cost",
    "no_scar_without_verdict_and_retention",
    "no_direct_tree_of_sophia_write",
    "assistants_may_serve_not_secretly_become_contestants",
]

EXPECTED_FIRST_PAIR_TRIALS = [
    {
        "office": "verifier",
        "assistant_form": "verifier.assistant",
        "agonic_form": "verifier.agonic",
        "trial_kind": "mechanical_duel",
        "assistant_authority": "proof_floor_witness_only",
        "agonic_authority": "contest_evidence_or_closure_only_after_owner_local_trial_gate",
        "witness_requirements": [
            "notary.assistant",
            "chronicler.assistant",
        ],
        "live_enrollment": False,
        "scar_authority": "none_from_center",
    },
    {
        "office": "chronicler",
        "assistant_form": "chronicler.assistant",
        "agonic_form": "chronicler.agonic",
        "trial_kind": "mechanical_duel",
        "assistant_authority": "record_and_format_scar_packet_only",
        "agonic_authority": "contest_rupture_or_biography_only_after_owner_local_trial_gate",
        "witness_requirements": [
            "notary.assistant",
            "verifier.assistant",
        ],
        "live_enrollment": False,
        "scar_authority": "none_from_center",
    },
    {
        "office": "librarian",
        "assistant_form": "librarian.assistant",
        "agonic_form": "librarian.agonic",
        "trial_kind": "mechanical_duel",
        "assistant_authority": "source_carrier_and_dossier_packager_only",
        "agonic_authority": "contest_reading_or_canonical_risk_only_after_owner_local_trial_gate",
        "witness_requirements": [
            "notary.assistant",
            "chronicler.assistant",
        ],
        "live_enrollment": False,
        "scar_authority": "none_from_center",
    },
]

EXPECTED_FLOW_KINDS = [
    "source_seed_received",
    "role_pair_predecessor_checked",
    "arena_charter_requested",
    "contestant_eligibility_checked",
    "service_witness_seats_declared",
    "sealed_stance_commit_required",
    "contradiction_ledger_required",
    "summon_cost_gate_required",
    "lawful_closure_gate_required",
    "delta_receipt_requested",
    "scar_retention_bridge_requested",
    "owner_landing_or_recharter_request_declared",
]

EXPECTED_FLOW_OWNERS = [
    "Agents-of-Abyss",
    "Agents-of-Abyss",
    "Agents-of-Abyss",
    "aoa-agents",
    "aoa-agents",
    "aoa-evals",
    "aoa-evals",
    "aoa-routing",
    "aoa-evals",
    "aoa-memo",
    "aoa-memo",
    "Agents-of-Abyss",
]

EXPECTED_FLOW_STOP_LINES = [
    ["no raw archive replay", "no generated clean-flow promotion"],
    ["no pair certification", "no live enrollment"],
    ["no arena without charter", "no center-created live arena"],
    ["no assistant contestant", "no hybrid contestant mask"],
    ["no assistant judge", "no assistant scar writer"],
    ["no unsealed stance", "no posthoc commit edit"],
    ["no closure over material open contradiction", "no false success"],
    ["no hidden summon", "no routing summon authority"],
    ["no Codex verdict", "no eval certification authority"],
    ["no learning claim without delta receipt", "memo is not truth"],
    ["no durable scar write", "no retention execution"],
    ["no runtime storage activation", "no direct Tree-of-Sophia write"],
]

EXPECTED_HARD_GUARDS = [
    "no_live_arena_activation",
    "no_assistant_contestant",
    "no_hidden_summon",
    "no_posthoc_stance_tamper",
    "no_closure_without_trace",
    "no_closure_over_material_open_contradiction",
    "no_codex_arena_verdict",
    "no_scar_without_retention",
    "no_durable_scar_or_retention_write",
    "no_rank_or_honor_mutation",
    "no_direct_tree_of_sophia_write",
    "no_runtime_storage_or_worker_activation",
]

EXPECTED_BLOCKING_CONTRACTS = {
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
        "live_arena_allowed": False,
        "live_runtime_allowed": False,
    },
    "contestant_eligibility": {
        "primary_contestant_kinds": [
            "agonic",
        ],
        "assistant_primary_contestant_allowed": False,
        "same_actor_service_and_contestant_allowed": False,
        "two_contestant_duel_only": True,
        "third_permanent_contestant_allowed": False,
    },
    "witness_contract": {
        "service_witness_required": True,
        "assistant_service_witness_allowed": True,
        "assistant_judge_allowed": False,
        "assistant_scar_writer_allowed": False,
        "assistant_retention_executor_allowed": False,
    },
    "stance_integrity": {
        "sealed_commit_required": True,
        "reveal_must_match_commit_hash": True,
        "posthoc_commit_edit_allowed": False,
    },
    "closure_contract": {
        "trace_required": True,
        "material_open_contradiction_blocks_closure": True,
        "closure_without_trace_allowed": False,
        "unresolved_protocol_breach_blocks_closure": True,
        "false_success_allowed": False,
    },
    "summon_economy": {
        "visible_summon_request_required": True,
        "summon_cost_required": True,
        "hidden_summon_allowed": False,
        "codex_summon_authority_allowed": False,
        "routing_summon_authority_allowed": False,
    },
    "verdict_boundary": {
        "allowed_issuer_kinds": [
            "evaluator",
            "operator",
            "council",
        ],
        "codex_verdict_allowed": False,
        "assistant_verdict_allowed": False,
        "runtime_verdict_allowed": False,
        "verdict_may_grant_scar_rank_retention": False,
    },
    "scar_retention": {
        "scar_candidate_only_required": True,
        "retention_schedule_candidate_only_required": True,
        "durable_scar_write_allowed": False,
        "retention_execution_allowed": False,
        "rank_mutation_allowed": False,
        "honor_mutation_allowed": False,
    },
    "tos_boundary": {
        "runtime_write_allowed": False,
        "direct_node_path_allowed": False,
        "canon_write_allowed": False,
        "dossier_candidate_only": True,
    },
    "runtime_storage": {
        "runtime_worker_activation_allowed": False,
        "storage_record_authoritative": False,
        "host_port_open_allowed": False,
        "scheduler_loop_allowed": False,
        "deployment_daemon_allowed": False,
    },
    "archive_consistency": {
        "clean_flow_may_inform_contract": True,
        "raw_generated_output_copied_as_truth": False,
        "fixture_generated_result_disagreement_allowed": False,
        "archive_pycache_allowed_in_owner_repo": False,
    },
}

EXPECTED_CODEX_MAY = [
    "simulate mechanical arena contract checks",
    "collect seed dry-run evidence",
    "propose owner-local arena requests",
    "run validators",
    "prepare contestant eligibility review packets",
]

REQUIRED_CODEX_DENIALS = [
    "activate live arena",
    "activate runtime storage",
    "issue arena verdict",
    "certify trial success",
    "enroll assistant as contestant",
    "grant summon authority",
    "write durable scar",
    "execute retention",
    "mutate rank or honor",
    "write directly to Tree-of-Sophia",
    "promote generated clean-flow output to owner truth",
    "copy raw archive proposals into owner truth",
]

REQUIRED_ASSISTANT_DENIALS = [
    "become primary contestant",
    "become judge",
    "issue verdict",
    "perform hidden summon",
    "write scars",
    "execute retention",
    "mutate rank or honor",
    "write directly to Tree-of-Sophia",
    "self-enroll into agonic trial",
]

EXPECTED_DERIVED_DENIALS = {
    "stats_as_proof",
    "memo_as_truth",
    "routing_as_owner",
    "kag_as_canon",
    "sdk_as_authority",
    "evals_as_live_verdict_authority",
    "playbooks_as_runtime",
    "runtime_as_doctrine",
    "dionysus_as_runtime",
}

REQUIRED_HUMAN_GATES = [
    "operator arena-kernel acceptance",
    "owner-local contestant eligibility approval",
    "owner-local eval approval before verdict bundle use",
    "owner-local memo approval before scar or retention intake",
    "runtime-owner gate before storage workers ports schedulers services or daemons",
    "Tree-of-Sophia review before canon or interpretive intake",
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

EXPECTED_OWNER_SPLIT = [
    {
        "repo": "Agents-of-Abyss",
        "owns": "center mechanical arena kernel law source bridge flow hard guards and authority stop-lines",
        "must_not": "replace owner-local arena role proof memory routing runtime or ToS truth",
    },
    {
        "repo": "aoa-agents",
        "owns": "contestant eligibility assistant witness boundaries agonic role posture and pair-trial actor profiles after owner-local landing",
        "must_not": "grant assistant contestant judge scar writer retention executor hidden summon or hybrid mask authority",
    },
    {
        "repo": "aoa-evals",
        "owns": "bounded verdict bundles stance-integrity checks contradiction-ledger checks summon-economy checks and scar-worthiness evals",
        "must_not": "issue live arena verdicts certify trials grant scars mutate rank or execute retention",
    },
    {
        "repo": "aoa-playbooks",
        "owns": "recurring mechanical trial choreography expected evidence fallback posture and owner-review run routes",
        "must_not": "execute live arena sessions become runtime or grant verdict scar rank or retention authority",
    },
    {
        "repo": "aoa-memo",
        "owns": "scar memory writeback gates retention review candidates delta receipt intake and biography boundaries",
        "must_not": "make memory truth write durable scars execute retention or grant future behavior rights",
    },
    {
        "repo": "aoa-stats",
        "owns": "derived arena dashboards summon economy metrics and mechanical agon rollups",
        "must_not": "become proof score verdict rank honor or quest authority",
    },
    {
        "repo": "aoa-routing",
        "owns": "advisory arena-entry contested-closure and service-to-Agon escalation gate candidates",
        "must_not": "open live gates own meaning grant summon authority or dispatch runtime arena sessions",
    },
    {
        "repo": "aoa-sdk",
        "owns": "typed packet helpers API contracts validation helpers and control-plane seams only",
        "must_not": "become semantic runtime verdict scar retention or storage authority",
    },
    {
        "repo": "aoa-kag",
        "owns": "derived arena pattern candidates only",
        "must_not": "become canon force Tree-of-Sophia uptake or claim arena truth",
    },
    {
        "repo": "aoa-skills",
        "owns": "bounded arena-adjacent workflows extracted from owner-accepted patterns",
        "must_not": "grant live move verdict summon scar rank retention or runtime authority",
    },
    {
        "repo": "aoa-techniques",
        "owns": "reusable contradiction analysis stance commit and trace reconstruction practice after owner acceptance",
        "must_not": "grant live arena canon verdict scar rank retention or runtime authority",
    },
    {
        "repo": "abyss-stack",
        "owns": "runtime storage workers deployment ports services and session persistence only after a separate runtime-owner gate",
        "must_not": "activate runtime from this center landing",
    },
    {
        "repo": "Tree-of-Sophia",
        "owns": "canon and interpretive review through its own path",
        "must_not": "receive direct runtime writes node paths canon writes or unreviewed arena dossiers",
    },
    {
        "repo": "Dionysus",
        "owns": "source lineage staged intake and later harvest trace",
        "must_not": "become runtime owner doctrine or live arena source of truth",
    },
    {
        "repo": "8Dionysus",
        "owns": "shared-root projection law where workspace projection surfaces are affected",
        "must_not": "absorb mechanical arena truth",
    },
]

EXPECTED_QUARANTINED_SURFACES = [
    "archive-local generated/mechanical_arena_clean_flow runtime-like examples",
    "archive-local generated scar_write and retention_schedule artifacts",
    "archive-local repo/* owner proposals outside this center contract",
    "archive-local __pycache__ files",
    "archive-local runtime storage records and dashboard outputs",
]

EXPECTED_SEED_EVIDENCE = {
    "archive_integrity": "unzip_t_passed",
    "schema_example_pairs": 33,
    "json_files": 108,
    "seed_tests_passed": 16,
    "claim_limit": "dry_run_only_not_owner_readiness",
}

REQUIRED_DOC_TOKENS = [
    "It is Wave 4 of the current v1.2-v2.0 planting campaign",
    "It is not `Experience Wave 4`",
    f"`{SOURCE_ARCHIVE}`",
    SOURCE_SHA256,
    "`EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS.md`",
    "`AGON_ARENA_SESSION_MODEL.md`",
    "`AGON_DUEL_KERNEL_MODEL.md`",
    "`AGON_MECHANICAL_TRIALS_OVER_DUEL_KERNEL.md`",
    "Current Agon arena, packet, verdict, duel-kernel, and mechanical-trial surfaces",
    "No arena without charter",
    "No contestant without agonic kind",
    "No stance without sealed commit",
    "No summon without visible request and cost",
    "`no_live_arena_activation`",
    "`no_assistant_contestant`",
    "`no_codex_arena_verdict`",
    "`active` is not a landing state",
    "generated clean-flow examples may inform checks",
    "stats become proof",
    "memo become truth",
    "routing become owner",
    "KAG become canon",
    "SDK become authority",
    "evals become live verdict authority",
]


class ValidationError(RuntimeError):
    """Raised when the v1.4 mechanical arena kernel contract drifts."""


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
    if schema.get("title") != "experience_v1_4_agonic_pair_trials_mechanical_arena_kernel_v1":
        fail("schema title must remain experience_v1_4_agonic_pair_trials_mechanical_arena_kernel_v1")
    if schema.get("additionalProperties") is not False:
        fail("schema must reject additional top-level properties")
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(payload),
        key=lambda error: list(error.path),
    )
    if errors:
        path = ".".join(str(part) for part in errors[0].path) or "<root>"
        fail(f"mechanical arena example does not match schema at {path}: {errors[0].message}")


def validate_payload(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    validate_schema(schema, payload)

    if payload["runtime_effect"] != "none":
        fail("runtime_effect must remain none")
    if payload["live_arena_activation"] is not False:
        fail("live_arena_activation must remain false")
    if payload["live_runtime_activation"] is not False:
        fail("live_runtime_activation must remain false")

    source = payload["source_seed"]
    if source["archive_name"] != SOURCE_ARCHIVE:
        fail("source_seed.archive_name must preserve the v1.4 archive")
    if source["sha256"] != SOURCE_SHA256:
        fail("source_seed.sha256 must preserve the Dionysus intake checksum")
    if source["claim_limit"] != "archive_readable_not_owner_ready":
        fail("source_seed.claim_limit must deny owner readiness")

    if payload["predecessor_surfaces"] != EXPECTED_PREDECESSORS:
        fail("predecessor_surfaces must preserve Dionysus, v1.2, v1.3, current Agon law, runtime, and stop-line order")
    if payload["arena_kernel_law"] != EXPECTED_ARENA_KERNEL_LAW:
        fail("arena_kernel_law must preserve the exact mechanical arena law")
    if payload["first_pair_trials"] != EXPECTED_FIRST_PAIR_TRIALS:
        fail("first_pair_trials must preserve assistant witness plus agonic contestant split")

    flow = payload["kernel_flow"]
    if [step["order"] for step in flow] != list(range(1, 13)):
        fail("kernel_flow orders must be contiguous from 1 to 12")
    if [step["kind"] for step in flow] != EXPECTED_FLOW_KINDS:
        fail("kernel_flow kinds must preserve the mechanical arena spine")
    if [step["owner"] for step in flow] != EXPECTED_FLOW_OWNERS:
        fail("kernel_flow owners must preserve center and downstream owner routing")
    for index, step in enumerate(flow):
        if step.get("stop_lines") != EXPECTED_FLOW_STOP_LINES[index]:
            fail(f"kernel_flow[{index}].stop_lines must preserve required stop-lines")
        authority_note = str(step["authority_note"]).lower()
        forbidden_note_tokens = [
            "live arena may run",
            "activate runtime",
            "may issue live verdict",
            "can issue live verdict",
            "issue live verdict allowed",
            "live verdict allowed",
            "codex verdict allowed",
            "assistant may judge",
            "assistant may contest",
            "hidden summon allowed",
            "durable scar write",
            "execute retention",
            "mutate rank",
            "mutate honor",
            "direct tree-of-sophia write",
            "routing owns meaning",
            "kag canon",
            "generated output becomes truth",
        ]
        leaked_note = [token for token in forbidden_note_tokens if token in authority_note]
        if leaked_note:
            fail(f"kernel_flow[{index}].authority_note grants forbidden authority: {leaked_note}")

    if payload["hard_guards"] != EXPECTED_HARD_GUARDS:
        fail("hard_guards must preserve the v1.4 non-negotiable guard order exactly")
    if payload["blocking_contracts"] != EXPECTED_BLOCKING_CONTRACTS:
        fail("blocking_contracts must preserve exact no-live-arena and no-durable-write contracts")

    authority = payload["authority"]
    if authority["contract_effect"] != "center_mechanical_arena_kernel_law_only":
        fail("authority.contract_effect must remain center_mechanical_arena_kernel_law_only")
    if authority["codex_may"] != EXPECTED_CODEX_MAY:
        fail("codex_may must remain the exact bounded allow-list")

    may_text = "\n".join(authority["codex_may"]).lower()
    forbidden_may_tokens = [
        "activate",
        "live",
        "verdict",
        "certify",
        "enroll",
        "assistant contestant",
        "scar",
        "retention",
        "rank",
        "honor",
        "tree-of-sophia",
        "generated",
        "copy raw",
        "runtime",
        "storage",
        "summon authority",
        "port",
        "scheduler",
        "worker",
        "daemon",
    ]
    leaked = [token for token in forbidden_may_tokens if token in may_text]
    if leaked:
        fail(f"codex_may grants forbidden mechanical arena authority: {leaked}")

    for phrase in REQUIRED_CODEX_DENIALS:
        assert_phrase_present(authority["codex_must_not"], phrase, "codex_must_not")
    for phrase in REQUIRED_ASSISTANT_DENIALS:
        assert_phrase_present(authority["assistant_must_not"], phrase, "assistant_must_not")

    derived = set(authority["derived_layers_must_not"])
    if derived != EXPECTED_DERIVED_DENIALS:
        fail("derived_layers_must_not must exactly deny stats, memo, routing, KAG, SDK, evals, playbooks, runtime, and Dionysus drift")

    for phrase in REQUIRED_HUMAN_GATES:
        assert_phrase_present(authority["human_gates_required"], phrase, "human_gates_required")

    owners = {entry["repo"] for entry in payload["owner_split"]}
    if owners != EXPECTED_OWNER_REPOS:
        fail(f"owner_split repo set mismatch: {sorted(owners)}")
    if payload["owner_split"] != EXPECTED_OWNER_SPLIT:
        fail("owner_split must preserve exact owner responsibilities and authority denials")

    for entry in payload["owner_split"]:
        if entry["repo"] == "aoa-agents" and "assistant contestant" not in entry["must_not"]:
            fail("aoa-agents owner_split entry must deny assistant contestant authority")
        if entry["repo"] == "aoa-evals" and "issue live arena verdicts" not in entry["must_not"]:
            fail("aoa-evals owner_split entry must deny live verdict authority")
        if entry["repo"] == "aoa-memo" and "write durable scars" not in entry["must_not"]:
            fail("aoa-memo owner_split entry must deny durable scar writes")
        if entry["repo"] == "aoa-routing" and "dispatch runtime arena sessions" not in entry["must_not"]:
            fail("aoa-routing owner_split entry must deny runtime dispatch")
        if entry["repo"] == "abyss-stack" and "separate runtime-owner gate" not in entry["owns"]:
            fail("abyss-stack owner_split entry must require a separate runtime-owner gate")
        if entry["repo"] == "Tree-of-Sophia" and "direct runtime writes" not in entry["must_not"]:
            fail("Tree-of-Sophia owner_split entry must deny direct runtime writes")

    if payload["quarantined_surfaces"] != EXPECTED_QUARANTINED_SURFACES:
        fail("quarantined_surfaces must preserve archive compost and generated-output stop-lines")
    if payload["seed_dry_run_evidence"] != EXPECTED_SEED_EVIDENCE:
        fail("seed_dry_run_evidence must preserve dry-run-only claim limits")


def validate_files() -> None:
    for path in (DOC_PATH, SCHEMA_PATH, EXAMPLE_PATH):
        if not path.exists():
            fail(f"missing mechanical arena kernel surface: {path.relative_to(ROOT).as_posix()}")

    doc_text = DOC_PATH.read_text(encoding="utf-8")
    assert_contains_all(doc_text, REQUIRED_DOC_TOKENS, "mechanical arena kernel doc")

    schema = read_json(SCHEMA_PATH)
    payload = read_json(EXAMPLE_PATH)
    validate_payload(payload, schema)


def main() -> int:
    validate_files()
    print("ok: Experience v1.4 agonic pair trials mechanical arena kernel center contract is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
