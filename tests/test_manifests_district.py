from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFESTS_ROOT = REPO_ROOT / "manifests"
REGISTRY = MANIFESTS_ROOT / "registry.json"
ROOT_README = MANIFESTS_ROOT / "README.md"
ROOT_AGENTS = MANIFESTS_ROOT / "AGENTS.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class ManifestsDistrictTestCase(unittest.TestCase):
    def test_root_manifests_is_registry_only(self) -> None:
        self.assertEqual({path.name for path in MANIFESTS_ROOT.glob("*.json")}, {"registry.json"})
        self.assertFalse((MANIFESTS_ROOT / "recurrence").exists())

    def test_registry_indexes_manifest_homes(self) -> None:
        registry = load_json(REGISTRY)

        self.assertEqual(registry["schema_version"], "aoa_manifests_registry_v1")
        self.assertEqual(registry["authority_ref"], "manifests/README.md")
        self.assertGreaterEqual(len(registry["manifest_homes"]), 1)

        home_refs = {home["home_ref"] for home in registry["manifest_homes"]}
        self.assertIn("manifest-home:agon-recurrence-adapter", home_refs)

    def test_registry_homes_have_local_docs_and_validator(self) -> None:
        registry = load_json(REGISTRY)

        for home in registry["manifest_homes"]:
            with self.subTest(home=home["home_ref"]):
                home_path = REPO_ROOT / home["path"]
                self.assertTrue(home_path.is_dir())
                self.assertTrue((home_path / "README.md").is_file())
                self.assertTrue((home_path / "AGENTS.md").is_file())
                self.assertTrue((REPO_ROOT / home["validator"]).is_file())
                self.assertTrue(list(REPO_ROOT.glob(home["component_glob"])))
                self.assertTrue(list(REPO_ROOT.glob(home["hook_glob"])))

    def test_readme_and_agents_name_registry_contract(self) -> None:
        readme = ROOT_README.read_text(encoding="utf-8")
        agents = ROOT_AGENTS.read_text(encoding="utf-8")

        self.assertIn("[`registry.json`](registry.json)", readme)
        self.assertIn("Registered Homes", readme)
        self.assertIn("python scripts/validate_manifests_registry.py", readme)
        self.assertIn("manifests/registry.json", agents)
        self.assertIn("Mechanic-owned component or hook records belong", agents)


if __name__ == "__main__":
    unittest.main()
