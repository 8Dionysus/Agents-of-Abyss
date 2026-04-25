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
python mechanics/experience/parts/office-operations/scripts/validate_office_operations.py
python mechanics/experience/parts/office-operations/scripts/validate_office_role_pairs.py
python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_operations.py mechanics/experience/parts/office-operations/tests/test_office_operations_seed_contracts.py mechanics/experience/parts/office-operations/tests/test_office_role_pairs.py
```
