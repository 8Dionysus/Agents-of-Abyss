# AOA-Q-AGON-0013: Move Owner Binding

## Intent

Land Wave IV owner binding in `Agents-of-Abyss`.

## Done when

- `config/agon_move_owner_bindings.seed.json` exists.
- `generated/agon_move_owner_binding_registry.min.json` is deterministic.
- all Wave III lawful moves are covered exactly once.
- no binding creates live arena behavior.
- assistant boundary remains explicit.

## Verify

```bash
python scripts/build_agon_move_owner_binding_registry.py --check
python scripts/validate_agon_move_owner_bindings.py
python -m pytest -q tests/test_agon_move_owner_bindings.py
```
