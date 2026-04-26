from __future__ import annotations

import json
import sys
from pathlib import Path

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

REPO_ROOT = _repo_root()
SCRIPTS = (
    REPO_ROOT
    / "mechanics"
    / "agon"
    / "parts"
    / "imposition-readiness"
    / "scripts"
)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from agon_imposition_common import READINESS_PATH, build_payload, render_payload, validate_payload


def test_agon_imposition_readiness_is_canonical() -> None:
    assert READINESS_PATH.exists()
    current = READINESS_PATH.read_text(encoding="utf-8")
    assert current == render_payload(build_payload())


def test_agon_imposition_payload_validates() -> None:
    payload = json.loads(READINESS_PATH.read_text(encoding="utf-8"))
    validate_payload(payload, check_refs=False)
    assert payload["status"] == "seed"
    assert "recharter" in payload["verdicts"]
    assert any(item["owner"] == "aoa-agents" for item in payload["owner_handoffs"])
    assert all("Tree-of-Sophia" not in line or "directly" in line for line in payload["stop_lines"])
