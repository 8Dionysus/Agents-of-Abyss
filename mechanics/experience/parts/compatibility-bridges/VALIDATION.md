# Compatibility Bridges Validation

## Required local check

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part compatibility-bridges
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python mechanics/experience/parts/runtime-boundary/scripts/validate_runtime_boundary_bridge.py
python mechanics/experience/parts/compatibility-bridges/scripts/validate_agonic_pair_trials_bridge.py
python mechanics/experience/parts/compatibility-bridges/scripts/validate_epistemic_duel_bridge.py
python -m pytest -q mechanics/experience/parts/runtime-boundary/tests/test_runtime_boundary_bridge.py mechanics/experience/parts/compatibility-bridges/tests/test_agonic_pair_trials_bridge.py mechanics/experience/parts/compatibility-bridges/tests/test_epistemic_duel_bridge.py
```
