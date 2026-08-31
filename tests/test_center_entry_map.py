from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from scripts.center_entry.center_entry_map_common import (
    CENTER_ENTRY_ARTIFACT_IDENTITY,
    ENTRY_SURFACE_REFS,
    REQUIRED_ROUTE_MODES,
    SURFACE_PAYLOAD,
    VALIDATION_BASELINE_REF,
    VALIDATION_REFS,
    build_payload,
    load_schema,
    validate_payload_schema,
)


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
        self.assertEqual(payload["artifact_identity"], CENTER_ENTRY_ARTIFACT_IDENTITY)

    def test_artifact_identity_marks_center_route_readmodel_contract(self) -> None:
        identity = build_payload()["artifact_identity"]

        self.assertEqual(identity["artifact_class"], "center_entry_route_readmodel")
        self.assertEqual(identity["surface_state"], "generated")
        self.assertEqual(identity["authority_ref"], "docs/START_HERE_ROUTE_CONTRACT.md")
        self.assertEqual(identity["trust_layer"], ["abi_contract_signature", "w3c_prov_lineage"])
        self.assertIn("owner-repo acceptance", identity["consumer_expectation"])
        self.assertIn("Public center route", identity["privacy_boundary"])

    def test_center_entry_schema_constrains_artifact_surface_state(self) -> None:
        schema = load_schema()
        surface_state_schema = schema["$defs"]["artifactIdentity"]["properties"]["surface_state"]
        self.assertEqual(surface_state_schema["const"], "generated")

        payload = build_payload()
        payload["artifact_identity"] = {
            **payload["artifact_identity"],
            "surface_state": "generated-runtime",
        }

        with self.assertRaisesRegex(ValueError, "artifact_identity.surface_state"):
            validate_payload_schema(payload)

    def test_route_modes_are_complete_and_ordered(self) -> None:
        payload = build_payload()
        routes = payload["routes"]
        self.assertEqual([route["priority"] for route in routes], list(range(1, len(routes) + 1)))
        self.assertEqual({route["route_mode"] for route in routes}, set(REQUIRED_ROUTE_MODES))
        self.assertEqual([route["route_id"] for route in routes], list(REQUIRED_ROUTE_MODES))

    def test_first_reading_route_keeps_human_path_short(self) -> None:
        payload = build_payload()
        route = next(route for route in payload["routes"] if route["route_id"] == "first-reading")
        self.assertEqual(
            route["human_path"],
            [
                "README.md",
                "CHARTER.md",
                "DESIGN.md",
                "ECOSYSTEM_MAP.md",
                "docs/FEDERATION_RULES.md",
            ],
        )
        self.assertIn("generated/center_entry_map.min.json", route["machine_surface_refs"])

    def test_route_contract_is_machine_visible(self) -> None:
        payload = build_payload()
        rendered = json.dumps(payload, separators=(",", ":"))
        self.assertIn("docs/START_HERE_ROUTE_CONTRACT.md", rendered)
        self.assertIn("organ-alignment", rendered)
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

    def test_district_work_route_names_local_eval_and_stats_ports(self) -> None:
        payload = build_payload()
        route = next(route for route in payload["routes"] if route["route_id"] == "district-work")
        route_contract = Path("docs/START_HERE_ROUTE_CONTRACT.md").read_text(encoding="utf-8")
        self.assertIn("evals/README.md", route["human_path"])
        self.assertIn("stats/AGENTS.md", route["human_path"])
        self.assertIn("stats/README.md", route["human_path"])
        self.assertIn("- `stats/AGENTS.md`", route_contract)
        self.assertIn("- `stats/README.md`", route_contract)
        self.assertIn("evals", route["need"])
        self.assertIn("stats", route["need"])

    def test_entry_surface_refs_are_declared(self) -> None:
        self.assertIn("AGENTS.md", ENTRY_SURFACE_REFS)
        self.assertIn("mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md", ENTRY_SURFACE_REFS)
        self.assertIn("generated/center_entry_map.min.json", ENTRY_SURFACE_REFS)

    def test_validation_refs_include_entry_sync(self) -> None:
        payload = build_payload()
        for ref in VALIDATION_REFS:
            self.assertIn(ref, payload["validation_refs"])
        self.assertIn(VALIDATION_BASELINE_REF, payload["validation_refs"])
        self.assertIn("scripts/organ_contract/validate_organ_contract.py", payload["validation_refs"])
        self.assertIn("scripts/center_entry/validate_entry_surface_sync.py", payload["validation_refs"])
        self.assertIn("tests/test_entry_surface_sync.py", payload["validation_refs"])

    def test_baseline_routes_to_executable_owners(self) -> None:
        baseline = Path(VALIDATION_BASELINE_REF).read_text(encoding="utf-8")
        release_gate = Path("scripts/release_gate/release_check.py").read_text(encoding="utf-8")

        self.assertIn("scripts/center_entry/center_entry_map_common.py", baseline)
        self.assertIn("scripts/center_entry/validate_entry_surface_sync.py", baseline)
        self.assertIn("scripts/release_gate/release_check.py", baseline)
        self.assertNotIn("```bash", baseline)
        self.assertIn("scripts/organ_contract/validate_organ_contract.py", release_gate)
        self.assertIn("python", Path("VALIDATION.md").read_text(encoding="utf-8"))

    def test_organ_alignment_route_preserves_owner_boundaries(self) -> None:
        payload = build_payload()
        route = next(route for route in payload["routes"] if route["route_id"] == "organ-alignment")
        self.assertEqual(route["surface_ref"], "docs/organ-contract/README.md")
        self.assertIn("docs/organ-contract/ORGAN_CONTRACT.md", route["human_path"])
        self.assertIn("docs/organ-contract/FIRST_CYCLE.md", route["human_path"])
        self.assertTrue(any("owner acceptance" in item for item in route["must_not_claim"]))


if __name__ == "__main__":
    unittest.main()
