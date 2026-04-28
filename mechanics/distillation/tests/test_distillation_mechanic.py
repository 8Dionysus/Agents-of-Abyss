from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = ROOT / "mechanics" / "distillation" / "scripts" / "validate_distillation_mechanic.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_distillation_mechanic", VALIDATOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DistillationMechanicTests(unittest.TestCase):
    def test_distillation_mechanic_validates(self) -> None:
        validator = load_validator()
        self.assertEqual(validator.validate(), [])


if __name__ == "__main__":
    unittest.main()
