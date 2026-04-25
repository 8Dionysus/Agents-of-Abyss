# Governance Polis Validation

## Required local check

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part governance-polis
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python mechanics/experience/parts/governance-polis/scripts/validate_governance_polis.py
python -m pytest -q mechanics/experience/parts/governance-polis/tests/test_governance_polis.py mechanics/experience/parts/governance-polis/tests/test_governance_polis_seed_contracts.py
```
