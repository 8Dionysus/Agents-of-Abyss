from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_decision_records as decisions  # noqa: E402


class DecisionRecordTests(unittest.TestCase):
    def test_repo_decision_records_validate(self) -> None:
        self.assertEqual(decisions.validate_all(), [])

    def test_record_requires_standard_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            record = root / "2026-04-29-test-decision.md"
            record.write_text(
                "# Test Decision\n\n"
                "Status: accepted\n"
                "Date: 2026-04-29\n\n"
                "## Context\n\n"
                "A real choice exists.\n",
                encoding="utf-8",
            )

            problems = decisions.validate_record(record)

        self.assertIn(
            "2026-04-29-test-decision.md: missing section ## Options considered",
            [problem.split("docs/decisions/")[-1] for problem in problems],
        )


if __name__ == "__main__":
    unittest.main()
