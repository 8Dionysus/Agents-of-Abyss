from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
WAVE3_PREFIXES = (
    "adoption_",
    "agent_adoption_",
    "agent_kind_",
    "agonic_",
    "aoa_experience_",
    "assistant_adoption_",
    "assistant_pattern_",
    "cross_repo_",
    "experience_adoption_",
    "experience_downstream_",
    "experience_owner_",
    "experience_pattern_",
    "experience_shadow_",
    "federation_",
    "kag_",
    "memo_to_kag_",
    "office_",
    "pattern_",
    "playbook_pattern_",
    "route_rule_",
    "sdk_",
    "shadow_",
    "shared_",
    "skill_",
    "source_owner_",
    "technique_",
    "tos_",
)


def load_validator():
    path = ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "scripts" / "validate_adoption_federation.py"
    spec = importlib.util.spec_from_file_location("experience_wave3_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads((ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "examples" / "experience_wave3_federation_adoption.example.json").read_text())


def load_contract(stem: str) -> tuple[dict[str, object], dict[str, object]]:
    schema_path = ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "schemas" / f"{stem}_v1.json"
    if stem == "experience_wave3_federation_adoption":
        schema_path = ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "schemas" / "experience-wave3-federation-adoption.schema.json"
    example_path = ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "examples" / f"{stem}.example.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    example = json.loads(example_path.read_text(encoding="utf-8"))
    return schema, example


def wave3_stems() -> set[str]:
    stems: set[str] = set()
    for example_path in sorted((ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "examples").glob("*.example.json")):
        stem = example_path.name.removesuffix(".example.json")
        if stem.endswith("_v1"):
            continue
        if stem.startswith(WAVE3_PREFIXES):
            stems.add(stem)
    for schema_path in sorted((ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "schemas").glob("*_v1.json")):
        stem = schema_path.name.removesuffix("_v1.json")
        if not (ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "examples" / f"{stem}.example.json").exists() and (
            ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "examples" / f"{stem}_v1.example.json"
        ).exists():
            continue
        if stem.startswith(WAVE3_PREFIXES):
            stems.add(stem)
    stems.add("experience_wave3_federation_adoption")
    return stems


def validation_errors(schema: dict[str, object], value: dict[str, object]) -> list[object]:
    return sorted(Draft202012Validator(schema).iter_errors(value), key=lambda error: list(error.path))


def assert_invalid(schema: dict[str, object], value: dict[str, object], label: str) -> None:
    errors = validation_errors(schema, value)
    assert errors, f"{label} unexpectedly validated"


def wrong_type_value(value: object) -> object:
    if isinstance(value, bool):
        return "not-a-boolean"
    if isinstance(value, int) and not isinstance(value, bool):
        return "not-an-integer"
    if isinstance(value, float):
        return "not-a-number"
    if isinstance(value, str):
        return 12345
    if isinstance(value, list):
        return {"not": "an array"}
    if isinstance(value, dict):
        return "not-an-object"
    return "not-null"


def test_experience_wave3_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/experience/parts/adoption-federation/scripts/validate_adoption_federation.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_wave3_rejects_codex_kag_promotion() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    may = authority["codex_may"]
    assert isinstance(may, list)
    may.append("promote to KAG")

    with pytest.raises(validator.ValidationError, match="denied authority"):
        validator.validate_example(bad_flow)


def test_experience_wave3_rejects_direct_tos_write() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    denied = authority["codex_must_not"]
    assert isinstance(denied, list)
    denied.remove("write directly to Tree-of-Sophia")

    with pytest.raises(validator.ValidationError, match="codex_must_not"):
        validator.validate_example(bad_flow)


def test_experience_wave3_requires_ordered_adoption_rollback() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    adoption_flow = bad_flow["adoption_flow"]
    assert isinstance(adoption_flow, list)
    adoption_flow.pop(8)

    with pytest.raises(validator.ValidationError, match="ordered spine"):
        validator.validate_example(bad_flow)


def test_experience_wave3_requires_owner_consent_step() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    adoption_flow = bad_flow["adoption_flow"]
    assert isinstance(adoption_flow, list)
    del adoption_flow[2]

    with pytest.raises(validator.ValidationError, match="ordered spine"):
        validator.validate_example(bad_flow)


def test_experience_wave3_requires_retention_step() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    adoption_flow = bad_flow["adoption_flow"]
    assert isinstance(adoption_flow, list)
    adoption_flow.pop()

    with pytest.raises(validator.ValidationError, match="ordered spine"):
        validator.validate_example(bad_flow)


def test_experience_wave3_rejects_routing_meaning_theft() -> None:
    validator = load_validator()
    flow = load_example()
    bad_flow = copy.deepcopy(flow)
    authority = bad_flow["authority"]
    assert isinstance(authority, dict)
    denied = authority["codex_must_not"]
    assert isinstance(denied, list)
    denied.remove("author routing meaning")

    with pytest.raises(validator.ValidationError, match="codex_must_not"):
        validator.validate_example(bad_flow)


def test_seeded_wave3_examples_validate_against_schemas() -> None:
    stems = wave3_stems()
    assert stems
    missing_pairs: list[str] = []
    for stem in sorted(stems):
        schema_path = ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "schemas" / f"{stem}_v1.json"
        if stem == "experience_wave3_federation_adoption":
            schema_path = ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "schemas" / "experience-wave3-federation-adoption.schema.json"
        example_path = ROOT / "mechanics" / "experience" / "parts" / "adoption-federation" / "examples" / f"{stem}.example.json"
        if not schema_path.exists():
            missing_pairs.append(f"{example_path.relative_to(ROOT)} -> {schema_path.relative_to(ROOT)}")
        if not example_path.exists():
            missing_pairs.append(f"{schema_path.relative_to(ROOT)} -> {example_path.relative_to(ROOT)}")
    assert not missing_pairs, "missing wave3 contract pair(s): " + ", ".join(missing_pairs)

    for stem in sorted(stems):
        schema, example = load_contract(stem)
        Draft202012Validator.check_schema(schema)
        errors = validation_errors(schema, example)
        assert not errors, f"{stem}: {errors[0].message if errors else ''}"


def test_seeded_wave3_schemas_reject_escape_hatches() -> None:
    stems = wave3_stems()
    assert stems
    for stem in sorted(stems):
        schema, example = load_contract(stem)

        with_unknown_top = copy.deepcopy(example)
        with_unknown_top["contract_escape"] = True
        assert_invalid(schema, with_unknown_top, f"{stem} unknown top-level field")

        refs = example.get("refs")
        if isinstance(refs, dict):
            with_unknown_ref = copy.deepcopy(example)
            assert isinstance(with_unknown_ref["refs"], dict)
            with_unknown_ref["refs"]["contract_escape"] = "loose-ref"
            assert_invalid(schema, with_unknown_ref, f"{stem} unknown refs field")

        payload = example.get("payload")
        if isinstance(payload, dict):
            with_unknown_payload = copy.deepcopy(example)
            assert isinstance(with_unknown_payload["payload"], dict)
            with_unknown_payload["payload"]["contract_escape"] = "loose-payload"
            assert_invalid(schema, with_unknown_payload, f"{stem} unknown payload field")

            if payload:
                key = next(iter(payload))
                with_wrong_payload_type = copy.deepcopy(example)
                assert isinstance(with_wrong_payload_type["payload"], dict)
                with_wrong_payload_type["payload"][key] = wrong_type_value(payload[key])
                assert_invalid(schema, with_wrong_payload_type, f"{stem} wrong payload type")
