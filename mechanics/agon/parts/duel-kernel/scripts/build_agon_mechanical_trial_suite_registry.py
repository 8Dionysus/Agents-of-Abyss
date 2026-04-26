#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, hashlib, pathlib, sys
def _repo_root() -> pathlib.Path:
    for candidate in pathlib.Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
SRC = ROOT / 'mechanics/agon/parts/duel-kernel/config/agon_mechanical_trial_suites.seed.json'
OUT = ROOT / 'mechanics/agon/parts/duel-kernel/generated/agon_mechanical_trial_suite_registry.min.json'
ITEM_KEY = 'trials'
REGISTRY_ID = 'agon.mechanical_trial_suite.registry.v0'
LINEAGE_REF = 'mechanical-trial-suite'

def digest_obj(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def build():
    data = json.loads(SRC.read_text(encoding='utf-8'))
    items = data.get(ITEM_KEY, [])
    return {
        'registry_id': data.get('registry_id', REGISTRY_ID),
        'lineage_ref': data.get('lineage_ref', LINEAGE_REF),
        'runtime_posture': data.get('runtime_posture', 'candidate_only'),
        'count': len(items),
        ITEM_KEY: items,
        'digest': digest_obj(items),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    reg = build()
    txt = json.dumps(reg, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n'
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding='utf-8') != txt:
            print('generated registry drift: run this builder without --check', file=sys.stderr)
            return 1
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(txt, encoding='utf-8')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
