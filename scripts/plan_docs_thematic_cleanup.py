#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, shutil, os
from datetime import datetime, timezone
from pathlib import Path
from docs_thematic_common import build_plan, load_classifier, REPO_ROOT

def rel_link(from_file:Path,target_rel:str,repo_root:Path)->str:
    return Path(os.path.relpath(repo_root/target_rel, from_file.parent)).as_posix()
def rewrite_links(repo_root:Path,moves:list[dict[str,str]]):
    mapping={m['source']:m.get('link_target',m['target']) for m in moves}
    changed=[]
    for md in sorted(repo_root.rglob('*.md')):
        if any(part in {'.git','.wave_d_backups','__pycache__'} for part in md.parts): continue
        text=md.read_text(encoding='utf-8'); original=text
        for old,new in mapping.items():
            old_name=Path(old).name; new_for_file=rel_link(md,new,repo_root); old_for_file=rel_link(md,old,repo_root)
            for candidate in {old,'../'+old,'./'+old,old_for_file}:
                text=text.replace(f']({candidate})',f']({new_for_file})')
            if md.parent==repo_root/'docs': text=text.replace(f']({old_name})',f']({new_for_file})')
        if text!=original:
            md.write_text(text,encoding='utf-8'); changed.append(str(md.relative_to(repo_root)))
    return changed
def apply_moves(repo_root:Path,moves:list[dict[str,str]],backup:bool):
    backup_root=repo_root/'.wave_d_backups'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'); applied=[]
    for move in moves:
        source=repo_root/move['source']; target=repo_root/move['target']
        if not source.exists(): continue
        target.parent.mkdir(parents=True,exist_ok=True)
        if backup:
            b=backup_root/move['source']; b.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(source,b)
        if target.exists():
            if source.read_bytes()==target.read_bytes(): source.unlink(); status='removed_duplicate_source'
            else:
                conflict=repo_root/'docs'/'traces'/'conflicts'/move['source'].replace('/','__'); conflict.parent.mkdir(parents=True,exist_ok=True); shutil.move(str(source),str(conflict)); status='target_exists_source_preserved_as_conflict_trace'; move={**move,'conflict_trace':str(conflict.relative_to(repo_root))}
        else: shutil.move(str(source),str(target)); status='moved'
        applied.append({**move,'status':status})
    links=rewrite_links(repo_root,applied)
    trace=repo_root/'docs'/'traces'/'WAVE_D_MOVE_MANIFEST.json'; trace.parent.mkdir(parents=True,exist_ok=True)
    trace.write_text(json.dumps({'schema_version':1,'created_utc':datetime.now(timezone.utc).isoformat(),'moves':applied,'link_update_files':links},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def main()->int:
    parser=argparse.ArgumentParser(); parser.add_argument('--repo-root',default=str(REPO_ROOT)); parser.add_argument('--apply',action='store_true'); parser.add_argument('--check',action='store_true'); parser.add_argument('--no-backup',action='store_true'); args=parser.parse_args(); repo_root=Path(args.repo_root).resolve()
    c=load_classifier(repo_root); moves=build_plan(repo_root,c)
    print(json.dumps(moves,indent=2,ensure_ascii=False) if moves else 'No flat docs require thematic migration.')
    if args.check and moves: raise SystemExit('docs thematic cleanup plan is not empty; run with --apply or move files manually')
    if args.apply and moves: apply_moves(repo_root,moves,backup=not args.no_backup); print(f'Applied {len(moves)} docs thematic moves.')
    elif args.apply: print('Nothing to apply.')
    return 0
if __name__=='__main__': raise SystemExit(main())
