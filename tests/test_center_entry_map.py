from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from center_entry_map_common import REQUIRED_ROUTE_MODES, SURFACE_PAYLOAD, build_payload


class CenterEntryMapTests(unittest.TestCase):
    def test_build_payload_stays_center_only(self) -> None:
        payload = build_payload()
        self.assertEqual(payload["schema_version"], "aoa_center_entry_map_v2")
        self.assertEqual(payload["schema_ref"], "schemas/center-entry-map.schema.json")
        self.assertEqual(payload["owner_repo"], "Agents-of-Abyss")
        self.assertEqual(payload["surface_kind"], "center_entry_map")
        self.assertEqual(payload["authority_ref"], SURFACE_PAYLOAD["authority_ref"])
        self.assertEqual(payload["public_root_ref"], "README.md")
        self.assertEqual(payload["route_contract_ref"], "docs/START_HERE_ROUTE_CONTRACT.md")

    def test_route_modes_are_complete_and_ordered(self) -> None:
        payload = build_payload()
        routes = payload["routes"]
        self.assertEqual([route["priority"] for route in routes], list(range(1, len(routes) + 1)))
        self.assertEqual({route["route_mode"] for route in routes}, set(REQUIRED_ROUTE_MODES))
        self.assertEqual(
            [route["route_id"] for route in routes],
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

    def test_first_reading_route_keeps_human_path_short(self) -> None:
        payload = build_payload()
        route = next(route for route in payload["routes"] if route["route_id"] == "first-reading")
        self.assertEqual(
            route["human_path"],
            [
                "README.md",
                "CHARTER.md",
                "ECOSYSTEM_MAP.md",
                "docs/FEDERATION_RULES.md",
            ],
        )
        self.assertIn("generated/center_entry_map.min.json", route["machine_surface_refs"])

    def test_route_contract_is_machine_visible(self) -> None:
        payload = build_payload()
        rendered = json.dumps(payload, separators=(",", ":"))
        self.assertIn("docs/START_HERE_ROUTE_CONTRACT.md", rendered)
        self.assertIn("public-claim-validation", rendered)
        self.assertIn("must_not_claim", rendered)
        self.assertNotIn('"surface_ref":"scripts/', rendered)
        self.assertNotIn('"surface_ref":"src/', rendered)

    def test_low_context_route_does_not_replace_human_docs(self) -> None:
        payload = build_payload()
        route = next(route for route in payload["routes"] if route["route_id"] == "low-context-agent")
        self.assertEqual(route["surface_ref"], "generated/center_entry_map.min.json")
        self.assertIn("README.md", route["human_path"])
        self.assertTrue(any("replaces human docs" in item for item in route["must_not_claim"]))


if __name__ == "__main__":
    unittest.main()
