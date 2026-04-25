from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()


def run_script(rel: str, *args: str):
    return subprocess.run([sys.executable, '-S', str(ROOT / rel), *args], cwd=ROOT, text=True, capture_output=True)


def test_arena_session_registry_is_up_to_date():
    result = run_script('scripts/build_agon_arena_session_model_registry.py', '--check')
    assert result.returncode == 0, result.stderr + result.stdout


def test_arena_session_models_validate():
    result = run_script('scripts/validate_agon_arena_session_models.py')
    assert result.returncode == 0, result.stderr + result.stdout


def test_registry_remains_pre_protocol():
    registry = json.loads((ROOT / 'generated' / 'agon_arena_session_model_registry.min.json').read_text(encoding='utf-8'))
    assert registry['live_protocol'] is False
    assert registry['runtime_effect'] == 'none'
    assert registry['session_model_count'] >= 8
    assert 'sealed_commit_slot' in registry['reserved_future_slots']
    for record in registry['records']:
        assert record['live_protocol'] is False
        assert record['runtime_effect'] == 'none'
        assert record['seats']['contestants']['cannot_be_assistant'] is True
        assert record['seats']['judge']['live_verdict_authority'] is False
        assert all(outcome['live_authority'] is False for outcome in record['terminal_outcomes'])
