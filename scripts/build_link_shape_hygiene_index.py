#!/usr/bin/env python3
"""Build the compact Wave E hygiene index."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from hygiene_common import GENERATED_PATH, dump_json, load_config, write_text_if_changed  # noqa: E402


def build(root: Path) -> dict[str, object]:
    config = load_config(root)
    guards = [
        {
            "id": "known-link-repair",
            "status": "active",
            "script": "scripts/repair_known_link_drifts.py",
            "source": "config/link_shape_hygiene.json",
        },
        {
            "id": "local-link-validation",
            "status": "active",
            "script": "scripts/validate_links.py",
            "source": "Markdown files",
        },
        {
            "id": "markdown-shape-validation",
            "status": "active",
            "script": "scripts/validate_markdown_shape.py",
            "source": "config/link_shape_hygiene.json",
        },
        {
            "id": "status-vocabulary-validation",
            "status": "active",
            "script": "scripts/validate_status_vocabulary.py",
            "source": "config/link_shape_hygiene.json",
        },
        {
            "id": "generated-freshness-validation",
            "status": "active",
            "script": "scripts/validate_generated_freshness.py",
            "source": "config/link_shape_hygiene.json",
        },
        {
            "id": "hygiene-index-validation",
            "status": "active",
            "script": "scripts/validate_link_shape_hygiene_index.py",
            "source": "generated/link_shape_hygiene.min.json",
        },
    ]
    return {
        "schema": "aoa.link_shape_hygiene_index.v1",
        "wave": "E",
        "purpose": config.get("purpose"),
        "protocol_ref": config.get("protocol_ref"),
        "index_ref": config.get("index_ref"),
        "config_ref": "config/link_shape_hygiene.json",
        "guardrails": guards,
        "known_rewrite_ids": [entry.get("id") for entry in config.get("link_validation", {}).get("known_rewrites", [])],
        "status_vocabularies": sorted(config.get("status_vocabulary", {}).keys()),
        "generated_freshness_outputs": [entry.get("output") for entry in config.get("generated_freshness", [])],
        "validation_commands": config.get("validation_commands", []),
        "note": "Generated mirror only; source meaning remains in docs and config.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    output = root / GENERATED_PATH
    text = dump_json(build(root))
    if args.check:
        if not output.exists():
            print(f"missing generated hygiene index: {GENERATED_PATH}")
            return 1
        current = output.read_text(encoding="utf-8")
        if current != text:
            print(f"generated hygiene index is stale: {GENERATED_PATH}")
            return 1
        print("generated hygiene index is current.")
        return 0
    changed = write_text_if_changed(output, text)
    print(f"wrote {GENERATED_PATH}" if changed else f"{GENERATED_PATH} already current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
