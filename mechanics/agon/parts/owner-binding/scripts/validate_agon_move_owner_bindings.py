#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

# Reuse the builder module so the validation rules stay single-sourced.
def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
PART_SCRIPTS = ROOT / "mechanics" / "agon" / "parts" / "owner-binding" / "scripts"
sys.path.insert(0, str(PART_SCRIPTS))

from build_agon_move_owner_binding_registry import (  # noqa: E402
    CONFIG_PATH,
    GENERATED_PATH,
    ValidationError,
    build_registry,
    read_json,
    validate_config,
)


def main() -> int:
    try:
        config = read_json(CONFIG_PATH)
        validate_config(config, require_wave3=True)
        expected = build_registry(config)
        actual = read_json(GENERATED_PATH)
        if actual != expected:
            raise ValidationError(f"{GENERATED_PATH} is stale; rerun build_agon_move_owner_binding_registry.py")
        print(f"ok: {expected['total_bindings']} Agon Wave IV owner bindings validated")
        return 0
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
