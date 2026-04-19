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

    assert "> Current release: `v0.2.1`" in readme
    assert "## [0.2.1] - 2026-04-12" in changelog
    assert "`v0.2.1`" in roadmap
    assert "Current release contour" in roadmap
    assert "roadmap continuity and owner-boundary" in roadmap
    assert "leaving checkpoint carry, candidate identity, seed staging" in roadmap

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
    assert "compact registry v1" in roadmap_lower

    current_release_surfaces = [
        "README.md",
        "CHARTER.md",
        "ECOSYSTEM_MAP.md",
        "docs/LAYERS.md",
        "docs/FEDERATION_RULES.md",
        "docs/PUBLIC_SUPPORT_POSTURE.md",
        "docs/DIRECTION_SURFACES.md",
        "generated/center_entry_map.min.json",
        "generated/ecosystem_registry.min.json",
        "generated/federation_supporting_inventory.min.json",
        "docs/REVIEWABLE_GROWTH_REFINERY.md",
        "docs/CANDIDATE_LINEAGE_CROSSWALK.md",
        "docs/OWNER_LANDING_AND_PRUNING.md",
        "examples/lineage_contract_chain.example.json",
        "scripts/validate_candidate_lineage_contract.py",
        "docs/SELF_AGENCY_CONTINUITY.md",
        "docs/COMPONENT_REFRESH_LAW.md",
        "docs/AGON_PREPARATION_POSTURE.md",
        "scripts/validate_wave4_kernel_automation.py",
    ]
    for surface in current_release_surfaces:
        assert (REPO_ROOT / surface).exists(), surface
        assert surface in roadmap
