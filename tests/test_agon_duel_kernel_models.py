import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _load_script(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_agon_duel_kernel_model_registry_build_check():
    result = subprocess.run([sys.executable, 'scripts/build_agon_duel_kernel_model_registry.py', '--check'], text=True, capture_output=True)
    assert result.returncode == 0, result.stderr


def test_agon_duel_kernel_model_registry_validates():
    result = subprocess.run([sys.executable, 'scripts/validate_agon_duel_kernel_models.py'], text=True, capture_output=True)
    assert result.returncode == 0, result.stderr


def test_agon_duel_kernel_model_registry_rejects_repeated_earlier_phase(tmp_path: Path):
    validator = _load_script(ROOT / "scripts" / "validate_agon_duel_kernel_models.py")
    registry = json.loads(
        (
            ROOT / "generated" / "agon_duel_kernel_model_registry.min.json"
        ).read_text(encoding="utf-8")
    )
    registry["kernels"][0]["event_sequence"].append("kernel.commit_phase_opened")

    registry_path = tmp_path / "agon_duel_kernel_model_registry.min.json"
    registry_path.write_text(json.dumps(registry), encoding="utf-8")
    validator.REG = registry_path

    assert validator.main() == 1
