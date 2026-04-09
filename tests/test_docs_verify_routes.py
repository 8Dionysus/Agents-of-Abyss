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

    def test_readme_and_public_support_posture_expose_center_entry_capsule(self) -> None:
        readme = read_text("README.md")
        posture = read_text("docs/PUBLIC_SUPPORT_POSTURE.md")

        self.assertIn("generated/center_entry_map.min.json", readme)
        self.assertIn("python scripts/build_center_entry_map.py --check", readme)
        self.assertIn("python scripts/validate_center_entry_map.py", readme)
        self.assertIn("generated/center_entry_map.min.json", posture)
        self.assertIn("python scripts/build_center_entry_map.py --check", posture)
        self.assertIn("python scripts/validate_center_entry_map.py", posture)


if __name__ == "__main__":
    unittest.main()
