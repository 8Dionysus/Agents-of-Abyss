from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from scripts.hygiene import validate_generated_freshness as freshness
from scripts.hygiene import validate_hygiene_suite as hygiene_suite
from scripts.release_gate.release_check import COMMANDS as RELEASE_COMMANDS


REPO_ROOT = Path(__file__).resolve().parents[1]


def normalized(command: list[str] | tuple[str, ...]) -> tuple[str, ...]:
    parts = list(command)
    if parts and Path(parts[0]).name.startswith("python"):
        parts[0] = "python"
    return tuple(parts)


def run_freshness(
    first_args: list[str],
    second_args: list[str],
    *,
    returncode: int = 0,
) -> tuple[list[str], list[tuple[str, ...]]]:
    with tempfile.TemporaryDirectory() as tempdir:
        root = Path(tempdir)
        for rel in ["config", "generated", "scripts"]:
            (root / rel).mkdir(parents=True)
        (root / "scripts/build_out.py").write_text("", encoding="utf-8")
        entries = []
        for name, args in [("out-a.txt", first_args), ("out-b.txt", second_args)]:
            (root / "generated" / name).write_text("ok\n", encoding="utf-8")
            entries.append({
                "output": f"generated/{name}",
                "builder": "scripts/build_out.py",
                "check_args": args,
                "required": True,
            })
        (root / "config/link_shape_hygiene.json").write_text(
            json.dumps({"generated_freshness": entries}),
            encoding="utf-8",
        )
        calls: list[tuple[str, ...]] = []

        def fake_run(command: tuple[str, ...], **_kwargs: object) -> subprocess.CompletedProcess[str]:
            calls.append(command)
            return subprocess.CompletedProcess(
                command,
                returncode,
                stdout="",
                stderr="shared builder stale\n" if returncode else "",
            )

        with patch.object(freshness.subprocess, "run", side_effect=fake_run):
            return freshness.validate(root), calls


class GeneratedFreshnessTest(unittest.TestCase):
    def test_groups_only_identical_commands_and_reports_all_outputs(self) -> None:
        problems, calls = run_freshness(["--check"], ["--check"])
        self.assertEqual(problems, [])
        self.assertEqual(len(calls), 1)

        problems, calls = run_freshness(["--alpha"], ["--beta"])
        self.assertEqual(problems, [])
        self.assertEqual([command[-1] for command in calls], ["--alpha", "--beta"])

        problems, calls = run_freshness(["--check"], ["--check"], returncode=7)
        self.assertEqual(len(calls), 1)
        self.assertEqual(len(problems), 1)
        self.assertIn("generated/out-a.txt, generated/out-b.txt", problems[0])
        self.assertIn("scripts/build_out.py", problems[0])
        self.assertIn("shared builder stale", problems[0])

    def test_release_owns_every_leaf_without_wrapper_reentry(self) -> None:
        release = [normalized(command) for _label, command in RELEASE_COMMANDS]
        self.assertEqual(len(release), 59)
        self.assertEqual(len(release), len(set(release)))

        expected_suite = [
            ["scripts/hygiene/repair_known_link_drifts.py", "--check"],
            ["scripts/hygiene/validate_links.py"],
            ["scripts/hygiene/validate_markdown_shape.py"],
            ["scripts/hygiene/validate_status_vocabulary.py"],
            ["scripts/hygiene/validate_generated_freshness.py"],
            ["scripts/hygiene/validate_link_shape_hygiene_index.py"],
        ]
        self.assertEqual(hygiene_suite.COMMANDS, expected_suite)
        release_paths = [command[1] for command in release]
        self.assertNotIn("scripts/hygiene/validate_hygiene_suite.py", release_paths)
        self.assertNotIn("scripts/hygiene/validate_generated_freshness.py", release_paths)

        direct_suite_leaves = {
            normalized([sys.executable, *command])
            for command in expected_suite
            if command[0] != "scripts/hygiene/validate_generated_freshness.py"
        }
        config = json.loads((REPO_ROOT / "config/link_shape_hygiene.json").read_text(encoding="utf-8"))
        freshness_leaves = {
            normalized([sys.executable, entry["builder"], *entry.get("check_args", ["--check"])])
            for entry in config["generated_freshness"]
        }
        self.assertLessEqual(direct_suite_leaves | freshness_leaves, set(release))

        labels = [label for label, _command in RELEASE_COMMANDS]
        self.assertLess(labels.index("check docs thematic index"), labels.index("validate docs thematic index"))
        self.assertLess(labels.index("check link-shape hygiene index"), labels.index("validate link-shape hygiene index"))

    def test_hygiene_suite_runs_later_checks_after_failure(self) -> None:
        seen: list[str] = []

        def fake_run(command: list[str], **_kwargs: object) -> subprocess.CompletedProcess[str]:
            seen.append(" ".join(command[1:]))
            failed = command[1].endswith("validate_markdown_shape.py")
            return subprocess.CompletedProcess(
                command,
                9 if failed else 0,
                stdout="",
                stderr="focused markdown failure\n" if failed else "",
            )

        stdout, stderr = StringIO(), StringIO()
        with patch.object(hygiene_suite.subprocess, "run", side_effect=fake_run):
            with redirect_stdout(stdout), redirect_stderr(stderr):
                returncode = hygiene_suite.main()

        self.assertEqual(returncode, 1)
        self.assertEqual(seen, [" ".join(command) for command in hygiene_suite.COMMANDS])
        self.assertIn("focused markdown failure", stdout.getvalue() + stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
