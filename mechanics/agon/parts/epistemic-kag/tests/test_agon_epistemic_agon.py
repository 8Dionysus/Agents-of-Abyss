from __future__ import annotations
import json, pathlib, subprocess, sys
def _repo_root() -> pathlib.Path:
    for candidate in pathlib.Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()

def test_generated_registry_shape():
    reg = json.loads((ROOT / 'mechanics/agon/parts/epistemic-kag/generated/agon_epistemic_agon_registry.min.json').read_text(encoding='utf-8'))
    assert reg['wave'] == 'XV'
    assert reg['runtime_posture'] in ('candidate_only', 'pre_protocol_candidate_only')
    assert reg['count'] == 8
    assert len(reg['epistemic_components']) == 8
    assert set(reg['epistemic_move_extensions']) == {
        move
        for item in reg['epistemic_components']
        for move in item['move_extensions']
    }
    for item in reg['epistemic_components']:
        assert item['live_protocol'] is False
        assert 'auto_doctrine_rewrite' in item.get('forbidden_effects', [])

def test_builder_check_and_validator():
    assert subprocess.run([sys.executable, str(ROOT / 'mechanics/agon/parts/epistemic-kag/scripts/build_agon_epistemic_agon_registry.py'), '--check'], cwd=ROOT).returncode == 0
    assert subprocess.run([sys.executable, str(ROOT / 'mechanics/agon/parts/epistemic-kag/scripts/validate_agon_epistemic_agon.py')], cwd=ROOT).returncode == 0
