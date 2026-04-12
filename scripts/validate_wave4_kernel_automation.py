#!/usr/bin/env python3
"""Validate the wave 4 kernel-automation seam across sibling repos."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ALLOWED_NEXT_SKILLS = {
    "aoa-session-route-forks",
    "aoa-session-self-diagnose",
    "aoa-session-self-repair",
    "aoa-session-progression-lift",
    "aoa-automation-opportunity-scan",
    "aoa-quest-harvest",
}
REQUIRED_SKILL_EXAMPLE_REFS = (
    "decision_fork.wave4.json",
    "diagnosis_packet.wave4.json",
    "repair_cycle.wave4.json",
    "progression_delta.wave4.json",
    "automation_candidate.wave4.json",
)


@dataclass(frozen=True)
class Wave4Paths:
    sdk_doc: Path
    sdk_example: Path
    skills_doc: Path
    skills_examples_dir: Path
    playbook_path: Path
    playbook_manifest: Path
    stats_branch_summary: Path
    stats_automation_summary: Path


@dataclass(frozen=True)
class Wave4Summary:
    workspace_root: Path
    recommended_next_skill: str
    branch_window_ref: str
    automation_window_ref: str


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


def resolve_wave4_paths(workspace_root: Path) -> Wave4Paths:
    return Wave4Paths(
        sdk_doc=workspace_root / "aoa-sdk" / "docs" / "SESSION_GROWTH_KERNEL_SIGNAL_RULES.md",
        sdk_example=workspace_root / "aoa-sdk" / "examples" / "closeout_followthrough_decision.example.json",
        skills_doc=workspace_root / "aoa-skills" / "docs" / "SESSION_GROWTH_KERNEL_MATURITY.md",
        skills_examples_dir=workspace_root / "aoa-skills" / "examples" / "session_growth_artifacts",
        playbook_path=(
            workspace_root / "aoa-playbooks" / "playbooks" / "reviewed-automation-followthrough" / "PLAYBOOK.md"
        ),
        playbook_manifest=workspace_root / "aoa-playbooks" / "generated" / "playbook_composition_manifest.json",
        stats_branch_summary=workspace_root / "aoa-stats" / "generated" / "session_growth_branch_summary.min.json",
        stats_automation_summary=workspace_root / "aoa-stats" / "generated" / "automation_followthrough_summary.min.json",
    )


def validate_wave4_kernel_automation(workspace_root: Path) -> Wave4Summary:
    root = workspace_root.expanduser().resolve()
    paths = resolve_wave4_paths(root)

    for required_path in (
        paths.sdk_doc,
        paths.sdk_example,
        paths.skills_doc,
        paths.playbook_path,
        paths.playbook_manifest,
        paths.stats_branch_summary,
        paths.stats_automation_summary,
    ):
        require(required_path.exists(), f"missing required wave4 path: {required_path}")

    for example_name in REQUIRED_SKILL_EXAMPLE_REFS:
        example_path = paths.skills_examples_dir / example_name
        require(example_path.exists(), f"missing wave4 skill example: {example_path}")

    closeout = read_json_object(paths.sdk_example)
    require(
        closeout.get("schema_version") == "aoa_sdk_closeout_followthrough_decision_v1",
        "aoa-sdk closeout example must use schema_version=aoa_sdk_closeout_followthrough_decision_v1",
    )
    recommended_next_skill = require_text(closeout, "recommended_next_skill", "aoa-sdk closeout example")
    require(
        recommended_next_skill in ALLOWED_NEXT_SKILLS,
        f"recommended_next_skill is outside the expected kernel set: {recommended_next_skill!r}",
    )
    require("seed_ref" not in closeout, "aoa-sdk closeout example must not mint seed_ref")

    playbook_text = paths.playbook_path.read_text(encoding="utf-8").lower()
    require(
        "scheduler authority" in playbook_text or "not a scheduler" in playbook_text,
        "reviewed automation follow-through playbook must explicitly disclaim scheduler authority",
    )

    manifest = read_json_object(paths.playbook_manifest)
    managed_playbooks = manifest.get("managed_playbooks")
    require(isinstance(managed_playbooks, list), "playbook composition manifest must carry managed_playbooks")
    require(
        "reviewed-automation-followthrough" not in managed_playbooks,
        "reviewed-automation-followthrough must stay out of the managed composition manifest",
    )

    branch_summary = read_json_object(paths.stats_branch_summary)
    require(
        branch_summary.get("schema_version") == "aoa_stats_session_growth_branch_summary_v1",
        "session growth branch summary must use schema_version=aoa_stats_session_growth_branch_summary_v1",
    )
    require(
        isinstance(branch_summary.get("counts_by_recommended_next_skill"), dict),
        "branch summary missing counts_by_recommended_next_skill",
    )
    branch_window_ref = require_text(branch_summary, "window_ref", "branch summary")

    automation_summary = read_json_object(paths.stats_automation_summary)
    require(
        automation_summary.get("schema_version") == "aoa_stats_automation_followthrough_summary_v1",
        "automation followthrough summary must use schema_version=aoa_stats_automation_followthrough_summary_v1",
    )
    require(
        "schedule_activation_count" not in automation_summary,
        "automation followthrough summary must not claim schedule activation",
    )
    require(
        all(key in automation_summary for key in ("seed_ready_count", "not_now_count", "playbook_seed_candidate_count")),
        "automation followthrough summary missing readiness or playbook-seed split",
    )
    if automation_summary.get("playbook_seed_candidate_count", 0):
        require(
            "reviewed-automation-followthrough" not in managed_playbooks,
            "playbook-seed candidacy must remain outside composition while wave4 is review-governed",
        )
    automation_window_ref = require_text(automation_summary, "window_ref", "automation followthrough summary")

    return Wave4Summary(
        workspace_root=root,
        recommended_next_skill=recommended_next_skill,
        branch_window_ref=branch_window_ref,
        automation_window_ref=automation_window_ref,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the wave 4 kernel-automation seam across sibling repos."
    )
    parser.add_argument(
        "--workspace-root",
        required=True,
        help="Sibling workspace root that contains aoa-sdk, aoa-skills, aoa-playbooks, and aoa-stats.",
    )
    args = parser.parse_args()

    try:
        summary = validate_wave4_kernel_automation(Path(args.workspace_root))
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    print("wave4 kernel automation contract: OK")
    print(f"workspace_root={summary.workspace_root}")
    print(f"recommended_next_skill={summary.recommended_next_skill}")
    print(f"branch_window_ref={summary.branch_window_ref}")
    print(f"automation_window_ref={summary.automation_window_ref}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
