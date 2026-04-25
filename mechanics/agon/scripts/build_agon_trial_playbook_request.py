#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
SRC = ROOT / "mechanics" / "agon" / "config" / "agon_trial_playbook_request.seed.json"
OUT = ROOT / "mechanics" / "agon" / "generated" / "agon_trial_playbook_request.min.json"

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def build():
    data = load_json(SRC)
    data = dict(data)
    data["generated_by"] = "mechanics/agon/scripts/build_agon_trial_playbook_request.py"
    data["trial_count"] = len(data.get("requested_trial_playbooks", []))
    return data

def dump_min(data):
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    built = dump_min(build())
    if args.check:
        if not OUT.exists():
            print(f"missing generated file: {OUT}", file=sys.stderr)
            return 1
        if OUT.read_text(encoding="utf-8") != built:
            print(f"generated drift: {OUT}", file=sys.stderr)
            return 1
        print("agon trial playbook request is up to date")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(built, encoding="utf-8")
    print(f"wrote {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
