import importlib.util
from pathlib import Path

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()


def _load_script(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_ccs_registry_is_current():
    builder = _load_script(ROOT / "mechanics" / "agon" / "parts" / "compatibility-bridges" / "scripts" / "build_agon_ccs_law_registry.py")
    seed = builder.load_json(ROOT / "mechanics" / "agon" / "parts" / "compatibility-bridges" / "config" / "agon_ccs_laws.seed.json")
    expected = builder.build(seed)
    current = builder.load_json(ROOT / "mechanics" / "agon" / "parts" / "compatibility-bridges" / "generated" / "agon_ccs_law_registry.min.json")
    assert current == expected


def test_ccs_laws_validate():
    validator = _load_script(ROOT / "mechanics" / "agon" / "parts" / "compatibility-bridges" / "scripts" / "validate_agon_ccs_laws.py")
    validator.validate()
