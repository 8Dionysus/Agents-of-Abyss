from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_ROOT = REPO_ROOT / "schemas"
REGISTRY = SCHEMAS_ROOT / "registry.json"
ROOT_README = SCHEMAS_ROOT / "README.md"
ROOT_AGENTS = SCHEMAS_ROOT / "AGENTS.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class SchemaDistrictTestCase(unittest.TestCase):
    def test_schema_registry_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_schema_registry.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_every_root_schema_is_registered(self) -> None:
        registry = load_json(REGISTRY)
        registered = {entry["path"] for entry in registry["root_schemas"]}
        discovered = {
            path.relative_to(REPO_ROOT).as_posix()
            for path in SCHEMAS_ROOT.glob("*.json")
            if path.name != "registry.json"
        }
        self.assertEqual(registered, discovered)

    def test_registered_root_schemas_are_valid_json_schemas(self) -> None:
        registry = load_json(REGISTRY)
        for entry in registry["root_schemas"]:
            with self.subTest(schema=entry["path"]):
                schema = load_json(REPO_ROOT / entry["path"])
                Draft202012Validator.check_schema(schema)

    def test_readme_and_agents_name_registry_contract(self) -> None:
        readme = ROOT_README.read_text(encoding="utf-8")
        agents = ROOT_AGENTS.read_text(encoding="utf-8")

        self.assertIn("[`registry.json`](registry.json)", readme)
        self.assertIn("Root Contracts", readme)
        self.assertIn("schemas/registry.json", agents)
        self.assertIn("python scripts/validate_schema_registry.py", agents)


if __name__ == "__main__":
    unittest.main()
