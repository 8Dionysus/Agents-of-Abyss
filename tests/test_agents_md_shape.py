from __future__ import annotations

import subprocess
import sys
import unittest


class AgentsMdShapeTests(unittest.TestCase):
    def test_agents_md_shape_validator_passes(self):
        result = subprocess.run([sys.executable, "scripts/validate_agents_md_shape.py"], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
