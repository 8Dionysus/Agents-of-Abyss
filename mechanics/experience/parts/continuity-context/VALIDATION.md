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
python mechanics/experience/scripts/validate_experience_v1_6_epistemic_memory_rank_reputation_engine.py
python mechanics/experience/scripts/validate_experience_v1_7_affective_economy_honor_treasury.py
python mechanics/experience/scripts/validate_experience_v1_8_context_routing_nervous_system.py
python mechanics/experience/scripts/validate_experience_v1_9_context_memory_weaving_continuity_loom.py
python -m pytest -q mechanics/experience/tests/test_experience_v1_6_epistemic_memory_rank_reputation_engine.py mechanics/experience/tests/test_experience_v1_7_affective_economy_honor_treasury.py mechanics/experience/tests/test_experience_v1_8_context_routing_nervous_system.py mechanics/experience/tests/test_experience_v1_9_context_memory_weaving_continuity_loom.py
```
