# AOA-Q-AGON-0010 — Lawful Move Language

## Intent

Land the first center-owned pre-protocol vocabulary of Agon lawful moves.

## Owner

`Agents-of-Abyss`

## Scope

- Add `mechanics/agon/config/agon_lawful_moves.seed.json`.
- Add schema docs and generated compact registry.
- Validate that every move remains pre-protocol.

## Out of scope

- Arena session lifecycle.
- Runtime packets.
- Verdicts.
- Scars.
- Retention.
- ToS promotion.

## Acceptance

```bash
python mechanics/agon/scripts/build_agon_lawful_move_registry.py --check
python mechanics/agon/scripts/validate_agon_lawful_moves.py
python -m pytest -q mechanics/agon/tests/test_agon_lawful_moves.py
```
