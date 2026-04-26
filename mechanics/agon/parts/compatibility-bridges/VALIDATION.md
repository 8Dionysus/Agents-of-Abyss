# Compatibility Bridges Validation

```bash
python mechanics/agon/parts/compatibility-bridges/scripts/build_agon_ccs_law_registry.py --check
python mechanics/agon/parts/compatibility-bridges/scripts/validate_agon_ccs_laws.py
python mechanics/agon/parts/compatibility-bridges/scripts/build_agon_slc_registry.py --check
python mechanics/agon/parts/compatibility-bridges/scripts/validate_agon_slc_registry.py
python -m pytest -q mechanics/agon/parts/compatibility-bridges/tests/test_agon_ccs_laws.py mechanics/agon/parts/compatibility-bridges/tests/test_agon_slc_registry.py
python mechanics/agon/scripts/validate_agon_distillation.py
```
