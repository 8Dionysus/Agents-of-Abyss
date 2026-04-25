#!/usr/bin/env python3
from __future__ import annotations
from docs_thematic_common import DOC_ROOT_REQUIRED,DISTRICT_README_HEADINGS,build_plan,load_classifier,validate_classifier_shape,REPO_ROOT
def main()->int:
    repo_root=REPO_ROOT; docs=repo_root/'docs'; errors=[]
    if not docs.exists(): raise SystemExit('missing docs directory')
    c=load_classifier(repo_root); errors.extend(validate_classifier_shape(c))
    for f in DOC_ROOT_REQUIRED:
        if not (docs/f).exists(): errors.append(f'missing docs/{f}')
    for name,d in c.get('districts',{}).items():
        p=repo_root/d['path']; readme=repo_root/d['readme']
        if not p.exists(): errors.append(f'missing district {d["path"]}'); continue
        if not readme.exists(): errors.append(f'missing district readme: {d["readme"]}'); continue
        text=readme.read_text(encoding='utf-8')
        for heading in DISTRICT_README_HEADINGS:
            if heading not in text: errors.append(f'{d["readme"]} missing heading {heading!r}')
    leftovers=build_plan(repo_root,c)
    if leftovers: errors.append('flat docs still classify into districts: '+', '.join(i['source'] for i in leftovers))
    docs_readme=(docs/'README.md').read_text(encoding='utf-8') if (docs/'README.md').exists() else ''
    for d in c.get('districts',{}).values():
        if d['path'].replace('docs/','')+'/' not in docs_readme and d['path'] not in docs_readme: errors.append(f'docs/README.md does not mention {d["path"]}')
    for cmd in c.get('validation_refs',[]):
        if cmd not in docs_readme: errors.append(f'docs/README.md missing validation command: {cmd}')
    root_law=(docs/'ROOT_SURFACE_LAW.md').read_text(encoding='utf-8') if (docs/'ROOT_SURFACE_LAW.md').exists() else ''
    for required in ['Wave D','THEMATIC_DISTRICT_PROTOCOL','docs root']:
        if required not in root_law: errors.append(f'ROOT_SURFACE_LAW.md missing {required!r}')
    if errors: raise SystemExit('docs thematic district validation failed:\n- '+'\n- '.join(errors))
    print('docs thematic districts validated'); return 0
if __name__=='__main__': raise SystemExit(main())
