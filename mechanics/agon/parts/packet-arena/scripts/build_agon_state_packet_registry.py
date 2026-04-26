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
CONFIG = ROOT / "mechanics" / "agon" / "parts" / "packet-arena" / "config" / "agon_state_packets.seed.json"
OUT = ROOT / "mechanics" / "agon" / "parts" / "packet-arena" / "generated" / "agon_state_packet_registry.min.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def build(seed: dict) -> dict:
    packets = []
    for p in seed['packet_models']:
        packets.append({
            'packet_type': p['packet_type'],
            'packet_class': p['packet_class'],
            'lifecycle_slot': p['lifecycle_slot'],
            'allowed_actor_kinds': p['allowed_actor_kinds'],
            'required_payload_fields': p['required_payload_fields'],
            'next_allowed_packet_types': p.get('next_allowed_packet_types', []),
            'live_protocol': False,
            'runtime_effect': 'none',
        })
    return {
        'registry_id': seed['registry_id'],
        'version': seed['version'],
        'status': seed['status'],
        'wave': seed['wave'],
        'home_repo': seed['home_repo'],
        'live_protocol': False,
        'runtime_effect': 'none',
        'packet_count': len(packets),
        'packet_types': [p['packet_type'] for p in packets],
        'packet_classes': sorted(set(p['packet_class'] for p in packets)),
        'lifecycle_slots': sorted(set(p['lifecycle_slot'] for p in packets)),
        'sealed_commit_packet': 'agon.sealed_commit',
        'reveal_packets': ['agon.reveal_request', 'agon.reveal_view'],
        'stop_lines': seed['stop_lines'],
        'packets': packets,
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
        current = OUT.read_text(encoding='utf-8')
        if current != text:
            raise SystemExit('mechanics/agon/parts/packet-arena/generated/agon_state_packet_registry.min.json is out of date')
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
