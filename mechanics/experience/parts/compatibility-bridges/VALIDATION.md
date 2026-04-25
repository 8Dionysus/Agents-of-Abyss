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

run the validator named by the bridge surface plus `python scripts/validate_mechanic_landing_logs.py --mechanic experience`.
