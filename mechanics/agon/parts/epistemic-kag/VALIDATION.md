# Epistemic KAG Validation

```bash
python mechanics/agon/scripts/build_agon_epistemic_agon_registry.py --check
python mechanics/agon/scripts/validate_agon_epistemic_agon.py
python mechanics/agon/scripts/build_agon_kag_promotion_path_registry.py --check
python mechanics/agon/scripts/validate_agon_kag_promotion_path_registry.py
python -m pytest -q mechanics/agon/tests/test_agon_epistemic_agon.py mechanics/agon/tests/test_agon_kag_promotion_path_registry.py
python mechanics/agon/scripts/validate_agon_distillation.py
```
