#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / 'config' / 'agon_arena_session_models.seed.json'
GENERATED = ROOT / 'generated' / 'agon_arena_session_model_registry.min.json'


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def dump_min(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n'


def build(config: dict) -> dict:
    records = sorted(config.get('session_models', []), key=lambda r: r.get('session_model_id', ''))
    moves = sorted({m for r in records for m in r.get('charter', {}).get('allowed_lawful_moves', [])})
    pressures = sorted({p.get('pressure_id') for r in records for p in r.get('pressure_profiles', []) if p.get('pressure_id')})
    outcomes = sorted({o.get('outcome_id') for r in records for o in r.get('terminal_outcomes', []) if o.get('outcome_id')})
    return {
        'schema_version': 'agon_arena_session_model_registry_v1',
        'source': 'config/agon_arena_session_models.seed.json',
        'wave': config.get('wave'),
        'owner_repo': config.get('owner_repo'),
        'status': config.get('status'),
        'live_protocol': config.get('live_protocol'),
        'runtime_effect': config.get('runtime_effect'),
        'registry_ref': config.get('registry_ref'),
        'session_model_count': len(records),
        'session_model_ids': [r.get('session_model_id') for r in records],
        'lawful_moves_referenced': moves,
        'pressure_profiles_referenced': pressures,
        'terminal_outcome_slots': outcomes,
        'reserved_future_slots': ['sealed_commit_slot', 'reveal_slot', 'adjudication_slot', 'inscription_slot', 'retention_slot'],
        'records': records,
        'required_stop_lines': config.get('required_stop_lines', []),
        'notes': config.get('notes', ''),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description='Build Agon arena session model registry.')
    parser.add_argument('--check', action='store_true', help='Fail if generated output is stale.')
    args = parser.parse_args()
    if not CONFIG.exists():
        print(f'missing config: {CONFIG}', file=sys.stderr)
        return 2
    rendered = dump_min(build(load(CONFIG)))
    if args.check:
        if not GENERATED.exists():
            print(f'missing generated registry: {GENERATED}', file=sys.stderr)
            return 1
        if GENERATED.read_text(encoding='utf-8') != rendered:
            print('generated/agon_arena_session_model_registry.min.json is stale', file=sys.stderr)
            return 1
        print('agon arena session model registry is up to date')
        return 0
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_text(rendered, encoding='utf-8')
    print(f'wrote {GENERATED}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
