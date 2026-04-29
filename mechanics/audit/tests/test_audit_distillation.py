from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


class AuditDistillationTest(unittest.TestCase):
    def test_audit_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "mechanics/audit/scripts/validate_audit_distillation.py"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
