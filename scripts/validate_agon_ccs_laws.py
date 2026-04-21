#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / 'config' / 'agon_ccs_laws.seed.json'
REGISTRY = ROOT / 'generated' / 'agon_ccs_law_registry.min.json'
REQUIRED_FAMILIES = {'contradiction', 'closure', 'summon'}
FORBIDDEN_GRANTS = {'live_closure', 'live_summon', 'verdict_authority', 'durable_scar_write', 'rank_mutation', 'tree_of_sophia_promotion'}


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def validate() -> None:
    seed = load(CONFIG)
    reg = load(REGISTRY)
    assert seed['live_protocol'] is False, 'seed must remain pre-protocol'
    assert seed['runtime_effect'] == 'none', 'seed must have no runtime effect'
    assert reg['live_protocol'] is False, 'registry must remain pre-protocol'
    assert reg['runtime_effect'] == 'none', 'registry must have no runtime effect'
    assert set(reg['law_families']) == REQUIRED_FAMILIES, 'must contain exactly contradiction, closure, summon families'
    assert reg['law_family_count'] == 3, 'law family count mismatch'

    families = {f['law_family']: f for f in seed['law_families']}
    contradiction = families['contradiction']
    closure = families['closure']
    summon = families['summon']

    assert 'open' in contradiction['status_model'], 'contradiction must support open status'
    assert 'localized' in contradiction['status_model'], 'contradiction must support localized status'
    assert contradiction['required_notice_packet'] == 'agon.contradiction_notice', 'contradiction law must bind to notice packet'

    closure_predicates = {p['predicate'] for p in closure['closure_predicates']}
    assert 'no_open_material_contradiction' in closure_predicates, 'closure must check open material contradiction'
    assert 'actor_lacks_closure_jurisdiction' in closure['denial_reasons'], 'closure must deny missing jurisdiction'
    assert closure['earned_jurisdiction']['granted_by_wave10'] is False, 'wave X must not grant closer jurisdiction'

    assert 'hidden_summon' in summon['prohibitions'], 'summon law must forbid hidden summon'
    assert 'assistant_initiated_summon' in summon['prohibitions'], 'summon law must forbid assistant-initiated summon'
    assert summon['cost_model']['granted_by_wave10'] is False, 'wave X must not grant summon currency or jurisdiction'

    interlocks = {i['interlock_id'] for i in seed['interlocks']}
    assert 'contradiction_blocks_closure' in interlocks, 'missing contradiction->closure interlock'
    assert 'summon_cannot_bypass_contradiction' in interlocks, 'missing summon->contradiction interlock'

    assistant_must_not = set(seed['assistant_boundary']['assistant_must_not'])
    assert {'become_contestant', 'grant_closure', 'initiate_summon', 'issue_verdict'} <= assistant_must_not, 'assistant boundary is too weak'

    all_text = json.dumps(seed, sort_keys=True)
    for forbidden in FORBIDDEN_GRANTS:
        if forbidden in all_text:
            assert f'no_{forbidden}' in all_text or forbidden in json.dumps([f.get('not_granted', []) for f in seed['law_families']]), f'possible forbidden authority leak: {forbidden}'


if __name__ == '__main__':
    validate()
    print('agon contradiction/closure/summon laws: ok')
