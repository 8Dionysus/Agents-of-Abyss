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

## Raw source accounting

Legacy raw sources for this part are listed in `mechanics/experience/legacy/INDEX.md`. If a raw source becomes active guidance, update this part's `README.md` or `CONTRACT.md` and add a note to `mechanics/experience/legacy/DISTILLATION_LOG.md`.
