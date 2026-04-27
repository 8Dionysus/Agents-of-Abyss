from __future__ import annotations

import importlib.util
from pathlib import Path


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


ROOT = _repo_root()
VALIDATOR = ROOT / "mechanics" / "rpg" / "scripts" / "validate_rpg_distillation.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_rpg_distillation", VALIDATOR)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_rpg_distillation_is_valid() -> None:
    module = load_validator()

    assert module.validate() == []


def test_rpg_parts_are_complete() -> None:
    module = load_validator()

    for slug in module.PART_SLUGS:
        part = module.RPG_ROOT / "parts" / slug
        assert (part / "README.md").is_file()
        assert (part / "CONTRACT.md").is_file()
        assert (part / "VALIDATION.md").is_file()


def test_raw_sources_are_preserved_only_in_legacy() -> None:
    module = load_validator()

    assert not list((module.RPG_ROOT / "docs").glob("RPG_*.md"))
    for raw in module.RAW_SOURCES:
        assert (module.RPG_ROOT / "legacy" / "raw" / raw).is_file()


def test_active_route_rejects_direct_raw_legacy_refs(tmp_path, monkeypatch) -> None:
    module = load_validator()
    repo = tmp_path / "repo"
    rpg = repo / "mechanics" / "rpg"
    (rpg / "parts" / "world-grammar").mkdir(parents=True)
    (rpg / "README.md").write_text("legacy/raw/RPG_LAYER_MODEL.md\n", encoding="utf-8")
    (rpg / "PROVENANCE.md").write_text("legacy/raw/RPG_LAYER_MODEL.md\n", encoding="utf-8")
    (rpg / "parts" / "world-grammar" / "README.md").write_text(
        "RPG_LAYER_MODEL.md\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(module, "REPO_ROOT", repo)
    monkeypatch.setattr(module, "RPG_ROOT", rpg)

    problems: list[str] = []
    module.validate_active_docs_are_clean(problems)

    assert "mechanics/rpg/README.md should route through PROVENANCE.md instead of legacy/raw" in problems
    assert "mechanics/rpg/README.md should not expose raw RPG_* filenames in active route" in problems
    assert "mechanics/rpg/parts/world-grammar/README.md should stay active and not expose raw legacy source names" in problems
    assert not any(problem.startswith("mechanics/rpg/PROVENANCE.md") for problem in problems)


def test_active_route_rejects_wave_language(tmp_path, monkeypatch) -> None:
    module = load_validator()
    repo = tmp_path / "repo"
    rpg = repo / "mechanics" / "rpg"
    part = rpg / "parts" / "quest-campaign"
    part.mkdir(parents=True)
    (rpg / "README.md").write_text("This first wave is active again.\n", encoding="utf-8")
    (part / "README.md").write_text(
        "## Use When\n\nThis wave is a bridge, not a throne.\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(module, "REPO_ROOT", repo)
    monkeypatch.setattr(module, "RPG_ROOT", rpg)

    problems: list[str] = []
    module.validate_active_docs_are_clean(problems)

    assert "mechanics/rpg/README.md should not use wave-era language in active route" in problems
    assert any(problem.endswith("should not use wave-era language in active route") for problem in problems)
    assert any(problem.endswith("should not keep bridge-wave slogans in active route") for problem in problems)


def test_part_readmes_use_common_active_route_shape() -> None:
    module = load_validator()

    problems: list[str] = []
    module.validate_part_readme_shape(problems)

    assert problems == []


def test_part_contracts_use_common_output_gate_shape() -> None:
    module = load_validator()

    problems: list[str] = []
    module.validate_part_contract_shape(problems)

    assert problems == []


def test_usage_contract_is_complete() -> None:
    module = load_validator()

    problems: list[str] = []
    module.validate_usage_contract(problems)

    assert problems == []


def test_playable_obligation_route_is_complete() -> None:
    module = load_validator()

    problems: list[str] = []
    module.validate_playable_obligation_route(problems)

    assert problems == []


def test_worked_route_example_is_single_and_complete() -> None:
    module = load_validator()

    problems: list[str] = []
    module.validate_worked_route_example(problems)

    assert problems == []
