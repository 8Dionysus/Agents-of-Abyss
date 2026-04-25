#!/usr/bin/env python3
"""Validate the Experience v1.8 context routing nervous system center contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, ValidationError


ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V1_8_CONTEXT_ROUTING_NERVOUS_SYSTEM.md"
SCHEMA_PATH = ROOT / "schemas" / "experience-v1-8-context-routing-nervous-system.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "experience_v1_8_context_routing_nervous_system.example.json"

SOURCE_SEED = {
    "archive_name": "aoa-experience-context-routing-nervous-system-seed-v1_8.zip",
    "seed_id": "aoa-experience-context-routing-nervous-system-seed-v1_8",
    "version": "v1.8",
    "sha256": "d8ff2d7adfa91fa06c0f1ba17ffe4d45b0c5f343b026a92806b5ec25b3e427c4",
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
    "mechanics/experience/legacy/raw/EXPERIENCE_AGON_SERVICE_SEAM_V1_1.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_AUTHORITY_RESOLVER.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_TOS_CANDIDATE_BOUNDARY.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_REPO_LANDING_ORDER.md",
    "mechanics/method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md",
    "mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md",
    "mechanics/agon/docs/AGON_PRE_PROTOCOL_STOP_LINES.md",
    "mechanics/agon/docs/AGON_GATE_ROUTING_HANDOFF.md",
    "mechanics/agon/docs/AGON_GATE_ROUTING_STOP_LINES.md",
    "mechanics/agon/docs/AGON_TRIAL_PLAYBOOK_HANDOFF.md",
    "mechanics/agon/docs/AGON_TRIAL_PLAYBOOK_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE7_CENTER_HANDOFF.md",
    "mechanics/agon/docs/AGON_COURT_MEMO_STATS_PREBINDING_HANDOFF.md",
    "mechanics/agon/docs/AGON_COURT_MEMO_STATS_PREBINDING_STOP_LINES.md",
]

EXPECTED_CONTEXT_ROUTING_LAW = [
    "no_new_repo_creation",
    "no_routing_without_reason_budget_and_receipt",
    "no_owner_meaning_theft",
    "no_salience_as_authority",
    "no_codex_context_override",
    "no_assistant_context_expansion_or_personal_overreach",
    "no_affect_or_rank_direct_rights_route",
    "no_service_to_agon_without_lawful_trigger",
    "no_direct_tree_of_sophia_write",
    "no_durable_memory_or_retention_execution",
    "no_runtime_cache_worker_or_scheduler_activation",
    "no_stats_memo_or_routing_as_authority",
]

EXPECTED_REQUESTS = [
    {
        "request": "context_signal_collection_review",
        "owner": "aoa-routing",
        "input_boundary": "task scope service state agonic pressure affect rank memory and canonical-risk signals",
        "output_candidate": "context_signal_candidate",
        "must_include": [
            "task_scope",
            "signal_refs",
            "candidate_layers",
            "non_authoritative_label",
        ],
        "must_not_include": [
            "owner_override",
            "verdict",
            "rights_grant",
            "direct_tos_write",
        ],
        "live_execution": False,
        "authority": "routing_candidate_only",
    },
    {
        "request": "salience_budget_review",
        "owner": "aoa-routing",
        "input_boundary": "signal set salience ordering attention budget route reason and receipt requirement",
        "output_candidate": "salience_budget_candidate",
        "must_include": [
            "salience_vector",
            "attention_budget",
            "route_reason",
            "receipt_required",
        ],
        "must_not_include": [
            "budgetless_expansion",
            "salience_as_authority",
            "automatic_escalation",
            "hidden_context_pull",
        ],
        "live_execution": False,
        "authority": "routing_candidate_only",
    },
    {
        "request": "assistant_personal_context_boundary_review",
        "owner": "aoa-agents",
        "input_boundary": "assistant service scope personal context trigger minimization posture and reversible expansion boundary",
        "output_candidate": "assistant_personal_context_candidate",
        "must_include": [
            "service_scope",
            "personal_context_minimized",
            "expansion_trigger",
            "reversible_posture",
        ],
        "must_not_include": [
            "assistant_self_override",
            "private_context_lock_in",
            "persona_seal",
            "verdict_authority",
        ],
        "live_execution": False,
        "authority": "actor_posture_candidate_only",
    },
    {
        "request": "memo_reentry_review",
        "owner": "aoa-memo",
        "input_boundary": "route receipt stale ttl reentry need and bounded non-durable memory intake posture",
        "output_candidate": "memo_reentry_candidate",
        "must_include": [
            "receipt_ref",
            "stale_ttl",
            "candidate_only",
            "non_durable_intake",
        ],
        "must_not_include": [
            "durable_memory_write",
            "retention_execution",
            "identity_truth_seal",
            "hidden_scheduler",
        ],
        "live_execution": False,
        "authority": "candidate_intake_only",
    },
    {
        "request": "route_integrity_review",
        "owner": "aoa-evals",
        "input_boundary": "layer selection trace boundary checks escalation basis and human review posture",
        "output_candidate": "route_integrity_candidate",
        "must_include": [
            "layer_selection_trace",
            "boundary_checks",
            "route_reason",
            "human_review_needed",
        ],
        "must_not_include": [
            "routing_sovereignty",
            "rights_grant",
            "sealed_verdict",
            "owner_override",
        ],
        "live_execution": False,
        "authority": "bounded_eval_request_only",
    },
    {
        "request": "canonical_dossier_boundary_review",
        "owner": "Tree-of-Sophia",
        "input_boundary": "canonical risk trace dossier path review requirement and no direct write boundary",
        "output_candidate": "canonical_dossier_candidate",
        "must_include": [
            "canonical_risk_trace",
            "review_path",
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
        "request": "derived_observability_review",
        "owner": "aoa-stats",
        "input_boundary": "reviewed route packets for bounded summaries only",
        "output_candidate": "context_observability_candidate",
        "must_include": [
            "derived_only",
            "source_refs",
            "non_authoritative_label",
            "review_trace",
        ],
        "must_not_include": [
            "route_verdict",
            "owner_truth",
            "rights_authority",
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
        "authority_note": "Dionysus archive is transport evidence; center may name v1.8 context routing law only",
        "stop_lines": ["no raw archive replay", "no generated clean-flow promotion"],
    },
    {
        "order": 2,
        "kind": "wave7_affect_predecessor_checked",
        "owner": "Agents-of-Abyss",
        "authority_note": "v1.7 remains predecessor law; routing may activate layers only after affect rank and rights boundaries are already candidate-bound",
        "stop_lines": ["no predecessor erasure", "no wave8 collision with arena-session law"],
    },
    {
        "order": 3,
        "kind": "context_routing_charter_requested",
        "owner": "Agents-of-Abyss",
        "authority_note": "charter is required before any owner-local routing engine policy or packet surface can land",
        "stop_lines": ["no new aoa-experience repo", "no center-created router engine"],
    },
    {
        "order": 4,
        "kind": "context_signal_collection_requested",
        "owner": "aoa-routing",
        "authority_note": "routing may collect bounded cross-layer signals but cannot author owner meaning or pull hidden context",
        "stop_lines": ["no hidden context pull", "no owner meaning theft"],
    },
    {
        "order": 5,
        "kind": "salience_and_budget_review_requested",
        "owner": "aoa-routing",
        "authority_note": "salience and budget may prioritize layers but can never become authority or budgetless expansion",
        "stop_lines": ["no budgetless expansion", "no salience as authority"],
    },
    {
        "order": 6,
        "kind": "assistant_and_personal_context_boundary_checked",
        "owner": "aoa-agents",
        "authority_note": "assistant scope and personal context minimization stay actor-bound and reversible never self-authorizing",
        "stop_lines": ["no assistant context expansion", "no personal context overreach"],
    },
    {
        "order": 7,
        "kind": "context_bundle_boundary_checked",
        "owner": "aoa-evals",
        "authority_note": "route bundles require traceable reasons layer selection boundary checks and receipt expectation before legitimacy can advance",
        "stop_lines": ["no bundle without reason", "no bundle without receipt"],
    },
    {
        "order": 8,
        "kind": "service_vs_agon_route_gate_checked",
        "owner": "aoa-evals",
        "authority_note": "service stays service until lawful trigger review; routing may point toward Agon but cannot grant rights verdict or protocol open",
        "stop_lines": ["no service-to-agon without trigger", "no affect or rank direct rights route"],
    },
    {
        "order": 9,
        "kind": "memo_reentry_candidate_requested",
        "owner": "aoa-memo",
        "authority_note": "memo may receive reentry and stale-context candidates but cannot write durable memory or execute retention here",
        "stop_lines": ["no durable memory write", "no retention execution"],
    },
    {
        "order": 10,
        "kind": "canonical_dossier_boundary_checked",
        "owner": "Tree-of-Sophia",
        "authority_note": "canonical risk may route to dossier review only; there is no direct Tree-of-Sophia write or canon promotion from this center",
        "stop_lines": ["no direct Tree-of-Sophia write", "no canon promotion"],
    },
    {
        "order": 11,
        "kind": "derived_observability_candidate_requested",
        "owner": "aoa-stats",
        "authority_note": "derived dashboards may summarize route packets but cannot become route verdict or owner truth",
        "stop_lines": ["no stats as authority", "no dashboard as verdict"],
    },
    {
        "order": 12,
        "kind": "owner_landing_or_recharter_request_declared",
        "owner": "Agents-of-Abyss",
        "authority_note": "future routing work returns to owner-local landings or human recharter requests not runtime activation from the center",
        "stop_lines": ["no runtime cache or worker activation", "no hidden scheduler action"],
    },
]

EXPECTED_HARD_GUARDS = [
    "no_live_context_routing_activation",
    "no_live_runtime_activation",
    "no_live_owner_override",
    "no_new_repo_creation",
    "no_routing_without_reason_budget_and_receipt",
    "no_salience_as_authority",
    "no_codex_context_override",
    "no_assistant_context_expansion",
    "no_personal_context_overreach",
    "no_affect_or_rank_direct_rights_route",
    "no_service_to_agon_without_lawful_trigger",
    "no_direct_tree_of_sophia_write",
    "no_durable_memory_write",
    "no_runtime_cache_worker_or_scheduler_activation",
    "no_stats_memo_or_routing_as_authority",
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
        "new_repo_creation_allowed": False,
    },
    "authority_boundary": {
        "routing_authorship_of_meaning_allowed": False,
        "owner_override_allowed": False,
        "codex_context_override_allowed": False,
        "assistant_context_expansion_allowed": False,
        "personal_context_overreach_allowed": False,
        "direct_tos_write_allowed": False,
    },
    "budget_boundary": {
        "route_without_reason_allowed": False,
        "route_without_budget_allowed": False,
        "route_without_receipt_allowed": False,
        "stale_context_reuse_allowed": False,
        "route_loop_allowed": False,
        "symbolic_overreach_allowed": False,
    },
    "escalation_boundary": {
        "service_to_agon_without_trigger_allowed": False,
        "affect_to_rights_direct_route_allowed": False,
        "rank_or_closure_direct_rights_route_allowed": False,
        "canonical_risk_direct_write_allowed": False,
        "automatic_runtime_failover_allowed": False,
    },
    "memory_runtime_boundary": {
        "durable_memory_write_allowed": False,
        "retention_execution_allowed": False,
        "runtime_cache_activation_allowed": False,
        "worker_job_activation_allowed": False,
        "hidden_scheduler_allowed": False,
    },
}

EXPECTED_AUTHORITY = {
    "center_owner": "Agents-of-Abyss",
    "runtime_owner": "none",
    "human_gates_required": [
        "operator review before non-routine context layer activation",
        "owner-local routing approval before layer selection policy adoption",
        "owner-local agents approval before assistant or personal context expansion",
        "owner-local eval approval before service-to-agon escalation",
        "owner-local eval approval before rights-sensitive route gate use",
        "owner-local memo approval before reentry or stale-context intake",
        "Tree-of-Sophia review before dossier review path use",
        "runtime-owner gate before cache workers schedulers storage APIs or daemons",
    ],
    "claim_limit": "routing_may_activate_layers_but_may_not_steal_owner_meaning",
}

EXPECTED_OWNER_SPLIT = [
    "Agents-of-Abyss owns this center law predecessor mapping layer grammar hard guards and authority stop-lines.",
    "aoa-routing owns advisory route engine salience budget reroute loop-breaker and receipt mechanics only after owner-local landing.",
    "aoa-agents owns assistant and personal-context posture boundaries only.",
    "aoa-evals owns bounded route-integrity and escalation legitimacy checks only.",
    "aoa-memo owns recall re-entry and stale-context intake candidates only.",
    "aoa-stats owns derived route dashboards and layer-health summaries only.",
    "aoa-playbooks owns drills runbooks and recurring reroute choreography only.",
    "aoa-sdk owns typed route packet helpers and client seams only.",
    "aoa-kag owns derived context-route pattern candidates only.",
    "abyss-stack owns cache storage worker and runtime health surfaces only after a separate runtime-owner gate.",
    "Tree-of-Sophia owns dossier review and canonical intake through its own path only.",
    "Dionysus owns source lineage and later harvest trace only.",
    "8Dionysus owns shared-root projection law only where later workspace surfaces are affected.",
]

EXPECTED_QUARANTINED_SURFACES = [
    "context_routing_decision_v1",
    "context_route_request_v1",
    "context_route_receipt_v1",
    "context_route_state_v1",
    "context_route_trace_v1",
    "context_dashboard_v1",
    "context_layer_health_v1",
    "context_runtime_cache_record_v1",
    "context_storage_record_v1",
    "context_worker_job_v1",
    "context_boundary_verdict_bundle_v1",
    "context_route_integrity_bundle_v1",
    "context_recall_gate_decision_v1",
    "context_stale_quarantine_v1",
    "context_routing_runbook_step_v1",
    "context_route_pattern_node_v1",
]

EXPECTED_SEED_DRY_RUN_EVIDENCE = {
    "schema_example_pairs": 43,
    "json_file_count": 129,
    "archive_file_count": 267,
    "seed_tests_passed": 28,
}

DOC_REQUIRED_SNIPPETS = [
    "It is Wave 8 of the current v1.2-v2.0 planting campaign.",
    "It is not `Experience Wave VIII`;",
    "routing may activate layers; it may not steal meaning from their owners",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def expect_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise ValidationError(f"{label} must preserve the Wave 8 center contract")


def validate_doc() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")
    for snippet in DOC_REQUIRED_SNIPPETS:
        if snippet not in text:
            raise ValidationError(f"doc boundary missing required snippet: {snippet}")


def validate_payload(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    Draft202012Validator(schema).validate(payload)
    validate_doc()

    expect_equal(payload["source_seed"], SOURCE_SEED, "source_seed")
    expect_equal(payload["predecessor_surfaces"], EXPECTED_PREDECESSORS, "predecessor_surfaces")
    expect_equal(payload["context_routing_law"], EXPECTED_CONTEXT_ROUTING_LAW, "context_routing_law")
    expect_equal(payload["context_requests"], EXPECTED_REQUESTS, "context_requests")
    expect_equal(payload["routing_flow"], EXPECTED_FLOW, "routing_flow")
    expect_equal(payload["hard_guards"], EXPECTED_HARD_GUARDS, "hard_guards")
    expect_equal(payload["blocking_contracts"], EXPECTED_BLOCKING_CONTRACTS, "blocking_contracts")
    expect_equal(payload["authority"], EXPECTED_AUTHORITY, "authority")
    expect_equal(payload["owner_split"], EXPECTED_OWNER_SPLIT, "owner_split")
    expect_equal(payload["quarantined_surfaces"], EXPECTED_QUARANTINED_SURFACES, "quarantined_surfaces")
    expect_equal(payload["seed_dry_run_evidence"], EXPECTED_SEED_DRY_RUN_EVIDENCE, "seed_dry_run_evidence")


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    payload = load_json(EXAMPLE_PATH)
    validate_payload(payload, schema)
    print("ok: Experience v1.8 context routing nervous system center contract is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
