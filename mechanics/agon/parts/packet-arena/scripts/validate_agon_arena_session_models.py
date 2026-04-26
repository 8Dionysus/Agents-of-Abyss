#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


ROOT = _repo_root()
sys.path.insert(0, str(SCRIPT_DIR))
from build_agon_arena_session_model_registry import build, dump_min  # noqa: E402

CONFIG = ROOT / "mechanics" / "agon" / "parts" / "packet-arena" / "config" / "agon_arena_session_models.seed.json"
GENERATED = ROOT / "mechanics" / "agon" / "parts" / "packet-arena" / "generated" / "agon_arena_session_model_registry.min.json"

ALLOWED_MOVES = {
    'assert_position', 'challenge_claim', 'request_evidence', 'offer_evidence_reference',
    'probe_trace', 'deny_trace_closure', 'mark_contradiction', 'localize_contradiction',
    'deny_closure', 'request_closure_review', 'request_summon_intent', 'request_witness',
    'revise_position', 'stand_fast', 'concede', 'defer_with_cost',
    'flag_scope_breach', 'escalate_to_agon_gate',
}
REQUIRED_PHASES = {
    'gate', 'charter', 'seat_assignment', 'sealed_commit_slot', 'reveal_slot',
    'engagement_window', 'pressure_window', 'revision_window', 'adjudication_slot',
    'inscription_slot', 'retention_slot', 'closeout',
}
FORBIDDEN_TRUE_KEYS = {
    'live_protocol', 'live_authority', 'live_verdict_authority', 'live_summon_authority',
    'writes_durable_state', 'mutates_rank', 'promotes_to_tos', 'opens_arena_session',
    'runs_hidden_scheduler',
}


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def walk(obj):
    if isinstance(obj, dict):
        yield obj
        for value in obj.values():
            yield from walk(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from walk(value)


def fail(msg: str) -> int:
    print(f'ERROR: {msg}', file=sys.stderr)
    return 1


def main() -> int:
    if not CONFIG.exists():
        return fail(f'missing config: {CONFIG}')
    if not GENERATED.exists():
        return fail(f'missing generated registry: {GENERATED}')
    config = load(CONFIG)
    generated = load(GENERATED)
    if GENERATED.read_text(encoding='utf-8') != dump_min(build(config)):
        return fail('generated registry is stale; run build_agon_arena_session_model_registry.py')
    if config.get('live_protocol') is not False or config.get('runtime_effect') != 'none':
        return fail('top-level registry must remain pre-protocol with runtime_effect=none')
    records = config.get('session_models', [])
    if len(records) < 8:
        return fail('expected at least 8 arena session models')
    ids = [r.get('session_model_id') for r in records]
    if len(ids) != len(set(ids)):
        return fail('duplicate session_model_id detected')
    for record in records:
        sid = record.get('session_model_id')
        if record.get('live_protocol') is not False or record.get('runtime_effect') != 'none':
            return fail(f'{sid}: must remain pre-protocol with runtime_effect=none')
        for node in walk(record):
            for key in FORBIDDEN_TRUE_KEYS:
                if node.get(key) is True:
                    return fail(f'{sid}: forbidden live authority flag {key}=true')
        moves = set((record.get('charter') or {}).get('allowed_lawful_moves') or [])
        unknown = moves - ALLOWED_MOVES
        if unknown:
            return fail(f'{sid}: unknown lawful moves: {sorted(unknown)}')
        phases = {p.get('phase_id') for p in record.get('lifecycle', [])}
        missing = REQUIRED_PHASES - phases
        if missing:
            return fail(f'{sid}: missing lifecycle phases: {sorted(missing)}')
        phase_status = {p.get('phase_id'): p.get('phase_status') for p in record.get('lifecycle', [])}
        if phase_status.get('sealed_commit_slot') != 'reserved_for_state_packet_commit_reveal':
            return fail(f'{sid}: sealed_commit_slot must be reserved for state-packet route')
        if phase_status.get('reveal_slot') != 'reserved_for_state_packet_commit_reveal':
            return fail(f'{sid}: reveal_slot must be reserved for state-packet route')
        contestants = ((record.get('seats') or {}).get('contestants') or {})
        if contestants.get('required_kind') != 'agonic' or contestants.get('cannot_be_assistant') is not True:
            return fail(f'{sid}: contestants must require agonic kind and block assistants')
        if not record.get('terminal_outcomes'):
            return fail(f'{sid}: terminal outcome slots required')
        for outcome in record.get('terminal_outcomes', []):
            if outcome.get('live_authority') is not False or outcome.get('runtime_effect') != 'none':
                return fail(f'{sid}: terminal outcome {outcome.get("outcome_id")} must be slot-only')
    if generated.get('session_model_count') != len(records):
        return fail('generated session_model_count mismatch')
    print('agon arena session models validate')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
