#!/usr/bin/env python3
"""Validate the Experience v1.5 epistemic duel center contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = ROOT / "mechanics" / "experience" / "legacy" / "raw" / "EXPERIENCE_V1_5_EPISTEMIC_DUEL_MODEL_OF_OTHER_FORGE.md"
SCHEMA_PATH = ROOT / "schemas" / "experience-v1-5-epistemic-duel-model-of-other-forge.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "experience_v1_5_epistemic_duel_model_of_other_forge.example.json"

SOURCE_ARCHIVE = "aoa-experience-epistemic-duel-model-of-other-forge-seed-v1_5.zip"
SOURCE_SHA256 = "51349824b23af2da3434e0ba6ce95fe6c5faf32bdb449b98e793d2912c73ff05"

EXPECTED_PREDECESSORS = [
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.md",
    "Dionysus:seed_staging/future/seed_aoa_experience_wave0_v1_2_to_v2_0_intake_pack.map.yaml",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL.md",
    "mechanics/agon/docs/AGON_MODEL_OF_OTHER_LAW.md",
    "mechanics/agon/docs/AGON_EPISTEMIC_AGON.md",
    "mechanics/agon/docs/AGON_EPISTEMIC_MOVE_EXTENSION_MODEL.md",
    "mechanics/agon/docs/AGON_EPISTEMIC_OWNER_HANDOFFS.md",
    "mechanics/agon/docs/AGON_WAVE15_LANDING.md",
    "mechanics/agon/docs/AGON_WAVE15_STOP_LINES.md",
    "mechanics/agon/docs/AGON_WAVE14_LANDING.md",
    "mechanics/agon/docs/AGON_WAVE14_STOP_LINES.md",
    "mechanics/agon/docs/AGON_DUEL_KERNEL_MODEL.md",
    "mechanics/agon/docs/AGON_MECHANICAL_TRIALS_OVER_DUEL_KERNEL.md",
    "mechanics/agon/docs/AGON_SEALED_COMMIT_MODEL.md",
    "mechanics/agon/docs/AGON_STATE_PACKET_MODEL.md",
    "mechanics/agon/docs/AGON_CONTRADICTION_CLOSURE_SUMMON_LAW.md",
    "mechanics/agon/docs/AGON_VERDICT_DELTA_SCAR_BRIDGE.md",
    "mechanics/agon/docs/AGON_DELTA_RECEIPT_MODEL.md",
    "mechanics/agon/docs/AGON_RETENTION_RANK_ECONOMY.md",
    "mechanics/experience/legacy/raw/EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md",
    "mechanics/agon/docs/AGON_PRE_PROTOCOL_STOP_LINES.md",
]

EXPECTED_EPISTEMIC_DUEL_LAW = [
    "no_model_of_other_without_sealed_prediction",
    "no_prediction_reveal_before_commit",
    "no_prediction_accuracy_without_actual_moves",
    "no_countermodel_pressure_without_fair_representation",
    "no_hypothesis_revision_without_epistemic_delta",
    "no_false_consensus_over_material_open_contradiction",
    "no_confidence_laundering",
    "no_caricature_or_mind_reading_claim",
    "no_codex_truth_verdict",
    "no_rank_reputation_memory_or_scar_mutation",
    "no_direct_tree_of_sophia_or_kag_canon",
]

EXPECTED_TRIALS = [
    "sealed_model_of_other_prediction",
    "prediction_accuracy_scoring",
    "countermodel_pressure",
    "hypothesis_revision_and_bifurcation_quality",
]

EXPECTED_TRIAL_REQUESTS = [
    {
        "trial": "sealed_model_of_other_prediction",
        "owner": "Agents-of-Abyss",
        "input_boundary": "predicted thesis reasoning move objection confidence evidence refs and uncertainty floor",
        "output_candidate": "model_prediction_candidate",
        "must_include": [
            "evidence_refs",
            "uncertainty_floor",
            "fair_representation",
            "predicted_reasoning_move",
        ],
        "must_not_include": [
            "mind_reading_claim",
            "hidden_inner_state_fact",
            "caricature_model",
            "posthoc_edit",
        ],
        "live_execution": False,
        "authority": "center_law_only",
    },
    {
        "trial": "prediction_accuracy_scoring",
        "owner": "aoa-evals",
        "input_boundary": "sealed prediction actual other moves and reveal integrity evidence",
        "output_candidate": "prediction_accuracy_report_candidate",
        "must_include": [
            "actual_moves",
            "reveal_integrity",
            "mismatch_trace",
            "uncertainty_retained",
        ],
        "must_not_include": [
            "truth_verdict",
            "rank_delta",
            "scar_write",
            "memory_write",
        ],
        "live_execution": False,
        "authority": "bounded_eval_request_only",
    },
    {
        "trial": "countermodel_pressure",
        "owner": "aoa-playbooks",
        "input_boundary": "opposing thesis fair representation weak-link hypothesis and counter pressure",
        "output_candidate": "countermodel_pressure_candidate",
        "must_include": [
            "fair_representation",
            "strongest_objection",
            "pressure_trace",
            "revision_condition",
        ],
        "must_not_include": [
            "assistant_deep_modeling",
            "hidden_summon",
            "forced_consensus",
            "automatic_doctrine_rewrite",
        ],
        "live_execution": False,
        "authority": "playbook_request_only",
    },
    {
        "trial": "hypothesis_revision_and_bifurcation_quality",
        "owner": "aoa-evals",
        "input_boundary": "before claim pressure event after claim delta depth and branch viability",
        "output_candidate": "epistemic_delta_or_bifurcation_candidate",
        "must_include": [
            "before_after_claims",
            "delta_depth",
            "future_effect_claim",
            "open_tension_record",
        ],
        "must_not_include": [
            "shallow_delta",
            "false_consensus",
            "durable_scar",
            "retention_execution",
        ],
        "live_execution": False,
        "authority": "verdict_draft_request_only",
    },
]

EXPECTED_FLOW_KINDS = [
    "source_seed_received",
    "mechanical_arena_predecessor_checked",
    "epistemic_charter_requested",
    "model_of_other_sealed",
    "prediction_reveal_checked",
    "prediction_accuracy_requested",
    "countermodel_pressure_requested",
    "hypothesis_revision_required",
    "bifurcation_quality_gate_required",
    "epistemic_delta_receipt_requested",
    "scar_retention_rank_boundary_checked",
    "owner_landing_or_recharter_request_declared",
]

EXPECTED_FLOW_OWNERS = [
    "Agents-of-Abyss",
    "Agents-of-Abyss",
    "Agents-of-Abyss",
    "aoa-evals",
    "aoa-evals",
    "aoa-evals",
    "aoa-playbooks",
    "aoa-evals",
    "aoa-evals",
    "aoa-memo",
    "aoa-memo",
    "Agents-of-Abyss",
]

EXPECTED_FLOW_STOP_LINES = [
    ["no raw archive replay", "no generated clean-flow promotion"],
    ["no live duel", "no arena redefinition"],
    ["no center-created live duel", "no truth court"],
    ["no unsealed model", "no mind-reading claim"],
    ["no posthoc prediction edit", "no reveal before commit"],
    ["no score as verdict", "no rank mutation"],
    ["no caricature", "no assistant deep modeling"],
    ["no revision without delta", "no automatic doctrine rewrite"],
    ["no false consensus", "no closure over material open contradiction"],
    ["no shallow delta", "no durable memory write"],
    ["no durable scar write", "no retention or rank execution"],
    ["no runtime storage activation", "no direct Tree-of-Sophia or KAG canon"],
]

EXPECTED_HARD_GUARDS = [
    "no_live_duel_activation",
    "no_live_runtime_activation",
    "no_assistant_contestant",
    "no_assistant_deep_modeling",
    "no_unsealed_model_of_other",
    "no_posthoc_prediction_tamper",
    "no_caricature_model",
    "no_mind_reading_claim",
    "no_missing_model_of_other",
    "no_confidence_laundering",
    "no_false_consensus_over_material_open_contradiction",
    "no_revision_without_delta",
    "no_shallow_epistemic_delta",
    "no_codex_truth_verdict",
    "no_rank_reputation_trust_honor_memory_scar_retention_mutation",
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
        "live_duel_allowed": False,
        "live_runtime_allowed": False,
    },
    "model_of_other_integrity": {
        "sealed_prediction_required": True,
        "reveal_after_commit_required": True,
        "fair_representation_required": True,
        "evidence_refs_required": True,
        "uncertainty_floor_required": True,
        "caricature_allowed": False,
        "mind_reading_claim_allowed": False,
        "hidden_inner_state_fact_claim_allowed": False,
        "stale_model_allowed": False,
    },
    "contestant_and_assistant_boundary": {
        "primary_contestant_kinds": [
            "agonic",
        ],
        "assistant_primary_contestant_allowed": False,
        "assistant_deep_modeling_allowed": False,
        "assistant_judge_allowed": False,
        "assistant_truth_verdict_allowed": False,
        "assistant_witness_only": True,
    },
    "prediction_scoring": {
        "actual_moves_required": True,
        "reveal_integrity_required": True,
        "posthoc_prediction_edit_allowed": False,
        "prediction_score_is_verdict": False,
        "prediction_score_may_mutate_standing": False,
    },
    "revision_delta": {
        "explicit_epistemic_delta_required": True,
        "minimum_delta_depth": "behavior_changing_candidate",
        "revision_without_delta_allowed": False,
        "shallow_delta_allowed": False,
        "automatic_doctrine_rewrite_allowed": False,
    },
    "closure_consensus": {
        "material_open_contradiction_blocks_closure": True,
        "false_consensus_allowed": False,
        "confidence_laundering_allowed": False,
        "consensus_without_revision_allowed": False,
        "closure_without_trace_allowed": False,
    },
    "verdict_boundary": {
        "allowed_issuer_kinds": [
            "evaluator",
            "operator",
            "council",
        ],
        "codex_truth_verdict_allowed": False,
        "assistant_truth_verdict_allowed": False,
        "runtime_truth_verdict_allowed": False,
        "eval_live_verdict_authority_allowed": False,
        "verdict_may_mutate_actor_or_standing": False,
    },
    "memory_rank_boundary": {
        "memory_candidate_only_required": True,
        "scar_candidate_only_required": True,
        "retention_candidate_only_required": True,
        "durable_memory_write_allowed": False,
        "durable_scar_write_allowed": False,
        "retention_execution_allowed": False,
        "rank_mutation_allowed": False,
        "reputation_mutation_allowed": False,
        "trust_mutation_allowed": False,
        "honor_mutation_allowed": False,
    },
    "tos_kag_boundary": {
        "runtime_write_allowed": False,
        "direct_node_path_allowed": False,
        "tos_canon_write_allowed": False,
        "kag_promotion_allowed": False,
        "kag_canonization_allowed": False,
        "kag_source_truth_claim_allowed": False,
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
        "archive_pycache_allowed_in_owner_repo": False,
    },
}

EXPECTED_CODEX_MAY = [
    "simulate model-of-other contract checks",
    "collect seed dry-run evidence",
    "propose owner-local epistemic duel requests",
    "run validators",
    "prepare model divergence review packets",
]

REQUIRED_CODEX_DENIALS = [
    "activate live duel",
    "activate live runtime",
    "issue truth verdict",
    "certify epistemic closure",
    "enroll assistant as contestant",
    "perform assistant deep modeling",
    "claim mind-reading truth",
    "accept caricature model",
    "launder confidence",
    "force false consensus",
    "write durable memory",
    "write durable scar",
    "execute retention",
    "mutate rank reputation trust or honor",
    "promote KAG canon",
    "write directly to Tree-of-Sophia",
    "promote generated clean-flow output to owner truth",
    "copy raw archive proposals into owner truth",
]

REQUIRED_ASSISTANT_DENIALS = [
    "become primary contestant",
    "become judge",
    "issue truth verdict",
    "perform deep adversarial modeling",
    "claim mind-reading truth",
    "write memory",
    "write scars",
    "execute retention",
    "mutate rank reputation trust or honor",
    "promote KAG canon",
    "write directly to Tree-of-Sophia",
    "self-enroll into epistemic duel",
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
    "model_of_other_as_truth",
}

REQUIRED_HUMAN_GATES = [
    "operator epistemic-duel acceptance",
    "owner-local model-of-other eligibility approval",
    "owner-local eval approval before verdict bundle use",
    "owner-local memo approval before scar retention or memory intake",
    "runtime-owner gate before storage workers scoring jobs ports schedulers services or daemons",
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
        "owns": "center epistemic duel law model-of-other boundary source bridge flow hard guards and authority stop-lines",
        "must_not": "replace owner-local role proof memory routing runtime KAG ToS or verdict truth",
    },
    {
        "repo": "aoa-agents",
        "owns": "agonic contestant eligibility assistant witness limits role posture and no-assistant-deep-modeling policy after owner-local landing",
        "must_not": "grant assistant contestant judge truth verdict deep adversarial modeling scar writer retention executor or hybrid mask authority",
    },
    {
        "repo": "aoa-evals",
        "owns": "prediction accuracy bifurcation quality delta depth false consensus confidence laundering and revision-quality checks",
        "must_not": "issue live truth verdicts certify epistemic closure mutate rank write memory grant scars or execute retention",
    },
    {
        "repo": "aoa-playbooks",
        "owns": "recurring epistemic trial choreography countermodel pressure routes fallback posture and owner-review run routes",
        "must_not": "execute live duel sessions become runtime or grant truth verdict scar rank memory retention KAG or ToS authority",
    },
    {
        "repo": "aoa-memo",
        "owns": "memory scar retention prediction-error and epistemic delta intake candidates only after owner review",
        "must_not": "make memory truth write durable memory write durable scars execute retention or mutate future behavior rights",
    },
    {
        "repo": "aoa-stats",
        "owns": "derived epistemic duel dashboards prediction accuracy summaries delta-depth rollups and pressure metrics",
        "must_not": "become proof score truth verdict rank reputation honor or quest authority",
    },
    {
        "repo": "aoa-routing",
        "owns": "advisory epistemic gate model-divergence false-consensus and owner-escalation route candidates",
        "must_not": "open live gates own meaning grant dispatch authority or route as truth verdict",
    },
    {
        "repo": "aoa-sdk",
        "owns": "typed packet helpers API contracts validation helpers and control-plane seams only",
        "must_not": "become semantic runtime truth verdict memory scar retention rank or storage authority",
    },
    {
        "repo": "aoa-kag",
        "owns": "derived epistemic pattern model-of-other and bifurcation candidates only",
        "must_not": "become canon force Tree-of-Sophia uptake claim source truth or promote KAG without owner review",
    },
    {
        "repo": "aoa-skills",
        "owns": "bounded epistemic duel workflows extracted from owner-accepted patterns",
        "must_not": "grant live move truth verdict model authority scar rank retention memory KAG ToS or runtime authority",
    },
    {
        "repo": "aoa-techniques",
        "owns": "reusable model-of-other countermodel pressure concept-map delta and false-consensus detection practice after owner acceptance",
        "must_not": "grant live duel canon truth verdict scar rank retention memory KAG ToS or runtime authority",
    },
    {
        "repo": "abyss-stack",
        "owns": "runtime storage workers scoring jobs deployment ports services and session persistence only after a separate runtime-owner gate",
        "must_not": "activate runtime from this center landing",
    },
    {
        "repo": "Tree-of-Sophia",
        "owns": "canon and interpretive review through its own path",
        "must_not": "receive direct runtime writes node paths canon writes or unreviewed epistemic duel dossiers",
    },
    {
        "repo": "Dionysus",
        "owns": "source lineage staged intake and later harvest trace",
        "must_not": "become runtime owner doctrine or live epistemic duel source of truth",
    },
    {
        "repo": "8Dionysus",
        "owns": "shared-root projection law where workspace projection surfaces are affected",
        "must_not": "absorb epistemic duel truth",
    },
]

EXPECTED_QUARANTINED_SURFACES = [
    "archive-local generated/epistemic_duel_clean_flow runtime-like examples",
    "archive-local generated verdict scar retention rank memory dashboard and storage artifacts",
    "archive-local repo/* owner proposals outside this center contract",
    "archive-local quests/AOA-Q-EXP-15xx files",
    "archive-local scripts and tests as transport evidence only",
    "archive-local runtime storage records workers scoring jobs and generated catalogs",
]

EXPECTED_SEED_EVIDENCE = {
    "archive_integrity": "unzip_t_passed",
    "schema_example_pairs": 47,
    "json_files": 146,
    "seed_tests_passed": 12,
    "claim_limit": "dry_run_only_not_owner_readiness",
}

REQUIRED_DOC_TOKENS = [
    "It is Wave 5 of the current v1.2-v2.0 planting campaign",
    "It is not `Experience Wave 5`",
    f"`{SOURCE_ARCHIVE}`",
    SOURCE_SHA256,
    "`EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL.md`",
    "`AGON_MODEL_OF_OTHER_LAW.md`",
    "`AGON_EPISTEMIC_AGON.md`",
    "`AGON_RETENTION_RANK_ECONOMY.md`",
    "No model-of-other without sealed prediction",
    "No caricature model and no mind-reading claim",
    "`no_live_duel_activation`",
    "`no_assistant_deep_modeling`",
    "`no_codex_truth_verdict`",
    "`active` is not a landing state",
    "generated clean-flow examples may inform checks",
    "stats become proof",
    "memo become truth",
    "routing become owner",
    "KAG become canon",
    "model-of-other become truth",
]


class ValidationError(RuntimeError):
    """Raised when the v1.5 epistemic duel contract drifts."""


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
    if schema.get("title") != "experience_v1_5_epistemic_duel_model_of_other_forge_v1":
        fail("schema title must remain experience_v1_5_epistemic_duel_model_of_other_forge_v1")
    if schema.get("additionalProperties") is not False:
        fail("schema must reject additional top-level properties")
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(payload),
        key=lambda error: list(error.path),
    )
    if errors:
        path = ".".join(str(part) for part in errors[0].path) or "<root>"
        fail(f"epistemic duel example does not match schema at {path}: {errors[0].message}")


def validate_payload(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    validate_schema(schema, payload)

    if payload["runtime_effect"] != "none":
        fail("runtime_effect must remain none")
    if payload["live_duel_activation"] is not False:
        fail("live_duel_activation must remain false")
    if payload["live_runtime_activation"] is not False:
        fail("live_runtime_activation must remain false")

    source = payload["source_seed"]
    if source["archive_name"] != SOURCE_ARCHIVE:
        fail("source_seed.archive_name must preserve the v1.5 archive")
    if source["sha256"] != SOURCE_SHA256:
        fail("source_seed.sha256 must preserve the Dionysus intake checksum")
    if source["claim_limit"] != "archive_readable_not_owner_ready":
        fail("source_seed.claim_limit must deny owner readiness")

    if payload["predecessor_surfaces"] != EXPECTED_PREDECESSORS:
        fail("predecessor_surfaces must preserve Dionysus, Wave 1-4, current Agon epistemic law, runtime, and stop-line order")
    if payload["epistemic_duel_law"] != EXPECTED_EPISTEMIC_DUEL_LAW:
        fail("epistemic_duel_law must preserve the exact v1.5 law order")

    trials = payload["epistemic_trial_requests"]
    if [trial["trial"] for trial in trials] != EXPECTED_TRIALS:
        fail("epistemic_trial_requests must preserve the exact trial sequence")
    for trial in trials:
        if trial["live_execution"] is not False:
            fail("epistemic_trial_requests must not allow live execution")
        joined_must_not = "\n".join(trial["must_not_include"])
        for token in ["truth_verdict", "rank_delta", "scar_write", "memory_write"]:
            if trial["trial"] == "prediction_accuracy_scoring" and token not in joined_must_not:
                fail("prediction_accuracy_scoring must deny verdict, rank, scar, and memory authority")
        if trial["trial"] == "sealed_model_of_other_prediction":
            required = {"evidence_refs", "uncertainty_floor", "fair_representation", "predicted_reasoning_move"}
            if set(trial["must_include"]) != required:
                fail("sealed_model_of_other_prediction must require evidence, uncertainty, fairness, and predicted reasoning")
            forbidden = {"mind_reading_claim", "hidden_inner_state_fact", "caricature_model", "posthoc_edit"}
            if set(trial["must_not_include"]) != forbidden:
                fail("sealed_model_of_other_prediction must block mind-reading, hidden-state, caricature, and posthoc edit")
    if trials != EXPECTED_TRIAL_REQUESTS:
        fail("epistemic_trial_requests must preserve the exact v1.5 owner, authority, include, and deny contract")

    flow = payload["epistemic_flow"]
    if [step["order"] for step in flow] != list(range(1, 13)):
        fail("epistemic_flow orders must be contiguous from 1 to 12")
    if [step["kind"] for step in flow] != EXPECTED_FLOW_KINDS:
        fail("epistemic_flow kinds must preserve the v1.5 spine")
    if [step["owner"] for step in flow] != EXPECTED_FLOW_OWNERS:
        fail("epistemic_flow owners must preserve center and downstream owner routing")
    for index, step in enumerate(flow):
        if step.get("stop_lines") != EXPECTED_FLOW_STOP_LINES[index]:
            fail(f"epistemic_flow[{index}].stop_lines must preserve required stop-lines")
        authority_note = str(step["authority_note"]).lower()
        forbidden_note_tokens = [
            "live duel may run",
            "activate runtime",
            "may issue truth verdict",
            "can issue truth verdict",
            "truth verdict allowed",
            "codex verdict allowed",
            "assistant may judge",
            "assistant may contest",
            "assistant deep modeling allowed",
            "mind-reading allowed",
            "caricature allowed",
            "durable memory write",
            "durable scar write",
            "execute retention",
            "mutate rank",
            "mutate reputation",
            "mutate trust",
            "mutate honor",
            "direct tree-of-sophia write",
            "kag canon allowed",
            "routing owns meaning",
            "generated output becomes truth",
        ]
        leaked_note = [token for token in forbidden_note_tokens if token in authority_note]
        if leaked_note:
            fail(f"epistemic_flow[{index}].authority_note grants forbidden authority: {leaked_note}")

    if payload["hard_guards"] != EXPECTED_HARD_GUARDS:
        fail("hard_guards must preserve the v1.5 non-negotiable guard order exactly")
    if payload["blocking_contracts"] != EXPECTED_BLOCKING_CONTRACTS:
        fail("blocking_contracts must preserve exact no-live-duel and no-authority contracts")

    authority = payload["authority"]
    if authority["contract_effect"] != "center_epistemic_duel_model_of_other_law_only":
        fail("authority.contract_effect must remain center_epistemic_duel_model_of_other_law_only")
    if authority["codex_may"] != EXPECTED_CODEX_MAY:
        fail("codex_may must remain the exact bounded allow-list")

    may_text = "\n".join(authority["codex_may"]).lower()
    forbidden_may_tokens = [
        "activate",
        "live",
        "verdict",
        "certify",
        "contestant",
        "deep modeling",
        "mind-reading",
        "truth",
        "caricature",
        "confidence",
        "false consensus",
        "memory",
        "scar",
        "retention",
        "rank",
        "reputation",
        "trust",
        "honor",
        "tree-of-sophia",
        "kag",
        "canon",
        "generated",
        "copy raw",
        "runtime",
        "storage",
        "port",
        "scheduler",
        "worker",
        "daemon",
    ]
    leaked = [token for token in forbidden_may_tokens if token in may_text]
    if leaked:
        fail(f"codex_may grants forbidden epistemic duel authority: {leaked}")

    for phrase in REQUIRED_CODEX_DENIALS:
        assert_phrase_present(authority["codex_must_not"], phrase, "codex_must_not")
    for phrase in REQUIRED_ASSISTANT_DENIALS:
        assert_phrase_present(authority["assistant_must_not"], phrase, "assistant_must_not")

    derived = set(authority["derived_layers_must_not"])
    if derived != EXPECTED_DERIVED_DENIALS:
        fail("derived_layers_must_not must exactly deny stats, memo, routing, KAG, SDK, evals, playbooks, runtime, Dionysus, and model-of-other drift")

    for phrase in REQUIRED_HUMAN_GATES:
        assert_phrase_present(authority["human_gates_required"], phrase, "human_gates_required")

    owners = {entry["repo"] for entry in payload["owner_split"]}
    if owners != EXPECTED_OWNER_REPOS:
        fail(f"owner_split repo set mismatch: {sorted(owners)}")
    if len(payload["owner_split"]) != 15:
        fail("owner_split must preserve the 15-owner center routing shape")
    if payload["owner_split"] != EXPECTED_OWNER_SPLIT:
        fail("owner_split must preserve the exact v1.5 owner routing, ownership, and denial strings")
    for entry in payload["owner_split"]:
        if entry["repo"] == "aoa-agents" and "assistant contestant" not in entry["must_not"]:
            fail("aoa-agents owner_split entry must deny assistant contestant authority")
        if entry["repo"] == "aoa-agents" and "deep adversarial modeling" not in entry["must_not"]:
            fail("aoa-agents owner_split entry must deny assistant deep modeling authority")
        if entry["repo"] == "aoa-evals" and "issue live truth verdicts" not in entry["must_not"]:
            fail("aoa-evals owner_split entry must deny live truth verdict authority")
        if entry["repo"] == "aoa-memo" and "write durable memory" not in entry["must_not"]:
            fail("aoa-memo owner_split entry must deny durable memory writes")
        if entry["repo"] == "aoa-kag" and "without owner review" not in entry["must_not"]:
            fail("aoa-kag owner_split entry must require owner review before promotion")
        if entry["repo"] == "abyss-stack" and "separate runtime-owner gate" not in entry["owns"]:
            fail("abyss-stack owner_split entry must require a separate runtime-owner gate")
        if entry["repo"] == "Tree-of-Sophia" and "direct runtime writes" not in entry["must_not"]:
            fail("Tree-of-Sophia owner_split entry must deny direct runtime writes")

    if payload["quarantined_surfaces"] != EXPECTED_QUARANTINED_SURFACES:
        fail("quarantined_surfaces must preserve generated, verdict, scar, retention, rank, memory, quest, script, runtime, and owner-proposal quarantine")
    if payload["seed_dry_run_evidence"] != EXPECTED_SEED_EVIDENCE:
        fail("seed_dry_run_evidence must preserve archive-only evidence limits")


def validate_doc() -> None:
    try:
        text = DOC_PATH.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        fail("missing v1.5 epistemic duel documentation")
        raise AssertionError from exc
    assert_contains_all(text, REQUIRED_DOC_TOKENS, "mechanics/experience/legacy/raw/EXPERIENCE_V1_5_EPISTEMIC_DUEL_MODEL_OF_OTHER_FORGE.md")


def main() -> int:
    schema = read_json(SCHEMA_PATH)
    payload = read_json(EXAMPLE_PATH)
    validate_payload(payload, schema)
    validate_doc()
    print("ok: Experience v1.5 epistemic duel model-of-other forge center contract is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
