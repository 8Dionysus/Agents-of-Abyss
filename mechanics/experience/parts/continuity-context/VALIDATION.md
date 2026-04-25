# Continuity Context Validation

## Required local check

```bash
python scripts/validate_experience_distillation.py --part continuity-context
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

run v1.6 through v1.9 validators and tests for memory, affect, context routing, and continuity loom surfaces.
