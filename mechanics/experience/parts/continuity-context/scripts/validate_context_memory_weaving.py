#!/usr/bin/env python3
"""Validate the Experience v1.9 context memory weaving continuity loom center contract."""

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
DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V1_9_CONTEXT_MEMORY_WEAVING_CONTINUITY_LOOM.md"
SCHEMA_PATH = ROOT / "mechanics" / "experience" / "parts" / "continuity-context" / "schemas" / "experience-v1-9-context-memory-weaving-continuity-loom.schema.json"
EXAMPLE_PATH = ROOT / "mechanics" / "experience" / "parts" / "continuity-context" / "examples" / "experience_v1_9_context_memory_weaving_continuity_loom.example.json"

SOURCE_SEED = {
    "archive_name": "aoa-experience-context-memory-weaving-continuity-loom-seed-v1_9.zip",
    "seed_id": "aoa-experience-context-memory-weaving-continuity-loom-seed-v1_9",
    "version": "v1.9",
    "sha256": "a3b06434cac02149644eb036a3676fe8fdd398be4c1de3eaa908835dd5e31d96",
    "claim_limit": "archive_readable_not_owner_ready",
    "no_new_repo": True,
}

EXPECTED_PREDECESSORS = [
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.md",
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.map.yaml",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_5_EPISTEMIC_DUEL_MODEL_OF_OTHER_FORGE.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_6_EPISTEMIC_MEMORY_RANK_REPUTATION_ENGINE.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_7_AFFECTIVE_ECONOMY_HONOR_TREASURY.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_8_CONTEXT_ROUTING_NERVOUS_SYSTEM.md",
    "mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md",
    "mechanics/method-growth/docs/METHOD_SPINE.md",
    "docs/FEDERATION_RULES.md",
    "mechanics/method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md",
    "mechanics/method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md",
    "mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_AUTHORITY_RESOLVER.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_AGON_SERVICE_SEAM_V1_1.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_REPO_LANDING_ORDER.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_TOS_CANDIDATE_BOUNDARY.md",
    "mechanics/agon/docs/AGON_PRE_PROTOCOL_STOP_LINES.md",
    "mechanics/agon/docs/AGON_GATE_ROUTING_STOP_LINES.md",
    "mechanics/agon/docs/AGON_TRIAL_PLAYBOOK_STOP_LINES.md",
    "mechanics/agon/docs/AGON_COURT_MEMO_STATS_PREBINDING_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE8_LANDING.md",
    "mechanics/agon/docs/AGON_ARENA_SESSION_MODEL.md",
    "mechanics/agon/docs/AGON_ARENA_SESSION_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE9_LANDING.md",
    "mechanics/agon/docs/AGON_STATE_PACKET_MODEL.md",
    "mechanics/agon/docs/AGON_WAVE10_STOP_LINES.md",
]

EXPECTED_CONTINUITY_LAW = [
    "no_continuity_without_purpose_evidence_freshness_and_budget",
    "no_false_continuity",
    "no_private_memory_sovereignty",
    "no_assistant_private_memory_expansion",
    "no_codex_continuity_approval",
    "no_memory_owner_theft",
    "no_personal_context_overreach",
    "no_symbolic_anchor_evidence_replacement",
    "no_stale_context_dominance",
    "no_continuity_as_consciousness_claim",
    "no_direct_tree_of_sophia_write",
    "no_runtime_continuity_installation",
    "no_dashboard_or_packet_sovereignty",
]

