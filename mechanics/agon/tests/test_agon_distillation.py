from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


ROOT = _repo_root()
VALIDATOR_PATH = ROOT / "mechanics" / "agon" / "scripts" / "validate_agon_distillation.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location("validate_agon_distillation", VALIDATOR_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_agon_distillation_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/agon/scripts/validate_agon_distillation.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_active_part_artifact_hygiene_rejects_numbered_wave_tokens_inside_labels(tmp_path) -> None:
    module = _load_validator()
    parts = tmp_path / "parts"
    artifact = parts / "packet-arena" / "config" / "bad.json"
    artifact.parent.mkdir(parents=True)
    artifact.write_text('{"label":"reserved_for_wave9_state_packets"}\n', encoding="utf-8")

    module.PARTS_ROOT = parts
    module.rel = lambda path: Path(path).as_posix()
    problems: list[str] = []
    module.validate_active_part_artifact_hygiene(problems)

    assert any("active part artifact pollution pattern" in problem for problem in problems)
