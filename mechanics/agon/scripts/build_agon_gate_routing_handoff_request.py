#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
CONFIG_PATH = ROOT / "config" / "agon_gate_routing_handoff_request.seed.json"
OUTPUT_PATH = ROOT / "generated" / "agon_gate_routing_handoff_request.min.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_min(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the Agon gate routing handoff request.")
    parser.add_argument("--check", action="store_true", help="Fail if generated output is stale.")
    args = parser.parse_args()

    request = load_json(CONFIG_PATH)
    rendered = dump_min(request)

    if args.check:
        if not OUTPUT_PATH.exists():
            raise SystemExit(f"Missing generated output: {OUTPUT_PATH}")
        if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            raise SystemExit("generated/agon_gate_routing_handoff_request.min.json is stale")
        print("Agon gate routing handoff request is up to date.")
        return 0

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
