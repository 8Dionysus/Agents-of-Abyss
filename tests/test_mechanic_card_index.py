from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = REPO_ROOT / "generated" / "mechanic_card_index.min.json"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=REPO_ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


class MechanicCardIndexTests(unittest.TestCase):
    def test_mechanic_card_index_is_current(self) -> None:
        result = run_script("scripts/build_mechanic_card_index.py", "--check")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_mechanic_card_index_validates(self) -> None:
        result = run_script("scripts/validate_mechanic_card_index.py")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_mechanic_card_index_matches_registry_slugs(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        self.assertEqual(index["schema_version"], "aoa_mechanic_card_index_v1")
        self.assertEqual([m["slug"] for m in index["mechanics"]], [m["slug"] for m in registry["mechanics"]])
        for mechanic in index["mechanics"]:
            self.assertTrue(mechanic["trigger"])
            self.assertTrue(mechanic["center_owns"])
            self.assertTrue(mechanic["stronger_owner_split"])
            self.assertTrue(mechanic["must_not_claim"])
            self.assertTrue(mechanic["next_route"])


if __name__ == "__main__":
    unittest.main()
