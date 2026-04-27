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
    / "method-growth"
    / "scripts"
    / "validate_method_growth_mechanic.py"
)


def load_validator():
    spec = importlib.util.spec_from_file_location(
        "validate_method_growth_mechanic", VALIDATOR
    )
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_method_growth_mechanic_is_valid() -> None:
    module = load_validator()

    assert module.validate() == []


def test_method_growth_active_parts_do_not_pull_sibling_source_paths() -> None:
    module = load_validator()
    problems: list[str] = []

    module.validate_provenance_boundary(problems)

    assert problems == []


def test_method_growth_owner_requests_are_root_surface() -> None:
    module = load_validator()
    problems: list[str] = []

    module.validate_registry(problems)

    assert not [
        problem
        for problem in problems
        if "owner_request_doc_ref" in problem or "canonical_docs missing" in problem
    ]
