from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
import unittest


class AgentsMeshIndexTests(unittest.TestCase):
    def test_generated_agents_mesh_index_is_current(self):
        build = subprocess.run([sys.executable, "scripts/agents_mesh/build_agents_mesh_index.py", "--check"], text=True, capture_output=True)
        self.assertEqual(build.returncode, 0, build.stdout + build.stderr)
        validate = subprocess.run([sys.executable, "scripts/agents_mesh/validate_agents_mesh_index.py"], text=True, capture_output=True)
        self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)

    def test_generated_agents_mesh_index_has_cards(self):
        data = json.loads(Path("generated/agents_mesh.min.json").read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"], "aoa_agents_mesh_index_v2")
        self.assertGreaterEqual(data["card_count"], 30)
        self.assertFalse(data["missing_cards"])
        self.assertEqual(data["chain_budget_bytes"], 32768)
        self.assertFalse(data["chains_over_budget"])
        self.assertLessEqual(data["chain_max_bytes"], data["chain_budget_bytes"])

    def test_generated_agents_mesh_index_includes_recurrence_parts_card(self):
        data = json.loads(Path("generated/agents_mesh.min.json").read_text(encoding="utf-8"))
        paths = {card["path"] for card in data["cards"]}
        self.assertIn("mechanics/recurrence/parts/AGENTS.md", paths)


if __name__ == "__main__":
    unittest.main()
