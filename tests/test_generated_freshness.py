from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class GeneratedFreshnessTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = Path(tempfile.mkdtemp())
        for rel in ["config", "generated", "scripts"]:
            (self.tempdir / rel).mkdir()
        repo_scripts = Path(__file__).resolve().parents[1] / "scripts"
        shutil.copy(repo_scripts / "hygiene_common.py", self.tempdir / "scripts/hygiene_common.py")
        shutil.copy(repo_scripts / "validate_generated_freshness.py", self.tempdir / "scripts/validate_generated_freshness.py")
        (self.tempdir / "generated/out.txt").write_text("ok\n", encoding="utf-8")
        (self.tempdir / "scripts/build_out.py").write_text("import sys\nsys.exit(0)\n", encoding="utf-8")
        (self.tempdir / "config/link_shape_hygiene.json").write_text(json.dumps({
            "generated_freshness": [{"output": "generated/out.txt", "builder": "scripts/build_out.py", "check_args": ["--check"], "required": True}]
        }), encoding="utf-8")

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)

    def test_generated_freshness(self) -> None:
        ok = subprocess.run([sys.executable, "scripts/validate_generated_freshness.py"], cwd=self.tempdir)
        self.assertEqual(ok.returncode, 0)
        (self.tempdir / "scripts/build_out.py").write_text("import sys\nsys.exit(7)\n", encoding="utf-8")
        bad = subprocess.run([sys.executable, "scripts/validate_generated_freshness.py"], cwd=self.tempdir, text=True, capture_output=True)
        self.assertNotEqual(bad.returncode, 0)


if __name__ == "__main__":
    unittest.main()
