#!/usr/bin/env python3
"""Validate release-deployment schemas and examples in their active part home."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


ROOT = _repo_root()
PART = "release-deployment"
ARTIFACT_MAP_PATH = ROOT / "mechanics" / "experience" / "artifact-map.json"
PART_ROOT = ROOT / "mechanics" / "experience" / "parts" / PART


class ValidationError(RuntimeError):
    """Raised when the release-deployment artifact set drifts."""


def fail(message: str) -> None:
    raise ValidationError(message)


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        fail(f"missing JSON file: {path.relative_to(ROOT).as_posix()}")
        raise AssertionError from exc
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT).as_posix()}: {exc}")
        raise AssertionError from exc


def normalized_contract_name(path_ref: str) -> str:
    name = Path(path_ref).name
    for suffix in (".schema.json", ".example.json", ".json"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break
    if name.endswith("_v1"):
        name = name[:-3]
    return name


def release_artifacts() -> list[dict[str, Any]]:
    data = read_json(ARTIFACT_MAP_PATH)
    artifacts = data.get("artifacts")
    if not isinstance(artifacts, list):
        fail("artifact-map artifacts must be a list")
    return [
        item
        for item in artifacts
        if isinstance(item, dict) and item.get("part") == PART
    ]


def validate_artifact_home(artifacts: list[dict[str, Any]]) -> None:
    if not (PART_ROOT / "schemas").is_dir():
        fail("release-deployment schemas directory is missing")
    if not (PART_ROOT / "examples").is_dir():
        fail("release-deployment examples directory is missing")
    if not any(item.get("kind") == "script" for item in artifacts):
        fail("release-deployment must own a local validator")
    if not any(item.get("kind") == "test" for item in artifacts):
        fail("release-deployment must own a local test")

    for item in artifacts:
        path_ref = str(item.get("path", ""))
        if not path_ref.startswith("mechanics/experience/parts/release-deployment/"):
            fail(f"release-deployment artifact outside part home: {path_ref}")
        if not (ROOT / path_ref).is_file():
            fail(f"release-deployment artifact missing: {path_ref}")


def validate_schema_example_pairs(artifacts: list[dict[str, Any]]) -> None:
    pairs: dict[str, dict[str, str]] = {}
    for item in artifacts:
        kind = item.get("kind")
        if kind not in {"schema", "example"}:
            continue
        path_ref = str(item.get("path", ""))
        pairs.setdefault(normalized_contract_name(path_ref), {})[str(kind)] = path_ref

    if len(pairs) < 20:
        fail("release-deployment must keep a substantial schema/example contract set")

    missing = sorted(
        name for name, pair in pairs.items() if set(pair) != {"schema", "example"}
    )
    if missing:
        fail("release-deployment missing schema/example pair(s): " + ", ".join(missing))

    for name, pair in sorted(pairs.items()):
        schema = read_json(ROOT / pair["schema"])
        example = read_json(ROOT / pair["example"])
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema).iter_errors(example),
            key=lambda err: list(err.absolute_path),
        )
        if errors:
            first = errors[0]
            fail(
                f"{name} example does not match schema at {list(first.absolute_path)}: {first.message}"
            )


def run_validation() -> list[str]:
    try:
        artifacts = release_artifacts()
        validate_artifact_home(artifacts)
        validate_schema_example_pairs(artifacts)
    except ValidationError as exc:
        return [str(exc)]
    return []


def main() -> int:
    errors = run_validation()
    if errors:
        for error in errors:
            print(f"[error] {error}", file=sys.stderr)
        return 1
    print("ok: Experience release-deployment artifacts are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
