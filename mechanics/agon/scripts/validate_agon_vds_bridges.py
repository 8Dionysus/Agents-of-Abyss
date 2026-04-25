from __future__ import annotations
import json
from pathlib import Path
def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
REGISTRY=ROOT / "mechanics" / "agon" / "generated"/'agon_vds_bridge_registry.min.json'
REQUIRED_OUTCOMES={'resolved','revised_and_resolved','bifurcated','deferred_with_cost','failed_honorably','invalidated','quarantined'}
def validate():
    d=json.loads(REGISTRY.read_text(encoding='utf-8'))
    assert d['registry_id']=='agon.vds_bridge.registry.v1'
    assert d['wave']=='XI' and d['live_protocol'] is False and d['runtime_effect']=='none'
    assert set(d['terminal_outcomes'])==REQUIRED_OUTCOMES
    assert d['bridge_count']==len(d['bridge_components'])
    ids=[c['component_id'] for c in d['bridge_components']]; assert len(ids)==len(set(ids))
    classes={c['component_class'] for c in d['bridge_components']}
    assert {'verdict_draft','delta_receipt_candidate','scar_request','retention_request','inscription_bundle_candidate'} <= classes
    scar=next(c for c in d['bridge_components'] if c['component_class']=='scar_request')
    assert scar['must_have']['memory_owner']=='aoa-memo'
    assert scar['must_have']['durable_write_allowed'] is False
    retention=next(c for c in d['bridge_components'] if c['component_class']=='retention_request')
    assert retention['must_have']['hidden_scheduler_allowed'] is False
    bundle=next(c for c in d['bridge_components'] if c['component_class']=='inscription_bundle_candidate')
    assert bundle['must_have']['canon_promotion_allowed'] is False
    stops=set(d['stop_lines'])
    assert {'no_live_verdict_authority','no_durable_scar_write','no_retention_execution','no_tree_of_sophia_promotion'} <= stops
    for c in d['bridge_components']:
        assert c['required_fields'] and c['owner_handoffs'] and c['not_granted']
    return d
if __name__=='__main__':
    d=validate(); print(f"validated {d['bridge_count']} VDS bridge components")
