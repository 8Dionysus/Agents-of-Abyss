# Runtime Boundary Validation

## Required local check

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part runtime-boundary
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python mechanics/experience/scripts/validate_experience_v2_0_living_workspace_continuity_runtime.py
python -m pytest -q mechanics/experience/tests/test_experience_v2_0_living_workspace_continuity_runtime.py
```
