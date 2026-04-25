# Capture Kernel Validation

## Required local check

```bash
python scripts/validate_experience_distillation.py --part capture-kernel
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

run `python scripts/validate_experience_wave1.py` and `python -m pytest -q tests/test_experience_wave1.py` for the Wave 1 kernel; run the distillation validator after part-surface moves.
