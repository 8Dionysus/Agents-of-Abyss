from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SPARK_ROOT = REPO_ROOT / "Spark"
REGISTRY = SPARK_ROOT / "registry.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class SparkLaneTestCase(unittest.TestCase):
    def test_spark_lane_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "Spark/scripts/validate_spark_lane.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_every_scenario_is_registered(self) -> None:
        registry = load_json(REGISTRY)
        registered = {scenario["path"] for scenario in registry["scenarios"]}
        discovered = {
            path.relative_to(REPO_ROOT).as_posix()
            for path in (SPARK_ROOT / "scenarios").iterdir()
            if path.is_dir()
        }
        self.assertEqual(registered, discovered)

    def test_unregistered_scenario_directory_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            shutil.copytree(
                SPARK_ROOT,
                temp_root / "Spark",
                ignore=shutil.ignore_patterns("__pycache__"),
            )
            (temp_root / "scripts").mkdir()
            (temp_root / "scripts/release_check.py").write_text(
                "Spark/scripts/validate_spark_lane.py\n",
                encoding="utf-8",
            )
            extra = temp_root / "Spark/scenarios/unregistered"
            (extra / "templates").mkdir(parents=True)
            (extra / "examples").mkdir(parents=True)
            (extra / "README.md").write_text("# Extra\n", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "Spark/scripts/validate_spark_lane.py",
                    "--repo-root",
                    str(temp_root),
                ],
                cwd=temp_root,
                check=False,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("Spark scenarios missing from registry", result.stdout)
        self.assertIn("Spark/scenarios/unregistered", result.stdout)

    def test_templates_have_done_or_handoff_shape(self) -> None:
        registry = load_json(REGISTRY)
        for scenario in registry["scenarios"]:
            result_template = REPO_ROOT / scenario["result_template_ref"]
            handoff_template = REPO_ROOT / scenario["handoff_template_ref"]
            self.assertIn("Status: done", result_template.read_text(encoding="utf-8"))
            self.assertIn("Status: handoff", handoff_template.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
