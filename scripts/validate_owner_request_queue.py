#!/usr/bin/env python3
"""Validate owner-request queue source, registry mirror, and generated compact queue."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = REPO_ROOT / "mechanics" / "owner-request-queue.json"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
GENERATED_PATH = REPO_ROOT / "generated" / "owner_request_queue.min.json"
REQUEST_ID_RE = re.compile(r"^ORQ-[A-Z0-9]+-[A-Z0-9]+-\d{3}$")
CANONICAL_SLUGS = (
    "method-growth",
    "distillation",
    "recurrence",
    "checkpoint",
    "experience",
    "agon",
    "antifragility",
    "questbook",
    "rpg",
    "boundary-bridge",
    "release-support",
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def require_path(rel: str, problems: list[str], label: str) -> None:
    if not rel or not (REPO_ROOT / rel).exists():
        problems.append(f"{label} missing: {rel}")


def validate_queue(selected: set[str] | None = None) -> list[str]:
    problems: list[str] = []
    if not QUEUE_PATH.exists():
        return ["mechanics/owner-request-queue.json is missing"]
    if not REGISTRY_PATH.exists():
        return ["mechanics/registry.json is missing"]
    queue = load_json(QUEUE_PATH)
    registry = load_json(REGISTRY_PATH)
    if queue.get("schema_version") != "aoa_owner_request_queue_v1":
        problems.append("owner-request-queue.json: schema_version must be aoa_owner_request_queue_v1")
    for key in ("authority_ref", "protocol_ref", "registry_ref", "generated_ref", "source_ref"):
        require_path(str(queue.get(key, "")), problems, key)
    status_vocabulary = queue.get("status_vocabulary")
    if not isinstance(status_vocabulary, dict) or not status_vocabulary:
        problems.append("owner-request-queue.json: status_vocabulary must be a non-empty object")
        status_vocabulary = {}
    priority_vocabulary = queue.get("priority_vocabulary")
    if not isinstance(priority_vocabulary, dict) or not priority_vocabulary:
        problems.append("owner-request-queue.json: priority_vocabulary must be a non-empty object")
        priority_vocabulary = {}
    allowed_owners = set(queue.get("allowed_owner_repositories") or [])
    if not allowed_owners:
        problems.append("owner-request-queue.json: allowed_owner_repositories must be non-empty")
    required = queue.get("request_required_fields")
    if not isinstance(required, list) or not required:
        problems.append("owner-request-queue.json: request_required_fields must be a non-empty list")
        required = []
    mechanics = registry.get("mechanics") or []
    registry_by_slug = {entry.get("slug"): entry for entry in mechanics if isinstance(entry, dict)}
    if tuple(registry_by_slug) != CANONICAL_SLUGS:
        problems.append("mechanics/registry.json: canonical slug order mismatch for owner request validation")
    requests = queue.get("requests")
    if not isinstance(requests, list) or not requests:
        return problems + ["owner-request-queue.json: requests must be a non-empty list"]
    seen_ids: set[str] = set()
    queue_ids_by_mechanic: dict[str, list[str]] = {slug: [] for slug in CANONICAL_SLUGS}
    for req in requests:
        if not isinstance(req, dict):
            problems.append("owner-request-queue.json: request entry is not an object")
            continue
        rid = str(req.get("id", ""))
        mechanic = str(req.get("mechanic", ""))
        if selected and mechanic not in selected:
            continue
        if not REQUEST_ID_RE.match(rid):
            problems.append(f"{rid or '<missing id>'}: invalid request id shape")
        if rid in seen_ids:
            problems.append(f"{rid}: duplicate request id")
        seen_ids.add(rid)
        for field in required:
            value = req.get(field)
            if value in (None, "", []):
                problems.append(f"{rid}: missing required field {field}")
        if mechanic not in registry_by_slug:
            problems.append(f"{rid}: mechanic {mechanic!r} not found in registry")
            continue
        queue_ids_by_mechanic.setdefault(mechanic, []).append(rid)
        if req.get("queue_status") not in status_vocabulary:
            problems.append(f"{rid}: queue_status must be one of status_vocabulary")
        if req.get("priority") not in priority_vocabulary:
            problems.append(f"{rid}: priority must be one of priority_vocabulary")
        if req.get("owner_repo") not in allowed_owners:
            problems.append(f"{rid}: owner_repo {req.get('owner_repo')!r} is not in allowed_owner_repositories")
        center_sources = req.get("center_sources")
        if not isinstance(center_sources, list) or not center_sources:
            problems.append(f"{rid}: center_sources must be a non-empty list")
        else:
            for rel in center_sources:
                require_path(str(rel), problems, f"{rid} center source")
        status = req.get("queue_status")
        if status in {"accepted", "landed"}:
            if not req.get("owner_landing_ref"):
                problems.append(f"{rid}: accepted/landed status requires owner_landing_ref")
        if status == "landed" and not req.get("owner_proof_ref"):
            problems.append(f"{rid}: landed status requires owner_proof_ref")
        if "center must not" not in str(req.get("stop_line", "")).lower() and "must not" not in str(req.get("stop_line", "")).lower():
            problems.append(f"{rid}: stop_line must be explicit")
    for slug in CANONICAL_SLUGS:
        if selected and slug not in selected:
            continue
        entry = registry_by_slug.get(slug) or {}
        doc_ref = entry.get("owner_request_doc_ref")
        require_path(str(doc_ref or ""), problems, f"{slug} owner_request_doc_ref")
        registry_ids = entry.get("owner_request_ids")
        if not isinstance(registry_ids, list) or not registry_ids:
            problems.append(f"{slug}: registry owner_request_ids must be a non-empty list")
        elif registry_ids != queue_ids_by_mechanic.get(slug, []):
            problems.append(f"{slug}: registry owner_request_ids do not match queue order")
    # generated file check via builder
    builder_path = REPO_ROOT / "scripts" / "build_owner_request_queue.py"
    if builder_path.exists() and GENERATED_PATH.exists():
        spec = importlib.util.spec_from_file_location("build_owner_request_queue", builder_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            expected = module.dumps_min(module.build_payload())
            actual = GENERATED_PATH.read_text(encoding="utf-8")
            if actual != expected:
                problems.append("generated/owner_request_queue.min.json is stale")
    return problems


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate owner request queue.")
    parser.add_argument("--mechanic", choices=CANONICAL_SLUGS, action="append", help="Mechanic slug to validate; may be repeated.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = set(args.mechanic) if args.mechanic else None
    problems = validate_queue(selected)
    if problems:
        print("Owner request queue validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    scope = ", ".join(sorted(selected)) if selected else "all mechanics"
    print(f"[ok] owner request queue validated: {scope}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
