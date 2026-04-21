import subprocess
import sys


def test_agon_duel_kernel_model_registry_build_check():
    result = subprocess.run([sys.executable, 'scripts/build_agon_duel_kernel_model_registry.py', '--check'], text=True, capture_output=True)
    assert result.returncode == 0, result.stderr


def test_agon_duel_kernel_model_registry_validates():
    result = subprocess.run([sys.executable, 'scripts/validate_agon_duel_kernel_models.py'], text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
