# Compatibility Bridges Validation

## Required local check

```bash
python scripts/validate_experience_distillation.py --part compatibility-bridges
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python scripts/validate_experience_v1_2_to_v2_0_bridge.py
python scripts/validate_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py
python scripts/validate_experience_v1_5_epistemic_duel_model_of_other_forge.py
python -m pytest -q tests/test_experience_v1_2_to_v2_0_bridge.py tests/test_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py tests/test_experience_v1_5_epistemic_duel_model_of_other_forge.py
```
