#!/usr/bin/env python3
"""Validate the Experience v2.0 living workspace continuity runtime center contract."""

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
    / "experience-v2-0-living-workspace-continuity-runtime.schema.json"
)
EXAMPLE_PATH = (
    ROOT
    / "mechanics"
    / "experience"
    / "parts"
    / "continuity-context"
    / "examples"
    / "experience_v2_0_living_workspace_continuity_runtime.example.json"
)

SOURCE_SEED = {
    "archive_name": "aoa-experience-living-workspace-continuity-runtime-seed-v2_0.zip",
    "seed_id": "aoa-experience-living-workspace-continuity-runtime-seed-v2_0",
    "version": "v2.0",
    "sha256": "2247d4095c52412512063bcac1b07b6db83539ac4597bd9b67a82adc3ba26d71",
    "claim_limit": "archive_readable_not_runtime_owner_ready",
    "runtime_seam": ".codex/continuity",
    "no_new_repo": True,
}

EXPECTED_PREDECESSORS = [
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_8_CONTEXT_ROUTING_NERVOUS_SYSTEM.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_9_CONTEXT_MEMORY_WEAVING_CONTINUITY_LOOM.md",
    "mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md",
    "docs/FEDERATION_RULES.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_REPO_LANDING_ORDER.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_TOS_CANDIDATE_BOUNDARY.md",
    "8Dionysus:docs/WORKSPACE_INSTALL.md",
    "8Dionysus:docs/CODEX_PLANE_REGENERATION.md",
    "mechanics/agon/docs/AGON_WAVE10_LANDING.md",
]

EXPECTED_RUNTIME_LAW = [
    "no_live_workspace_runtime_activation",
    "no_hidden_codex_continuity_installation",
    "no_self_continuity_sovereignty",
    "no_assistant_self_authorized_continuity",
    "no_codex_durable_continuity_approval",
    "no_checkpoint_export_without_budget_and_evidence",
    "no_memory_owner_theft",
    "no_personal_context_overreach",
    "no_stale_context_as_fresh_evidence",
    "no_replay_hash_break_bypass",
    "no_route_loop_runtime_escalation",
    "no_runtime_migration_without_backup_and_operator_gate",
    "no_worker_scheduler_or_daemon_activation",
    "no_direct_tree_of_sophia_runtime_write",
    "no_dashboard_or_state_machine_sovereignty",
    "no_continuity_as_consciousness_claim",
    "no_raw_archive_or_generated_runtime_promotion",
]

