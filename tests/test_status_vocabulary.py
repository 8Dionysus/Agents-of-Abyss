from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class StatusVocabularyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = Path(tempfile.mkdtemp())
        (self.tempdir / "config").mkdir()
        (self.tempdir / "mechanics").mkdir()
        (self.tempdir / "config/link_shape_hygiene.json").write_text(json.dumps({
            "status_vocabulary": {"mechanic_status": ["planted", "landed"]},
            "status_checks": [{"file": "mechanics/registry.json", "json_path": "mechanics.*.status", "vocabulary": "mechanic_status", "required": True}]
        }), encoding="utf-8")
        scripts = self.tempdir / "scripts"
        scripts.mkdir()
        repo_scripts = Path(__file__).resolve().parents[1] / "scripts"
        shutil.copy(repo_scripts / "hygiene_common.py", scripts / "hygiene_common.py")
        shutil.copy(repo_scripts / "validate_status_vocabulary.py", scripts / "validate_status_vocabulary.py")

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)

    def test_status_vocabulary(self) -> None:
        (self.tempdir / "mechanics/registry.json").write_text(json.dumps({"mechanics": {"agon": {"status": "landed"}}}), encoding="utf-8")
        ok = subprocess.run([sys.executable, "scripts/validate_status_vocabulary.py"], cwd=self.tempdir)
        self.assertEqual(ok.returncode, 0)
        (self.tempdir / "mechanics/registry.json").write_text(json.dumps({"mechanics": {"agon": {"status": "magic"}}}), encoding="utf-8")
        bad = subprocess.run([sys.executable, "scripts/validate_status_vocabulary.py"], cwd=self.tempdir, text=True, capture_output=True)
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("magic", bad.stdout)


if __name__ == "__main__":
    unittest.main()
