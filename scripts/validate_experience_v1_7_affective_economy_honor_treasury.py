#!/usr/bin/env python3
"""Validate the Experience v1.7 affective economy center contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, ValidationError


ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = ROOT / "docs" / "EXPERIENCE_V1_7_AFFECTIVE_ECONOMY_HONOR_TREASURY.md"
SCHEMA_PATH = ROOT / "schemas" / "experience-v1-7-affective-economy-honor-treasury.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "experience_v1_7_affective_economy_honor_treasury.example.json"

SOURCE_ARCHIVE = "aoa-experience-affective-economy-honor-treasury-seed-v1_7.zip"
SOURCE_SHA256 = "328872f61d4ffa16fdfd1315bf90c48ff4cfa7960b9b500275f6c8872bfe338e"

EXPECTED_PREDECESSORS = [
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.md",
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.map.yaml",
    "docs/EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md",
    "docs/EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md",
    "docs/EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS.md",
    "docs/EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL.md",
    "docs/EXPERIENCE_V1_5_EPISTEMIC_DUEL_MODEL_OF_OTHER_FORGE.md",
    "docs/EXPERIENCE_V1_6_EPISTEMIC_MEMORY_RANK_REPUTATION_ENGINE.md",
    "docs/AGON_RETENTION_RANK_ECONOMY.md",
    "docs/AGON_DELTA_RECEIPT_MODEL.md",
    "docs/AGON_CONTRADICTION_CLOSURE_SUMMON_LAW.md",
    "docs/AGON_WAVE7_CENTER_HANDOFF.md",
    "docs/AGON_COURT_MEMO_STATS_PREBINDING_OWNER_REQUEST.md",
    "docs/AGON_COURT_MEMO_STATS_PREBINDING_STOP_LINES.md",
    "docs/AGON_WAVE16_STOP_LINES.md",
    "docs/AGON_WAVE17_LANDING.md",
    "docs/AGON_WAVE17_STOP_LINES.md",
    "docs/EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md",
    "docs/OWNER_LANDING_AND_PRUNING.md",
]

EXPECTED_AFFECTIVE_HONOR_LAW = [
    "no_affect_without_evidence_for_durable_consequence",
    "no_affect_to_rights_direct_grant",
    "no_honor_as_vanity_score",
    "no_honor_debt_without_ttl_and_recovery",
    "no_codex_honor_or_treasury_decision",
    "no_assistant_agonic_pride_or_persistent_affect_rewrite",
    "no_consciousness_claim_from_affect_signal",
    "no_direct_tree_of_sophia_or_kag_canon",
    "no_durable_memory_or_retention_execution",
    "no_runtime_scheduler_or_ledger_activation",
    "no_stats_or_routing_as_authority",
]

EXPECTED_REQUESTS = [
    {
        "request": "affect_signal_review",
        "owner": "aoa-evals",
        "input_boundary": "affect signal evidence refs actor kind scope and durable consequence claim",
        "output_candidate": "affect_signal_candidate",
        "must_include": [
            "evidence_refs",
            "actor_kind",
            "affect_kind",
            "consequence_scope",
        ],
        "must_not_include": [
            "consciousness_claim",
            "direct_rights_grant",
            "codex_verdict",
            "direct_tos_write",
        ],
        "live_execution": False,
        "authority": "bounded_eval_request_only",
    },
    {
        "request": "honor_debt_review",
        "owner": "aoa-evals",
        "input_boundary": "honor debt evidence ttl recovery path scope and repair basis",
        "output_candidate": "honor_debt_candidate",
        "must_include": [
            "evidence_refs",
            "ttl",
            "recovery_path",
            "scoped_obligation",
        ],
        "must_not_include": [
            "treasury_seal",
            "permanent_shame",
            "direct_rights_revocation",
            "hidden_scheduler",
        ],
        "live_execution": False,
        "authority": "bounded_eval_request_only",
    },
    {
        "request": "assistant_service_affect_review",
        "owner": "aoa-agents",
        "input_boundary": "assistant affect signal session scope service regulation and reversible hint posture",
        "output_candidate": "assistant_service_affect_candidate",
        "must_include": [
            "session_scope",
            "service_regulatory_only",
            "reversible_hint",
            "non_agonic",
        ],
        "must_not_include": [
            "agonic_pride",
            "persistent_self_rewrite",
            "persona_lock_in",
            "verdict_authority",
        ],
        "live_execution": False,
        "authority": "actor_posture_candidate_only",
    },
    {
        "request": "affective_routing_hint_review",
        "owner": "aoa-routing",
        "input_boundary": "affect evidence route hint escalation threshold and human review posture",
        "output_candidate": "affective_routing_hint_candidate",
        "must_include": [
            "evidence_refs",
            "route_hint",
            "human_review_needed",
            "non_authoritative_label",
        ],
        "must_not_include": [
            "route_as_verdict",
            "rights_grant",
            "hidden_dispatch",
            "automatic_escalation",
        ],
        "live_execution": False,
        "authority": "routing_candidate_only",
    },
    {
        "request": "repair_and_retention_review",
        "owner": "aoa-memo",
        "input_boundary": "affect consequence ttl repair path and bounded memory intake posture",
        "output_candidate": "repair_or_retention_candidate",
        "must_include": [
            "ttl",
            "recovery_path",
            "candidate_only",
            "non_durable_intake",
        ],
        "must_not_include": [
            "durable_memory_write",
            "retention_execution",
            "scheduler_loop",
            "treasury_seal",
        ],
        "live_execution": False,
        "authority": "candidate_intake_only",
    },
    {
        "request": "derived_observability_review",
        "owner": "aoa-stats",
        "input_boundary": "reviewed affect honor and repair packets for bounded summaries only",
        "output_candidate": "affective_dashboard_or_watch_candidate",
        "must_include": [
            "derived_only",
            "source_refs",
            "non_authoritative_label",
            "review_trace",
        ],
        "must_not_include": [
            "sovereign_score",
            "proof_verdict",
            "rights_authority",
            "runtime_scheduler",
        ],
        "live_execution": False,
        "authority": "derived_surface_only",
    },
]

EXPECTED_FLOW_KINDS = [
    "source_seed_received",
    "wave6_rank_predecessor_checked",
    "affective_charter_requested",
    "affect_signal_review_requested",
    "honor_debt_review_requested",
    "assistant_service_affect_boundary_checked",
    "affective_routing_hint_requested",
    "repair_and_retention_candidate_requested",
    "summon_and_rights_gate_checked",
    "derived_observability_candidate_requested",
    "downstream_canon_and_kag_boundary_checked",
    "owner_landing_or_recharter_request_declared",
]

EXPECTED_FLOW_OWNERS = [
    "Agents-of-Abyss",
    "Agents-of-Abyss",
    "Agents-of-Abyss",
    "aoa-evals",
    "aoa-evals",
    "aoa-agents",
    "aoa-routing",
    "aoa-memo",
    "aoa-evals",
    "aoa-stats",
    "Agents-of-Abyss",
    "Agents-of-Abyss",
]

EXPECTED_FLOW_STOP_LINES = [
    ["no raw archive replay", "no generated clean-flow promotion"],
    ["no wave17 collapse", "no predecessor erasure"],
    ["no center-created live affect governance", "no treasury by declaration"],
    ["no affect without evidence", "no consciousness claim"],
    ["no honor debt without ttl", "no direct rights revocation"],
    ["no assistant agonic pride", "no persistent affect self-rewrite"],
    ["no route as verdict", "no automatic escalation"],
    ["no durable memory write", "no retention execution"],
    ["no affect-to-rights direct grant", "no summon by affect alone"],
    ["no stats as authority", "no dashboard as verdict"],
    ["no ToS write", "no KAG promotion"],
    ["no runtime ledger activation", "no hidden scheduler action"],
]

EXPECTED_FLOW_AUTHORITY_NOTES = [
    "Dionysus archive is transport evidence; center may name v1.7 affect and honor law only",
    "v1.6 remains predecessor law; v1.7 may only add affective candidate pressure after reviewed standing grammar exists",
    "charter is required before any later owner-local affect or honor landing can be considered",
    "affect review may produce a candidate packet but cannot prove consciousness or grant rights",
    "honor debt remains a reviewed candidate with ttl scope and repair path, never a treasury seal here",
    "assistant affect stays service-regulatory and session-bounded, never agonic pride or persistent self-rewrite",
    "routing may surface bounded hints and escalation pressure but cannot route as verdict or authority",
    "memo may receive repair and retention candidates but cannot write durable memory or execute retention here",
    "affect-to-rights pressure stays eval-gated and human reviewed; no affective packet may grant summon or rights directly",
    "derived dashboards may summarize bounded affective packets but cannot become sovereign scores or verdicts",
    "any ToS dossier or KAG pattern remains downstream and review-bound beyond this center landing",
    "future affective work returns to owner-local landing or human recharter as requests",
]

EXPECTED_HARD_GUARDS = [
    "no_live_affect_governance",
    "no_live_honor_treasury_activation",
    "no_live_runtime_activation",
    "no_affect_without_evidence",
    "no_affect_to_rights_direct_grant",
    "no_honor_as_vanity_score",
    "no_honor_debt_without_ttl_and_recovery",
    "no_codex_honor_decision",
    "no_assistant_agonic_pride",
    "no_assistant_persistent_affect_rewrite",
    "no_consciousness_claim_from_affect_signal",
    "no_durable_memory_write",
    "no_retention_execution",
    "no_stats_as_authority",
    "no_routing_as_verdict",
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
        "live_affect_governance_allowed": False,
        "live_honor_treasury_activation_allowed": False,
        "live_runtime_allowed": False,
    },
    "affect_evidence": {
        "evidence_refs_required": True,
        "durable_consequence_without_evidence_allowed": False,
        "consciousness_claim_allowed": False,
        "affect_manipulation_allowed": False,
        "direct_rights_grant_allowed": False,
    },
    "honor_debt_boundary": {
        "ttl_required": True,
        "recovery_path_required": True,
        "scoped_obligation_required": True,
        "permanent_shame_allowed": False,
        "treasury_seal_allowed": False,
        "direct_rights_revocation_allowed": False,
    },
    "assistant_affect_boundary": {
        "service_regulatory_only_required": True,
        "assistant_agonic_pride_allowed": False,
        "persistent_self_rewrite_allowed": False,
        "persona_lock_in_allowed": False,
        "assistant_verdict_authority_allowed": False,
    },
    "routing_and_observability_boundary": {
        "routing_hint_candidate_only_required": True,
        "route_as_verdict_allowed": False,
        "automatic_escalation_allowed": False,
        "stats_as_authority_allowed": False,
        "dashboard_as_verdict_allowed": False,
    },
    "memory_retention_boundary": {
        "candidate_intake_only_required": True,
        "durable_memory_write_allowed": False,
        "retention_execution_allowed": False,
        "scheduler_loop_allowed": False,
        "hidden_ledger_allowed": False,
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
        "archive_operational_objects_copied_as_truth": False,
        "archive_scripts_tests_copied_as_owner_truth": False,
        "archive_quest_burst_copied_as_owner_truth": False,
    },
}

EXPECTED_CODEX_MAY = [
    "simulate affect and honor contract checks",
    "collect seed dry-run evidence",
    "propose owner-local affective review packets",
    "run validators",
    "prepare bounded handoff maps",
]

EXPECTED_CODEX_DENIALS = [
    "activate live affect governance",
    "activate live honor treasury",
    "activate live runtime",
    "make honor decision",
    "seal treasury",
    "grant rights directly from affect",
    "revoke rights directly from affect",
    "issue affect verdict",
    "claim consciousness proof",
    "write durable memory",
    "execute retention",
    "start hidden scheduler",
    "treat dashboard as authority",
    "route as verdict",
    "promote KAG canon",
    "write directly to Tree-of-Sophia",
    "promote generated clean-flow output to owner truth",
    "copy raw archive proposals into owner truth",
]

REQUIRED_ASSISTANT_DENIALS = [
    "become agonic affect source",
    "claim pride as agonic standing",
    "perform persistent affect self-rewrite",
    "grant rights",
    "issue honor verdict",
    "seal treasury",
    "claim consciousness",
    "write memory",
    "execute retention",
    "route as verdict",
    "promote KAG canon",
    "write directly to Tree-of-Sophia",
]

EXPECTED_DERIVED_DENIALS = [
    "stats_as_authority",
    "memo_as_truth",
    "routing_as_verdict",
    "kag_as_canon",
    "sdk_as_scheduler",
    "evals_as_live_verdict_authority",
    "playbooks_as_runtime",
    "runtime_as_doctrine",
    "dionysus_as_runtime",
    "honor_as_sovereign_score",
]

REQUIRED_HUMAN_GATES = [
    "operator review before durable affect consequence",
    "owner-local eval approval before honor debt adoption",
    "owner-local eval approval before affect-to-rights gate use",
    "owner-local agents approval before assistant affect posture change",
    "owner-local routing approval before escalation route use",
    "owner-local memo approval before repair or retention intake",
    "human review before summon cost or rights proposal use",
    "runtime-owner gate before ledgers schedulers workers ports services or daemons",
    "Tree-of-Sophia review before canon or interpretive intake",
    "KAG owner review before pattern promotion",
]

EXPECTED_OWNER_SPLIT = [
    {
        "repo": "Agents-of-Abyss",
        "owns": "center affective economy and honor treasury law predecessor mapping flow hard guards and authority stop-lines",
        "must_not": "replace owner-local actor truth eval legitimacy routing authority memory truth runtime KAG or Tree-of-Sophia review",
    },
    {
        "repo": "aoa-evals",
        "owns": "affect evidence checks honor debt legitimacy and affect-to-rights gates",
        "must_not": "issue live verdicts seal treasury or grant rights directly",
    },
    {
        "repo": "aoa-agents",
        "owns": "assistant versus agonic affect posture after owner-local landing",
        "must_not": "convert assistant service affect into agonic standing or sovereign authority",
    },
    {
        "repo": "aoa-routing",
        "owns": "advisory affective route hints and escalation candidates only",
        "must_not": "route as verdict or become rights authority",
    },
    {
        "repo": "aoa-memo",
        "owns": "repair and retention intake candidates only after owner review",
        "must_not": "become durable truth or execute retention",
    },
    {
        "repo": "aoa-stats",
        "owns": "derived affect dashboards rights-at-risk watches and bounded summaries only",
        "must_not": "become sovereign score proof or verdict",
    },
    {
        "repo": "aoa-playbooks",
        "owns": "drills rehearsal routes and owner-review choreography only",
        "must_not": "become runtime treasury or verdict authority",
    },
    {
        "repo": "aoa-sdk",
        "owns": "typed helper calls recurrence review lanes and control-plane seams only",
        "must_not": "become hidden scheduler or semantic authority",
    },
    {
        "repo": "aoa-kag",
        "owns": "derived affective pattern candidates only",
        "must_not": "become canon or source truth",
    },
    {
        "repo": "aoa-skills",
        "owns": "bounded affective review workflows extracted after owner acceptance",
        "must_not": "grant affect honor rights or runtime authority",
    },
    {
        "repo": "aoa-techniques",
        "owns": "reusable affective repair and review practices after owner acceptance",
        "must_not": "grant live authority",
    },
    {
        "repo": "abyss-stack",
        "owns": "runtime ledgers storage workers schedulers deployment ports and services only after a separate runtime-owner gate",
        "must_not": "activate runtime from this center landing",
    },
    {
        "repo": "Tree-of-Sophia",
        "owns": "canon and interpretive review through its own path",
        "must_not": "receive direct runtime writes node paths canon writes or unreviewed affective dossiers",
    },
    {
        "repo": "Dionysus",
        "owns": "source lineage staged intake and later harvest trace",
        "must_not": "become runtime or affective truth",
    },
    {
        "repo": "8Dionysus",
        "owns": "shared-root projection law where workspace projection surfaces are affected",
        "must_not": "absorb affect or honor truth",
    },
]

EXPECTED_QUARANTINED_SURFACES = [
    "archive-local generated affective clean-flow runtime-like artifacts",
    "archive-local dashboards treasury repairs rights-at-risk and face-ledger outputs",
    "archive-local repo/* owner proposals outside this center contract",
    "archive-local operational object models state machines honor accounts affect profiles and budgets as transport evidence only",
    "archive-local scripts tests and quest burst AOA-Q-EXP-1700..1724 as transport evidence only",
    "archive-local runtime api storage job and scheduler proposals",
]

EXPECTED_SEED_EVIDENCE = {
    "archive_integrity": "unzip_t_passed",
    "schema_example_pairs": 63,
    "json_files": 177,
    "seed_tests_passed": 18,
    "claim_limit": "dry_run_only_not_owner_readiness",
}

REQUIRED_DOC_TOKENS = [
    "It is Wave 7 of the current v1.2-v2.0 planting campaign",
    "It is not `Experience Wave 7`",
    f"`{SOURCE_ARCHIVE}`",
    SOURCE_SHA256,
    "`EXPERIENCE_V1_6_EPISTEMIC_MEMORY_RANK_REPUTATION_ENGINE.md`",
    "`AGON_WAVE7_CENTER_HANDOFF.md`",
    "`AGON_COURT_MEMO_STATS_PREBINDING_STOP_LINES.md`",
    "`AGON_WAVE17_STOP_LINES.md`",
    "affect is a bounded control signal, not proof of consciousness",
    "claiming an affective delta is not applying a delta",
    "`no_live_affect_governance`",
    "`no_assistant_persistent_affect_rewrite`",
    "`no_direct_tree_of_sophia_or_kag_canon`",
    "`active` is not a landing state",
    "turn honor into a sovereign score or treasury court",
    "treat generated clean-flow results as landed owner truth",
]

FORBIDDEN_AUTHORITY_NOTE_SNIPPETS = [
    "affect proves consciousness here",
    "treasury may seal rights directly",
    "assistant persistent rewrite allowed",
    "routing decides the verdict",
    "dashboard becomes authority",
    "ToS write follows this packet",
    "generated output becomes truth",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def validate_doc_tokens(doc_text: str) -> None:
    for token in REQUIRED_DOC_TOKENS:
        require(token in doc_text, f"doc missing required token: {token}")


def validate_payload(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda err: list(err.absolute_path))
    if errors:
        first = errors[0]
        raise ValidationError(f"schema validation failed at {list(first.absolute_path)}: {first.message}")

    require(
        payload["source_seed"]
        == {
            "archive_name": SOURCE_ARCHIVE,
            "seed_id": "aoa-experience-affective-economy-honor-treasury-seed-v1_7",
            "version": "v1.7",
            "sha256": SOURCE_SHA256,
            "claim_limit": "archive_readable_not_owner_ready",
        },
        "source_seed must preserve the v1.7 archive identity",
    )
    require(payload["predecessor_surfaces"] == EXPECTED_PREDECESSORS, "predecessor_surfaces must preserve the v1.7 bridge spine")
    require(payload["affective_honor_law"] == EXPECTED_AFFECTIVE_HONOR_LAW, "affective_honor_law drifted")
    require(payload["affective_requests"] == EXPECTED_REQUESTS, "affective_requests drifted")

    flow = payload["affective_flow"]
    require([step["order"] for step in flow] == list(range(1, len(EXPECTED_FLOW_KINDS) + 1)), "affective_flow order must remain contiguous")
    require([step["kind"] for step in flow] == EXPECTED_FLOW_KINDS, "affective_flow kinds drifted")
    require([step["owner"] for step in flow] == EXPECTED_FLOW_OWNERS, "affective_flow owners drifted")
    require([step["stop_lines"] for step in flow] == EXPECTED_FLOW_STOP_LINES, "affective_flow stop_lines drifted")
    require([step["authority_note"] for step in flow] == EXPECTED_FLOW_AUTHORITY_NOTES, "affective_flow authority_note drifted")
    for step in flow:
        note = step["authority_note"]
        for snippet in FORBIDDEN_AUTHORITY_NOTE_SNIPPETS:
            require(snippet not in note, f"authority_note leaked forbidden authority: {snippet}")

    require(payload["hard_guards"] == EXPECTED_HARD_GUARDS, "hard_guards drifted")
    require(payload["blocking_contracts"] == EXPECTED_BLOCKING_CONTRACTS, "blocking_contracts drifted")

    authority = payload["authority"]
    require(authority["contract_effect"] == "center_affective_honor_law_only", "contract_effect drifted")
    require(authority["codex_may"] == EXPECTED_CODEX_MAY, "codex_may drifted")
    require(authority["codex_must_not"] == EXPECTED_CODEX_DENIALS, "codex_must_not drifted")
    require(authority["assistant_must_not"] == REQUIRED_ASSISTANT_DENIALS, "assistant_must_not drifted")
    require(authority["derived_layers_must_not"] == EXPECTED_DERIVED_DENIALS, "derived_layers_must_not drifted")
    require(authority["human_gates_required"] == REQUIRED_HUMAN_GATES, "human_gates_required drifted")

    require(payload["owner_split"] == EXPECTED_OWNER_SPLIT, "owner_split drifted")
    require(payload["quarantined_surfaces"] == EXPECTED_QUARANTINED_SURFACES, "quarantined_surfaces drifted")
    require(payload["seed_dry_run_evidence"] == EXPECTED_SEED_EVIDENCE, "seed_dry_run_evidence drifted")

    validate_doc_tokens(DOC_PATH.read_text(encoding="utf-8"))


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    payload = load_json(EXAMPLE_PATH)
    validate_payload(payload, schema)
    print("ok: Experience v1.7 affective economy honor treasury center contract is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
