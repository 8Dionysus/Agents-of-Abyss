from __future__ import annotations
import subprocess, sys
from pathlib import Path

def test_agon_recurrence_adapter_request_validates():
    root = next(
        candidate
        for candidate in Path(__file__).resolve().parents
        if (candidate / "mechanics" / "registry.json").is_file()
    )
    result = subprocess.run(
        [sys.executable, "mechanics/agon/parts/recurrence-adapter/scripts/validate_agon_recurrence_adapter_request.py"],
        cwd=root,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
