from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from center_entry_map_common import (  # noqa: E402
    BASELINE_VALIDATION_COMMANDS,
    ENTRY_SURFACE_REFS,
    REQUIRED_ROUTE_MODES,
    VALIDATION_BASELINE_REF,
    build_payload,
    resolve_local_ref,
)
from validate_entry_surface_sync import (  # noqa: E402
    SURFACE_ROUTE_MODE_EXEMPTIONS,
    SURFACE_VALIDATION_AUTHORITY_REFS,
    collect_problems,
)


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

    def test_mechanics_entry_validation_can_live_in_agents(self) -> None:
        self.assertEqual(SURFACE_VALIDATION_AUTHORITY_REFS["mechanics/README.md"], "mechanics/AGENTS.md")
        self.assertEqual(
            SURFACE_VALIDATION_AUTHORITY_REFS["mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md"],
            "mechanics/release-support/docs/AGENTS.md",
        )

    def test_mechanic_change_route_uses_registry_instead_of_manual_package_list(self) -> None:
        payload = build_payload()
        route = next(item for item in payload["routes"] if item["route_id"] == "mechanic-change")
        self.assertIn("mechanics/registry.json", route["need"])
        self.assertIn("mechanics/registry.json", route["machine_surface_refs"])
        self.assertNotIn("Agon, Experience", route["need"])

    def test_validation_baseline_surface_names_all_baseline_commands(self) -> None:
        text = resolve_local_ref(VALIDATION_BASELINE_REF).read_text(encoding="utf-8")
        for command in BASELINE_VALIDATION_COMMANDS:
            self.assertIn(command, text)

    def test_root_agents_can_point_to_validation_baseline(self) -> None:
        text = Path("AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(VALIDATION_BASELINE_REF, text)


if __name__ == "__main__":
    unittest.main()
