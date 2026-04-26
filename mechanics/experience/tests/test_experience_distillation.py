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
    / "experience"
    / "scripts"
    / "validate_experience_distillation.py"
)


def load_validator():
    spec = importlib.util.spec_from_file_location(
        "validate_experience_distillation", VALIDATOR
    )
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


def test_active_route_rejects_route_pollution_markers(monkeypatch) -> None:
    module = load_validator()
    original_read = module.read
    target = ROOT / "mechanics" / "experience" / "parts" / "README.md"

    def fake_read(path: Path) -> str:
        if path == target:
            return "Functioning parts stay small enough for a low-context agent before touching legacy provenance.\n"
        return original_read(path)

    monkeypatch.setattr(module, "read", fake_read)
    problems: list[str] = []

    module.validate_active_docs_are_lean(problems)

    assert any("route-pollution marker" in problem for problem in problems)


def test_experience_closeout_does_not_pull_archive_by_default(monkeypatch) -> None:
    module = load_validator()
    original_read = module.read
    target = ROOT / "mechanics" / "experience" / "AGENTS.md"

    def fake_read(path: Path) -> str:
        if path == target:
            return "Closeout must name archival sources consulted through `PROVENANCE.md`.\n"
        return original_read(path)

    monkeypatch.setattr(module, "read", fake_read)
    problems: list[str] = []

    module.validate_active_docs_are_lean(problems)

    assert any("archival sources consulted" in problem for problem in problems)


def test_experience_thematic_route_points_to_preserved_raw_provenance() -> None:
    module = load_validator()
    problems: list[str] = []

    module.validate_thematic_experience_route(problems)

    assert problems == []


def test_experience_owner_stop_lines_are_reflected() -> None:
    module = load_validator()
    problems: list[str] = []

    module.validate_registry(problems)

    assert not [problem for problem in problems if "must_not_claim missing" in problem]
    assert not [
        problem for problem in problems if "missing owner stop-line phrase" in problem
    ]


def test_part_validators_do_not_direct_read_raw_legacy() -> None:
    module = load_validator()
    problems: list[str] = []

    module.validate_raw_source_requirements(problems)

    assert not [problem for problem in problems if "direct-read legacy/raw" in problem]


def test_active_artifacts_do_not_use_release_contour_identity() -> None:
    module = load_validator()
    problems: list[str] = []

    module.validate_active_artifact_names(problems)

    assert problems == []


def test_raw_legacy_readme_uses_package_validator_route() -> None:
    readme = (
        ROOT / "mechanics" / "experience" / "legacy" / "raw" / "README.md"
    ).read_text(encoding="utf-8")

    assert (
        "python mechanics/experience/scripts/validate_experience_distillation.py"
        in readme
    )
    assert "python scripts/validate_experience_distillation.py" not in readme
