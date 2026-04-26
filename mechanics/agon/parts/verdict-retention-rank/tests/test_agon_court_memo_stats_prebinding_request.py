from __future__ import annotations
import pathlib
import subprocess
import sys

def _repo_root() -> pathlib.Path:
    for candidate in pathlib.Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()


def run(cmd):
    return subprocess.run([sys.executable, *cmd], cwd=ROOT, text=True, capture_output=True)


def test_wave7_generated_surface_is_current():
    result = run(['mechanics/agon/parts/verdict-retention-rank/scripts/build_agon_court_memo_stats_prebinding_request.py', '--check'])
    assert result.returncode == 0, result.stderr


def test_wave7_validator_passes():
    result = run(['mechanics/agon/parts/verdict-retention-rank/scripts/validate_agon_court_memo_stats_prebinding_request.py'])
    assert result.returncode == 0, result.stderr
