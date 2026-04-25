# Adoption Federation Validation

## Required local check

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part adoption-federation
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python mechanics/experience/parts/adoption-federation/scripts/validate_adoption_federation.py
python -m pytest -q mechanics/experience/parts/adoption-federation/tests/test_adoption_federation.py
python scripts/validate_owner_request_queue.py --mechanic experience
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic experience
```
