from __future__ import annotations

import json
import unittest
from pathlib import Path

import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from center_entry_map_common import SURFACE_PAYLOAD, build_payload


class CenterEntryMapTests(unittest.TestCase):
    def test_build_payload_stays_center_only(self) -> None:
        payload = build_payload()

        self.assertEqual(payload["schema_version"], "aoa_center_entry_map_v1")
        self.assertEqual(payload["schema_ref"], "schemas/center-entry-map.schema.json")
        self.assertEqual(payload["owner_repo"], "Agents-of-Abyss")
        self.assertEqual(payload["surface_kind"], "center_entry_map")
        self.assertEqual(payload["authority_ref"], SURFACE_PAYLOAD["authority_ref"])
        self.assertEqual(payload["public_root_ref"], "README.md")
        self.assertEqual(
            [route["route_id"] for route in payload["routes"]],
            [
                "center-overview",
                "constitutional-boundary",
                "public-contour",
                "source-of-truth-rules",
            ],
        )

    def test_public_contour_route_keeps_registry_and_supporting_inventory_split(self) -> None:
        payload = build_payload()
        route = next(route for route in payload["routes"] if route["route_id"] == "public-contour")

        self.assertEqual(route["surface_ref"], "generated/ecosystem_registry.min.json")
        self.assertEqual(
            route["verification_refs"],
            [
                "ECOSYSTEM_MAP.md",
                "generated/federation_supporting_inventory.min.json",
            ],
        )

    def test_payload_is_json_serializable(self) -> None:
        payload = build_payload()
        rendered = json.dumps(payload, separators=(",", ":"))

        self.assertIn("center_entry_map", rendered)
        self.assertNotIn('"surface_ref":"scripts/', rendered)
        self.assertNotIn('"surface_ref":"src/', rendered)


if __name__ == "__main__":
    unittest.main()
