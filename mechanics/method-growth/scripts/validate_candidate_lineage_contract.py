#!/usr/bin/env python3
"""Validate the first-wave candidate-lineage example chain across sibling repos."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ALLOWED_STATUS_POSTURE = {"early", "reanchor", "thin-evidence", "stable"}
ALLOWED_LIFECYCLE = {
    "staged",
    "open-wave",
    "planting-in-progress",
    "planted",
    "superseded",
    "dropped",
}


@dataclass(frozen=True)
class LineageExamplePaths:
    sdk: Path
    skills: Path
    seed: Path


@dataclass(frozen=True)
class LineageSummary:
    workspace_root: Path
    cluster_ref: str
    candidate_ref: str
    seed_ref: str


def read_json_object(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid json in {path}: {exc}") from exc

    if not isinstance(payload, dict):
        raise ValueError(f"expected json object in {path}")
    return payload


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def require_text(payload: dict[str, Any], key: str, label: str) -> str:
    value = payload.get(key)
    require(isinstance(value, str) and bool(value.strip()), f"{label} must carry non-empty {key}")
    return value


def resolve_example_paths(workspace_root: Path) -> LineageExamplePaths:
    return LineageExamplePaths(
        sdk=workspace_root / "aoa-sdk" / "examples" / "checkpoint_lineage_hint.example.json",
        skills=(
            workspace_root
            / "aoa-skills"
            / "examples"
            / "session_growth_artifacts"
            / "candidate_lineage_receipt.alpha.json"
        ),
        seed=workspace_root / "Dionysus" / "examples" / "seed_lineage_entry.example.json",
    )


def validate_chain(workspace_root: Path) -> LineageSummary:
    root = workspace_root.expanduser().resolve()
    paths = resolve_example_paths(root)

    sdk = read_json_object(paths.sdk)
    skills = read_json_object(paths.skills)
    seed = read_json_object(paths.seed)

    require(
        sdk.get("schema_version") == "aoa_checkpoint_lineage_hint_v1",
        "aoa-sdk example must use schema_version=aoa_checkpoint_lineage_hint_v1",
    )
    require(
        skills.get("schema_version") == "aoa_candidate_lineage_receipt_v1",
        "aoa-skills example must use schema_version=aoa_candidate_lineage_receipt_v1",
    )
    require(
        seed.get("schema_version") == "dionysus_seed_lineage_entry_v1",
        "Dionysus example must use schema_version=dionysus_seed_lineage_entry_v1",
    )

    sdk_cluster_ref = require_text(sdk, "cluster_ref", "aoa-sdk example")
    skills_cluster_ref = require_text(skills, "cluster_ref", "aoa-skills example")
    skills_candidate_ref = require_text(skills, "candidate_ref", "aoa-skills example")
    seed_candidate_ref = require_text(seed, "candidate_ref", "Dionysus example")
    seed_ref = require_text(seed, "seed_ref", "Dionysus example")

    require(
        sdk_cluster_ref == skills_cluster_ref,
        "cluster_ref drift between aoa-sdk and aoa-skills examples",
    )
    require(
        skills_candidate_ref == seed_candidate_ref,
        "candidate_ref drift between aoa-skills and Dionysus examples",
    )
    require(
        seed.get("cluster_ref") in {None, skills_cluster_ref},
        "Dionysus cluster_ref must be null or match the upstream cluster_ref",
    )

    for label, payload in (
        ("aoa-sdk", sdk),
        ("aoa-skills", skills),
        ("Dionysus", seed),
    ):
        status_posture = payload.get("status_posture")
        require(
            status_posture in ALLOWED_STATUS_POSTURE,
            f"invalid {label} status_posture: {status_posture!r}",
        )

    lifecycle_status = seed.get("lifecycle_status")
    require(
        lifecycle_status in ALLOWED_LIFECYCLE,
        f"invalid Dionysus lifecycle_status: {lifecycle_status!r}",
    )

    for forbidden_key in ("candidate_ref", "seed_ref", "object_ref"):
        require(forbidden_key not in sdk, f"aoa-sdk example must not mint {forbidden_key}")
    for forbidden_key in ("seed_ref", "object_ref"):
        require(forbidden_key not in skills, f"aoa-skills example must not mint {forbidden_key}")

    object_ref = seed.get("object_ref")
    if lifecycle_status == "planted":
        require(object_ref, "planted seed must carry object_ref")
    if lifecycle_status in {"staged", "open-wave", "planting-in-progress"}:
        require(object_ref in {None, ""}, "pre-plant seed should keep object_ref null/empty")
    if lifecycle_status == "superseded":
        require(seed.get("merged_into"), "superseded seed must carry merged_into")
    if lifecycle_status == "dropped":
        require(seed.get("drop_reason"), "dropped seed must carry drop_reason")

    return LineageSummary(
        workspace_root=root,
        cluster_ref=sdk_cluster_ref,
        candidate_ref=skills_candidate_ref,
        seed_ref=seed_ref,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the first-wave candidate-lineage example chain across sibling repos."
    )
    parser.add_argument(
        "--workspace-root",
        required=True,
        help="Sibling workspace root that contains aoa-sdk, aoa-skills, and Dionysus.",
    )
    args = parser.parse_args()

    try:
        summary = validate_chain(Path(args.workspace_root))
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    print("candidate-lineage contract: OK")
    print(f"workspace_root={summary.workspace_root}")
    print(f"cluster_ref={summary.cluster_ref}")
    print(f"candidate_ref={summary.candidate_ref}")
    print(f"seed_ref={summary.seed_ref}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
