from __future__ import annotations
import json
from pathlib import Path
from typing import Any
REPO_ROOT=Path(__file__).resolve().parents[1]
CLASSIFIER_REL=Path('docs/thematic_districts.json')
INDEX_REL=Path('generated/docs_thematic_index.min.json')
DOC_ROOT_REQUIRED=['README.md','AGENTS.md','THEMATIC_DISTRICT_PROTOCOL.md','CURRENT_SURFACE_INDEX.md','thematic_districts.json']
DISTRICT_README_HEADINGS=['# ','## District law','## Current surfaces','## Must not claim','## Promotion path','## Validation']
def load_classifier(repo_root:Path|None=None)->dict[str,Any]:
    root=repo_root or REPO_ROOT
    return json.loads((root/CLASSIFIER_REL).read_text(encoding='utf-8'))
def render_index(classifier:dict[str,Any])->str:
    data={'schema_version':classifier['schema_version'],'source':str(CLASSIFIER_REL),'purpose':'Compact machine-facing map of docs thematic districts.','generated_rule':'Reflects docs/thematic_districts.json; does not author meaning.','current_root_allowlist':classifier.get('current_root_allowlist',[]),'districts':{name:{'path':d['path'],'readme':d['readme'],'role':d['role'],'authority':d['authority'],'current_route':d.get('current_route')} for name,d in classifier.get('districts',{}).items()},'exact_migration_count':len(classifier.get('exact_migrations',[])),'pattern_migration_count':len(classifier.get('pattern_migrations',[])),'validation_refs':classifier.get('validation_refs',[])}
    return json.dumps(data,separators=(',',':'),ensure_ascii=False)+'\n'
def normalize_name(path:Path|str)->str: return Path(path).name.upper().replace('-','_')
def validate_classifier_shape(classifier:dict[str,Any])->list[str]:
    errors=[]
    if classifier.get('schema_version')!=2: errors.append('schema_version must be 2')
    for key in ['current_root_allowlist','districts','tie_break_order','exact_migrations','pattern_migrations','validation_refs']:
        if key not in classifier: errors.append(f'missing classifier key: {key}')
    districts=classifier.get('districts',{})
    if set(classifier.get('tie_break_order',[]))!=set(districts): errors.append('tie_break_order must name exactly all districts')
    seen_sources=set(); seen_targets=set()
    for name,d in districts.items():
        for key in ['path','readme','role','authority','patterns','must_not_claim']:
            if key not in d: errors.append(f'district {name} missing {key}')
    for item in classifier.get('exact_migrations',[]):
        for key in ['source','target','district','reason']:
            if key not in item: errors.append(f'exact migration missing {key}: {item}')
        if item.get('source') in seen_sources: errors.append(f'duplicate exact migration source: {item.get("source")}')
        seen_sources.add(item.get('source'))
        if item.get('target') in seen_targets: errors.append(f'duplicate exact migration target: {item.get("target")}')
        seen_targets.add(item.get('target'))
        if item.get('district') not in districts: errors.append(f'unknown exact migration district: {item.get("district")}')
    return errors
def classify_flat_docs_file(path:Path,classifier:dict[str,Any])->str|None:
    if path.name in set(classifier.get('current_root_allowlist',[])): return None
    if path.suffix.lower() not in {'.md','.json','.yaml','.yml'}: return None
    normalized=normalize_name(path)
    for district_name in classifier.get('tie_break_order',[]):
        for pattern in classifier['districts'][district_name].get('patterns',[]):
            if pattern.upper().replace('-','_') in normalized: return district_name
    return None
def build_plan(repo_root:Path,classifier:dict[str,Any])->list[dict[str,str]]:
    moves=[]; seen=set()
    for item in classifier.get('exact_migrations',[]):
        if (repo_root/item['source']).exists():
            moves.append({'source':item['source'],'target':item['target'],'district':item['district'],'reason':item.get('reason','exact migration'),'link_target':item.get('link_target',item['target'])}); seen.add(item['source'])
    docs=repo_root/'docs'
    if docs.exists():
        for child in sorted(docs.iterdir()):
            if not child.is_file(): continue
            rel=str(child.relative_to(repo_root))
            if rel in seen: continue
            d=classify_flat_docs_file(child,classifier)
            if not d: continue
            target=repo_root/classifier['districts'][d]['path']/child.name
            moves.append({'source':rel,'target':str(target.relative_to(repo_root)),'district':d,'reason':'matched district pattern','link_target':str(target.relative_to(repo_root))}); seen.add(rel)
    for rule in classifier.get('pattern_migrations',[]):
        for source in sorted(repo_root.glob(rule['source_glob'])):
            if not source.is_file(): continue
            rel=str(source.relative_to(repo_root))
            if rel in seen: continue
            target=repo_root/rule['target_dir']/source.name
            if target==source: continue
            moves.append({'source':rel,'target':str(target.relative_to(repo_root)),'district':rule['district'],'reason':rule.get('reason','pattern migration'),'link_target':str(target.relative_to(repo_root))}); seen.add(rel)
    return moves
