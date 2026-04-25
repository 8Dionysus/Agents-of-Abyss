#!/usr/bin/env python3
"""Build the compact mechanic card index from mechanics/registry.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
OUTPUT_PATH = REPO_ROOT / "generated" / "mechanic_card_index.min.json"
SCHEMA_VERSION = "aoa_mechanic_card_index_v1"


def load_registry() -> dict[str, Any]:
    with REGISTRY_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def build_index(registry: dict[str, Any]) -> dict[str, Any]:
    mechanics = []
    for entry in registry.get("mechanics", []):
        card = entry.get("card", {})
        mechanics.append(
            {
                "slug": entry.get("slug"),
                "title": entry.get("title"),
                "status": entry.get("status"),
                "entry_ref": entry.get("entry_ref"),
                "owner_boundary": entry.get("owner_boundary"),
                "trigger": card.get("trigger"),
                "center_owns": card.get("center_owns"),
                "stronger_owner_split": card.get("stronger_owner_split", []),
                "must_not_claim": entry.get("must_not_claim", []),
                "validation_refs": entry.get("validation_refs", []),
                "next_route": card.get("next_route", []),
            }
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "source_registry": "mechanics/registry.json",
        "card_contract_ref": registry.get("card_contract_ref", "mechanics/README.md#mechanic-card-contract"),
        "generated_truth_rule": "generated indexes reflect registry and package cards; they do not author mechanic meaning",
        "mechanics": mechanics,
    }


def dump_compact(data: dict[str, Any]) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build generated/mechanic_card_index.min.json")
    parser.add_argument("--check", action="store_true", help="fail if the generated file is not current")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rendered = dump_compact(build_index(load_registry()))
    if args.check:
        if not OUTPUT_PATH.exists():
            print(f"missing generated card index: {OUTPUT_PATH.relative_to(REPO_ROOT)}")
            return 1
        current = OUTPUT_PATH.read_text(encoding="utf-8")
        if current != rendered:
            print(f"generated card index is stale: {OUTPUT_PATH.relative_to(REPO_ROOT)}")
            return 1
        print(f"[ok] generated card index current: {OUTPUT_PATH.relative_to(REPO_ROOT)}")
        return 0
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    print(f"[ok] wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
