#!/usr/bin/env python3
"""Check or apply exact known link-drift repairs from hygiene config."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from hygiene_common import load_config, relpath  # noqa: E402


def apply_or_check(root: Path, *, apply: bool, write_manifest: bool) -> tuple[list[str], list[dict[str, object]]]:
    config = load_config(root)
    rewrites = config.get("link_validation", {}).get("known_rewrites", [])
    problems: list[str] = []
    manifest: list[dict[str, object]] = []
    for entry in rewrites:
        rel = entry["file"]
        path = root / rel
        old = entry["old"]
        new = entry["new"]
        record = {
            "id": entry.get("id"),
            "file": rel,
            "old": old,
            "new": new,
            "reason": entry.get("reason", ""),
            "status": "skipped",
        }
        if not path.exists():
            record["status"] = "missing-file"
            manifest.append(record)
            continue
        text = path.read_text(encoding="utf-8")
        if old not in text:
            record["status"] = "already-clean"
            manifest.append(record)
            continue
        if apply:
            path.write_text(text.replace(old, new), encoding="utf-8")
            record["status"] = "applied"
        else:
            record["status"] = "stale-fragment-present"
            problems.append(f"{rel}: stale link fragment remains for {entry.get('id')}: {old} -> {new}")
        manifest.append(record)
    if write_manifest:
        trace_path = root / "docs/traces/HYGIENE_REPAIR_MANIFEST.json"
        trace_path.parent.mkdir(parents=True, exist_ok=True)
        trace_path.write_text(
            json.dumps(
                {
                    "schema": "aoa.link_shape_hygiene_repair_manifest.v1",
                    "generated_at": datetime.now(timezone.utc).isoformat(),
                    "repairs": manifest,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
    return problems, manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="apply exact known rewrites")
    mode.add_argument("--check", action="store_true", help="fail when stale fragments remain")
    parser.add_argument("--write-manifest", action="store_true", help="write docs/traces repair manifest")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    apply = bool(args.apply)
    problems, manifest = apply_or_check(root, apply=apply, write_manifest=args.write_manifest or apply)
    if problems:
        print("Known link-drift repair check failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    action = "applied" if apply else "checked"
    print(f"Known link-drift repairs {action}: {len(manifest)} configured repair(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
