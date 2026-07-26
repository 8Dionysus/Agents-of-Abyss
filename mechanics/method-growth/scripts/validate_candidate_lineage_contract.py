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
@dataclass(frozen=True)
class LineageExamplePaths:
    sdk: Path
    skills: Path


@dataclass(frozen=True)
class LineageSummary:
    workspace_root: Path
    cluster_ref: str
    candidate_ref: str


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
    )


def validate_chain(workspace_root: Path) -> LineageSummary:
    root = workspace_root.expanduser().resolve()
    paths = resolve_example_paths(root)

    sdk = read_json_object(paths.sdk)
    skills = read_json_object(paths.skills)

    require(
        sdk.get("schema_version") == "aoa_checkpoint_lineage_hint_v1",
        "aoa-sdk example must use schema_version=aoa_checkpoint_lineage_hint_v1",
    )
    require(
        skills.get("schema_version") == "aoa_candidate_lineage_receipt_v1",
        "aoa-skills example must use schema_version=aoa_candidate_lineage_receipt_v1",
    )

    sdk_cluster_ref = require_text(sdk, "cluster_ref", "aoa-sdk example")
    skills_cluster_ref = require_text(skills, "cluster_ref", "aoa-skills example")
    skills_candidate_ref = require_text(skills, "candidate_ref", "aoa-skills example")

    require(
        sdk_cluster_ref == skills_cluster_ref,
        "cluster_ref drift between aoa-sdk and aoa-skills examples",
    )
    for label, payload in (
        ("aoa-sdk", sdk),
        ("aoa-skills", skills),
    ):
        status_posture = payload.get("status_posture")
        require(
            status_posture in ALLOWED_STATUS_POSTURE,
            f"invalid {label} status_posture: {status_posture!r}",
        )

    for forbidden_key in ("candidate_ref", "seed_ref", "object_ref"):
        require(forbidden_key not in sdk, f"aoa-sdk example must not mint {forbidden_key}")
    for forbidden_key in ("seed_ref", "object_ref"):
        require(forbidden_key not in skills, f"aoa-skills example must not mint {forbidden_key}")

    return LineageSummary(
        workspace_root=root,
        cluster_ref=sdk_cluster_ref,
        candidate_ref=skills_candidate_ref,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the first-wave candidate-lineage example chain across sibling repos."
    )
    parser.add_argument(
        "--workspace-root",
        required=True,
        help="Sibling workspace root that contains aoa-sdk and aoa-skills.",
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