EXPECTED_REQUESTS = [
    {
        "request": "continuity_thread_candidate_review",
        "owner": "aoa-memo",
        "input_boundary": "session signal continuity cue evidence refs freshness window budget ref and privacy-minimized carryover posture",
        "output_candidate": "continuity_thread_candidate",
        "must_include": [
            "signal_refs",
            "evidence_refs",
            "freshness_window",
            "budget_ref",
        ],
        "must_not_include": [
            "durable_memory_write",
            "identity_truth_seal",
            "hidden_private_memory",
            "runtime_installation",
        ],
        "live_execution": False,
        "authority": "candidate_intake_only",
    },
    {
        "request": "privacy_and_projection_boundary_review",
        "owner": "aoa-agents",
        "input_boundary": "assistant carryover personal context projection minimization and reversible boundary posture",
        "output_candidate": "privacy_projection_boundary_candidate",
        "must_include": [
            "service_scope",
            "privacy_minimized",
            "projection_boundary",
            "reversible_posture",
        ],
        "must_not_include": [
            "assistant_self_memory",
            "personal_lock_in",
            "hidden_profile_growth",
            "verdict_authority",
        ],
        "live_execution": False,
        "authority": "actor_posture_candidate_only",
    },
    {
        "request": "continuity_legitimacy_review",
        "owner": "aoa-evals",
        "input_boundary": "continuity basis evidence trace false continuity risk and human review posture",
        "output_candidate": "continuity_legitimacy_candidate",
        "must_include": [
            "evidence_trace",
            "false_continuity_risk",
            "review_basis",
            "human_review_needed",
        ],
        "must_not_include": [
            "sealed_verdict",
            "identity_authority",
            "runtime_authorization",
            "owner_override",
        ],
        "live_execution": False,
        "authority": "bounded_eval_request_only",
    },
    {
        "request": "receipt_backed_reentry_route_review",
        "owner": "aoa-routing",
        "input_boundary": "reentry receipt route reason session budget and lawful return path",
        "output_candidate": "receipt_backed_reentry_candidate",
        "must_include": [
            "receipt_ref",
            "route_reason",
            "budget_ref",
            "reentry_path",
        ],
        "must_not_include": [
            "direct_resume",
            "hidden_context_pull",
            "owner_override",
            "runtime_activation",
        ],
        "live_execution": False,
        "authority": "routing_candidate_only",
    },
    {
        "request": "canonical_anchor_boundary_review",
        "owner": "Tree-of-Sophia",
        "input_boundary": "canonical anchor risk dossier boundary and no direct write posture",
        "output_candidate": "canonical_anchor_boundary_candidate",
        "must_include": [
            "anchor_refs",
            "dossier_boundary",
            "candidate_only",
            "no_direct_write",
        ],
        "must_not_include": [
            "canon_entry",
            "direct_tos_write",
            "automatic_promotion",
            "hidden_dossier_write",
        ],
        "live_execution": False,
        "authority": "dossier_boundary_candidate_only",
    },
    {
        "request": "derived_continuity_observability_review",
        "owner": "aoa-stats",
        "input_boundary": "reviewed continuity traces for derived summaries only",
        "output_candidate": "continuity_observability_candidate",
        "must_include": [
            "derived_only",
            "source_refs",
            "non_authoritative_label",
            "review_trace",
        ],
        "must_not_include": [
            "continuity_verdict",
            "owner_truth",
            "runtime_trigger",
            "hidden_policy_write",
        ],
        "live_execution": False,
        "authority": "derived_surface_only",
    },
]

EXPECTED_FLOW = [
    {
        "order": 1,
        "kind": "source_seed_received",
        "owner": "Agents-of-Abyss",
        "authority_note": "Dionysus archive is transport evidence; center may name v1.9 continuity loom law only",
        "stop_lines": ["no raw archive replay", "no generated clean-flow promotion"],
    },
    {
        "order": 2,
        "kind": "wave8_routing_predecessor_checked",
        "owner": "Agents-of-Abyss",
        "authority_note": "v1.8 routing remains predecessor law; continuity may request receipt-backed reentry only after routing boundaries are already candidate-bound",
        "stop_lines": ["no predecessor erasure", "no packet collision with agon wave ix surfaces"],
    },
    {
        "order": 3,
        "kind": "continuity_loom_charter_requested",
        "owner": "Agents-of-Abyss",
        "authority_note": "charter is required before any owner-local continuity thread packet dashboard or runtime surface can land",
        "stop_lines": ["no center-created continuity engine", "no .codex/continuity installation"],
    },
    {
        "order": 4,
        "kind": "continuity_thread_candidate_requested",
        "owner": "aoa-memo",
        "authority_note": "memo may surface thread candidates and stale posture only as candidate intake not durable identity truth",
        "stop_lines": ["no private memory truth", "no hidden thread canon"],
    },
    {
        "order": 5,
        "kind": "freshness_and_privacy_gate_checked",
        "owner": "aoa-agents",
        "authority_note": "assistant carryover and personal context require minimization freshness and reversible boundaries before any reentry candidate advances",
        "stop_lines": ["no assistant private memory expansion", "no personal context overreach"],
    },
    {
        "order": 6,
        "kind": "continuity_legitimacy_review_requested",
        "owner": "aoa-evals",
        "authority_note": "continuity requires evidence trace false-continuity screening and human review before legitimacy can advance",
        "stop_lines": ["no continuity without evidence", "no codex continuity approval"],
    },
    {
        "order": 7,
        "kind": "receipt_backed_reentry_route_requested",
        "owner": "aoa-routing",
        "authority_note": "routing may suggest a receipt-backed return path but may not declare continuity truth or direct runtime resume",
        "stop_lines": ["no route as continuity truth", "no direct runtime resume"],
    },
    {
        "order": 8,
        "kind": "stale_decay_or_retire_candidate_requested",
        "owner": "aoa-memo",
        "authority_note": "stale or broken continuity must decay quarantine or retire through explicit candidate posture only",
        "stop_lines": ["no stale dominance", "no forgetting by hidden scheduler"],
    },
    {
        "order": 9,
        "kind": "replay_and_boundary_integrity_checked",
        "owner": "aoa-evals",
        "authority_note": "replay hash and owner-boundary integrity must remain reviewable before merge split or reentry confidence can advance",
        "stop_lines": ["no replay hash blindness", "no false continuity reuse"],
    },
    {
        "order": 10,
        "kind": "canonical_anchor_boundary_checked",
        "owner": "Tree-of-Sophia",
        "authority_note": "canonical anchors may constrain dossier review paths but cannot authorize direct canon write",
        "stop_lines": ["no direct tree-of-sophia write", "no canon promotion"],
    },
    {
        "order": 11,
        "kind": "derived_continuity_observability_candidate_requested",
        "owner": "aoa-stats",
        "authority_note": "stats may summarize reviewed continuity traces only as derived observability",
        "stop_lines": ["no dashboard as verdict", "no stats as authority"],
    },
    {
        "order": 12,
        "kind": "owner_landing_or_recharter_request_declared",
        "owner": "Agents-of-Abyss",
        "authority_note": "center may route owner landing or recharter requests only after explicit boundary review and without runtime activation",
        "stop_lines": ["no runtime continuity install", "no hidden worker or daemon"],
    },
]

