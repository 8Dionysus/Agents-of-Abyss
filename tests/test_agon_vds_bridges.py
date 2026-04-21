from __future__ import annotations
import importlib.util, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def _load(path):
    spec=importlib.util.spec_from_file_location(path.stem,path); module=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(module); return module
def test_vds_registry_is_build_clean():
    r=subprocess.run([sys.executable,str(ROOT/'scripts'/'build_agon_vds_bridge_registry.py'),'--check'],cwd=ROOT,text=True,capture_output=True)
    assert r.returncode==0, r.stdout+r.stderr
def test_vds_registry_validates():
    data=_load(ROOT/'scripts'/'validate_agon_vds_bridges.py').validate()
    assert data['bridge_count']>=5
