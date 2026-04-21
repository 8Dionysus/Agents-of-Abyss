from __future__ import annotations
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_wave17_registry_shape():
    reg = json.loads((ROOT / 'generated/agon_kag_promotion_path_registry.min.json').read_text(encoding='utf-8'))
    assert reg['wave'] == 'XVII'
    assert reg['count'] == 10
    assert len(reg['kag_promotion_components']) == 10
    for item in reg['kag_promotion_components']:
        assert item['live_protocol'] is False
        assert 'no_kag_as_canon' in item.get('stop_lines', [])
        assert 'single_event_promotion' in item.get('forbidden_effects', [])
        assert item.get('canonical_status') not in ('canon', 'canonical', 'tree_of_sophia_canon')

def test_builder_check_and_validator():
    assert subprocess.run([sys.executable, str(ROOT / 'scripts/build_agon_kag_promotion_path_registry.py'), '--check'], cwd=ROOT).returncode == 0
    assert subprocess.run([sys.executable, str(ROOT / 'scripts/validate_agon_kag_promotion_path_registry.py')], cwd=ROOT).returncode == 0
