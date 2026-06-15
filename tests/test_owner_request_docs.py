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
        module = load("validate_owner_request_docs", "scripts/owner_requests/validate_owner_request_docs.py")
        self.assertEqual(module.validate_docs(None), [])

    def test_receipt_backed_validation_is_packet_scoped(self):
        module = load("validate_owner_request_docs", "scripts/owner_requests/validate_owner_request_docs.py")
        text = """## Ready-to-carry packets

### ORQ-FAKE-REQUESTED-001

Status: `requested`, not accepted.

Return receipt: update `owner_landing_ref` or `owner_proof_ref` after a receipt exists.

### ORQ-FAKE-SKILLS-001

Status: `landed`; owner receipt linked.
"""
        problems = module.receipt_backed_packet_section_problems(
            "fake/OWNER_REQUESTS.md",
            text,
            [{"id": "ORQ-FAKE-SKILLS-001", "queue_status": "landed"}],
        )
        self.assertIn("fake/OWNER_REQUESTS.md: ORQ-FAKE-SKILLS-001 must distinguish its receipt-backed status", problems)
        self.assertIn("fake/OWNER_REQUESTS.md: ORQ-FAKE-SKILLS-001 must name owner_landing_ref in its packet", problems)
        self.assertIn("fake/OWNER_REQUESTS.md: ORQ-FAKE-SKILLS-001 must name owner_proof_ref in its packet", problems)

        fixed = text + "\nReceipt-backed status: `owner_landing_ref` and `owner_proof_ref` are linked here.\n"
        self.assertEqual(
            module.receipt_backed_packet_section_problems(
                "fake/OWNER_REQUESTS.md",
                fixed,
                [{"id": "ORQ-FAKE-SKILLS-001", "queue_status": "landed"}],
            ),
            [],
        )

    def test_owner_request_protocol_declines_center_activation(self):
        text = (ROOT / "mechanics/OWNER_REQUEST_PROTOCOL.md").read_text(encoding="utf-8")
        self.assertIn("A request packet is not owner acceptance", text)
        self.assertIn("must not", text.lower())


if __name__ == "__main__":
    unittest.main()
