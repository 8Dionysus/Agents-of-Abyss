from __future__ import annotations

import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT / "scripts"))

from validate_boundary_bridge_distillation import validate


def test_boundary_bridge_distillation_surfaces_are_current() -> None:
    assert validate() == []
