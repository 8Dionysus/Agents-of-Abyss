from __future__ import annotations
import argparse, json
from pathlib import Path
def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
CONFIG=ROOT / "mechanics" / "agon" / "parts" / "verdict-retention-rank" / "config" / "agon_vds_bridges.seed.json"
OUTPUT=ROOT / "mechanics" / "agon" / "parts" / "verdict-retention-rank" / "generated" / "agon_vds_bridge_registry.min.json"
def compact(o): return json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n'
def build_registry():
    s=json.loads(CONFIG.read_text(encoding='utf-8'))
    return {'registry_id':s['registry_id'],'version':s['version'],'wave':s['wave'],'status':s['status'],'live_protocol':False,'runtime_effect':'none','bridge_count':len(s['bridge_components']),'terminal_outcomes':s['terminal_outcomes'],'bridge_components':s['bridge_components'],'outcome_bridge_matrix':s['outcome_bridge_matrix'],'stop_lines':s['stop_lines']}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); args=ap.parse_args()
    txt=compact(build_registry())
    if args.check:
        if not OUTPUT.exists(): raise SystemExit(f'missing generated registry: {OUTPUT}')
        if OUTPUT.read_text(encoding='utf-8')!=txt: raise SystemExit('generated agon_vds_bridge_registry.min.json is stale')
        print('agon_vds_bridge_registry.min.json is up to date'); return 0
    OUTPUT.parent.mkdir(parents=True,exist_ok=True); OUTPUT.write_text(txt,encoding='utf-8'); print(f'wrote {OUTPUT}'); return 0
if __name__=='__main__': raise SystemExit(main())
