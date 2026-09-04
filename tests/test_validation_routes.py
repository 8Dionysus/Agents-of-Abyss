from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = REPO_ROOT / "mechanics" / "validation-routes.json"


class ValidationRoutesTests(unittest.TestCase):
    def test_manifest_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/mechanics_topology/validate_validation_routes.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_migrated_routes_preserve_command_coverage(self) -> None:
        self.skipTest("retired legacy route inventory")
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"], "aoa_mechanics_validation_routes_v1")
        self.assertGreaterEqual(len(data["routes"]), 63)
        command_count = sum(len(route["commands"]) for route in data["routes"].values())
        self.assertGreaterEqual(command_count, 405)

    def test_rpg_owner_request_uses_its_nearest_package_card(self) -> None:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        route = data["routes"]["mechanics/rpg/OWNER_REQUESTS.md"]
        self.assertEqual(route["owner_card"], "mechanics/rpg/AGENTS.md")

    def test_show_is_an_inspection_only_route(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "scripts/mechanics_topology/run_validation_route.py",
                "--surface",
                "mechanics/rpg/OWNER_REQUESTS.md",
                "--show",
            ],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("owner card: mechanics/rpg/AGENTS.md", result.stdout)
        self.assertIn("validate_owner_request_queue.py --mechanic rpg", result.stdout)
        self.assertNotIn("[ok]", result.stdout)

    def test_legacy_inline_route_markers_are_absent(self) -> None:
        for card in (REPO_ROOT / "mechanics").glob("**/AGENTS.md"):
            text = card.read_text(encoding="utf-8")
            self.assertNotIn("centralized-child-validation", text, card.as_posix())

    def test_manifest_keyed_validation_surfaces_use_direct_runner_routes(self) -> None:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        for surface in data["routes"]:
            if not surface.endswith("VALIDATION.md"):
                continue
            text = (REPO_ROOT / surface).read_text(encoding="utf-8")
            self.assertIn("mechanics/validation-routes.json", text, surface)
            self.assertIn(
                f"run_validation_route.py --surface {surface} --show", text, surface
            )
            self.assertIn(
                f"run_validation_route.py --surface {surface}", text, surface
            )
            self.assertNotRegex(text, r"AGENTS\.md#(?:validation|verify)", surface)

    def test_active_route_residue_guard_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/mechanics_topology/validate_validation_routes.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)


if __name__ == "__main__":
    unittest.main()
