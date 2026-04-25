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


class OwnerRequestDocTests(unittest.TestCase):
    def test_owner_request_docs_validate(self):
        module = load("validate_owner_request_docs", "scripts/validate_owner_request_docs.py")
        self.assertEqual(module.validate_docs(None), [])

    def test_owner_request_protocol_declines_center_activation(self):
        text = (ROOT / "mechanics/OWNER_REQUEST_PROTOCOL.md").read_text(encoding="utf-8")
        self.assertIn("A request packet is not owner acceptance", text)
        self.assertIn("must not", text.lower())


if __name__ == "__main__":
    unittest.main()
