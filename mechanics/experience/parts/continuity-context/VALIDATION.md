# Continuity Context Validation

## Required local check

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part continuity-context
```

## Mechanic checks

```bash
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

## Targeted checks

```bash
python mechanics/experience/parts/continuity-context/scripts/validate_memory_rank_reputation.py
python mechanics/experience/parts/continuity-context/scripts/validate_affective_economy.py
python mechanics/experience/parts/continuity-context/scripts/validate_context_routing.py
python mechanics/experience/parts/continuity-context/scripts/validate_context_memory_weaving.py
python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_memory_rank_reputation.py mechanics/experience/parts/continuity-context/tests/test_affective_economy.py mechanics/experience/parts/continuity-context/tests/test_context_routing.py mechanics/experience/parts/continuity-context/tests/test_context_memory_weaving.py
```
