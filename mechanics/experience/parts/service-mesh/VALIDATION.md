# Service Mesh Validation

## Required local check

```bash
python scripts/validate_experience_distillation.py --part service-mesh
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python scripts/validate_experience_v1_2_service_mesh_operations.py
python -m pytest -q tests/test_experience_v1_2_service_mesh_operations.py
```
