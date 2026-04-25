from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


REPO_ROOT = _repo_root()


class QuestbookLifecycleTests(unittest.TestCase):
    def test_validator_accepts_current_board(self) -> None:
        result = subprocess.run(
            [sys.executable, "mechanics/questbook/scripts/validate_questbook_lifecycle.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_root_quest_entries_are_absent(self) -> None:
        root_entries = sorted((REPO_ROOT / "quests").glob("AOA-Q-*"))
        self.assertEqual(root_entries, [])


if __name__ == "__main__":
    unittest.main()
