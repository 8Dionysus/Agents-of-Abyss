from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def load_json(relative_path: str) -> object:
    return json.loads((REPO_ROOT / relative_path).read_text(encoding="utf-8"))


def test_roadmap_keeps_public_and_supporting_contour_aligned() -> None:
    roadmap = read_text("ROADMAP.md")
    roadmap_lower = roadmap.lower()
    readme = read_text("README.md")
    changelog = read_text("CHANGELOG.md")
    registry = load_json("generated/ecosystem_registry.min.json")
    supporting = load_json("generated/federation_supporting_inventory.min.json")

    assert "> Current release: `v0.2.3`" in readme
    assert "## [0.2.3] - 2026-04-23" in changelog
    assert "`v0.2.3`" in roadmap
    assert "Current release contour" in roadmap
    assert "roadmap continuity and owner-boundary" in roadmap
    assert "leaving checkpoint carry, candidate identity, seed staging" in roadmap
    assert "mechanics/agon/LANDING_LOG.md" in roadmap
    assert "mechanics/experience/LANDING_LOG.md" in roadmap

    registry_names = {entry["name"] for entry in registry["repos"]}
    supporting_names = {entry["name"] for entry in supporting["repos"]}

    for name in {
        "Agents-of-Abyss",
        "aoa-stats",
        "aoa-routing",
        "aoa-kag",
        "Tree-of-Sophia",
        "abyss-stack",
    }:
        assert name in registry_names
        assert f"`{name}`" in roadmap

    assert "aoa-sdk" in supporting_names
    assert "aoa-sdk" not in registry_names
    assert "`aoa-sdk`" in roadmap
    assert "supporting inventory" in roadmap_lower
    assert "ecosystem registry v2" in roadmap_lower

    current_release_surfaces = [
        "README.md",
        "CHARTER.md",
        "ECOSYSTEM_MAP.md",
        "docs/LAYERS.md",
        "docs/FEDERATION_RULES.md",
        "mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md",
        "mechanics/release-support/docs/DIRECTION_SURFACES.md",
        "generated/center_entry_map.min.json",
        "generated/ecosystem_registry.min.json",
        "generated/federation_supporting_inventory.min.json",
        "mechanics/method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md",
        "mechanics/method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md",
        "mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md",
        "mechanics/method-growth/examples/lineage_contract_chain.example.json",
        "mechanics/method-growth/scripts/validate_candidate_lineage_contract.py",
        "mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md",
        "mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md",
        "mechanics/agon/legacy/raw/AGON_PREPARATION_POSTURE.md",
        "mechanics/method-growth/scripts/validate_wave4_kernel_automation.py",
        "mechanics/agon/LANDING_LOG.md",
        "mechanics/experience/LANDING_LOG.md",
    ]
    for surface in current_release_surfaces:
        assert (REPO_ROOT / surface).exists(), surface
        assert surface in roadmap


def test_roadmap_names_released_agon_imposition_gate_surfaces() -> None:
    landing_log = read_text("mechanics/agon/LANDING_LOG.md")
    roadmap = read_text("ROADMAP.md")

    assert "### Agon imposition gate" in landing_log
    assert "mechanics/agon/LANDING_LOG.md" in roadmap

    unreleased_surfaces = [
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
    ]
    for surface in unreleased_surfaces:
        assert (REPO_ROOT / surface).exists(), surface
        assert surface in landing_log


def test_roadmap_names_released_agon_lawful_move_language_surfaces() -> None:
    landing_log = read_text("mechanics/agon/LANDING_LOG.md")
    roadmap = read_text("ROADMAP.md")

    assert "### Agon lawful move language" in landing_log
    assert "mechanics/agon/LANDING_LOG.md" in roadmap

    unreleased_surfaces = [
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
    ]
    for surface in unreleased_surfaces:
        assert (REPO_ROOT / surface).exists(), surface
        assert surface in landing_log


def test_roadmap_names_released_agon_move_owner_binding_surfaces() -> None:
    landing_log = read_text("mechanics/agon/LANDING_LOG.md")
    roadmap = read_text("ROADMAP.md")

    assert "### Agon move owner binding" in landing_log
    assert "mechanics/agon/LANDING_LOG.md" in roadmap

    unreleased_surfaces = [
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
    ]
    for surface in unreleased_surfaces:
        assert (REPO_ROOT / surface).exists(), surface
        assert surface in landing_log


def test_roadmap_names_released_agon_gate_routing_handoff_surfaces() -> None:
    landing_log = read_text("mechanics/agon/LANDING_LOG.md")
    roadmap = read_text("ROADMAP.md")

    assert "### Agon gate routing handoff" in landing_log
    assert "mechanics/agon/LANDING_LOG.md" in roadmap

    unreleased_surfaces = [
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
    ]
    for surface in unreleased_surfaces:
        assert (REPO_ROOT / surface).exists(), surface
        assert surface in landing_log


def test_roadmap_names_released_agon_trial_playbook_handoff_surfaces() -> None:
    landing_log = read_text("mechanics/agon/LANDING_LOG.md")
    roadmap = read_text("ROADMAP.md")

    assert "### Agon trial playbook handoff" in landing_log
    assert "mechanics/agon/LANDING_LOG.md" in roadmap

    unreleased_surfaces = [
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
    ]
    for surface in unreleased_surfaces:
        assert (REPO_ROOT / surface).exists(), surface
        assert surface in landing_log
