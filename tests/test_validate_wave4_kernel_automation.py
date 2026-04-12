from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_wave4_kernel_automation import validate_wave4_kernel_automation


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class Wave4KernelAutomationValidatorTests(unittest.TestCase):
    def write_valid_workspace(self, root: Path) -> None:
        write_text(root / "aoa-sdk" / "docs" / "SESSION_GROWTH_KERNEL_SIGNAL_RULES.md", "# rules\n")
        write_json(
            root / "aoa-sdk" / "examples" / "closeout_followthrough_decision.example.json",
            {
                "schema_version": "aoa_sdk_closeout_followthrough_decision_v1",
                "session_ref": "session:test-wave4",
                "reviewed_closeout_context_ref": ".aoa/session-growth/current/test/closeout-context.json",
                "cluster_ref": "cluster:route:aoa-playbooks-playbook-registry-min",
                "recommended_next_skill": "aoa-automation-opportunity-scan",
                "also_considered": ["aoa-session-route-forks"],
                "reason_codes": ["repeated_manual_route"],
                "checkpoint_required": True,
                "approval_posture": "review_required",
                "defer_allowed": True,
                "owner_hypothesis": "aoa-playbooks",
                "nearest_wrong_target": "aoa-skills",
                "status_posture": "reanchor",
            },
        )
        write_text(root / "aoa-skills" / "docs" / "SESSION_GROWTH_KERNEL_MATURITY.md", "# maturity\n")
        for example_name in (
            "decision_fork.wave4.json",
            "diagnosis_packet.wave4.json",
            "repair_cycle.wave4.json",
            "progression_delta.wave4.json",
            "automation_candidate.wave4.json",
        ):
            write_json(
                root / "aoa-skills" / "examples" / "session_growth_artifacts" / example_name,
                {"example": example_name},
            )
        write_text(
            root / "aoa-playbooks" / "playbooks" / "reviewed-automation-followthrough" / "PLAYBOOK.md",
            "This playbook is not a scheduler and does not claim scheduler authority.\n",
        )
        write_json(
            root / "aoa-playbooks" / "generated" / "playbook_composition_manifest.json",
            {"managed_playbooks": ["session-growth-cycle"]},
        )
        write_json(
            root / "aoa-stats" / "generated" / "session_growth_branch_summary.min.json",
            {
                "schema_version": "aoa_stats_session_growth_branch_summary_v1",
                "window_ref": "window:2026-04",
                "counts_by_recommended_next_skill": {
                    "aoa-automation-opportunity-scan": 1
                },
            },
        )
        write_json(
            root / "aoa-stats" / "generated" / "automation_followthrough_summary.min.json",
            {
                "schema_version": "aoa_stats_automation_followthrough_summary_v1",
                "window_ref": "window:2026-04",
                "seed_ready_count": 1,
                "not_now_count": 1,
                "playbook_seed_candidate_count": 1,
            },
        )

    def test_accepts_wave4_workspace_with_review_governed_playbook(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_valid_workspace(root)

            summary = validate_wave4_kernel_automation(root)

        self.assertEqual(summary.recommended_next_skill, "aoa-automation-opportunity-scan")
        self.assertEqual(summary.branch_window_ref, "window:2026-04")
        self.assertEqual(summary.automation_window_ref, "window:2026-04")

    def test_rejects_playbook_if_it_enters_composition_manifest(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_valid_workspace(root)
            write_json(
                root / "aoa-playbooks" / "generated" / "playbook_composition_manifest.json",
                {"managed_playbooks": ["reviewed-automation-followthrough"]},
            )

            with self.assertRaisesRegex(
                ValueError,
                "reviewed-automation-followthrough must stay out of the managed composition manifest",
            ):
                validate_wave4_kernel_automation(root)

    def test_rejects_automation_summary_schedule_activation_claim(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_valid_workspace(root)
            payload = json.loads(
                (root / "aoa-stats" / "generated" / "automation_followthrough_summary.min.json").read_text(
                    encoding="utf-8"
                )
            )
            payload["schedule_activation_count"] = 1
            write_json(root / "aoa-stats" / "generated" / "automation_followthrough_summary.min.json", payload)

            with self.assertRaisesRegex(
                ValueError,
                "automation followthrough summary must not claim schedule activation",
            ):
                validate_wave4_kernel_automation(root)


if __name__ == "__main__":
    unittest.main()
