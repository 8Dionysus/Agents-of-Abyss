from __future__ import annotations

import importlib.util
from pathlib import Path


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


ROOT = _repo_root()
VALIDATOR = ROOT / "mechanics" / "questbook" / "scripts" / "validate_questbook_distillation.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_questbook_distillation", VALIDATOR)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_questbook_distillation_is_valid() -> None:
    module = load_validator()

    assert module.validate() == []


def test_questbook_distillation_single_part_is_valid() -> None:
    module = load_validator()

    assert module.validate({"lane-owner-routes"}) == []


def test_active_docs_reject_direct_raw_legacy_links(monkeypatch) -> None:
    module = load_validator()
    original_read = module.read
    target = ROOT / "mechanics" / "questbook" / "parts" / "README.md"

    def fake_read(path: Path) -> str:
        if path == target:
            return "See [raw](../legacy/raw/QUESTBOOK_FIRST_WAVE.md) for the current route.\n"
        return original_read(path)

    monkeypatch.setattr(module, "read", fake_read)
    problems: list[str] = []

    module.validate_no_direct_raw_links(problems)

    assert any("legacy/raw" in problem for problem in problems)


def test_validation_commands_are_centralized(monkeypatch) -> None:
    module = load_validator()
    original_read = module.read
    target = ROOT / "mechanics" / "questbook" / "parts" / "README.md"

    def fake_read(path: Path) -> str:
        if path == target:
            return "## Validation\n\n```bash\npython scripts/validate_links.py\n```\n"
        return original_read(path)

    monkeypatch.setattr(module, "read", fake_read)
    problems: list[str] = []

    module.validate_validation_commands_are_centralized(problems)

    assert any("must route validation commands" in problem for problem in problems)


def test_legacy_index_maps_raw_sources_to_active_parts() -> None:
    module = load_validator()
    problems: list[str] = []

    module.validate_legacy_index(problems)

    assert problems == []
