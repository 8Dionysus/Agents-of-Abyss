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
    / "parts"
    / "release-deployment"
    / "scripts"
    / "validate_release_deployment.py"
)


def load_validator():
    spec = importlib.util.spec_from_file_location(
        "validate_release_deployment", VALIDATOR
    )
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_release_deployment_artifacts_are_valid() -> None:
    module = load_validator()

    assert module.run_validation() == []


def test_release_deployment_has_local_validator_and_test() -> None:
    module = load_validator()
    artifacts = module.release_artifacts()
    paths = {item["path"] for item in artifacts}

    assert (
        "mechanics/experience/parts/release-deployment/scripts/validate_release_deployment.py"
        in paths
    )
    assert (
        "mechanics/experience/parts/release-deployment/tests/test_release_deployment.py"
        in paths
    )
