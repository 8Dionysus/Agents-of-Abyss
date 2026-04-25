from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
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


class MechanicReadmeCardTests(unittest.TestCase):
    def test_mechanic_readme_cards_validator_accepts_all_cards(self) -> None:
        result = run_script("scripts/validate_mechanic_readme_cards.py")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_every_mechanic_card_has_required_headings(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        headings = registry["mechanic_card_required_headings"]
        for entry in registry["mechanics"]:
            text = (REPO_ROOT / entry["entry_ref"]).read_text(encoding="utf-8")
            positions = []
            for heading in headings:
                self.assertIn(heading, text, f"{entry['slug']} missing {heading}")
                positions.append(text.index(heading))
            self.assertEqual(positions, sorted(positions), f"{entry['slug']} headings are out of order")

    def test_registry_card_values_are_non_empty(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        for entry in registry["mechanics"]:
            card = entry.get("card")
            self.assertIsInstance(card, dict, entry["slug"])
            assert isinstance(card, dict)
            for key in ("trigger", "center_owns", "stronger_owner_split", "inputs", "outputs", "next_route"):
                self.assertTrue(card.get(key), f"{entry['slug']} missing card.{key}")
            self.assertTrue(entry.get("must_not_claim"), entry["slug"])
            self.assertTrue(entry.get("validation_refs"), entry["slug"])


if __name__ == "__main__":
    unittest.main()
