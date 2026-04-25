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

```bash
python scripts/validate_experience_wave3.py
python -m pytest -q tests/test_experience_wave3.py
python scripts/validate_owner_request_queue.py --mechanic experience
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic experience
```