EXPECTED_HARD_GUARDS = [
    "no_live_continuity_loom_activation",
    "no_live_runtime_activation",
    "no_private_memory_sovereignty",
    "no_continuity_without_purpose_evidence_freshness_and_budget",
    "no_false_continuity",
    "no_assistant_private_memory_expansion",
    "no_codex_continuity_approval",
    "no_memory_owner_theft",
    "no_personal_context_overreach",
    "no_symbolic_anchor_evidence_replacement",
    "no_stale_context_dominance",
    "no_continuity_as_consciousness_claim",
    "no_direct_tree_of_sophia_write",
    "no_runtime_continuity_installation",
    "no_dashboard_or_packet_sovereignty",
]

EXPECTED_BLOCKING_CONTRACTS = {
    "activation_state": {
        "allowed_landing_states": ["draft", "proposed", "reviewed", "blocked", "quarantined", "candidate_only"],
        "active_runtime_allowed": False,
        "continuity_installation_allowed": False,
    },
    "evidence_boundary": {
        "continuity_without_evidence_allowed": False,
        "false_continuity_allowed": False,
        "codex_continuity_approval_allowed": False,
        "consciousness_claim_allowed": False,
        "replay_hash_break_ignored_allowed": False,
    },
    "privacy_boundary": {
        "assistant_private_memory_allowed": False,
        "memory_owner_theft_allowed": False,
        "personal_context_overreach_allowed": False,
        "symbolic_anchor_overreach_allowed": False,
        "direct_tos_write_allowed": False,
    },
    "continuity_boundary": {
        "reentry_without_receipt_allowed": False,
        "reentry_without_budget_allowed": False,
        "stale_context_dominance_allowed": False,
        "context_flood_allowed": False,
        "merge_without_boundary_review_allowed": False,
    },
    "runtime_boundary": {
        "durable_memory_write_allowed": False,
        "retention_execution_allowed": False,
        "runtime_continuity_install_allowed": False,
        "hidden_scheduler_allowed": False,
        "worker_or_daemon_activation_allowed": False,
    },
}

EXPECTED_AUTHORITY = {
    "center_owner": "Agents-of-Abyss",
    "runtime_owner": "none",
    "claim_limit": "continuity_may_weave_reviewable_reentry_but_may_not_claim_private_memory_sovereignty",
    "human_gates_required": [
        "operator review before cross-session continuity adoption",
        "owner-local memo approval before thread lookup stale-decay or forgetting intake",
        "owner-local agents approval before assistant or personal-context carryover",
        "owner-local eval approval before merge split or replay integrity use",
        "owner-local routing approval before receipt-backed reentry route use",
        "Tree-of-Sophia review before canon-anchor or dossier path use",
        "runtime-owner gate before runtime continuity install cache worker checkpoint export or daemon",
    ],
}

