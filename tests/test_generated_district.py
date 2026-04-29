from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATED_ROOT = REPO_ROOT / "generated"
README_PATH = GENERATED_ROOT / "README.md"
AGENTS_PATH = GENERATED_ROOT / "AGENTS.md"

EXPECTED_ROOT_JSON = {
    "agents_mesh.min.json": {
        "class": "Root-built",
        "builder": "scripts/build_agents_mesh_index.py",
        "validator": "scripts/validate_agents_mesh_index.py",
    },
    "center_entry_map.min.json": {
        "class": "Root-built",
        "builder": "scripts/build_center_entry_map.py",
        "validator": "scripts/validate_center_entry_map.py",
    },
    "docs_thematic_index.min.json": {
        "class": "Root-built",
        "builder": "scripts/build_docs_thematic_index.py",
        "validator": "scripts/validate_docs_thematic_index.py",
    },
    "ecosystem_registry.min.json": {
        "class": "Manual published summary",
        "builder": "manual, no builder",
        "validator": "scripts/validate_ecosystem.py",
    },
    "federation_supporting_inventory.min.json": {
        "class": "Manual published summary",
        "builder": "manual, no builder",
        "validator": "scripts/validate_ecosystem.py",
    },
    "link_shape_hygiene.min.json": {
        "class": "Root-built",
        "builder": "scripts/build_link_shape_hygiene_index.py",
        "validator": "scripts/validate_link_shape_hygiene_index.py",
    },
    "mechanic_card_index.min.json": {
        "class": "Root-built",
        "builder": "scripts/build_mechanic_card_index.py",
        "validator": "scripts/validate_mechanic_card_index.py",
    },
    "owner_request_queue.min.json": {
        "class": "Root-built",
        "builder": "scripts/build_owner_request_queue.py",
        "validator": "scripts/validate_generated_owner_request_queue.py",
    },
    "questbook_frontier.min.json": {
        "class": "Mechanic-built root-published",
        "builder": "mechanics/questbook/scripts/build_questbook_index.py",
        "validator": "mechanics/questbook/scripts/validate_questbook_index.py",
    },
    "questbook_index.min.json": {
        "class": "Mechanic-built root-published",
        "builder": "mechanics/questbook/scripts/build_questbook_index.py",
        "validator": "mechanics/questbook/scripts/validate_questbook_index.py",
    },
    "questbook_relations.min.json": {
        "class": "Mechanic-built root-published",
        "builder": "mechanics/questbook/scripts/build_questbook_index.py",
        "validator": "mechanics/questbook/scripts/validate_questbook_index.py",
    },
}


class GeneratedDistrictTestCase(unittest.TestCase):
    def test_root_generated_json_set_has_no_orphans(self) -> None:
        actual = {path.name for path in GENERATED_ROOT.glob("*.json")}
        self.assertEqual(actual, set(EXPECTED_ROOT_JSON))

    def test_readme_indexes_every_root_generated_surface(self) -> None:
        readme = README_PATH.read_text(encoding="utf-8")

        for surface, metadata in EXPECTED_ROOT_JSON.items():
            with self.subTest(surface=surface):
                self.assertIn(f"[`{surface}`]({surface})", readme)
                self.assertIn(metadata["class"], readme)
                self.assertIn(metadata["builder"], readme)
                self.assertIn(metadata["validator"], readme)

    def test_generated_agents_keeps_root_scope(self) -> None:
        agents = AGENTS_PATH.read_text(encoding="utf-8")

        self.assertIn("Mechanic-built root-published Questbook read models", agents)
        self.assertIn("Do not place mechanic part-local generated capsules in root `generated/`.", agents)
        self.assertNotIn("mechanics/agon/parts/", agents)
        self.assertNotIn("agon_imposition_readiness", agents)
        self.assertNotIn("agon_gate_routing_handoff_request", agents)


if __name__ == "__main__":
    unittest.main()
