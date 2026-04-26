from __future__ import annotations

import importlib.util
from pathlib import Path


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


ROOT = _repo_root()
VALIDATOR = (
    ROOT
    / "mechanics"
    / "rpg"
    / "parts"
    / "vocabulary-overlay"
    / "scripts"
    / "validate_vocabulary_overlay.py"
)


def load_validator():
    spec = importlib.util.spec_from_file_location(
        "validate_vocabulary_overlay", VALIDATOR
    )
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_rpg_dual_vocabulary_overlay_is_valid() -> None:
    module = load_validator()

    assert module.validate() == []


def test_first_frontend_minimum_resolves_to_expected_contract() -> None:
    module = load_validator()
    terminology = module.read_text(module.TERMINOLOGY_PATH)

    keys = module.first_frontend_minimum_keys(terminology)

    assert len(keys) == 26
    assert keys[:3] == ["class_archetype", "execution_origin", "rank"]
    assert keys[15:20] == ["inspect", "expand", "handoff", "verify", "reanchor"]
    assert keys[-2:] == ["boundary_trust", "review_trust"]


def test_schema_required_keys_match_terminology_order() -> None:
    module = load_validator()
    terminology = module.read_text(module.TERMINOLOGY_PATH)
    schema = module.load_json(module.SCHEMA_PATH)

    assert module.schema_required_keys(schema) == module.first_frontend_minimum_keys(
        terminology
    )
