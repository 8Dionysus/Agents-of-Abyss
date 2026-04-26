# Epistemic KAG Validation

```bash
python mechanics/agon/parts/epistemic-kag/scripts/build_agon_epistemic_agon_registry.py --check
python mechanics/agon/parts/epistemic-kag/scripts/validate_agon_epistemic_agon.py
python mechanics/agon/parts/epistemic-kag/scripts/build_agon_kag_promotion_path_registry.py --check
python mechanics/agon/parts/epistemic-kag/scripts/validate_agon_kag_promotion_path_registry.py
python -m pytest -q mechanics/agon/parts/epistemic-kag/tests/test_agon_epistemic_agon.py mechanics/agon/parts/epistemic-kag/tests/test_agon_kag_promotion_path_registry.py
python mechanics/agon/scripts/validate_agon_distillation.py
```
