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

run `python scripts/validate_experience_wave5.py` and targeted office validators or seed-contract tests.
