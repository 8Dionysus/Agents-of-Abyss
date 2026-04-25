from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class MarkdownShapeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = Path(tempfile.mkdtemp())
        (self.tempdir / "config").mkdir()
        (self.tempdir / "config/link_shape_hygiene.json").write_text(json.dumps({
            "markdown_shape": {
                "default_max_line_length": 20,
                "default_min_lines": 1,
                "targets": [{"path": "README.md", "required": True, "min_lines": 2, "max_line_length": 40, "require_h1": True, "require_h2": True}]
            }
        }), encoding="utf-8")
        scripts = self.tempdir / "scripts"
        scripts.mkdir()
        repo_scripts = Path(__file__).resolve().parents[1] / "scripts"
        shutil.copy(repo_scripts / "hygiene_common.py", scripts / "hygiene_common.py")
        shutil.copy(repo_scripts / "validate_markdown_shape.py", scripts / "validate_markdown_shape.py")

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)

    def test_shape_passes_and_fails(self) -> None:
        (self.tempdir / "README.md").write_text("# Root\n\n## Gate\n", encoding="utf-8")
        ok = subprocess.run([sys.executable, "scripts/validate_markdown_shape.py"], cwd=self.tempdir)
        self.assertEqual(ok.returncode, 0)
        (self.tempdir / "README.md").write_text("# Root\n", encoding="utf-8")
        bad = subprocess.run([sys.executable, "scripts/validate_markdown_shape.py"], cwd=self.tempdir, text=True, capture_output=True)
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("missing second-level heading", bad.stdout)


if __name__ == "__main__":
    unittest.main()
