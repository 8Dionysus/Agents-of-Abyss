from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_mechanic_landing_logs import validate_log


class MechanicLandingLogTests(unittest.TestCase):
    def test_checkpoint_landing_log_carries_center_boundary(self) -> None:
        problems = validate_log("checkpoint")

        self.assertEqual(problems, [])

    def test_recurrence_landing_log_carries_active_part_distillation(self) -> None:
        problems = validate_log("recurrence")

        self.assertEqual(problems, [])

    def test_agon_landing_log_carries_release_anchors(self) -> None:
        problems = validate_log("agon")

        self.assertEqual(problems, [])

    def test_experience_landing_log_carries_versioned_center_line(self) -> None:
        problems = validate_log("experience")

        self.assertEqual(problems, [])

    def test_questbook_landing_log_carries_lane_first_topology(self) -> None:
        problems = validate_log("questbook")

        self.assertEqual(problems, [])

    def test_rpg_landing_log_carries_vocabulary_overlay_contract(self) -> None:
        problems = validate_log("rpg")

        self.assertEqual(problems, [])


if __name__ == "__main__":
    unittest.main()
