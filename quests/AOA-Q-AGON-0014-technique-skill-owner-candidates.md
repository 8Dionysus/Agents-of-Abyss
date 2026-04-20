# AOA-Q-AGON-0014: Technique and Skill Owner Candidates

## Intent

Land the companion candidate request surfaces in `aoa-techniques` and `aoa-skills`.

## Done when

- technique candidate index exists and remains requested-only;
- skill candidate index exists and remains requested-only;
- neither owner repo claims lawful move vocabulary;
- neither owner repo starts runtime arena behavior.

## Verify

In `aoa-techniques`:

```bash
python scripts/build_agon_technique_binding_candidates.py --check
python scripts/validate_agon_technique_binding_candidates.py
python -m pytest -q tests/test_agon_technique_binding_candidates.py
```

In `aoa-skills`:

```bash
python scripts/build_agon_skill_binding_candidates.py --check
python scripts/validate_agon_skill_binding_candidates.py
python -m pytest -q tests/test_agon_skill_binding_candidates.py
```
