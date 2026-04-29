from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_ROOT = REPO_ROOT / "examples"
README = EXAMPLES_ROOT / "README.md"
EXEMPT_MARKDOWN = {"README.md", "AGENTS.md"}
REQUIRED_HEADINGS = (
    "## Source Surfaces",
    "## Demonstrates",
    "## Boundary",
    "## Checks",
    "## Closeout",
)


def example_markdown_paths() -> list[Path]:
    return [
        path
        for path in sorted(EXAMPLES_ROOT.rglob("*.md"))
        if path.name not in EXEMPT_MARKDOWN
    ]


class ExamplesDistrictTestCase(unittest.TestCase):
    def test_root_examples_are_indexed_by_readme(self) -> None:
        readme = README.read_text(encoding="utf-8")

        for path in example_markdown_paths():
            rel = path.relative_to(EXAMPLES_ROOT).as_posix()
            with self.subTest(example=rel):
                self.assertIn(rel, readme)

    def test_root_examples_keep_required_worked_shape(self) -> None:
        for path in example_markdown_paths():
            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(REPO_ROOT).as_posix()
            with self.subTest(example=rel):
                for heading in REQUIRED_HEADINGS:
                    self.assertIn(heading, text)
                self.assertIn("../", text)
                self.assertIn("source", text.lower())

    def test_root_examples_do_not_create_flat_mechanic_receipts(self) -> None:
        for path in example_markdown_paths():
            rel = path.relative_to(EXAMPLES_ROOT).as_posix()
            with self.subTest(example=rel):
                self.assertNotIn("/legacy/raw/", rel)
                self.assertNotIn("/parts/", rel)


if __name__ == "__main__":
    unittest.main()
