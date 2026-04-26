# Sophian Threshold Validation

```bash
python mechanics/agon/parts/sophian-threshold/scripts/build_agon_sophian_threshold_registry.py --check
python mechanics/agon/parts/sophian-threshold/scripts/validate_agon_sophian_threshold_registry.py
python -m pytest -q mechanics/agon/parts/sophian-threshold/tests/test_agon_sophian_threshold_registry.py
python mechanics/agon/scripts/validate_agon_distillation.py
```
