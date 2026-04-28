from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class HygieneIndexTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = Path(tempfile.mkdtemp())
        for rel in ["config", "docs", "generated", "scripts"]:
            (self.tempdir / rel).mkdir()
        (self.tempdir / "docs/guardrails").mkdir()
        repo = Path(__file__).resolve().parents[1]
        for script in ["hygiene_common.py", "build_link_shape_hygiene_index.py", "validate_link_shape_hygiene_index.py"]:
            shutil.copy(repo / "scripts" / script, self.tempdir / "scripts" / script)
        (self.tempdir / "docs/guardrails/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md").write_text("# Protocol\n\n## Gate\n", encoding="utf-8")
        (self.tempdir / "docs/guardrails/HYGIENE_GUARDRAIL_INDEX.md").write_text("# Index\n\n## Gate\n", encoding="utf-8")
        (self.tempdir / "config/link_shape_hygiene.json").write_text(json.dumps({
            "purpose": "test",
            "protocol_ref": "docs/guardrails/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md",
            "index_ref": "docs/guardrails/HYGIENE_GUARDRAIL_INDEX.md",
            "link_validation": {"known_rewrites": [{"id": "x"}]},
            "status_vocabulary": {"hygiene_status": ["active"]},
            "generated_freshness": [],
            "validation_commands": []
        }), encoding="utf-8")

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)

    def test_build_and_validate(self) -> None:
        build = subprocess.run([sys.executable, "scripts/build_link_shape_hygiene_index.py"], cwd=self.tempdir)
        self.assertEqual(build.returncode, 0)
        check = subprocess.run([sys.executable, "scripts/build_link_shape_hygiene_index.py", "--check"], cwd=self.tempdir)
        self.assertEqual(check.returncode, 0)
        valid = subprocess.run([sys.executable, "scripts/validate_link_shape_hygiene_index.py"], cwd=self.tempdir)
        self.assertEqual(valid.returncode, 0)


if __name__ == "__main__":
    unittest.main()
