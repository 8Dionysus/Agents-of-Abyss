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
    registry = load_json("generated/ecosystem_registry.min.json")
    supporting = load_json("generated/federation_supporting_inventory.min.json")

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
    assert "`aoa-sdk`" in roadmap
    assert "supporting inventory" in roadmap_lower
    assert "compact registry v1" in roadmap_lower
