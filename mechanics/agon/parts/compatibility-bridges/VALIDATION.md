# Compatibility Bridges Validation

```bash
python mechanics/agon/scripts/build_agon_ccs_law_registry.py --check
python mechanics/agon/scripts/validate_agon_ccs_laws.py
python mechanics/agon/scripts/build_agon_slc_registry.py --check
python mechanics/agon/scripts/validate_agon_slc_registry.py
python -m pytest -q mechanics/agon/tests/test_agon_ccs_laws.py mechanics/agon/tests/test_agon_slc_registry.py
python mechanics/agon/scripts/validate_agon_distillation.py
```
