from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
import unittest


class AgentsMeshTests(unittest.TestCase):
    def test_agents_mesh_validator_passes(self):
        result = subprocess.run([sys.executable, "scripts/agents_mesh/validate_agents_mesh.py"], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_mechanic_agents_refs_are_registered(self):
        config = json.loads(Path("config/agents_mesh.json").read_text(encoding="utf-8"))
        registry = json.loads(Path("mechanics/registry.json").read_text(encoding="utf-8"))
        paths = {entry["path"] for entry in config["entries"]}
        for mechanic in registry.get("mechanics", []):
            self.assertIn(mechanic["agents_ref"], paths)

    def test_local_stack_readiness_requires_items(self):
        result = subprocess.run(
            [sys.executable, ".agents/skills/aoa-local-stack-bringup/scripts/readiness_summary.py"],
            input=json.dumps({"readiness_items": []}),
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["overall"], "fail")
        self.assertEqual(payload["counts"]["fail"], 1)


if __name__ == "__main__":
    unittest.main()
