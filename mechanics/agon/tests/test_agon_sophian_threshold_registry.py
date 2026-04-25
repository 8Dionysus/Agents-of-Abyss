from __future__ import annotations

import json
import pathlib
import subprocess
import sys

def _repo_root() -> pathlib.Path:
    for candidate in pathlib.Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
GENERATED = ROOT / 'mechanics/agon/generated/agon_sophian_threshold_registry.min.json'
SCRIPT = ROOT / 'mechanics/agon/scripts/build_agon_sophian_threshold_registry.py'
VALIDATOR = ROOT / 'mechanics/agon/scripts/validate_agon_sophian_threshold_registry.py'
EXPECTED_COUNT = 10
ITEM_KEY = 'threshold_components'

def test_generated_registry_shape():
    reg = json.loads(GENERATED.read_text(encoding='utf-8'))
    assert reg['wave'] == 'XVIII'
    assert reg['count'] == EXPECTED_COUNT
    assert len(reg[ITEM_KEY]) == EXPECTED_COUNT
    assert all(item.get('live_protocol') is False for item in reg[ITEM_KEY])
    assert all(item.get('review_status') == 'candidate_only' for item in reg[ITEM_KEY])

def test_builder_check():
    result = subprocess.run([sys.executable, str(SCRIPT), '--check'], cwd=str(ROOT), text=True, capture_output=True)
    assert result.returncode == 0, result.stderr


def test_validator():
    result = subprocess.run([sys.executable, str(VALIDATOR)], cwd=str(ROOT), text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
