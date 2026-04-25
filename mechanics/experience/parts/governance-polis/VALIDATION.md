# Governance Polis Validation

## Required local check

```bash
python scripts/validate_experience_distillation.py --part governance-polis
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python scripts/validate_experience_wave4.py
python -m pytest -q tests/test_experience_wave4.py tests/test_experience_wave4_seed_contracts.py
```
