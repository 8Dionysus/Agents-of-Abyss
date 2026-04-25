from __future__ import annotations
import json, pathlib, subprocess, sys
def _repo_root() -> pathlib.Path:
    for candidate in pathlib.Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()

def test_wave17_registry_shape():
    reg = json.loads((ROOT / 'mechanics/agon/generated/agon_kag_promotion_path_registry.min.json').read_text(encoding='utf-8'))
    assert reg['wave'] == 'XVII'
    assert reg['count'] == 10
    assert len(reg['kag_promotion_components']) == 10
    for item in reg['kag_promotion_components']:
        assert item['live_protocol'] is False
        assert 'no_kag_as_canon' in item.get('stop_lines', [])
        assert 'single_event_promotion' in item.get('forbidden_effects', [])
        assert item.get('canonical_status') not in ('canon', 'canonical', 'tree_of_sophia_canon')

def test_builder_check_and_validator():
    assert subprocess.run([sys.executable, str(ROOT / 'mechanics/agon/scripts/build_agon_kag_promotion_path_registry.py'), '--check'], cwd=ROOT).returncode == 0
    assert subprocess.run([sys.executable, str(ROOT / 'mechanics/agon/scripts/validate_agon_kag_promotion_path_registry.py')], cwd=ROOT).returncode == 0
