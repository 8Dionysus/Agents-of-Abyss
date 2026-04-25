#!/usr/bin/env python3
"""Build the compact owner-request queue from source queue and registry."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = REPO_ROOT / "mechanics" / "owner-request-queue.json"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
OUTPUT_PATH = REPO_ROOT / "generated" / "owner_request_queue.min.json"


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def build_payload() -> dict[str, Any]:
    queue = load_json(QUEUE_PATH)
    registry = load_json(REGISTRY_PATH)
    by_slug = {entry["slug"]: entry for entry in registry.get("mechanics", [])}
    requests: list[dict[str, Any]] = []
    for req in queue.get("requests", []):
        mechanic = req["mechanic"]
        requests.append({
            "id": req["id"],
            "mechanic": mechanic,
            "owner_repo": req["owner_repo"],
            "queue_status": req["queue_status"],
            "priority": req["priority"],
            "slice": req["slice"],
            "center_status": req["center_status"],
            "owner_request_doc_ref": by_slug.get(mechanic, {}).get("owner_request_doc_ref", ""),
            "required_owner_landing": req["required_owner_landing"],
            "proof_route": req["proof_route"],
            "stop_line": req["stop_line"],
        })
    return {
        "schema_version": "aoa_generated_owner_request_queue_v1",
        "generated_from": ["mechanics/owner-request-queue.json", "mechanics/registry.json"],
        "authority_ref": queue.get("authority_ref"),
        "protocol_ref": queue.get("protocol_ref"),
        "source_ref": queue.get("source_ref"),
        "registry_ref": queue.get("registry_ref"),
        "request_count": len(requests),
        "mechanic_count": len({item["mechanic"] for item in requests}),
        "status_counts": {status: sum(1 for item in requests if item["queue_status"] == status) for status in queue.get("status_vocabulary", {}) if any(item["queue_status"] == status for item in requests)},
        "owner_counts": {owner: sum(1 for item in requests if item["owner_repo"] == owner) for owner in sorted({item["owner_repo"] for item in requests})},
        "requests": requests,
        "generated_note": "This compact map reflects source queue and registry surfaces. It does not author owner-local truth, acceptance, proof, runtime, memory, or ToS meaning.",
    }


def dumps_min(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build generated owner request queue.")
    parser.add_argument("--check", action="store_true", help="fail if generated file is stale")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    expected = dumps_min(build_payload())
    if args.check:
        if not OUTPUT_PATH.exists():
            print(f"missing generated file: {OUTPUT_PATH.relative_to(REPO_ROOT)}")
            return 1
        actual = OUTPUT_PATH.read_text(encoding="utf-8")
        if actual != expected:
            print("generated/owner_request_queue.min.json is stale; run scripts/build_owner_request_queue.py")
            return 1
        print("[ok] generated owner request queue is current")
        return 0
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(expected, encoding="utf-8")
    print(f"[ok] wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
