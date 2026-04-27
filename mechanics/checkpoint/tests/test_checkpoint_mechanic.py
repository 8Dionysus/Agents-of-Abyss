from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "mechanics" / "checkpoint" / "scripts" / "validate_checkpoint_mechanic.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_checkpoint_mechanic", VALIDATOR_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CheckpointMechanicTests(unittest.TestCase):
    def test_checkpoint_mechanic_validates(self) -> None:
        module = load_validator()
        self.assertEqual(module.validate(), [])

    def test_expected_owner_request_ids_are_checkpoint_scoped(self) -> None:
        module = load_validator()
        self.assertTrue(module.OWNER_REQUEST_IDS)
        for request_id in module.OWNER_REQUEST_IDS:
            self.assertRegex(request_id, r"^ORQ-CHECKPOINT-[A-Z0-9]+-\d{3}$")

    def test_all_parts_have_contract_and_validation_surfaces(self) -> None:
        module = load_validator()
        for part in module.PARTS:
            part_dir = module.PACKAGE_ROOT / "parts" / part
            for file_name in module.PART_FILES:
                self.assertTrue((part_dir / file_name).is_file(), f"{part}/{file_name}")


if __name__ == "__main__":
    unittest.main()
