# Adoption Federation Validation

## Required local check

```bash
python scripts/validate_experience_distillation.py --part adoption-federation
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

run `python scripts/validate_experience_wave3.py`, owner-request validators, and generated queue checks.
