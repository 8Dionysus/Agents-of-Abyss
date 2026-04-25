#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
CONFIG = ROOT / 'config' / 'agon_ccs_laws.seed.json'
OUT = ROOT / 'generated' / 'agon_ccs_law_registry.min.json'


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def build(seed: dict) -> dict:
    laws = []
    for fam in seed['law_families']:
        laws.append({
            'law_family': fam['law_family'],
            'law_id': fam['law_id'],
            'statement': fam['statement'],
            'allowed_lawful_moves': fam['allowed_lawful_moves'],
            'owner_handoffs': fam['owner_handoffs'],
            'not_granted': fam['not_granted'],
        })
    return {
        'registry_id': seed['registry_id'],
        'version': seed['version'],
        'wave': seed['wave'],
        'status': seed['status'],
        'home_repo': seed['home_repo'],
        'live_protocol': False,
        'runtime_effect': 'none',
        'law_family_count': len(seed['law_families']),
        'law_families': [l['law_family'] for l in seed['law_families']],
        'law_ids': [l['law_id'] for l in seed['law_families']],
        'interlock_count': len(seed['interlocks']),
        'interlock_ids': [i['interlock_id'] for i in seed['interlocks']],
        'contradiction_statuses': next(l['status_model'] for l in seed['law_families'] if l['law_family'] == 'contradiction'),
        'closure_denial_reasons': next(l['denial_reasons'] for l in seed['law_families'] if l['law_family'] == 'closure'),
        'summon_types': next(l['summon_types'] for l in seed['law_families'] if l['law_family'] == 'summon'),
        'stop_lines': seed['stop_lines'],
        'assistant_boundary': seed['assistant_boundary'],
        'laws': laws,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()

    expected = build(load_json(CONFIG))
    text = json.dumps(expected, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n'

    if args.check:
        if not OUT.exists():
            raise SystemExit(f'missing generated registry: {OUT}')
        if OUT.read_text(encoding='utf-8') != text:
            raise SystemExit('generated/agon_ccs_law_registry.min.json is out of date')
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
