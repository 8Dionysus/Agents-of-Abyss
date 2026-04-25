#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
from docs_thematic_common import INDEX_REL, load_classifier, render_index, REPO_ROOT
def main()->int:
    parser=argparse.ArgumentParser(); parser.add_argument('--repo-root',default=str(REPO_ROOT)); parser.add_argument('--check',action='store_true'); args=parser.parse_args(); repo_root=Path(args.repo_root).resolve()
    rendered=render_index(load_classifier(repo_root)); target=repo_root/INDEX_REL
    if args.check:
        if not target.exists() or target.read_text(encoding='utf-8')!=rendered: raise SystemExit('generated docs thematic index is stale; run scripts/build_docs_thematic_index.py')
        print('generated docs thematic index is current'); return 0
    target.parent.mkdir(parents=True,exist_ok=True); target.write_text(rendered,encoding='utf-8'); print(f'wrote {target.relative_to(repo_root)}'); return 0
if __name__=='__main__': raise SystemExit(main())
