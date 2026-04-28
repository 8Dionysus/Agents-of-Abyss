from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OwnerRequestQueueTests(unittest.TestCase):
    def test_owner_request_queue_validates(self):
        module = load("validate_owner_request_queue", "scripts/validate_owner_request_queue.py")
        self.assertEqual(module.validate_queue(None), [])

    def test_owner_request_queue_generated_payload_current(self):
        builder = load("build_owner_request_queue", "scripts/build_owner_request_queue.py")
        expected = builder.dumps_min(builder.build_payload())
        actual = (ROOT / "generated/owner_request_queue.min.json").read_text(encoding="utf-8")
        self.assertEqual(actual, expected)

    def test_owner_request_queue_has_every_mechanic(self):
        builder = load("build_owner_request_queue", "scripts/build_owner_request_queue.py")
        payload = builder.build_payload()
        mechanics = {request["mechanic"] for request in payload["requests"]}
        self.assertEqual(
            mechanics,
            {"method-growth", "distillation", "growth-cycle", "recurrence", "checkpoint", "experience", "agon", "antifragility", "questbook", "rpg", "boundary-bridge", "release-support"},
        )


if __name__ == "__main__":
    unittest.main()
