from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"


def test_mechanics_registry_has_canonical_slug_set() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    slugs = {entry["slug"] for entry in registry["mechanics"]}
    assert slugs == {
        "method-growth",
        "recurrence",
        "experience",
        "agon",
        "antifragility",
        "questbook",
        "rpg",
        "tos-bridge",
        "release-support",
    }


def test_every_mechanic_package_has_required_entry_surfaces() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    for entry in registry["mechanics"]:
        package = REPO_ROOT / entry["package_path"]
        assert (package / "AGENTS.md").exists()
        assert (package / "README.md").exists()
        assert (package / "ROADMAP.md").exists()
        assert (package / "LANDING_LOG.md").exists()
        assert (package / "docs").is_dir()


def test_no_flat_agon_experience_or_rpg_docs_remain() -> None:
    docs = REPO_ROOT / "docs"
    assert not list(docs.glob("AGON_*.md"))
    assert not list(docs.glob("EXPERIENCE_*.md"))
    assert not list(docs.glob("RPG_*.md"))
