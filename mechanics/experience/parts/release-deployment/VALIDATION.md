# Release Deployment Validation

## Required local check

```bash
python scripts/validate_experience_distillation.py --part release-deployment
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

run targeted deployment, installation, release, and rollback validators or tests named by the touched surface.
