#!/usr/bin/env python3
"""Validate the Experience v1.6 rank/reputation center contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, ValidationError


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
    / "continuity-context"
    / "schemas"
    / "experience-v1-6-epistemic-memory-rank-reputation-engine.schema.json"
)
EXAMPLE_PATH = (
    ROOT
    / "mechanics"
    / "experience"
    / "parts"
    / "continuity-context"
    / "examples"
    / "experience_v1_6_epistemic_memory_rank_reputation_engine.example.json"
)

SOURCE_ARCHIVE = "aoa-experience-epistemic-memory-rank-reputation-engine-seed-v1_6.zip"
SOURCE_SHA256 = "51e403eb0ca9ac384b1edba959b67bdf457efc5813ba3aa7577e94ee87591475"

EXPECTED_PREDECESSORS = [
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.md",
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.map.yaml",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_5_EPISTEMIC_DUEL_MODEL_OF_OTHER_FORGE.md",
    "mechanics/agon/docs/AGON_WAVE14_LANDING.md",
    "mechanics/agon/docs/AGON_WAVE14_STOP_LINES.md",
    "mechanics/agon/docs/AGON_RETENTION_RANK_ECONOMY.md",
    "mechanics/agon/docs/AGON_RETENTION_OWNER_HANDOFFS.md",
    "mechanics/agon/docs/AGON_RANK_JURISDICTION_MODEL.md",
    "mechanics/agon/docs/AGON_CONTRADICTION_CLOSURE_SUMMON_LAW.md",
    "mechanics/agon/docs/AGON_WAVE15_LANDING.md",
    "mechanics/agon/docs/AGON_WAVE15_STOP_LINES.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md",
]

EXPECTED_RANK_REPUTATION_LAW = [
    "no_standing_from_single_blaze",
    "no_reputation_event_without_evidence",
    "no_rank_delta_without_retention_and_review",
    "no_jurisdiction_grant_without_reviewed_basis",
    "no_closure_right_without_contradiction_trace",
    "no_summon_right_without_visible_cost",
    "no_codex_rank_or_rights_authority",
    "no_assistant_agonic_rank_or_jurisdiction",
    "no_memory_or_model_history_as_truth",
    "no_runtime_ledger_or_scheduler_authority",
    "no_direct_tree_of_sophia_or_kag_canon",
]

EXPECTED_REQUESTS = [
    {
        "request": "reputation_event_review",
        "owner": "aoa-evals",
        "input_boundary": "verdict trace recurrence evidence retention context and actor posture",
        "output_candidate": "reputation_event_candidate",
        "must_include": [
            "evidence_refs",
            "verdict_trace",
            "recurrence_trace",
            "retention_context",
        ],
        "must_not_include": [
            "codex_rank_assignment",
            "direct_rights_grant",
            "durable_memory_write",
            "direct_tos_write",
        ],
        "live_execution": False,
        "authority": "bounded_eval_request_only",
    },
    {
        "request": "retention_window_review",
        "owner": "aoa-memo",
        "input_boundary": "scar delta recurrence record reentry evidence and owner review posture",
        "output_candidate": "retention_result_candidate",
        "must_include": [
            "reentry_window",
            "recurrence_trace",
            "owner_review_needed",
            "candidate_only",
        ],
        "must_not_include": [
            "durable_memory_write",
            "scheduler_loop",
            "automatic_decay",
            "rank_mutation",
        ],
        "live_execution": False,
        "authority": "candidate_intake_only",
    },
    {
        "request": "standing_transition_review",
        "owner": "aoa-agents",
        "input_boundary": "reviewed basis retention result jurisdiction kind and actor standing posture",
        "output_candidate": "standing_or_jurisdiction_candidate",
        "must_include": [
            "reviewed_basis",
            "retention_result",
            "jurisdiction_kind",
            "contradiction_status",
        ],
        "must_not_include": [
            "assistant_rank_assignment",
            "codex_authority",
            "one_event_promotion",
            "hidden_right_grant",
        ],
        "live_execution": False,
        "authority": "owner_local_candidate_only",
    },
    {
        "request": "model_history_update_review",
        "owner": "aoa-memo",
        "input_boundary": "bounded model-of-other history candidate with trace and non-canon limits",
        "output_candidate": "model_history_candidate",
        "must_include": [
            "source_refs",
            "history_delta",
            "non_canon_label",
            "review_trace",
        ],
        "must_not_include": [
            "durable_identity_claim",
            "canon_anchor_write",
            "hidden_memory_thread",
            "pairing_lock_in",
        ],
        "live_execution": False,
        "authority": "candidate_history_only",
    },
    {
        "request": "derived_observability_review",
        "owner": "aoa-stats",
        "input_boundary": "reviewed consequence packets and bounded summary candidates",
        "output_candidate": "dashboard_or_watch_candidate",
        "must_include": [
            "derived_only",
            "source_refs",
            "non_authoritative_label",
            "review_trace",
        ],
        "must_not_include": [
            "proof_score",
            "canon_write",
            "routing_authority",
            "runtime_scheduler",
        ],
        "live_execution": False,
        "authority": "derived_surface_only",
    },
]

EXPECTED_FLOW_KINDS = [
    "source_seed_received",
    "wave5_epistemic_predecessor_checked",
    "consequence_charter_requested",
    "reputation_event_review_requested",
    "memo_intake_candidate_requested",
    "retention_check_candidate_requested",
    "repeated_retention_result_candidate_checked",
    "standing_and_jurisdiction_candidate_requested",
    "summon_and_closure_rights_gate_checked",
    "derived_observability_candidate_requested",
    "owner_landing_or_recharter_request_declared",
]

EXPECTED_FLOW_OWNERS = [
    "Agents-of-Abyss",
    "Agents-of-Abyss",
    "Agents-of-Abyss",
    "aoa-evals",
    "aoa-memo",
    "aoa-memo",
    "aoa-evals",
    "aoa-agents",
    "aoa-agents",
    "aoa-stats",
    "Agents-of-Abyss",
]

EXPECTED_FLOW_STOP_LINES = [
    ["no raw archive replay", "no generated clean-flow promotion"],
    ["no wave16 collapse", "no predecessor erasure"],
    ["no center-created live standing", "no rights by declaration"],
    ["no reputation without evidence", "no direct rights grant"],
    ["no durable memory write", "no memo as truth"],
    ["no scheduler loop", "no automatic decay execution"],
    ["no one-event retention win", "no retention without recurrence"],
    ["no assistant agonic rank", "no codex standing authority"],
    ["no closure over open contradiction", "no summon without visible cost"],
    ["no stats as proof", "no dashboard as verdict"],
    ["no runtime ledger activation", "no direct Tree-of-Sophia or KAG canon"],
]

EXPECTED_FLOW_AUTHORITY_NOTES = [
    "Dionysus archive is transport evidence; center may name v1.6 standing and rights law only",
    "v1.5 remains predecessor law; v1.6 may only add consequence grammar after the epistemic layer",
    "charter is required before any later owner-local standing or rights landing can be considered",
    "reputation review may produce a candidate packet but cannot issue final standing or rights",
    "memo may receive bounded consequence candidates but cannot convert them into durable truth here",
    "retention windows remain candidate-only and may not become scheduler execution or automatic decay",
    "retention legitimacy may be checked as bounded evidence without mutating standing on its own",
    "standing and jurisdiction remain owner-local candidates and may not be assigned by assistants or Codex",
    "summon and closure stay reviewed jurisdictions behind contradiction law and visible cost",
    "derived dashboards may summarize bounded packets but cannot become proof, score, or verdict authority",
    "future consequence work returns to owner-local landing or human recharter as requests",
]

EXPECTED_HARD_GUARDS = [
    "no_live_rank_mutation",
    "no_live_rights_activation",
    "no_live_runtime_activation",
    "no_codex_rank_assignment",
    "no_assistant_agonic_rank",
    "no_reputation_without_evidence",
    "no_rank_delta_without_retention_and_review",
    "no_single_event_standing",
    "no_closure_right_without_contradiction_trace",
    "no_summon_right_without_visible_cost",
    "no_memory_or_model_history_as_truth",
    "no_durable_memory_write",
    "no_runtime_decay_or_scheduler",
    "no_stats_as_proof",
    "no_routing_as_owner",
    "no_direct_tree_of_sophia_or_kag_canon",
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
        "live_rank_mutation_allowed": False,
        "live_rights_activation_allowed": False,
        "live_runtime_allowed": False,
    },
    "reputation_evidence": {
        "evidence_refs_required": True,
        "verdict_trace_required": True,
        "recurrence_trace_required": True,
        "retention_context_required": True,
        "missing_evidence_allowed": False,
        "direct_rights_grant_allowed": False,
        "one_event_promotion_allowed": False,
    },
    "retention_boundary": {
        "memo_candidate_only_required": True,
        "recurrence_required": True,
        "reentry_window_required": True,
        "automatic_decay_execution_allowed": False,
        "scheduler_loop_allowed": False,
        "retention_result_may_mutate_standing": False,
    },
    "standing_and_jurisdiction": {
        "standing_candidate_only_required": True,
        "reviewed_basis_required": True,
        "retention_result_required": True,
        "jurisdiction_review_required": True,
        "rank_jump_without_review_allowed": False,
        "closure_without_trace_allowed": False,
        "summon_without_visible_cost_allowed": False,
    },
    "actor_boundary": {
        "assistant_rank_assignment_allowed": False,
        "assistant_jurisdiction_grant_allowed": False,
        "assistant_judge_allowed": False,
        "codex_rank_assignment_allowed": False,
        "codex_rights_grant_allowed": False,
        "codex_memory_write_allowed": False,
    },
    "memory_history_boundary": {
        "durable_memory_write_allowed": False,
        "model_history_candidate_only_required": True,
        "durable_identity_claim_allowed": False,
        "hidden_memory_thread_allowed": False,
        "pairing_lock_in_allowed": False,
    },
    "derived_layer_boundary": {
        "stats_as_proof_allowed": False,
        "routing_as_owner_allowed": False,
        "memo_as_truth_allowed": False,
        "eval_live_verdict_authority_allowed": False,
        "dashboard_as_verdict_allowed": False,
    },
    "tos_kag_boundary": {
        "runtime_write_allowed": False,
        "direct_node_path_allowed": False,
        "tos_canon_write_allowed": False,
        "kag_promotion_allowed": False,
        "kag_canonization_allowed": False,
        "dossier_candidate_only": True,
    },
    "runtime_storage": {
        "runtime_worker_activation_allowed": False,
        "storage_record_authoritative": False,
        "host_port_open_allowed": False,
        "scheduler_loop_allowed": False,
        "scoring_job_allowed": False,
        "deployment_daemon_allowed": False,
    },
    "archive_consistency": {
        "clean_flow_may_inform_contract": True,
        "raw_generated_output_copied_as_truth": False,
        "fixture_generated_result_disagreement_allowed": False,
        "archive_scripts_tests_copied_as_owner_truth": False,
        "archive_runtime_outputs_copied_as_owner_truth": False,
    },
}

EXPECTED_CODEX_MAY = [
    "simulate rank and rights contract checks",
    "collect seed dry-run evidence",
    "propose owner-local standing review packets",
    "run validators",
    "prepare bounded handoff maps",
]

EXPECTED_CODEX_DENIALS = [
    "activate live rank mutation",
    "activate live rights grant",
    "activate live runtime",
    "assign rank",
    "grant summon right",
    "grant closure right",
    "issue reputation verdict",
    "seal standing truth",
    "write durable memory",
    "write model history as truth",
    "execute retention",
    "start decay scheduler",
    "promote dashboard to proof",
    "route as owner",
    "promote KAG canon",
    "write directly to Tree-of-Sophia",
    "promote generated clean-flow output to owner truth",
    "copy raw archive proposals into owner truth",
]

REQUIRED_ASSISTANT_DENIALS = [
    "become primary rank authority",
    "grant summon right",
    "grant closure right",
    "issue reputation verdict",
    "become judge",
    "write memory",
    "write model history as truth",
    "execute retention",
    "start decay scheduler",
    "mutate standing or jurisdiction",
    "promote KAG canon",
    "write directly to Tree-of-Sophia",
]

EXPECTED_DERIVED_DENIALS = [
    "stats_as_proof",
    "memo_as_truth",
    "routing_as_owner",
    "kag_as_canon",
    "sdk_as_authority",
    "evals_as_live_verdict_authority",
    "playbooks_as_runtime",
    "runtime_as_doctrine",
    "dionysus_as_runtime",
    "reputation_as_live_score",
]

REQUIRED_HUMAN_GATES = [
    "operator review before reputation event adoption",
    "owner-local memo approval before retention intake",
    "owner-local eval approval before legitimacy verdict use",
    "owner-local agents approval before standing or jurisdiction mutation",
    "human review before summon right grant",
    "human review before closure right grant",
    "runtime-owner gate before ledger scheduler workers ports services or daemons",
    "Tree-of-Sophia review before canon or interpretive intake",
    "KAG owner review before pattern promotion",
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
        "owns": "center rank reputation and jurisdiction law predecessor mapping flow hard guards and authority stop-lines",
        "must_not": "replace owner-local actor truth memory retention routing runtime KAG ToS or eval legitimacy",
    },
    {
        "repo": "aoa-agents",
        "owns": "standing and jurisdiction truth surfaces after owner-local landing",
        "must_not": "grant one-event rank assistant authority hidden rights or direct closure by default",
    },
    {
        "repo": "aoa-evals",
        "owns": "legitimacy checks over evidence recurrence retention and standing-transition requests",
        "must_not": "issue live verdicts assign rank grant rights or convert evidence into runtime law",
    },
    {
        "repo": "aoa-playbooks",
        "owns": "recurring consequence choreography fallback posture and operator review routes",
        "must_not": "become runtime or standing authority",
    },
    {
        "repo": "aoa-memo",
        "owns": "retention and model-history intake candidates only after owner review",
        "must_not": "become memory truth durable storage or self-justifying history",
    },
    {
        "repo": "aoa-stats",
        "owns": "derived dashboards watch orders and consequence summaries only",
        "must_not": "become proof score or reputation truth",
    },
    {
        "repo": "aoa-routing",
        "owns": "advisory route candidates only",
        "must_not": "dispatch as owner truth or right-grant authority",
    },
    {
        "repo": "aoa-sdk",
        "owns": "typed packet helpers validation helpers and control-plane seams only",
        "must_not": "become semantic standing or runtime authority",
    },
    {
        "repo": "aoa-kag",
        "owns": "derived consequence pattern candidates only",
        "must_not": "become canon or source truth",
    },
    {
        "repo": "aoa-skills",
        "owns": "bounded standing and review workflows extracted after owner acceptance",
        "must_not": "grant rank reputation rights or runtime authority",
    },
    {
        "repo": "aoa-techniques",
        "owns": "reusable retention and review practices after owner acceptance",
        "must_not": "grant live authority",
    },
    {
        "repo": "abyss-stack",
        "owns": "runtime ledger storage workers schedulers deployment ports and services only after a separate runtime-owner gate",
        "must_not": "activate runtime from this center landing",
    },
    {
        "repo": "Tree-of-Sophia",
        "owns": "canon and interpretive review through its own path",
        "must_not": "receive direct runtime writes node paths canon writes or unreviewed consequence dossiers",
    },
    {
        "repo": "Dionysus",
        "owns": "source lineage staged intake and later harvest trace",
        "must_not": "become runtime or standing truth",
    },
    {
        "repo": "8Dionysus",
        "owns": "shared-root projection law where workspace projection surfaces are affected",
        "must_not": "absorb rank or rights truth",
    },
]

EXPECTED_QUARANTINED_SURFACES = [
    "archive-local generated rank reputation clean-flow runtime-like artifacts",
    "archive-local generated dashboards watch orders and right resolutions",
    "archive-local repo/* owner proposals outside this center contract",
    "archive-local face ledgers trust vectors model histories and policy artifacts as transport evidence only",
    "archive-local scripts and tests as transport evidence only",
    "archive-local runtime storage records workers schedulers and catalogs",
]

EXPECTED_SEED_EVIDENCE = {
    "archive_integrity": "unzip_t_passed",
    "schema_example_pairs": 53,
    "json_files": 146,
    "seed_tests_passed": 12,
    "claim_limit": "dry_run_only_not_owner_readiness",
}

FORBIDDEN_AUTHORITY_NOTE_SNIPPETS = [
    "live rank may run after this gate",
    "Codex rank assignment allowed",
    "assistant rank authority allowed",
    "rights may be granted automatically",
    "durable memory write follows this packet",
    "dashboard becomes proof",
    "generated output becomes truth",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def validate_payload(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    validator = Draft202012Validator(schema)
    errors = sorted(
        validator.iter_errors(payload), key=lambda err: list(err.absolute_path)
    )
    if errors:
        first = errors[0]
        raise ValidationError(
            f"schema validation failed at {list(first.absolute_path)}: {first.message}"
        )

    require(
        payload["source_seed"]
        == {
            "archive_name": SOURCE_ARCHIVE,
            "seed_id": "aoa-experience-epistemic-memory-rank-reputation-engine-seed-v1_6",
            "version": "v1.6",
            "sha256": SOURCE_SHA256,
            "claim_limit": "archive_readable_not_owner_ready",
        },
        "source_seed must preserve the v1.6 archive identity",
    )
    require(
        payload["predecessor_surfaces"] == EXPECTED_PREDECESSORS,
        "predecessor_surfaces must preserve the v1.6 bridge spine",
    )
    require(
        payload["rank_reputation_law"] == EXPECTED_RANK_REPUTATION_LAW,
        "rank_reputation_law drifted",
    )
    require(
        payload["consequence_requests"] == EXPECTED_REQUESTS,
        "consequence_requests drifted",
    )

    flow = payload["consequence_flow"]
    require(
        [step["order"] for step in flow]
        == list(range(1, len(EXPECTED_FLOW_KINDS) + 1)),
        "consequence_flow order must remain contiguous",
    )
    require(
        [step["kind"] for step in flow] == EXPECTED_FLOW_KINDS,
        "consequence_flow kinds drifted",
    )
    require(
        [step["owner"] for step in flow] == EXPECTED_FLOW_OWNERS,
        "consequence_flow owners drifted",
    )
    require(
        [step["stop_lines"] for step in flow] == EXPECTED_FLOW_STOP_LINES,
        "consequence_flow stop_lines drifted",
    )
    require(
        [step["authority_note"] for step in flow] == EXPECTED_FLOW_AUTHORITY_NOTES,
        "consequence_flow authority_note drifted",
    )
    for step in flow:
        note = step["authority_note"]
        for snippet in FORBIDDEN_AUTHORITY_NOTE_SNIPPETS:
            require(
                snippet not in note,
                f"authority_note leaked forbidden authority: {snippet}",
            )

    require(payload["hard_guards"] == EXPECTED_HARD_GUARDS, "hard_guards drifted")
    require(
        payload["blocking_contracts"] == EXPECTED_BLOCKING_CONTRACTS,
        "blocking_contracts drifted",
    )

    authority = payload["authority"]
    require(
        authority["contract_effect"]
        == "center_rank_reputation_and_jurisdiction_law_only",
        "contract_effect drifted",
    )
    require(authority["codex_may"] == EXPECTED_CODEX_MAY, "codex_may drifted")
    require(
        authority["codex_must_not"] == EXPECTED_CODEX_DENIALS, "codex_must_not drifted"
    )
    require(
        authority["assistant_must_not"] == REQUIRED_ASSISTANT_DENIALS,
        "assistant_must_not drifted",
    )
    require(
        authority["derived_layers_must_not"] == EXPECTED_DERIVED_DENIALS,
        "derived_layers_must_not drifted",
    )
    require(
        authority["human_gates_required"] == REQUIRED_HUMAN_GATES,
        "human_gates_required drifted",
    )

    owner_split = payload["owner_split"]
    require(owner_split == EXPECTED_OWNER_SPLIT, "owner_split drifted")
    require(
        {entry["repo"] for entry in owner_split} == EXPECTED_OWNER_REPOS,
        "owner_split repo set drifted",
    )

    require(
        payload["quarantined_surfaces"] == EXPECTED_QUARANTINED_SURFACES,
        "quarantined_surfaces drifted",
    )
    require(
        payload["seed_dry_run_evidence"] == EXPECTED_SEED_EVIDENCE,
        "seed_dry_run_evidence drifted",
    )


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    payload = load_json(EXAMPLE_PATH)
    validate_payload(payload, schema)
    print(
        "ok: Experience v1.6 epistemic memory rank reputation engine center contract is valid"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
