from pathlib import Path
import importlib.util

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


def test_state_packet_registry_is_current():
    build = load_module(ROOT / "mechanics" / "agon" / "scripts" / 'build_agon_state_packet_registry.py', 'build_agon_state_packet_registry')
    seed = build.load_json(build.CONFIG)
    expected = build.build(seed)
    current = build.load_json(build.OUT)
    assert current == expected


def test_state_packet_validation():
    validate = load_module(ROOT / "mechanics" / "agon" / "scripts" / 'validate_agon_state_packets.py', 'validate_agon_state_packets')
    validate.validate()
