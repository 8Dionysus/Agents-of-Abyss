from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ConfigRegistryTests(unittest.TestCase):
    def test_current_config_registry_is_valid(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_config_registry.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_every_root_config_json_is_registered(self) -> None:
        registry = json.loads((REPO_ROOT / "config/registry.json").read_text(encoding="utf-8"))
        registered = {entry["path"] for entry in registry["configs"]}
        discovered = {path.relative_to(REPO_ROOT).as_posix() for path in (REPO_ROOT / "config").glob("*.json")}
        self.assertEqual(registered, discovered)

    def test_unregistered_root_config_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            shutil.copytree(REPO_ROOT / "config", temp_root / "config")
            shutil.copytree(REPO_ROOT / "docs", temp_root / "docs")
            shutil.copytree(REPO_ROOT / "generated", temp_root / "generated")
            shutil.copytree(REPO_ROOT / "scripts", temp_root / "scripts")
            shutil.copytree(REPO_ROOT / "tests", temp_root / "tests")
            (temp_root / "config/unregistered.json").write_text('{"status":"active"}\n', encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "scripts/validate_config_registry.py", "--repo-root", str(temp_root)],
                cwd=temp_root,
                check=False,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("config JSON files missing from registry", result.stdout)
        self.assertIn("config/unregistered.json", result.stdout)


if __name__ == "__main__":
    unittest.main()
