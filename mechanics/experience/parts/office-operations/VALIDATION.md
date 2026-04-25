# Office Operations Validation

## Required local check

```bash
python scripts/validate_experience_distillation.py --part office-operations
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python scripts/validate_experience_wave5.py
python scripts/validate_experience_v1_3_office_foundry_role_pairs.py
python -m pytest -q tests/test_experience_wave5.py tests/test_experience_wave5_seed_contracts.py tests/test_experience_v1_3_office_foundry_role_pairs.py
```
