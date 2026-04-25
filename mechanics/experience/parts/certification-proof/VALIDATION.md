# Certification Proof Validation

## Required local check

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part certification-proof
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python mechanics/experience/parts/certification-proof/scripts/validate_certification_proof.py
python -m pytest -q mechanics/experience/parts/certification-proof/tests/test_certification_proof.py
```
