# Office Operations Validation

## Required local check

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part office-operations
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python mechanics/experience/scripts/validate_experience_wave5.py
python mechanics/experience/scripts/validate_experience_v1_3_office_foundry_role_pairs.py
python -m pytest -q mechanics/experience/tests/test_experience_wave5.py mechanics/experience/tests/test_experience_wave5_seed_contracts.py mechanics/experience/tests/test_experience_v1_3_office_foundry_role_pairs.py
```
