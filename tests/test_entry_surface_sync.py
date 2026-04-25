from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from center_entry_map_common import ENTRY_SURFACE_REFS, REQUIRED_ROUTE_MODES  # noqa: E402
from validate_entry_surface_sync import SURFACE_ROUTE_MODE_EXEMPTIONS, collect_problems  # noqa: E402


class EntrySurfaceSyncTests(unittest.TestCase):
    def test_route_modes_are_visible_on_entry_surfaces(self) -> None:
        problems = collect_problems()
        self.assertEqual(problems, [])

    def test_contract_declares_all_expected_surfaces(self) -> None:
        self.assertIn("README.md", ENTRY_SURFACE_REFS)
        self.assertIn("AGENTS.md", ENTRY_SURFACE_REFS)
        self.assertIn("docs/README.md", ENTRY_SURFACE_REFS)
        self.assertIn("docs/START_HERE_ROUTE_CONTRACT.md", ENTRY_SURFACE_REFS)
        self.assertIn("CONTRIBUTING.md", ENTRY_SURFACE_REFS)
        self.assertIn("mechanics/README.md", ENTRY_SURFACE_REFS)
        self.assertIn("mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md", ENTRY_SURFACE_REFS)

    def test_route_mode_order_is_stable(self) -> None:
        self.assertEqual(
            list(REQUIRED_ROUTE_MODES),
            [
                "first-reading",
                "root-editing",
                "direction-change",
                "ownership-routing",
                "mechanic-change",
                "public-claim-validation",
                "low-context-agent",
                "district-work",
            ],
        )

    def test_mechanics_atlas_does_not_need_low_context_route_label(self) -> None:
        self.assertIn("low-context-agent", SURFACE_ROUTE_MODE_EXEMPTIONS["mechanics/README.md"])


if __name__ == "__main__":
    unittest.main()
