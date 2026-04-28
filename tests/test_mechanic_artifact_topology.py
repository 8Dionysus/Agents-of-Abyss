from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class MechanicArtifactTopologyTests(unittest.TestCase):
    def test_artifact_topology_keeps_alias_rule_inside_placement_law(self) -> None:
        topology = (REPO_ROOT / "mechanics" / "ARTIFACT_TOPOLOGY.md").read_text()
        self.assertNotIn("## No Root Aliases", topology)
        self.assertIn("do not add root or flat", topology)
        self.assertIn("Package-local `legacy/raw`, seed, and landing receipt districts are allowed", topology)
        self.assertIn("without becoming alternate active routes", topology)
        self.assertIn("Questbook is the one intentional root-store exception", topology)

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

    def test_root_agon_artifacts_are_absent(self) -> None:
        for district in ("schemas", "examples", "config", "generated"):
            for path in (REPO_ROOT / district).glob("agon*"):
                self.fail(f"{path} should live only under mechanics/agon/")

    def test_root_experience_artifacts_are_absent(self) -> None:
        for district in ("schemas", "examples"):
            for path in (REPO_ROOT / district).glob("experience*"):
                self.fail(f"{path} should live only under mechanics/experience/")


if __name__ == "__main__":
    unittest.main()
