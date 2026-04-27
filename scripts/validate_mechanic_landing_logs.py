#!/usr/bin/env python3
"""Validate mechanic landing logs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FIELDS = (
    "Status:",
    "Owner boundary:",
    "Surfaces:",
    "Validation:",
    "Stop-lines:",
    "Next route:",
)

MECHANICS: dict[str, dict[str, object]] = {
    "checkpoint": {
        "path": "mechanics/checkpoint/LANDING_LOG.md",
        "required_phrases": (
            "Center checkpoint mechanic landing",
            "center law, owner map, active parts, and owner-request",
            "no checkpoint implementation authority",
            "runtime activation or owner acceptance",
        ),
        "required_surfaces": (
            "mechanics/checkpoint/AGENTS.md",
            "mechanics/checkpoint/README.md",
            "mechanics/checkpoint/DIRECTION.md",
            "mechanics/checkpoint/PARTS.md",
            "mechanics/checkpoint/OWNER_MAP.md",
            "mechanics/checkpoint/PROVENANCE.md",
            "mechanics/checkpoint/OWNER_REQUESTS.md",
            "mechanics/checkpoint/ROADMAP.md",
            "mechanics/checkpoint/LANDING_LOG.md",
            "mechanics/checkpoint/docs/CHECKPOINT_LAW.md",
            "mechanics/checkpoint/docs/CHECKPOINT_OWNER_BOUNDARY.md",
            "mechanics/checkpoint/parts/README.md",
            "mechanics/checkpoint/parts/session-carry/README.md",
            "mechanics/checkpoint/parts/review-gate/README.md",
            "mechanics/checkpoint/parts/return-reentry/README.md",
            "mechanics/checkpoint/parts/closeout-bridge/README.md",
            "mechanics/checkpoint/parts/runtime-export/README.md",
            "mechanics/checkpoint/parts/owner-handoff/README.md",
            "mechanics/checkpoint/scripts/validate_checkpoint_mechanic.py",
            "mechanics/checkpoint/tests/test_checkpoint_mechanic.py",
            "mechanics/registry.json",
            "mechanics/owner-request-queue.json",
            "generated/mechanic_card_index.min.json",
            "generated/owner_request_queue.min.json",
            "scripts/validate_mechanics_topology.py",
            "scripts/validate_mechanic_landing_logs.py",
            "scripts/release_check.py",
            "tests/test_mechanics_topology.py",
            "tests/test_owner_request_queue.py",
            "CHANGELOG.md",
        ),
        "glob_families": (
            "mechanics/checkpoint/parts/*/README.md",
            "mechanics/checkpoint/parts/*/CONTRACT.md",
            "mechanics/checkpoint/parts/*/VALIDATION.md",
            "mechanics/checkpoint/scripts/validate_checkpoint_mechanic.py",
            "mechanics/checkpoint/tests/test_checkpoint_mechanic.py",
        ),
    },
    "recurrence": {
        "path": "mechanics/recurrence/LANDING_LOG.md",
        "required_phrases": (
            "Recurrence active-part distillation",
            "Owner repositories own typed carry",
            "no ambient continuity",
            "automatic recursor spawn",
            "control-plane carry to `aoa-sdk`",
        ),
        "required_surfaces": (
            "mechanics/recurrence/AGENTS.md",
            "mechanics/recurrence/README.md",
            "mechanics/recurrence/DIRECTION.md",
            "mechanics/recurrence/PARTS.md",
            "mechanics/recurrence/OWNER_MAP.md",
            "mechanics/recurrence/PROVENANCE.md",
            "mechanics/recurrence/OWNER_REQUESTS.md",
            "mechanics/recurrence/ROADMAP.md",
            "mechanics/recurrence/LANDING_LOG.md",
            "mechanics/recurrence/parts/README.md",
            "mechanics/recurrence/parts/anchor-return/README.md",
            "mechanics/recurrence/parts/continuity-window/README.md",
            "mechanics/recurrence/parts/component-refresh/README.md",
            "mechanics/recurrence/parts/control-plane-carry/README.md",
            "mechanics/recurrence/parts/reentry-routing/README.md",
            "mechanics/recurrence/parts/memory-recall/README.md",
            "mechanics/recurrence/parts/scenario-choreography/README.md",
            "mechanics/recurrence/parts/proof-gates/README.md",
            "mechanics/recurrence/parts/runtime-return/README.md",
            "mechanics/recurrence/parts/recursor-boundary/README.md",
            "mechanics/recurrence/scripts/validate_recurrence_mechanic.py",
            "mechanics/recurrence/tests/test_recurrence_mechanic.py",
            "mechanics/owner-request-queue.json",
            "mechanics/OWNER_REQUEST_QUEUE.md",
            "mechanics/registry.json",
            "generated/mechanic_card_index.min.json",
            "generated/owner_request_queue.min.json",
            "scripts/validate_mechanic_landing_logs.py",
            "CHANGELOG.md",
        ),
        "glob_families": (
            "mechanics/recurrence/parts/*/README.md",
            "mechanics/recurrence/parts/*/CONTRACT.md",
            "mechanics/recurrence/parts/*/VALIDATION.md",
            "mechanics/recurrence/scripts/validate_recurrence_mechanic.py",
            "mechanics/recurrence/tests/test_recurrence_mechanic.py",
        ),
    },
    "method-growth": {
        "path": "mechanics/method-growth/LANDING_LOG.md",
        "required_phrases": (
            "Method-growth active-part distillation",
            "Owner repositories own",
            "no center-owned final object truth",
            "candidate_ref` minting in center",
            "owner packets to `aoa-skills`",
        ),
        "required_surfaces": (
            "mechanics/method-growth/AGENTS.md",
            "mechanics/method-growth/README.md",
            "mechanics/method-growth/DIRECTION.md",
            "mechanics/method-growth/PARTS.md",
            "mechanics/method-growth/OWNER_MAP.md",
            "mechanics/method-growth/PROVENANCE.md",
            "mechanics/method-growth/OWNER_REQUESTS.md",
            "mechanics/method-growth/ROADMAP.md",
            "mechanics/method-growth/LANDING_LOG.md",
            "mechanics/method-growth/docs/AGENTS.md",
            "mechanics/method-growth/docs/METHOD_GROWTH_OWNER_REPO_REQUESTS.md",
            "mechanics/method-growth/docs/METHOD_SPINE.md",
            "mechanics/method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md",
            "mechanics/method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md",
            "mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md",
            "mechanics/method-growth/parts/README.md",
            "mechanics/method-growth/parts/donor-refinery/README.md",
            "mechanics/method-growth/parts/candidate-lineage/README.md",
            "mechanics/method-growth/parts/owner-landing/README.md",
            "mechanics/method-growth/parts/pruning/README.md",
            "mechanics/method-growth/parts/proof-route/README.md",
            "mechanics/method-growth/parts/method-promotion/README.md",
            "mechanics/method-growth/parts/technique-skill-split/README.md",
            "mechanics/method-growth/parts/memory-writeback/README.md",
            "mechanics/method-growth/parts/maturity-ladder/README.md",
            "mechanics/method-growth/parts/growth-closeout/README.md",
            "mechanics/method-growth/scripts/validate_method_growth_mechanic.py",
            "mechanics/method-growth/tests/test_method_growth_mechanic.py",
            "mechanics/registry.json",
            "mechanics/owner-request-queue.json",
            "mechanics/OWNER_REQUEST_QUEUE.md",
            "generated/mechanic_card_index.min.json",
            "generated/owner_request_queue.min.json",
            "generated/agents_mesh.min.json",
            "scripts/validate_mechanic_landing_logs.py",
            "scripts/validate_mechanic_artifact_topology.py",
            "scripts/release_check.py",
            "tests/test_mechanic_landing_logs.py",
            "CHANGELOG.md",
        ),
        "glob_families": (
            "mechanics/method-growth/parts/*/README.md",
            "mechanics/method-growth/parts/*/CONTRACT.md",
            "mechanics/method-growth/parts/*/VALIDATION.md",
            "mechanics/method-growth/scripts/validate_method_growth_mechanic.py",
            "mechanics/method-growth/tests/test_method_growth_mechanic.py",
        ),
    },
    "agon": {
        "path": "mechanics/agon/LANDING_LOG.md",
        "required_phrases": (
            "Agon imposition gate",
            "Agon lawful move language",
            "Agon move owner binding",
            "Agon gate routing handoff",
            "Agon trial playbook handoff",
            "Agon active route distillation",
            "Agon legacy raw provenance district",
            "Agon part artifact homes",
            "Later Agon center waves",
            "not live arena execution",
        ),
        "required_surfaces": (
            "mechanics/agon/DIRECTION.md",
            "mechanics/agon/PARTS.md",
            "mechanics/agon/OWNER_REQUESTS.md",
            "mechanics/agon/PROVENANCE.md",
            "mechanics/agon/artifact-map.json",
            "mechanics/agon/parts/README.md",
            "mechanics/agon/parts/imposition-readiness/README.md",
            "mechanics/agon/parts/lawful-move-grammar/README.md",
            "mechanics/agon/parts/owner-binding/README.md",
            "mechanics/agon/parts/gate-routing/README.md",
            "mechanics/agon/parts/trial-handoff/README.md",
            "mechanics/agon/parts/recurrence-adapter/README.md",
            "mechanics/agon/parts/packet-arena/README.md",
            "mechanics/agon/parts/duel-kernel/README.md",
            "mechanics/agon/parts/verdict-retention-rank/README.md",
            "mechanics/agon/parts/epistemic-kag/README.md",
            "mechanics/agon/parts/sophian-threshold/README.md",
            "mechanics/agon/parts/compatibility-bridges/README.md",
            "mechanics/agon/docs/README.md",
            "mechanics/agon/docs/AGENTS.md",
            "mechanics/agon/legacy/README.md",
            "mechanics/agon/legacy/AGENTS.md",
            "mechanics/agon/legacy/INDEX.md",
            "mechanics/agon/legacy/DISTILLATION_LOG.md",
            "mechanics/agon/legacy/artifacts/README.md",
            "mechanics/agon/legacy/raw/README.md",
            "mechanics/agon/scripts/validate_agon_distillation.py",
            "mechanics/agon/tests/test_agon_distillation.py",
            "mechanics/agon/legacy/raw/AGON_IMPOSITION_POSTURE.md",
            "mechanics/agon/legacy/raw/AGON_SURVIVAL_CRITERIA.md",
            "mechanics/agon/legacy/raw/AGON_DOUBT_AUDIT.md",
            "mechanics/agon/legacy/raw/PRE_AGON_BASELINE.md",
            "mechanics/agon/legacy/raw/AGON_WAVE0_LANDING.md",
            "mechanics/agon/parts/imposition-readiness/generated/agon_imposition_readiness.min.json",
            "mechanics/agon/parts/imposition-readiness/schemas/agon-imposition-readiness.schema.json",
            "mechanics/agon/parts/imposition-readiness/examples/agon_doubt_audit.example.json",
            "mechanics/agon/parts/imposition-readiness/scripts/build_agon_imposition_readiness.py",
            "mechanics/agon/parts/imposition-readiness/scripts/validate_agon_imposition_readiness.py",
            "mechanics/agon/parts/imposition-readiness/tests/test_agon_imposition_readiness.py",
            "mechanics/agon/legacy/raw/AGON_LAWFUL_MOVE_LANGUAGE.md",
            "mechanics/agon/legacy/raw/AGON_MOVE_REGISTRY_MODEL.md",
            "mechanics/agon/legacy/raw/AGON_MOVE_OWNER_HANDOFFS.md",
            "mechanics/agon/legacy/raw/AGON_WAVE3_LANDING.md",
            "mechanics/agon/parts/lawful-move-grammar/config/agon_lawful_moves.seed.json",
            "mechanics/agon/parts/lawful-move-grammar/generated/agon_lawful_move_registry.min.json",
            "mechanics/agon/parts/lawful-move-grammar/schemas/agon-lawful-move.schema.json",
            "mechanics/agon/parts/lawful-move-grammar/schemas/agon-lawful-move-registry.schema.json",
            "mechanics/agon/parts/lawful-move-grammar/examples/agon_lawful_move.example.json",
            "mechanics/agon/parts/lawful-move-grammar/scripts/build_agon_lawful_move_registry.py",
            "mechanics/agon/parts/lawful-move-grammar/scripts/validate_agon_lawful_moves.py",
            "mechanics/agon/parts/lawful-move-grammar/tests/test_agon_lawful_moves.py",
            "mechanics/agon/legacy/raw/AGON_MOVE_OWNER_BINDING.md",
            "mechanics/agon/legacy/raw/AGON_MOVE_BINDING_MATRIX_MODEL.md",
            "mechanics/agon/legacy/raw/AGON_OWNER_REPO_REQUESTS.md",
            "mechanics/agon/legacy/raw/AGON_PRE_PROTOCOL_STOP_LINES.md",
            "mechanics/agon/legacy/raw/AGON_WAVE4_LANDING.md",
            "mechanics/agon/parts/owner-binding/config/agon_move_owner_bindings.seed.json",
            "mechanics/agon/parts/owner-binding/generated/agon_move_owner_binding_registry.min.json",
            "mechanics/agon/parts/owner-binding/schemas/agon-move-owner-binding.schema.json",
            "mechanics/agon/parts/owner-binding/schemas/agon-move-owner-binding-registry.schema.json",
            "mechanics/agon/parts/owner-binding/examples/agon_move_owner_binding.example.json",
            "mechanics/agon/parts/owner-binding/scripts/build_agon_move_owner_binding_registry.py",
            "mechanics/agon/parts/owner-binding/scripts/validate_agon_move_owner_bindings.py",
            "mechanics/agon/parts/owner-binding/tests/test_agon_move_owner_bindings.py",
            "mechanics/agon/legacy/raw/AGON_GATE_ROUTING_HANDOFF.md",
            "mechanics/agon/legacy/raw/AGON_GATE_ROUTING_OWNER_REQUEST.md",
            "mechanics/agon/legacy/raw/AGON_GATE_ROUTING_STOP_LINES.md",
            "mechanics/agon/legacy/raw/AGON_WAVE5_CENTER_HANDOFF.md",
            "mechanics/agon/parts/gate-routing/config/agon_gate_routing_handoff_request.seed.json",
            "mechanics/agon/parts/gate-routing/generated/agon_gate_routing_handoff_request.min.json",
            "mechanics/agon/parts/gate-routing/schemas/agon-gate-routing-handoff-request.schema.json",
            "mechanics/agon/parts/gate-routing/examples/agon_gate_routing_handoff_request.example.json",
            "mechanics/agon/parts/gate-routing/scripts/build_agon_gate_routing_handoff_request.py",
            "mechanics/agon/parts/gate-routing/scripts/validate_agon_gate_routing_handoff_request.py",
            "mechanics/agon/parts/gate-routing/tests/test_agon_gate_routing_handoff_request.py",
            "mechanics/agon/legacy/raw/AGON_TRIAL_PLAYBOOK_HANDOFF.md",
            "mechanics/agon/legacy/raw/AGON_TRIAL_PLAYBOOK_OWNER_REQUEST.md",
            "mechanics/agon/legacy/raw/AGON_TRIAL_PLAYBOOK_STOP_LINES.md",
            "mechanics/agon/legacy/raw/AGON_WAVE6_CENTER_HANDOFF.md",
            "mechanics/agon/parts/trial-handoff/config/agon_trial_playbook_request.seed.json",
            "mechanics/agon/parts/trial-handoff/generated/agon_trial_playbook_request.min.json",
            "mechanics/agon/parts/trial-handoff/schemas/agon-trial-playbook-request.schema.json",
            "mechanics/agon/parts/trial-handoff/examples/agon_trial_playbook_request.example.json",
            "mechanics/agon/parts/trial-handoff/scripts/build_agon_trial_playbook_request.py",
            "mechanics/agon/parts/trial-handoff/scripts/validate_agon_trial_playbook_request.py",
            "mechanics/agon/parts/trial-handoff/tests/test_agon_trial_playbook_request.py",
        ),
        "glob_families": (
            "mechanics/agon/legacy/raw/AGON_*.md",
            "mechanics/agon/parts/*/generated/agon_*.min.json",
            "mechanics/agon/parts/*/schemas/agon-*.schema.json",
            "mechanics/agon/parts/*/config/agon_*.seed.json",
            "mechanics/agon/parts/*/examples/agon_*.example.json",
            "mechanics/agon/parts/*/scripts/*agon*.py",
            "mechanics/agon/parts/*/tests/test_agon_*.py",
            "mechanics/agon/scripts/validate_agon_distillation.py",
            "mechanics/agon/tests/test_agon_distillation.py",
        ),
    },
    "experience": {
        "path": "mechanics/experience/LANDING_LOG.md",
        "required_phrases": (
            "Experience Wave 1 kernel",
            "Experience Wave 5 sovereign office",
            "Experience v1.2 to v2.0 bridge",
            "Experience v2.0 living workspace continuity runtime",
            "Experience active parts plus provenance bridge",
            "Experience active docs provenance-load cleanup",
            "Experience part artifact homes",
            "does not activate live workspace",
        ),
        "required_surfaces": (
            "mechanics/experience/DIRECTION.md",
            "mechanics/experience/PARTS.md",
            "mechanics/experience/artifact-map.json",
            "mechanics/experience/parts/README.md",
            "mechanics/experience/PROVENANCE.md",
            "mechanics/experience/OWNER_REQUESTS.md",
            "mechanics/experience/parts/capture-kernel/README.md",
            "mechanics/experience/parts/certification-proof/README.md",
            "mechanics/experience/parts/adoption-federation/README.md",
            "mechanics/experience/parts/governance-polis/README.md",
            "mechanics/experience/parts/office-operations/README.md",
            "mechanics/experience/parts/runtime-boundary/README.md",
            "mechanics/experience/parts/service-mesh/README.md",
            "mechanics/experience/parts/compatibility-bridges/README.md",
            "mechanics/experience/parts/continuity-context/README.md",
            "mechanics/experience/parts/capture-kernel/scripts/validate_capture_kernel.py",
            "mechanics/experience/parts/certification-proof/scripts/validate_certification_proof.py",
            "mechanics/experience/parts/adoption-federation/scripts/validate_adoption_federation.py",
            "mechanics/experience/parts/governance-polis/scripts/validate_governance_polis.py",
            "mechanics/experience/parts/office-operations/scripts/validate_office_operations.py",
            "mechanics/experience/scripts/validate_experience_distillation.py",
            "mechanics/experience/parts/compatibility-bridges/scripts/validate_agonic_pair_trials_bridge.py",
            "mechanics/experience/parts/compatibility-bridges/scripts/validate_epistemic_duel_bridge.py",
            "mechanics/experience/parts/continuity-context/scripts/validate_affective_economy.py",
            "mechanics/experience/parts/continuity-context/scripts/validate_context_memory_weaving.py",
            "mechanics/experience/parts/continuity-context/scripts/validate_context_routing.py",
            "mechanics/experience/parts/runtime-boundary/scripts/validate_runtime_boundary_bridge.py",
            "mechanics/experience/parts/service-mesh/scripts/validate_service_mesh.py",
            "mechanics/experience/parts/office-operations/scripts/validate_office_role_pairs.py",
            "mechanics/experience/parts/continuity-context/scripts/validate_memory_rank_reputation.py",
            "mechanics/experience/parts/continuity-context/scripts/validate_living_workspace_continuity.py",
            "mechanics/experience/parts/capture-kernel/tests/test_capture_kernel.py",
            "mechanics/experience/parts/certification-proof/tests/test_certification_proof.py",
            "mechanics/experience/parts/adoption-federation/tests/test_adoption_federation.py",
            "mechanics/experience/parts/governance-polis/tests/test_governance_polis.py",
            "mechanics/experience/parts/governance-polis/tests/test_governance_polis_seed_contracts.py",
            "mechanics/experience/parts/office-operations/tests/test_office_operations.py",
            "mechanics/experience/parts/office-operations/tests/test_office_operations_seed_contracts.py",
            "mechanics/experience/tests/test_experience_distillation.py",
            "mechanics/experience/parts/compatibility-bridges/tests/test_agonic_pair_trials_bridge.py",
            "mechanics/experience/parts/compatibility-bridges/tests/test_epistemic_duel_bridge.py",
            "mechanics/experience/parts/continuity-context/tests/test_affective_economy.py",
            "mechanics/experience/parts/continuity-context/tests/test_context_memory_weaving.py",
            "mechanics/experience/parts/continuity-context/tests/test_context_routing.py",
            "mechanics/experience/parts/runtime-boundary/tests/test_runtime_boundary_bridge.py",
            "mechanics/experience/parts/service-mesh/tests/test_service_mesh.py",
            "mechanics/experience/parts/office-operations/tests/test_office_role_pairs.py",
            "mechanics/experience/parts/continuity-context/tests/test_memory_rank_reputation.py",
            "mechanics/experience/parts/continuity-context/tests/test_living_workspace_continuity.py",
        ),
        "glob_families": (
            "mechanics/experience/legacy/raw/EXPERIENCE_*.md",
            "mechanics/experience/parts/*/schemas/*.json",
            "mechanics/experience/parts/*/examples/*.json",
            "mechanics/experience/parts/*/scripts/*.py",
            "mechanics/experience/parts/*/tests/test_*.py",
            "mechanics/experience/scripts/validate_experience_distillation.py",
            "mechanics/experience/tests/test_experience_distillation.py",
        ),
    },
    "antifragility": {
        "path": "mechanics/antifragility/LANDING_LOG.md",
        "required_phrases": (
            "Antifragility active-part distillation",
            "active part topology",
            "legacy/raw material in active parts",
            "owner packets to `aoa-evals`, `aoa-memo`, `aoa-stats`, and `aoa-playbooks`",
            "one-score health",
            "deletion theater",
            "owner-local cleanup authority",
        ),
        "required_surfaces": (
            "mechanics/antifragility/AGENTS.md",
            "mechanics/antifragility/README.md",
            "mechanics/antifragility/DIRECTION.md",
            "mechanics/antifragility/PARTS.md",
            "mechanics/antifragility/OWNER_MAP.md",
            "mechanics/antifragility/OWNER_REQUESTS.md",
            "mechanics/antifragility/PROVENANCE.md",
            "mechanics/antifragility/ROADMAP.md",
            "mechanics/antifragility/LANDING_LOG.md",
            "mechanics/antifragility/docs/ANTIFRAGILITY.md",
            "mechanics/antifragility/docs/VIA_NEGATIVA.md",
            "mechanics/antifragility/docs/ANTI_AUTHORITY_RULES.md",
            "mechanics/antifragility/docs/ONE_IN_ONE_OUT.md",
            "mechanics/antifragility/docs/ANTIFRAGILITY_OWNER_REPO_REQUESTS.md",
            "mechanics/antifragility/FRAGILITY_BLACKLIST.md",
            "mechanics/antifragility/parts/AGENTS.md",
            "mechanics/antifragility/parts/README.md",
            "mechanics/antifragility/parts/stress-review/README.md",
            "mechanics/antifragility/parts/via-negativa/README.md",
            "mechanics/antifragility/parts/authority-boundary/README.md",
            "mechanics/antifragility/parts/sprawl-control/README.md",
            "mechanics/antifragility/parts/fragility-registry/README.md",
            "mechanics/antifragility/parts/repair-proof/README.md",
            "mechanics/antifragility/parts/memory-return/README.md",
            "mechanics/antifragility/parts/owner-handoff/README.md",
            "mechanics/antifragility/legacy/AGENTS.md",
            "mechanics/antifragility/legacy/README.md",
            "mechanics/antifragility/legacy/raw/README.md",
            "mechanics/antifragility/legacy/raw/ANTIFRAGILITY_FIRST_WAVE.md",
            "mechanics/antifragility/legacy/raw/VIA_NEGATIVA_CHECKLIST.md",
            "mechanics/antifragility/scripts/validate_antifragility_distillation.py",
            "mechanics/antifragility/tests/test_via_negativa_surfaces.py",
            "mechanics/registry.json",
            "mechanics/owner-request-queue.json",
            "generated/mechanic_card_index.min.json",
            "generated/owner_request_queue.min.json",
            "scripts/validate_mechanic_landing_logs.py",
            "scripts/release_check.py",
            "tests/test_mechanic_landing_logs.py",
            "CHANGELOG.md",
        ),
        "glob_families": (
            "mechanics/antifragility/parts/*/README.md",
            "mechanics/antifragility/parts/*/CONTRACT.md",
            "mechanics/antifragility/parts/*/VALIDATION.md",
            "mechanics/antifragility/legacy/raw/*.md",
            "mechanics/antifragility/scripts/validate_antifragility_distillation.py",
            "mechanics/antifragility/tests/test_via_negativa_surfaces.py",
        ),
    },
    "questbook": {
        "path": "mechanics/questbook/LANDING_LOG.md",
        "required_phrases": (
            "Root mechanics topology migration",
            "Quest lifecycle board activation",
            "Lane-first quest topology",
            "Quest relation model",
            "no root quest aliases",
            "generated surface as quest authority",
        ),
        "required_surfaces": (
            "mechanics/questbook/DIRECTION.md",
            "mechanics/questbook/PARTS.md",
            "mechanics/questbook/PROVENANCE.md",
            "mechanics/questbook/README.md",
            "mechanics/questbook/ROADMAP.md",
            "mechanics/questbook/OWNER_REQUESTS.md",
            "mechanics/questbook/parts/README.md",
            "mechanics/questbook/parts/model-spine/README.md",
            "mechanics/questbook/parts/public-index/README.md",
            "mechanics/questbook/parts/quest-store/README.md",
            "mechanics/questbook/parts/lifecycle-law/README.md",
            "mechanics/questbook/parts/generated-views/README.md",
            "mechanics/questbook/parts/relation-shape/README.md",
            "mechanics/questbook/parts/execution-passport/README.md",
            "mechanics/questbook/parts/harvest-route/README.md",
            "mechanics/questbook/parts/owner-handoffs/README.md",
            "mechanics/questbook/parts/lane-owner-routes/README.md",
            "mechanics/questbook/parts/lane-owner-routes/experience-ready-owner-routes.json",
            "mechanics/questbook/parts/lane-owner-routes/experience-ready-owner-routes.md",
            "mechanics/questbook/legacy/INDEX.md",
            "mechanics/questbook/legacy/DISTILLATION_LOG.md",
            "mechanics/questbook/legacy/raw/QUESTBOOK_FIRST_WAVE.md",
            "mechanics/questbook/scripts/build_questbook_index.py",
            "mechanics/questbook/scripts/build_ready_owner_routes.py",
            "mechanics/questbook/scripts/validate_questbook_lifecycle.py",
            "mechanics/questbook/scripts/validate_questbook_index.py",
            "mechanics/questbook/scripts/validate_quest_relations.py",
            "mechanics/questbook/scripts/validate_ready_owner_routes.py",
            "generated/questbook_index.min.json",
            "generated/questbook_frontier.min.json",
            "generated/questbook_relations.min.json",
            "QUESTBOOK.md",
            "quests/README.md",
            "quests/center/README.md",
            "quests/agon/README.md",
            "quests/experience/README.md",
        ),
        "glob_families": (
            "quests/*/*/AOA-Q-*",
            "mechanics/questbook/scripts/*questbook*.py",
            "mechanics/questbook/tests/test_questbook_*.py",
        ),
    },
    "rpg": {
        "path": "mechanics/rpg/LANDING_LOG.md",
        "required_phrases": (
            "Root mechanics topology migration",
            "RPG vocabulary overlay and route polish",
            "RPG world-grammar direction",
            "RPG active parts and legacy provenance distillation",
            "dual-vocabulary contract",
            "world grammar",
            "legacy provenance",
            "no hidden ontology",
            "runtime ledger",
            "role-canon mutation",
            "presentation-label overwrite",
        ),
        "required_surfaces": (
            "mechanics/rpg/AGENTS.md",
            "mechanics/rpg/README.md",
            "mechanics/rpg/DIRECTION.md",
            "mechanics/rpg/PARTS.md",
            "mechanics/rpg/PROVENANCE.md",
            "mechanics/rpg/OWNER_REQUESTS.md",
            "mechanics/rpg/ROADMAP.md",
            "mechanics/rpg/LANDING_LOG.md",
            "mechanics/rpg/docs/README.md",
            "mechanics/rpg/docs/AGENTS.md",
            "mechanics/rpg/parts/README.md",
            "mechanics/rpg/parts/AGENTS.md",
            "mechanics/rpg/parts/world-grammar/README.md",
            "mechanics/rpg/parts/source-boundary/README.md",
            "mechanics/rpg/parts/vocabulary-overlay/README.md",
            "mechanics/rpg/parts/vocabulary-overlay/TERMINOLOGY.md",
            "mechanics/rpg/parts/quest-campaign/README.md",
            "mechanics/rpg/parts/progression-unlocks/README.md",
            "mechanics/rpg/parts/runtime-projection/README.md",
            "mechanics/rpg/parts/owner-handoffs/README.md",
            "mechanics/rpg/parts/vocabulary-overlay/schemas/dual_vocabulary_overlay.schema.json",
            "mechanics/rpg/parts/vocabulary-overlay/examples/dual_vocabulary_overlay.example.json",
            "mechanics/rpg/parts/vocabulary-overlay/generated/dual_vocabulary_overlay.json",
            "mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py",
            "mechanics/rpg/parts/vocabulary-overlay/tests/test_vocabulary_overlay.py",
            "mechanics/rpg/legacy/AGENTS.md",
            "mechanics/rpg/legacy/README.md",
            "mechanics/rpg/legacy/INDEX.md",
            "mechanics/rpg/legacy/DISTILLATION_LOG.md",
            "mechanics/rpg/legacy/raw/README.md",
            "mechanics/rpg/legacy/artifacts/README.md",
            "mechanics/rpg/legacy/raw/RPG_LAYER_MODEL.md",
            "mechanics/rpg/legacy/raw/RPG_ARCHITECTURE_RFC.md",
            "mechanics/rpg/legacy/raw/RPG_BOUNDARY_MAP.md",
            "mechanics/rpg/legacy/raw/RPG_FIRST_WAVE.md",
            "mechanics/rpg/legacy/raw/RPG_SECOND_WAVE.md",
            "mechanics/rpg/legacy/raw/RPG_SKILLS_AND_FEATS.md",
            "mechanics/rpg/legacy/raw/RPG_BRIDGE_WAVE.md",
            "mechanics/rpg/legacy/raw/RPG_RUNTIME_PROJECTION_WAVE.md",
            "mechanics/rpg/scripts/validate_rpg_distillation.py",
            "mechanics/rpg/tests/test_rpg_distillation.py",
            "mechanics/registry.json",
            "mechanics/owner-request-queue.json",
            "scripts/validate_mechanic_artifact_topology.py",
            "scripts/validate_mechanic_landing_logs.py",
            "scripts/release_check.py",
            "tests/test_mechanic_landing_logs.py",
            "CHANGELOG.md",
        ),
        "glob_families": (
            "mechanics/rpg/legacy/raw/RPG_*.md",
            "mechanics/rpg/parts/*/README.md",
            "mechanics/rpg/parts/*/CONTRACT.md",
            "mechanics/rpg/parts/*/VALIDATION.md",
            "mechanics/rpg/parts/vocabulary-overlay/schemas/dual_vocabulary_overlay.schema.json",
            "mechanics/rpg/parts/vocabulary-overlay/examples/dual_vocabulary_overlay.example.json",
            "mechanics/rpg/parts/vocabulary-overlay/generated/dual_vocabulary_overlay.json",
            "mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py",
            "mechanics/rpg/parts/vocabulary-overlay/tests/test_vocabulary_overlay.py",
            "mechanics/rpg/scripts/validate_rpg_distillation.py",
            "mechanics/rpg/tests/test_rpg_distillation.py",
        ),
    },
}


def iter_entries(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^### .+$", text, flags=re.MULTILINE))
    entries: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        title = match.group(0).removeprefix("### ").strip()
        entries.append((title, text[match.start() : end]))
    return entries


def looks_like_surface(ref: str) -> bool:
    return (
        "/" in ref
        or ref.endswith((".md", ".py", ".json"))
        or ref in {"README.md", "ROADMAP.md", "CHANGELOG.md"}
    )


def validate_log(mechanic: str) -> list[str]:
    spec = MECHANICS[mechanic]
    rel_path = str(spec["path"])
    path = REPO_ROOT / rel_path
    problems: list[str] = []

    if not path.exists():
        return [f"{rel_path}: missing"]

    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        problems.append(f"{rel_path}: missing final newline")

    for phrase in spec["required_phrases"]:
        if str(phrase) not in text:
            problems.append(f"{rel_path}: missing required phrase {phrase!r}")

    entries = iter_entries(text)
    if not entries:
        problems.append(f"{rel_path}: missing landing entries")

    for title, entry in entries:
        for field in REQUIRED_FIELDS:
            if field not in entry:
                problems.append(f"{rel_path}: entry {title!r} missing {field}")

    for surface in spec["required_surfaces"]:
        surface_text = str(surface)
        if f"`{surface_text}`" not in text:
            problems.append(f"{rel_path}: missing required surface `{surface_text}`")
        if not (REPO_ROOT / surface_text).exists():
            problems.append(f"{rel_path}: listed required surface does not exist: {surface_text}")

    for match in re.finditer(r"`([^`]+)`", text):
        ref = match.group(1)
        if not looks_like_surface(ref):
            continue
        path_ref = ref.partition("#")[0]
        if "*" in path_ref:
            continue
        if path_ref.startswith(("python ", "v")):
            continue
        if not (REPO_ROOT / path_ref).exists():
            problems.append(f"{rel_path}: backtick surface does not exist: {ref}")

    return problems


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate mechanic LANDING_LOG surfaces.")
    parser.add_argument(
        "--mechanic",
        choices=sorted(MECHANICS),
        action="append",
        help="Mechanic to validate; may be passed more than once. Defaults to all.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    mechanics = args.mechanic or sorted(MECHANICS)
    problems: list[str] = []
    for mechanic in mechanics:
        problems.extend(validate_log(mechanic))

    if problems:
        print("Mechanic landing log validation failed:")
        for problem in problems:
            print(f"  - {problem}")
        return 1

    print("[ok] validated mechanic LANDING_LOG surfaces: " + ", ".join(mechanics))
    return 0


if __name__ == "__main__":
    sys.exit(main())
