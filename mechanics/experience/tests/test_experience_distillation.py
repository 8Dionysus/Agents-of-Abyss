from __future__ import annotations

import importlib.util
import json
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


def test_historical_receipts_accept_full_commit_sources() -> None:
    module = load_validator()
    problems: list[str] = []
    ids = module.validate_provenance_receipts(problems)
    assert ids
    assert problems == []


def test_historical_receipts_reject_floating_or_traversing_refs(monkeypatch) -> None:
    module = load_validator()
    original = module.load_provenance_receipts()
    for suffix in (
        "blob/main/mechanics/agon/legacy/raw/AGON_WAVE17_LANDING.md",
        "blob/" + "a" * 40 + "/mechanics/agon/../legacy/raw/packet.md",
    ):
        data = json.loads(json.dumps(original))
        data["receipts"][0]["source_ref"] = module.HISTORICAL_SOURCE_PREFIX + suffix
        monkeypatch.setattr(module, "load_provenance_receipts", lambda: data)
        problems: list[str] = []
        module.validate_provenance_receipts(problems)
        assert any("historical source_ref must use a full commit" in p for p in problems)


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
    assert not (ROOT / "mechanics/experience/legacy").exists()


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


def test_part_validation_commands_use_routed_manifest() -> None:
    module = load_validator()
    problems: list[str] = []
    route_data = json.loads(
        (ROOT / "mechanics" / "validation-routes.json").read_text(encoding="utf-8")
    )

    module.validate_parts(None, problems)

    assert problems == []
    for slug in module.PART_SLUGS:
        validation = (
            ROOT / "mechanics" / "experience" / "parts" / slug / "VALIDATION.md"
        ).read_text(encoding="utf-8")
        assert "mechanics/validation-routes.json" in validation
        assert "run_validation_route.py --surface" in validation
        route = route_data["routes"][
            f"mechanics/experience/parts/{slug}/VALIDATION.md"
        ]
        route_text = "\n".join(" ".join(command) for command in route["commands"])
        assert route["owner_card"] == "mechanics/experience/parts/AGENTS.md"
        assert f"validate_experience_distillation.py --part {slug}" in route_text


def test_raw_legacy_readme_uses_package_validator_route() -> None:
    assert not (ROOT / "mechanics/experience/legacy").exists()


def test_receipt_ref_schema_without_explicit_values_is_shape_only(tmp_path, monkeypatch) -> None:
    module = load_validator()
    parts = tmp_path / "parts"
    parts.mkdir()
    (parts / "schema.json").write_text(
        json.dumps(
            {
                "type": "object",
                "properties": {
                    "source_receipt_refs": {
                        "type": "array",
                        "items": {"type": "string"},
                    }
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(module, "PARTS_ROOT", parts)
    monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
    problems: list[str] = []

    module.validate_active_receipt_refs({"receipt:v1"}, problems)

    assert problems == []


def test_receipt_ref_schema_items_enum_is_validated(tmp_path, monkeypatch) -> None:
    module = load_validator()
    parts = tmp_path / "parts"
    parts.mkdir()
    (parts / "schema.json").write_text(
        json.dumps(
            {
                "type": "object",
                "properties": {
                    "source_receipt_refs": {
                        "type": "array",
                        "items": {"enum": ["receipt:missing"]},
                    }
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(module, "PARTS_ROOT", parts)
    monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
    problems: list[str] = []

    module.validate_active_receipt_refs({"receipt:v1"}, problems)

    assert any("unknown receipt ref 'receipt:missing'" in problem for problem in problems)
