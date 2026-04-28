#!/usr/bin/env python3
from __future__ import annotations
import json
from docs_thematic_common import INDEX_REL, load_classifier, render_index, REPO_ROOT
def main()->int:
    target=REPO_ROOT/INDEX_REL
    if not target.exists(): raise SystemExit(f'missing {INDEX_REL}')
    actual=target.read_text(encoding='utf-8'); expected=render_index(load_classifier(REPO_ROOT))
    if actual!=expected: raise SystemExit('generated docs thematic index does not match docs/guardrails/thematic_districts.json')
    data=json.loads(actual)
    if data.get('generated_rule')!='Reflects docs/guardrails/thematic_districts.json; does not author meaning.': raise SystemExit('generated docs thematic index missing generated rule')
    print('generated docs thematic index validated'); return 0
if __name__=='__main__': raise SystemExit(main())
