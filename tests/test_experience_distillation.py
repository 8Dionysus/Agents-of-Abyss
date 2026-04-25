from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_experience_distillation.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_experience_distillation", VALIDATOR)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_experience_distillation_is_valid() -> None:
    module = load_validator()

    assert module.validate() == []


def test_experience_distillation_part_validation_is_valid() -> None:
    module = load_validator()

    assert module.validate({"runtime-boundary"}) == []