EXPECTED_REQUESTS = [
    {
        "request": "shared_root_projection_boundary_review",
        "owner": "8Dionysus",
        "input_boundary": "source-owned shared-root projection surfaces and no runtime truth transfer",
        "output_candidate": "shared_root_projection_boundary_candidate",
        "must_include": [
            "source_owned_projection_law",
            "projected_surface_list",
            "no_runtime_truth_transfer",
            "check_before_execute",
        ],
        "must_not_include": [
            "live_install",
            "source_truth_transfer",
            "workspace_sovereignty",
            "runtime_authority",
        ],
        "live_execution": False,
        "authority": "projection_candidate_only",
    },
    {
        "request": "workspace_helper_seam_review",
        "owner": "aoa-sdk",
        "input_boundary": "typed workspace discovery ingress guard and helper seam boundary",
        "output_candidate": "workspace_helper_seam_candidate",
        "must_include": [
            "typed_helpers",
            "discovery_boundary",
            "guard_boundary",
            "non_authoritative_label",
        ],
        "must_not_include": [
            "direct_install",
            "authority_transfer",
            "hidden_projection",
            "runtime_activation",
        ],
        "live_execution": False,
        "authority": "sdk_helper_candidate_only",
    },
    {
        "request": "runtime_substrate_gate_review",
        "owner": "abyss-stack",
        "input_boundary": "runtime storage backup migration and daemon gate posture",
        "output_candidate": "runtime_substrate_gate_candidate",
        "must_include": [
            "backup_requirement",
            "operator_gate",
            "substrate_boundary",
            "disabled_by_default",
        ],
        "must_not_include": [
            "live_worker_activation",
            "hidden_scheduler",
            "background_resume",
            "center_authority",
        ],
        "live_execution": False,
        "authority": "runtime_candidate_only",
    },
    {
        "request": "continuity_memory_gate_review",
        "owner": "aoa-memo",
        "input_boundary": "continuity thread carry retention gate and stale quarantine posture",
        "output_candidate": "continuity_memory_gate_candidate",
        "must_include": [
            "thread_refs",
            "retention_boundary",
            "stale_quarantine",
            "reentry_receipts",
        ],
        "must_not_include": [
            "durable_memory_sovereignty",
            "identity_truth_seal",
            "hidden_persistence",
            "owner_theft",
        ],
        "live_execution": False,
        "authority": "candidate_intake_only",
    },
    {
        "request": "continuity_run_posture_review",
        "owner": "aoa-agents",
        "input_boundary": "assistant continuity-backed run notary posture and personal-context boundary",
        "output_candidate": "continuity_run_posture_candidate",
        "must_include": [
            "assistant_office",
            "notary_limit",
            "operator_review",
            "personal_boundary",
        ],
        "must_not_include": [
            "assistant_self_authorization",
            "persona_lock_in",
            "durable_self_claim",
            "verdict_authority",
        ],
        "live_execution": False,
        "authority": "actor_posture_candidate_only",
    },
    {
        "request": "live_session_reentry_route_review",
        "owner": "aoa-routing",
        "input_boundary": "receipt-backed live session return route and loop guard posture",
        "output_candidate": "live_session_reentry_candidate",
        "must_include": [
            "receipt_ref",
            "route_reason",
            "loop_guard",
            "budget_ref",
        ],
        "must_not_include": [
            "routing_truth_claim",
            "direct_runtime_resume",
            "hidden_context_pull",
            "owner_override",
        ],
        "live_execution": False,
        "authority": "routing_candidate_only",
    },
    {
        "request": "runtime_integrity_review",
        "owner": "aoa-evals",
        "input_boundary": "checkpoint export budget evidence replay integrity and runtime-boundary legitimacy",
        "output_candidate": "runtime_integrity_candidate",
        "must_include": [
            "budget_ref",
            "evidence_refs",
            "replay_requirements",
            "human_review_needed",
        ],
        "must_not_include": [
            "sealed_verdict",
            "activation_authority",
            "owner_override",
            "canon_write",
        ],
        "live_execution": False,
        "authority": "bounded_eval_request_only",
    },
    {
        "request": "canonical_runtime_boundary_review",
        "owner": "Tree-of-Sophia",
        "input_boundary": "runtime dossier boundary and no direct write posture",
        "output_candidate": "canonical_runtime_boundary_candidate",
        "must_include": [
            "boundary_refs",
            "dossier_path",
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
        "request": "derived_runtime_observability_review",
        "owner": "aoa-stats",
        "input_boundary": "reviewed runtime traces for derived summaries only",
        "output_candidate": "runtime_observability_candidate",
        "must_include": [
            "derived_only",
            "source_refs",
            "non_authoritative_label",
            "review_trace",
        ],
        "must_not_include": [
            "dashboard_verdict",
            "owner_truth",
            "runtime_policy_write",
            "hidden_trigger",
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
        "authority_note": "Dionysus archive is transport evidence; center may name v2.0 runtime law only",
        "stop_lines": ["no raw archive replay", "no generated runtime promotion"],
    },
    {
        "order": 2,
        "kind": "wave9_continuity_predecessor_checked",
        "owner": "Agents-of-Abyss",
        "authority_note": "v1.9 continuity loom remains predecessor law; v2.0 may not outrun continuity boundaries already fixed in the center",
        "stop_lines": [
            "no predecessor erasure",
            "no living-workspace runtime before wave9 boundary",
        ],
    },
    {
        "order": 3,
        "kind": "living_workspace_runtime_charter_requested",
        "owner": "Agents-of-Abyss",
        "authority_note": "charter is required before any install projection runtime or live-run surface can land elsewhere",
        "stop_lines": [
            "no experience wave x naming",
            "no center-created runtime activation",
        ],
    },
    {
        "order": 4,
        "kind": "shared_root_projection_boundary_requested",
        "owner": "8Dionysus",
        "authority_note": "shared-root projection law may govern selected workspace-root surfaces without transferring runtime truth",
        "stop_lines": [
            "no workspace sovereignty transfer",
            "no live .codex continuity projection",
        ],
    },
    {
        "order": 5,
        "kind": "workspace_helper_seam_requested",
        "owner": "aoa-sdk",
        "authority_note": "sdk may later own typed workspace discovery and helper seams only",
        "stop_lines": ["no helper authority theft", "no install by sdk shorthand"],
    },
    {
        "order": 6,
        "kind": "runtime_substrate_gate_requested",
        "owner": "abyss-stack",
        "authority_note": "stack may later own runtime substrate only after a separate runtime-owner gate",
        "stop_lines": ["no live cache worker or daemon", "no background resume loop"],
    },
    {
        "order": 7,
        "kind": "continuity_memory_gate_requested",
        "owner": "aoa-memo",
        "authority_note": "memo may advise continuity thread carry and retention posture only as candidate memory",
        "stop_lines": ["no durable memory sovereignty", "no owner truth theft"],
    },
    {
        "order": 8,
        "kind": "continuity_run_posture_checked",
        "owner": "aoa-agents",
        "authority_note": "assistant continuity-backed runs remain notary-limited and operator-reviewed",
        "stop_lines": [
            "no assistant self-authorized continuity",
            "no personal context overreach",
        ],
    },
    {
        "order": 9,
        "kind": "live_session_reentry_route_requested",
        "owner": "aoa-routing",
        "authority_note": "routing may suggest receipt-backed return paths only as non-authoritative hints",
        "stop_lines": ["no route loop escalation", "no routing as runtime truth"],
    },
    {
        "order": 10,
        "kind": "runtime_integrity_and_replay_checked",
        "owner": "aoa-evals",
        "authority_note": "checkpoint export replay and runtime integrity require bounded proof before any owner-local adoption",
        "stop_lines": [
            "no replay hash bypass",
            "no checkpoint export without budget and evidence",
        ],
    },
    {
        "order": 11,
        "kind": "canonical_runtime_boundary_checked",
        "owner": "Tree-of-Sophia",
        "authority_note": "runtime continuity may prepare dossier boundaries only through Tree-of-Sophia review paths",
        "stop_lines": ["no direct tree-of-sophia runtime write", "no canon promotion"],
    },
    {
        "order": 12,
        "kind": "derived_runtime_observability_candidate_requested",
        "owner": "aoa-stats",
        "authority_note": "stats may summarize reviewed runtime traces only as derived observability",
        "stop_lines": ["no dashboard as verdict", "no state machine as authority"],
    },
    {
        "order": 13,
        "kind": "owner_landing_or_runtime_gate_request_declared",
        "owner": "Agents-of-Abyss",
        "authority_note": "center may route later owner-local landings or a separate runtime-owner gate only after explicit boundary review",
        "stop_lines": ["no hidden install path", "no cross-repo meaning theft"],
    },
]

EXPECTED_HARD_GUARDS = [
    "no_live_workspace_runtime_activation",
    "no_hidden_codex_continuity_installation",
    "no_self_continuity_sovereignty",
    "no_assistant_self_authorized_continuity",
    "no_codex_durable_continuity_approval",
    "no_checkpoint_export_without_budget_and_evidence",
    "no_memory_owner_theft",
    "no_personal_context_overreach",
    "no_stale_context_as_fresh_evidence",
    "no_replay_hash_break_bypass",
    "no_route_loop_runtime_escalation",
    "no_runtime_migration_without_backup_and_operator_gate",
    "no_worker_scheduler_or_daemon_activation",
    "no_direct_tree_of_sophia_runtime_write",
    "no_dashboard_or_state_machine_sovereignty",
    "no_continuity_as_consciousness_claim",
    "no_raw_archive_or_generated_runtime_promotion",
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
        "active_runtime_allowed": False,
        "codex_continuity_installation_allowed": False,
    },
    "projection_boundary": {
        "shared_root_projection_without_source_owner_allowed": False,
        "live_codex_continuity_path_write_allowed": False,
        "helper_seam_authority_theft_allowed": False,
        "missing_layout_promotion_allowed": False,
        "workspace_sovereignty_claim_allowed": False,
    },
    "authority_boundary": {
        "assistant_self_continuity_allowed": False,
        "codex_durable_continuity_approval_allowed": False,
        "memory_owner_theft_allowed": False,
        "personal_context_overreach_allowed": False,
        "direct_tos_runtime_write_allowed": False,
    },
    "integrity_boundary": {
        "checkpoint_export_without_budget_allowed": False,
        "checkpoint_export_without_evidence_allowed": False,
        "stale_context_as_fresh_evidence_allowed": False,
        "replay_hash_break_ignored_allowed": False,
        "route_loop_ignored_allowed": False,
    },
    "runtime_boundary": {
        "migration_without_backup_allowed": False,
        "worker_or_daemon_activation_allowed": False,
        "hidden_scheduler_allowed": False,
        "auto_runtime_resume_allowed": False,
        "dashboard_or_state_machine_authority_allowed": False,
    },
}

EXPECTED_AUTHORITY = {
    "center_owner": "Agents-of-Abyss",
    "runtime_owner": "none",
    "claim_limit": "living_workspace_runtime_may_name_a_future_workspace_seam_but_may_not_install_or_self_authorize_it",
    "human_gates_required": [
        "operator review before any workspace continuity adoption",
        "8Dionysus source-owner review before shared-root projection or .codex continuity path adoption",
        "owner-local sdk approval before workspace helper or discovery seam adoption",
        "runtime-owner gate before install storage cache worker scheduler daemon or background resume",
        "owner-local memo approval before durable thread carry or retention handoff",
        "owner-local agents approval before assistant continuity-backed run beyond notary posture",
        "owner-local eval approval before replay audit or runtime integrity verdict use",
        "owner-local routing approval before live session reentry route use",
        "Tree-of-Sophia review before dossier or canon boundary use",
    ],
}

EXPECTED_OWNER_SPLIT = [
    "Agents-of-Abyss owns this v2.0 center contract predecessor mapping hard guards quarantine list and human gates.",
    "8Dionysus owns shared-root projection law and the source-owned copies of AGENTS.md AOA_WORKSPACE_ROOT .agents and .codex only.",
    "aoa-sdk owns typed workspace discovery ingress guard and helper seams only.",
    "aoa-memo owns continuity and reentry candidates only never workspace sovereignty.",
    "aoa-routing owns receipt-backed route hints only.",
    "aoa-agents owns continuity-backed assistant posture only.",
    "aoa-evals owns replay integrity and runtime legitimacy proof only.",
    "aoa-stats owns derived summaries only.",
    "aoa-playbooks owns recurring choreography only if that route later matures.",
    "aoa-kag owns derived pattern lift only after later owner-local landing.",
    "abyss-stack owns actual runtime export cache worker scheduler and daemon surfaces only after a separate runtime-owner gate.",
    "Tree-of-Sophia owns dossier and canon intake only through its own review path.",
    "Dionysus owns source lineage and later harvest trace only.",
]

EXPECTED_QUARANTINED_SURFACES = [
    ".codex/continuity/**",
    "workspace_continuity_layout_v1",
    "codex_continuity_feed_v1",
    "live_session_thread_index_v1",
    "checkpoint_weave_export_v1",
    "operator_continuity_console_state_v1",
    "continuity_runtime_event_v1",
    "continuity_replay_audit_v1",
    "stale_context_quarantine_v1",
    "continuity_runtime_migration_v1",
    "continuity_runtime_rollback_v1",
    "first_continuity_run_v1",
    "continuity_runtime_dashboard_v1",
    "continuity_runtime_authority_decision_v1",
    "workspace_continuity_smoke_result_v1",
    "continuity_runtime_state_v1",
    "continuity_checkpoint_receipt_v1",
    "continuity_runtime_patchset_v1",
    "continuity_live_session_bootstrap_v1",
    "owner_local_runtime_fanout_under_aoa_memo_aoa_routing_aoa_agents_aoa_evals_aoa_stats_aoa_playbooks_aoa_sdk_aoa_kag_abyss_stack_aoa_skills_aoa_techniques_tree_of_sophia",
]

EXPECTED_SEED_EVIDENCE = {
    "schema_example_pairs": 55,
    "json_file_count": 163,
    "archive_file_count": 317,
    "seed_tests_passed": 18,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def expect_equal(name: str, actual: Any, expected: Any, detail: str) -> None:
    if actual != expected:
        raise ValidationError(f"{name} {detail}")


def validate_payload(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    Draft202012Validator(schema).validate(payload)

    expect_equal(
        "source_seed",
        payload["source_seed"],
        SOURCE_SEED,
        "must preserve v2.0 seed provenance",
    )
    expect_equal(
        "predecessor_surfaces",
        payload["predecessor_surfaces"],
        EXPECTED_PREDECESSORS,
        "must preserve the v2.0 predecessor chain",
    )
    expect_equal(
        "runtime_law",
        payload["runtime_law"],
        EXPECTED_RUNTIME_LAW,
        "must preserve runtime law",
    )
    expect_equal(
        "runtime_requests",
        payload["runtime_requests"],
        EXPECTED_REQUESTS,
        "must preserve runtime request ownership and boundaries",
    )
    expect_equal(
        "runtime_flow",
        payload["runtime_flow"],
        EXPECTED_FLOW,
        "must preserve the runtime flow spine",
    )
    expect_equal(
        "hard_guards",
        payload["hard_guards"],
        EXPECTED_HARD_GUARDS,
        "must preserve hard guards",
    )
    expect_equal(
        "blocking_contracts",
        payload["blocking_contracts"],
        EXPECTED_BLOCKING_CONTRACTS,
        "must preserve non-runtime blocking contracts",
    )
    expect_equal(
        "authority",
        payload["authority"],
        EXPECTED_AUTHORITY,
        "must preserve center authority posture",
    )
    expect_equal(
        "owner_split",
        payload["owner_split"],
        EXPECTED_OWNER_SPLIT,
        "must preserve owner split",
    )
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
    schema = load_json(SCHEMA_PATH)
    payload = load_json(EXAMPLE_PATH)
    validate_payload(payload, schema)
    print(
        "ok: Experience v2.0 living workspace continuity runtime center contract is valid"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
