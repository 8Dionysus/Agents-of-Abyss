#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / 'config' / 'agon_state_packets.seed.json'
REGISTRY = ROOT / 'generated' / 'agon_state_packet_registry.min.json'
REQUIRED_PACKET_TYPES = {
    'agon.sealed_commit',
    'agon.commit_receipt',
    'agon.reveal_request',
    'agon.reveal_view',
    'agon.move_declaration',
    'agon.revision_statement',
    'agon.adjudication_request',
    'agon.inscription_candidate',
}
FORBIDDEN_WORDS = {'verdict_authority', 'durable_scar_write', 'rank_mutation', 'tree_of_sophia_promotion'}


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def validate() -> None:
    seed = load(CONFIG)
    reg = load(REGISTRY)

    assert seed['live_protocol'] is False, 'seed must remain pre-protocol'
    assert seed['runtime_effect'] == 'none', 'seed must have no runtime effect'
    assert reg['live_protocol'] is False, 'registry must remain pre-protocol'
    assert reg['runtime_effect'] == 'none', 'registry must have no runtime effect'
    assert reg['packet_count'] == len(seed['packet_models']), 'packet count mismatch'

    packet_types = {p['packet_type'] for p in seed['packet_models']}
    assert REQUIRED_PACKET_TYPES <= packet_types, f'missing required packet types: {sorted(REQUIRED_PACKET_TYPES - packet_types)}'
    assert len(packet_types) == len(seed['packet_models']), 'duplicate packet_type found'

    for model in seed['packet_models']:
        assert model['packet_type'].startswith('agon.'), model['packet_type']
        assert model.get('required_payload_fields'), f"{model['packet_type']} lacks required_payload_fields"
        assert 'allowed_actor_kinds' in model and model['allowed_actor_kinds'], f"{model['packet_type']} lacks actor kind constraints"
        text = json.dumps(model, sort_keys=True)
        for bad in FORBIDDEN_WORDS:
            # Stop-line names are allowed only as explicit negative boundaries.
            if bad in text:
                assert 'no_' + bad in text or bad in json.dumps(seed['stop_lines']), f'possible authority leak in {model["packet_type"]}: {bad}'

    sealed = next(p for p in seed['packet_models'] if p['packet_type'] == 'agon.sealed_commit')
    required_sealed = {'thesis', 'confidence', 'beliefs_at_risk', 'revision_conditions', 'predicted_other', 'affect_snapshot', 'self_image_claim', 'stake_acceptance'}
    assert required_sealed <= set(sealed.get('sealed_fields', [])), 'sealed commit missing anti-mimicry fields'

    assistant_contestant_leaks = [
        p['packet_type'] for p in seed['packet_models']
        if p['packet_type'] == 'agon.sealed_commit' and 'assistant' in p.get('allowed_actor_kinds', [])
    ]
    assert not assistant_contestant_leaks, f'assistant cannot emit sealed contestant commit: {assistant_contestant_leaks}'


if __name__ == '__main__':
    validate()
    print('agon state packet surfaces: ok')
