from __future__ import annotations

import json
import copy
import subprocess
import sys
import unittest
from pathlib import Path

from scripts.mechanics_topology.validate_mechanics_topology import validate_registry_shape

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
CANONICAL_SLUGS = (
    "method-growth",
    "distillation",
    "growth-cycle",
    "recurrence",
    "checkpoint",
    "experience",
    "agon",
    "antifragility",
    "questbook",
    "rpg",
    "boundary-bridge",
    "audit",
    "release-support",
)


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=REPO_ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


class MechanicsTopologyTests(unittest.TestCase):
    def _agon_registry(self) -> dict:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        return copy.deepcopy(registry)

    def _docs_path_problems(self, value: object, *, omit: bool = False) -> list[str]:
        registry = self._agon_registry()
        entry = next(item for item in registry["mechanics"] if item["slug"] == "agon")
        if omit:
            entry.pop("docs_path", None)
        else:
            entry["docs_path"] = value
        return validate_registry_shape(registry, {"agon"})

    def test_omitted_docs_path_is_allowed(self) -> None:
        self.assertFalse(any("docs_path" in problem for problem in self._docs_path_problems(None, omit=True)))

    def test_declared_docs_path_rejects_null_empty_non_string_wrong_and_missing(self) -> None:
        for value in (None, "", [], "mechanics/experience/docs", "mechanics/agon/missing"):
            with self.subTest(value=value):
                problems = self._docs_path_problems(value)
                self.assertTrue(any("docs_path" in problem for problem in problems))

    def test_missing_canonical_source_remains_rejected(self) -> None:
        registry = self._agon_registry()
        entry = next(item for item in registry["mechanics"] if item["slug"] == "agon")
        entry["canonical_docs"][0] = "mechanics/agon/MISSING.md"
        problems = validate_registry_shape(registry, {"agon"})
        self.assertTrue(any("canonical_docs" in problem and "missing" in problem for problem in problems))

    def test_mechanics_registry_has_canonical_slug_set_and_order(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        slugs = tuple(entry["slug"] for entry in registry["mechanics"])
        self.assertEqual(slugs, CANONICAL_SLUGS)

    def test_every_mechanic_package_has_required_entry_surfaces(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        for entry in registry["mechanics"]:
            package = REPO_ROOT / entry["package_path"]
            self.assertTrue((package / "AGENTS.md").exists())
            self.assertTrue((package / "README.md").exists())
            self.assertTrue((package / "ROADMAP.md").exists())
            self.assertTrue((package / "LANDING_LOG.md").exists())
            docs_path = entry.get("docs_path")
            if docs_path:
                self.assertTrue((REPO_ROOT / docs_path).is_dir())

    def test_mechanics_topology_validator_accepts_all_mechanics(self) -> None:
        result = run_script("scripts/mechanics_topology/validate_mechanics_topology.py")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_no_flat_agon_experience_or_rpg_docs_remain(self) -> None:
        docs = REPO_ROOT / "docs"
        self.assertFalse(list(docs.glob("AGON_*.md")))
        self.assertFalse(list(docs.glob("EXPERIENCE_*.md")))
        self.assertFalse(list(docs.glob("RPG_*.md")))

    def test_fragility_blacklist_is_mechanic_owned(self) -> None:
        self.assertFalse((REPO_ROOT / "FRAGILITY_BLACKLIST.md").exists())
        self.assertTrue((REPO_ROOT / "mechanics" / "antifragility" / "FRAGILITY_BLACKLIST.md").exists())


if __name__ == "__main__":
    unittest.main()
