from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_ROOT = REPO_ROOT / "scripts"
REGISTRY = SCRIPTS_ROOT / "registry.json"
ROOT_README = SCRIPTS_ROOT / "README.md"
ROOT_AGENTS = SCRIPTS_ROOT / "AGENTS.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class ScriptsDistrictTestCase(unittest.TestCase):
    def test_scripts_district_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_scripts_district.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_every_root_script_is_registered(self) -> None:
        registry = load_json(REGISTRY)
        registered = {
            rel
            for family in registry["script_families"]
            for rel in family["paths"]
        }
        discovered = {
            path.relative_to(REPO_ROOT).as_posix()
            for path in SCRIPTS_ROOT.glob("*.py")
            if path.name != "__init__.py"
        }
        self.assertEqual(registered, discovered)

    def test_unregistered_root_script_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            shutil.copytree(
                SCRIPTS_ROOT,
                temp_root / "scripts",
                ignore=shutil.ignore_patterns("__pycache__"),
            )
            (temp_root / "scripts/temporary_unregistered.py").write_text(
                "# temporary test script\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/validate_scripts_district.py",
                    "--repo-root",
                    str(temp_root),
                ],
                cwd=temp_root,
                check=False,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("root scripts missing from registry", result.stdout)
        self.assertIn("scripts/temporary_unregistered.py", result.stdout)

    def test_readme_and_agents_name_registry_contract(self) -> None:
        readme = ROOT_README.read_text(encoding="utf-8")
        agents = ROOT_AGENTS.read_text(encoding="utf-8")

        self.assertIn("[`registry.json`](registry.json)", readme)
        self.assertIn("Script Families", readme)
        self.assertIn("scripts/registry.json", agents)
        self.assertIn("python scripts/validate_scripts_district.py", agents)


if __name__ == "__main__":
    unittest.main()
