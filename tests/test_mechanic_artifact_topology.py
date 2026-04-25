from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class MechanicArtifactTopologyTests(unittest.TestCase):
    def test_validator_accepts_current_topology(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_mechanic_artifact_topology.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_root_agon_artifacts_are_aliases(self) -> None:
        for district in ("schemas", "examples", "config", "generated"):
            for path in (REPO_ROOT / district).glob("agon*"):
                self.assertTrue(path.is_symlink(), f"{path} should be a compatibility alias")

    def test_root_experience_artifacts_are_aliases(self) -> None:
        for district in ("schemas", "examples"):
            for path in (REPO_ROOT / district).glob("experience*"):
                self.assertTrue(path.is_symlink(), f"{path} should be a compatibility alias")


if __name__ == "__main__":
    unittest.main()
