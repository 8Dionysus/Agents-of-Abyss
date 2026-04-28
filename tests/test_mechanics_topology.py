from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
CANONICAL_SLUGS = (
    "method-growth",
    "distillation",
    "recurrence",
    "checkpoint",
    "experience",
    "agon",
    "antifragility",
    "questbook",
    "rpg",
    "boundary-bridge",
    "release-support",
)


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=REPO_ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


class MechanicsTopologyTests(unittest.TestCase):
    def test_mechanics_registry_has_canonical_slug_set_and_order(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        slugs = tuple(entry["slug"] for entry in registry["mechanics"])
        self.assertEqual(slugs, CANONICAL_SLUGS)

    def test_every_mechanic_package_has_required_entry_surfaces(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        for entry in registry["mechanics"]:
            package = REPO_ROOT / entry["package_path"]
            self.assertTrue((package / "AGENTS.md").exists())
            self.assertTrue((package / "README.md").exists())
            self.assertTrue((package / "ROADMAP.md").exists())
            self.assertTrue((package / "LANDING_LOG.md").exists())
            self.assertTrue((package / "docs").is_dir())

    def test_mechanics_topology_validator_accepts_all_mechanics(self) -> None:
        result = run_script("scripts/validate_mechanics_topology.py")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_no_flat_agon_experience_or_rpg_docs_remain(self) -> None:
        docs = REPO_ROOT / "docs"
        self.assertFalse(list(docs.glob("AGON_*.md")))
        self.assertFalse(list(docs.glob("EXPERIENCE_*.md")))
        self.assertFalse(list(docs.glob("RPG_*.md")))


if __name__ == "__main__":
    unittest.main()
