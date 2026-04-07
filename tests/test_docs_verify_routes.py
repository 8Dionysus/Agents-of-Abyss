from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


class DocsVerifyRoutesTestCase(unittest.TestCase):
    def test_public_and_operator_surfaces_include_full_bounded_battery(self) -> None:
        for relative_path in (
            "README.md",
            "docs/README.md",
            "AGENTS.md",
            "docs/AGENTS.md",
            "CONTRIBUTING.md",
            "generated/AGENTS.md",
        ):
            with self.subTest(path=relative_path):
                text = read_text(relative_path)
                self.assertIn("python scripts/validate_ecosystem.py", text)
                self.assertIn("python -m pytest -q tests", text)

    def test_readme_keeps_aoa_sdk_outside_compact_registry_v1_but_routes_to_supporting_inventory(self) -> None:
        readme = read_text("README.md")
        self.assertIn("aoa-sdk", readme)
        self.assertIn("outside the compact registry v1 by design", readme)
        self.assertIn("supporting machine-readable inventory", readme)

    def test_generated_agents_keeps_registry_as_publication_surface(self) -> None:
        generated_agents = read_text("generated/AGENTS.md")
        self.assertIn("published summary surface", generated_agents)
        self.assertIn("not a hidden second charter", generated_agents)


if __name__ == "__main__":
    unittest.main()
