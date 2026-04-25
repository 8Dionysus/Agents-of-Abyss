#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from docs_thematic_common import load_classifier, validate_classifier_shape, REPO_ROOT
def main()->int:
    c=load_classifier(REPO_ROOT); errors=validate_classifier_shape(c); districts=c.get('districts',{})
    for item in c.get('exact_migrations',[]):
        d=item.get('district'); target=item.get('target','')
        if d in districts and not target.startswith(districts[d]['path']+'/'): errors.append(f'exact migration target {target} is not under district {d}')
        if Path(item.get('source','')).name=='README.md': errors.append('migration map must not move README.md surfaces')
    for rule in c.get('pattern_migrations',[]):
        d=rule.get('district'); target_dir=rule.get('target_dir','')
        if d not in districts: errors.append(f'pattern migration has unknown district {d}')
        elif target_dir != districts[d]['path']: errors.append(f'pattern migration target_dir {target_dir} does not match district {d}')
    if errors: raise SystemExit('docs migration map validation failed:\n- '+'\n- '.join(errors))
    print('docs migration map validated'); return 0
if __name__=='__main__': raise SystemExit(main())
