from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = ROOT / "mechanics" / "growth-cycle" / "scripts" / "validate_growth_cycle_mechanic.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_growth_cycle_mechanic", VALIDATOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GrowthCycleMechanicTests(unittest.TestCase):
    def test_growth_cycle_package_validates(self) -> None:
        module = load_validator()
        self.assertEqual(module.validate(), [])

    def test_growth_cycle_names_all_active_parts(self) -> None:
        module = load_validator()
        parts_text = (ROOT / "mechanics" / "growth-cycle" / "PARTS.md").read_text(encoding="utf-8")
        for part in module.PARTS:
            self.assertIn(f"parts/{part}/README.md", parts_text)


if __name__ == "__main__":
    unittest.main()
