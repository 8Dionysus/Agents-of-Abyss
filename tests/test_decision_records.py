from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.docs_districts import validate_decision_records as decisions  # noqa: E402


class DecisionRecordTests(unittest.TestCase):
    def test_repo_decision_records_validate(self) -> None:
        self.assertEqual(decisions.validate_all(), [])

    def test_record_requires_standard_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            record = root / "AOA-CENTER-D-9999-test-decision.md"
            record.write_text(
                "# Test Decision\n\n"
                "- Decision ID: AOA-CENTER-D-9999\n\n"
                "## Status\n\n"
                "Accepted.\n\n"
                "## Index Metadata\n\n"
                "- Original date: 2026-04-29\n"
                "- Surface classes: decision record\n"
                "- Center facets: decision index\n"
                "- Mechanic parents: none\n"
                "- Guard families: decision index/read-model\n"
                "- Posture: accepted\n\n"
                "## Context\n\n"
                "A real choice exists.\n",
                encoding="utf-8",
            )

            problems = decisions.validate_record(record)

        self.assertIn(
            "AOA-CENTER-D-9999-test-decision.md: missing section ## Options considered",
            [problem.split("docs/decisions/")[-1] for problem in problems],
        )

    def test_metadata_and_sections_must_be_in_canonical_positions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            record = root / "AOA-CENTER-D-9999-test-decision.md"
            record.write_text(
                "# Test Decision\n\n"
                "## Context\n\n"
                "- Decision ID: AOA-CENTER-D-9999\n"
                "## Status\n\n"
                "Accepted.\n\n"
                "Options considered were real.\n"
                "Decision: chosen.\n"
                "Consequences: known.\n",
                encoding="utf-8",
            )

            problems = [problem.split("docs/decisions/")[-1] for problem in decisions.validate_record(record)]

        self.assertIn(
            "AOA-CENTER-D-9999-test-decision.md: missing top metadata '- Decision ID: AOA-CENTER-D-####'",
            problems,
        )
        self.assertIn("AOA-CENTER-D-9999-test-decision.md: missing section ## Index Metadata", problems)
        self.assertIn("AOA-CENTER-D-9999-test-decision.md: missing section ## Options considered", problems)


if __name__ == "__main__":
    unittest.main()
