# Capture Kernel Validation

## Required local check

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part capture-kernel
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python mechanics/experience/parts/capture-kernel/scripts/validate_capture_kernel.py
python -m pytest -q mechanics/experience/parts/capture-kernel/tests/test_capture_kernel.py
```
