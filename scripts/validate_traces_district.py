#!/usr/bin/env python3
"""Validate the docs/traces receipt district."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
TRACE_DIR = Path("docs/traces")
ALLOWED_DIRECT_MARKDOWN = {"AGENTS.md", "README.md"}
ALLOWED_SUBDIRS = {"conflicts"}
MECHANIC_NAME_TOKENS = {
    "AGON",
    "ANTIFRAGILITY",
    "AUDIT",
    "BOUNDARY_BRIDGE",
    "CHECKPOINT",
    "DISTILLATION",
    "EXPERIENCE",
    "GROWTH_CYCLE",
    "METHOD_GROWTH",
    "QUESTBOOK",
    "RECURRENCE",
    "RELEASE_SUPPORT",
    "RPG",
    "TOS_BRIDGE",
}

KNOWN_TRACE_SHAPES = {
    "aoa.link_shape_hygiene_repair_manifest.v1": {"generated_at", "repairs"},
    "aoa.wave_e_apply_manifest.v1": {"applied_at", "payload_files"},
    "schema_version:1": {"moves", "link_update_files"},
}


def _rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _schema_key(payload: dict[str, Any]) -> str | None:
    schema = payload.get("schema")
    if isinstance(schema, str):
        return schema
    schema_version = payload.get("schema_version")
    if isinstance(schema_version, (str, int)):
        return f"schema_version:{schema_version}"
    return None


def _normalized_name(path: Path) -> str:
    return path.name.upper().replace("-", "_")


def _validate_json_trace(path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    rel = _rel(path, root)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{rel} is not valid JSON: {exc}"]

    if not isinstance(payload, dict):
        return [f"{rel} must contain a JSON object"]

    schema_key = _schema_key(payload)
    if not schema_key:
        errors.append(f"{rel} must declare schema or schema_version")
        return errors

    required = KNOWN_TRACE_SHAPES.get(schema_key)
    if required:
        missing = sorted(key for key in required if key not in payload)
        if missing:
            errors.append(f"{rel} missing required keys for {schema_key}: {', '.join(missing)}")
    return errors


def validate_traces(repo_root: Path) -> list[str]:
    errors: list[str] = []
    trace_dir = repo_root / TRACE_DIR
    readme = trace_dir / "README.md"
    agents = trace_dir / "AGENTS.md"

    if not trace_dir.is_dir():
        return [f"missing {TRACE_DIR.as_posix()}"]
    if not readme.exists():
        errors.append("missing docs/traces/README.md")
    if not agents.exists():
        errors.append("missing docs/traces/AGENTS.md")

    readme_text = readme.read_text(encoding="utf-8") if readme.exists() else ""
    for required in [
        "Traces explain movement",
        "## Current surfaces",
        "## Routes away",
        "## Mechanic connection",
        "empty trace doors",
    ]:
        if required not in readme_text:
            errors.append(f"docs/traces/README.md missing {required!r}")

    direct_files = sorted(path for path in trace_dir.iterdir() if path.is_file())
    for path in direct_files:
        if path.suffix == ".md" and path.name not in ALLOWED_DIRECT_MARKDOWN:
            errors.append(f"{_rel(path, repo_root)} is a Markdown receipt; route it to a source owner")
        if path.name not in ALLOWED_DIRECT_MARKDOWN and path.name not in readme_text:
            errors.append(f"docs/traces/README.md does not index {_rel(path, repo_root)}")
        for token in MECHANIC_NAME_TOKENS:
            if token in _normalized_name(path):
                errors.append(f"{_rel(path, repo_root)} looks mechanic-specific; route to mechanics/<slug>/")

    for path in sorted(trace_dir.iterdir()):
        if path.is_dir() and path.name not in ALLOWED_SUBDIRS:
            errors.append(f"unexpected docs/traces subdirectory: {_rel(path, repo_root)}")

    for path in sorted(trace_dir.rglob("*.json")):
        if path.relative_to(trace_dir).parts[0] == "conflicts":
            continue
        errors.extend(_validate_json_trace(path, repo_root))

    conflicts = trace_dir / "conflicts"
    if conflicts.exists() and "conflicts/" not in readme_text:
        errors.append("docs/traces/README.md must document conflicts/ when it exists")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    errors = validate_traces(repo_root)
    if errors:
        raise SystemExit("traces district validation failed:\n- " + "\n- ".join(errors))
    print("traces district validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
