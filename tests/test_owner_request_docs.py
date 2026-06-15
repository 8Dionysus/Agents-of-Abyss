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

    def test_receipt_backed_validation_requires_matching_packet_section(self):
        module = load("validate_owner_request_docs", "scripts/owner_requests/validate_owner_request_docs.py")
        text = """## Ready-to-carry packets

| Request | Status |
|---|---|
| `ORQ-FAKE-SKILLS-001` | `landed` |

### ORQ-FAKE-SKILLS-TYPO-001

Receipt-backed status: `owner_landing_ref` and `owner_proof_ref` are linked here.
"""
        problems = module.receipt_backed_packet_section_problems(
            "fake/OWNER_REQUESTS.md",
            text,
            [{"id": "ORQ-FAKE-SKILLS-001", "queue_status": "landed"}],
        )
        self.assertEqual(
            problems,
            ["fake/OWNER_REQUESTS.md: ORQ-FAKE-SKILLS-001 must have its own ready-to-carry packet section"],
        )

    def test_request_packet_body_stops_before_later_h2_sections(self):
        module = load("validate_owner_request_docs", "scripts/owner_requests/validate_owner_request_docs.py")
        text = """## Ready-to-carry packets

### ORQ-FAKE-SKILLS-001

Status: `landed`; owner receipt linked.

## Center sources

Receipt-backed status: `owner_landing_ref` and `owner_proof_ref` are generic later text.
"""
        body = module.request_packet_body(text, "ORQ-FAKE-SKILLS-001")
        self.assertIsNotNone(body)
        self.assertNotIn("## Center sources", body)
        problems = module.receipt_backed_packet_section_problems(
            "fake/OWNER_REQUESTS.md",
            text,
            [{"id": "ORQ-FAKE-SKILLS-001", "queue_status": "landed"}],
        )
        self.assertIn("fake/OWNER_REQUESTS.md: ORQ-FAKE-SKILLS-001 must distinguish its receipt-backed status", problems)
        self.assertIn("fake/OWNER_REQUESTS.md: ORQ-FAKE-SKILLS-001 must name owner_landing_ref in its packet", problems)
        self.assertIn("fake/OWNER_REQUESTS.md: ORQ-FAKE-SKILLS-001 must name owner_proof_ref in its packet", problems)

    def test_request_packet_body_stops_before_next_h3_packet(self):
        module = load("validate_owner_request_docs", "scripts/owner_requests/validate_owner_request_docs.py")
        text = """## Ready-to-carry packets

### ORQ-FAKE-SKILLS-001

Status: `landed`; owner receipt linked.

### ORQ-FAKE-SKILLS-002

Receipt-backed status: `owner_landing_ref` and `owner_proof_ref` are linked here.
"""
        body = module.request_packet_body(text, "ORQ-FAKE-SKILLS-001")
        self.assertIsNotNone(body)
        self.assertNotIn("ORQ-FAKE-SKILLS-002", body)
        problems = module.receipt_backed_packet_section_problems(
            "fake/OWNER_REQUESTS.md",
            text,
            [{"id": "ORQ-FAKE-SKILLS-001", "queue_status": "landed"}],
        )
        self.assertIn("fake/OWNER_REQUESTS.md: ORQ-FAKE-SKILLS-001 must distinguish its receipt-backed status", problems)
        self.assertIn("fake/OWNER_REQUESTS.md: ORQ-FAKE-SKILLS-001 must name owner_landing_ref in its packet", problems)
        self.assertIn("fake/OWNER_REQUESTS.md: ORQ-FAKE-SKILLS-001 must name owner_proof_ref in its packet", problems)

    def test_owner_request_protocol_declines_center_activation(self):
        text = (ROOT / "mechanics/OWNER_REQUEST_PROTOCOL.md").read_text(encoding="utf-8")
        self.assertIn("A request packet is not owner acceptance", text)
        self.assertIn("must not", text.lower())


if __name__ == "__main__":
    unittest.main()