EXPECTED_OWNER_SPLIT = [
    "Agents-of-Abyss owns this center law predecessor mapping continuity-weave grammar hard guards and authority stop-lines.",
    "aoa-memo owns continuity thread lookup reentry stale decay forgetting and intake candidates only.",
    "aoa-agents owns assistant private and personal-context boundaries only.",
    "aoa-evals owns continuity legitimacy merge-split review and replay integrity checks only.",
    "aoa-routing owns receipt-backed reentry hints only.",
    "aoa-stats owns derived continuity summaries only.",
    "aoa-playbooks owns recurring reentry choreography only.",
    "aoa-sdk owns typed continuity helper seams only.",
    "aoa-kag owns derived continuity pattern candidates only.",
    "abyss-stack owns future runtime continuity exports caches workers and daemons only after a separate runtime-owner gate.",
    "Tree-of-Sophia owns dossier review and canon-anchor intake through its own path only.",
    "Dionysus owns source lineage and later harvest trace only.",
    "8Dionysus owns shared-root projection law only where later workspace surfaces are affected.",
]

EXPECTED_QUARANTINED_SURFACES = [
    "continuity_context_packet_v1",
    "cross_session_handoff_packet_v1",
    "continuity_dashboard_v1",
    "continuity_drift_alarm_v1",
    "continuity_checkpoint_export_v1",
    "continuity_replay_event_v1",
    "continuity_replay_result_v1",
    "continuity_merge_decision_v1",
    "continuity_split_decision_v1",
    "continuity_owner_boundary_verdict_v1",
    "continuity_retention_check_v1",
    "context_continuity_thread_v1",
    "memory_thread_index_v1",
    "project_lineage_thread_v1",
    "continuity_tos_dossier_boundary_v1",
]

EXPECTED_SEED_EVIDENCE = {
    "schema_example_pairs": 44,
    "json_file_count": 160,
    "archive_file_count": 300,
    "seed_tests_passed": 18,
}

REQUIRED_DOC_SNIPPETS = [
    "aoa-experience-context-memory-weaving-continuity-loom-seed-v1_9.zip",
    "It is Wave 9 of the current `v1.2 -> v2.0` planting campaign.",
    "`Experience Wave IX`",
    "No private memory sovereignty.",
    "No runtime continuity installation.",
    "not a live continuity runtime",
]

BANNED_DOC_SNIPPETS = [
    "aoa-experience-context-routing-nervous-system-seed-v1_8.zip",
    "It is Wave 8 of the current v1.2-v2.0 planting campaign.",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def expect_equal(name: str, actual: Any, expected: Any, detail: str) -> None:
    if actual != expected:
        raise ValidationError(f"{name} {detail}")


def validate_document() -> None:
    doc_text = load_text(DOC_PATH)
    for snippet in REQUIRED_DOC_SNIPPETS:
        if snippet not in doc_text:
            raise ValidationError(f"documentation missing required continuity loom phrase: {snippet}")
    for snippet in BANNED_DOC_SNIPPETS:
        if snippet in doc_text:
            raise ValidationError(f"documentation still carries stale phrase: {snippet}")


def validate_payload(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    Draft202012Validator(schema).validate(payload)

    expect_equal("source_seed", payload["source_seed"], SOURCE_SEED, "must preserve continuity loom seed provenance")
    expect_equal(
        "predecessor_surfaces",
        payload["predecessor_surfaces"],
        EXPECTED_PREDECESSORS,
        "must preserve the v1.9 predecessor chain",
    )
    expect_equal("continuity_law", payload["continuity_law"], EXPECTED_CONTINUITY_LAW, "must preserve continuity law")
    expect_equal(
        "continuity_requests",
        payload["continuity_requests"],
        EXPECTED_REQUESTS,
        "must preserve continuity request ownership and boundaries",
    )
    expect_equal("continuity_flow", payload["continuity_flow"], EXPECTED_FLOW, "must preserve the continuity flow spine")
    expect_equal("hard_guards", payload["hard_guards"], EXPECTED_HARD_GUARDS, "must preserve hard guards")
    expect_equal(
        "blocking_contracts",
        payload["blocking_contracts"],
        EXPECTED_BLOCKING_CONTRACTS,
        "must preserve non-runtime blocking contracts",
    )
    expect_equal("authority", payload["authority"], EXPECTED_AUTHORITY, "must preserve center authority posture")
    expect_equal("owner_split", payload["owner_split"], EXPECTED_OWNER_SPLIT, "must preserve owner split")
    expect_equal(
        "quarantined_surfaces",
        payload["quarantined_surfaces"],
        EXPECTED_QUARANTINED_SURFACES,
        "must preserve quarantined surfaces",
    )
    expect_equal(
        "seed_dry_run_evidence",
        payload["seed_dry_run_evidence"],
        EXPECTED_SEED_EVIDENCE,
        "must preserve seed dry-run evidence",
    )


def main() -> int:
    validate_document()
    schema = load_json(SCHEMA_PATH)
    payload = load_json(EXAMPLE_PATH)
    validate_payload(payload, schema)
    print("ok: Experience v1.9 context memory weaving continuity loom center contract is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
