from __future__ import annotations

import os
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
            [sys.executable, "scripts/validate_questbook_lifecycle.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_root_quest_entries_are_compatibility_aliases(self) -> None:
        root_entries = sorted((REPO_ROOT / "quests").glob("AOA-Q-*"))
        self.assertGreater(len(root_entries), 0)
        for path in root_entries:
            self.assertTrue(path.is_symlink(), path)
            target = (path.parent / os.readlink(path)).resolve()
            target_rel = target.relative_to(REPO_ROOT).parts
            self.assertEqual(target_rel[0], "quests")
            self.assertIn(
                target_rel[1],
                {"captured", "triaged", "ready", "active", "blocked", "reanchor", "done", "dropped"},
            )
            self.assertEqual(target.name, path.name)


if __name__ == "__main__":
    unittest.main()
