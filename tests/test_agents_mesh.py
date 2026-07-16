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

    def test_recurrence_parts_agents_ref_is_registered(self):
        config = json.loads(Path("config/agents_mesh.json").read_text(encoding="utf-8"))
        paths = {entry["path"] for entry in config["entries"]}
        self.assertIn("mechanics/recurrence/parts/AGENTS.md", paths)

if __name__ == "__main__":
    unittest.main()
