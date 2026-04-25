from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class ValidateLinksTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = Path(tempfile.mkdtemp())
        (self.tempdir / "config").mkdir()
        (self.tempdir / "docs").mkdir()
        (self.tempdir / "config/link_shape_hygiene.json").write_text(json.dumps({
            "link_validation": {"scan_globs": ["**/*.md"], "exclude_globs": [], "ignore_schemes": ["http", "https", "mailto", "tel", "data"]}
        }), encoding="utf-8")
        scripts = self.tempdir / "scripts"
        scripts.mkdir()
        repo_scripts = Path(__file__).resolve().parents[1] / "scripts"
        shutil.copy(repo_scripts / "hygiene_common.py", scripts / "hygiene_common.py")
        shutil.copy(repo_scripts / "validate_links.py", scripts / "validate_links.py")

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)

    def run_validator(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, "scripts/validate_links.py"], cwd=self.tempdir, text=True, capture_output=True)

    def test_valid_local_link_passes(self) -> None:
        (self.tempdir / "README.md").write_text("# Root\n\n[Docs](docs/README.md)\n", encoding="utf-8")
        (self.tempdir / "docs/README.md").write_text("# Docs\n", encoding="utf-8")
        self.assertEqual(self.run_validator().returncode, 0)

    def test_broken_local_link_fails(self) -> None:
        (self.tempdir / "README.md").write_text("# Root\n\n[Missing](docs/MISSING.md)\n", encoding="utf-8")
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("broken local", result.stdout)


if __name__ == "__main__":
    unittest.main()
