# Scripts District

This directory holds builders, validators, release checks, and local guardrails for the AoA center.

Scripts may build or validate compact surfaces. They do not create constitutional authority by themselves.

## Main families

| Family | Examples | Role |
|---|---|---|
| Center builders | `build_center_entry_map.py` | build compact center-entry surfaces |
| Center validators | `validate_center_entry_map.py`, `validate_ecosystem.py` | check center and registry contracts |
| Agon builders and validators | `build_agon_*.py`, `validate_agon_*.py` | build and check Agon pre-protocol surfaces |
| Experience validators | `validate_experience_*.py` | check staged Experience contracts |
| Release checks | `release_check.py` | guard public release posture |
| Documentation guardrails | `validate_markdown_shape.py` | protect human and agent readability of civic docs |

## Rules

- Prefer dry-run, check-only, or explicit output paths when possible.
- A builder should have a corresponding source document, schema, generated surface, validator, or test.
- A validator should state what it checks and what it does not check.
- Do not hide mutation behind a convenience script.
- Do not make a script the only place where a constitutional boundary is explained.

## Baseline checks

```bash
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_ecosystem.py
python scripts/validate_markdown_shape.py
python -m pytest -q tests
```

Run narrower or wider checks based on the touched surfaces.
