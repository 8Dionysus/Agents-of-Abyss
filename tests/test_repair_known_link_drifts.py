from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class KnownRepairTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = Path(tempfile.mkdtemp())
        (self.tempdir / "config").mkdir()
        (self.tempdir / "docs").mkdir()
        (self.tempdir / "config/link_shape_hygiene.json").write_text(json.dumps({
            "link_validation": {"known_rewrites": [{"id": "x", "file": "docs/FEDERATION_RULES.md", "old": "(OLD.md)", "new": "(new/NEW.md)", "reason": "test"}]}
        }), encoding="utf-8")
        (self.tempdir / "docs/FEDERATION_RULES.md").write_text("[Old](OLD.md)\n", encoding="utf-8")
        scripts = self.tempdir / "scripts"
        scripts.mkdir()
        repo_scripts = Path(__file__).resolve().parents[1] / "scripts"
        shutil.copy(repo_scripts / "hygiene_common.py", scripts / "hygiene_common.py")
        shutil.copy(repo_scripts / "repair_known_link_drifts.py", scripts / "repair_known_link_drifts.py")

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)

    def test_check_fails_then_apply_passes(self) -> None:
        bad = subprocess.run([sys.executable, "scripts/repair_known_link_drifts.py", "--check"], cwd=self.tempdir, text=True, capture_output=True)
        self.assertNotEqual(bad.returncode, 0)
        apply = subprocess.run([sys.executable, "scripts/repair_known_link_drifts.py", "--apply"], cwd=self.tempdir)
        self.assertEqual(apply.returncode, 0)
        ok = subprocess.run([sys.executable, "scripts/repair_known_link_drifts.py", "--check"], cwd=self.tempdir)
        self.assertEqual(ok.returncode, 0)
        self.assertIn("(new/NEW.md)", (self.tempdir / "docs/FEDERATION_RULES.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
