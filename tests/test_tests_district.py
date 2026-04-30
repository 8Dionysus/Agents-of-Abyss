from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TESTS_ROOT = REPO_ROOT / "tests"
REGISTRY = TESTS_ROOT / "registry.json"
ROOT_README = TESTS_ROOT / "README.md"
ROOT_AGENTS = TESTS_ROOT / "AGENTS.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class TestsDistrictTestCase(unittest.TestCase):
    def test_tests_district_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_tests_district.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_every_root_test_is_registered(self) -> None:
        registry = load_json(REGISTRY)
        registered = {
            rel
            for family in registry["test_families"]
            for rel in family["paths"]
        }
        discovered = {
            path.relative_to(REPO_ROOT).as_posix()
            for path in TESTS_ROOT.glob("test*.py")
        }
        self.assertEqual(registered, discovered)

    def test_unregistered_root_test_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            shutil.copytree(
                TESTS_ROOT,
                temp_root / "tests",
                ignore=shutil.ignore_patterns("__pycache__"),
            )
            shutil.copytree(
                REPO_ROOT / "scripts",
                temp_root / "scripts",
                ignore=shutil.ignore_patterns("__pycache__"),
            )
            (temp_root / "tests/test_temporary_unregistered.py").write_text(
                "def test_placeholder():\n    assert True\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/validate_tests_district.py",
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
        self.assertIn("root tests missing from registry", result.stdout)
        self.assertIn("tests/test_temporary_unregistered.py", result.stdout)

    def test_readme_and_agents_name_registry_contract(self) -> None:
        readme = ROOT_README.read_text(encoding="utf-8")
        agents = ROOT_AGENTS.read_text(encoding="utf-8")

        self.assertIn("[`registry.json`](registry.json)", readme)
        self.assertIn("Test Families", readme)
        self.assertIn("tests/registry.json", agents)
        self.assertIn("python scripts/validate_tests_district.py", agents)


if __name__ == "__main__":
    unittest.main()
