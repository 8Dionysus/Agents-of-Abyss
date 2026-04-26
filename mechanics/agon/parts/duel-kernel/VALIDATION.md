# Duel Kernel Validation

```bash
python mechanics/agon/scripts/build_agon_duel_kernel_model_registry.py --check
python mechanics/agon/scripts/validate_agon_duel_kernel_models.py
python mechanics/agon/scripts/build_agon_mechanical_trial_suite_registry.py --check
python mechanics/agon/scripts/validate_agon_mechanical_trial_suites.py
python -m pytest -q mechanics/agon/tests/test_agon_duel_kernel_models.py mechanics/agon/tests/test_agon_mechanical_trial_suites.py
python mechanics/agon/scripts/validate_agon_distillation.py
```
