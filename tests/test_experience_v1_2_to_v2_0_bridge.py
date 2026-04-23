from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_validator():
    path = ROOT / "scripts" / "validate_experience_v1_2_to_v2_0_bridge.py"
    spec = importlib.util.spec_from_file_location("experience_bridge_validator_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_example() -> dict[str, object]:
    return json.loads(
        (ROOT / "examples" / "experience_v1_2_to_v2_0_bridge.example.json").read_text(
            encoding="utf-8"
        )
    )


def load_schema() -> dict[str, object]:
    return json.loads(
        (ROOT / "schemas" / "experience-v1-2-v2-0-bridge.schema.json").read_text(
            encoding="utf-8"
        )
    )


def test_experience_bridge_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_experience_v1_2_to_v2_0_bridge.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_experience_bridge_requires_source_order() -> None:
    validator = load_validator()
    bridge = load_example()
    schema = load_schema()
    bad_bridge = copy.deepcopy(bridge)
    seeds = bad_bridge["source_seeds"]
    assert isinstance(seeds, list)
    seeds.reverse()

    with pytest.raises(validator.ValidationError, match="source_seeds"):
        validator.validate_payload(bad_bridge, schema)


def test_experience_bridge_rejects_runtime_effect() -> None:
    validator = load_validator()
    bridge = load_example()
    schema = load_schema()
    bad_bridge = copy.deepcopy(bridge)
    bad_bridge["runtime_effect"] = "live"

    with pytest.raises(validator.ValidationError, match="schema"):
        validator.validate_payload(bad_bridge, schema)


def test_experience_bridge_rejects_codex_live_arena_authority() -> None:
    validator = load_validator()
    bridge = load_example()
    schema = load_schema()
    bad_bridge = copy.deepcopy(bridge)
    authority = bad_bridge["authority"]
    assert isinstance(authority, dict)
    may = authority["codex_may"]
    assert isinstance(may, list)
    may.append("open live arena")

    with pytest.raises(validator.ValidationError, match="forbidden authority"):
        validator.validate_payload(bad_bridge, schema)


def test_experience_bridge_requires_assistant_contestant_denial() -> None:
    validator = load_validator()
    bridge = load_example()
    schema = load_schema()
    bad_bridge = copy.deepcopy(bridge)
    authority = bad_bridge["authority"]
    assert isinstance(authority, dict)
    denied = authority["assistant_must_not"]
    assert isinstance(denied, list)
    denied.remove("become contestant")

    with pytest.raises(validator.ValidationError, match="assistant_must_not"):
        validator.validate_payload(bad_bridge, schema)


def test_experience_bridge_requires_all_owner_repos() -> None:
    validator = load_validator()
    bridge = load_example()
    schema = load_schema()
    bad_bridge = copy.deepcopy(bridge)
    owner_split = bad_bridge["owner_split"]
    assert isinstance(owner_split, list)
    owner_split[:] = [
        item for item in owner_split if item.get("repo") != "Tree-of-Sophia"
    ]

    with pytest.raises(validator.ValidationError, match="owner_split"):
        validator.validate_payload(bad_bridge, schema)


def test_experience_bridge_requires_runtime_owner_gate() -> None:
    validator = load_validator()
    bridge = load_example()
    schema = load_schema()
    bad_bridge = copy.deepcopy(bridge)
    owner_split = bad_bridge["owner_split"]
    assert isinstance(owner_split, list)
    for entry in owner_split:
        if entry.get("repo") == "abyss-stack":
            entry["owns"] = "runtime deployment storage and worker substrate"

    with pytest.raises(validator.ValidationError, match="runtime-owner gate"):
        validator.validate_payload(bad_bridge, schema)


def test_experience_bridge_requires_campaign_route_order() -> None:
    validator = load_validator()
    bridge = load_example()
    schema = load_schema()
    bad_bridge = copy.deepcopy(bridge)
    route = bad_bridge["campaign_route"]
    assert isinstance(route, list)
    route[4], route[5] = route[5], route[4]

    with pytest.raises(validator.ValidationError, match="contiguous|spine"):
        validator.validate_payload(bad_bridge, schema)
