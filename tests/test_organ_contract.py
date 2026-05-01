from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class OrganContractTests(unittest.TestCase):
    def test_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_organ_contract.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_first_cycle_is_first_route_not_runtime_engine(self) -> None:
        text = (REPO_ROOT / "docs/organ-contract/FIRST_CYCLE.md").read_text(encoding="utf-8")
        self.assertIn("first route through an AbyssOS organ", text)
        self.assertIn("It is not a full lifecycle", text)
        for step in ("`intent`", "`route`", "`work`", "`proof`", "`record`", "`land`", "`handoff`"):
            self.assertIn(step, text)

    def test_contract_preserves_downstream_owners(self) -> None:
        text = (REPO_ROOT / "docs/organ-contract/README.md").read_text(encoding="utf-8")
        for owner in ("aoa-sdk", "aoa-routing", "aoa-evals", "aoa-memo", "abyss-stack", "Tree-of-Sophia"):
            self.assertIn(owner, text)


if __name__ == "__main__":
    unittest.main()
