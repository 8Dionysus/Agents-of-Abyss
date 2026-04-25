# Service Mesh Validation

## Required local check

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part service-mesh
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python mechanics/experience/parts/service-mesh/scripts/validate_service_mesh.py
python -m pytest -q mechanics/experience/parts/service-mesh/tests/test_service_mesh.py
```
