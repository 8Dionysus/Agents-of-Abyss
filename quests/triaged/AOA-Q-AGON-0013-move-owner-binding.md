# AOA-Q-AGON-0013: Move Owner Binding

## Intent

Land Wave IV owner binding in `Agents-of-Abyss`.

## Done when

- `mechanics/agon/parts/owner-binding/config/agon_move_owner_bindings.seed.json` exists.
- `mechanics/agon/parts/owner-binding/generated/agon_move_owner_binding_registry.min.json` is deterministic.
- all Wave III lawful moves are covered exactly once.
- no binding creates live arena behavior.
- assistant boundary remains explicit.

## Verify

```bash
python mechanics/agon/parts/owner-binding/scripts/build_agon_move_owner_binding_registry.py --check
python mechanics/agon/parts/owner-binding/scripts/validate_agon_move_owner_bindings.py
python -m pytest -q mechanics/agon/parts/owner-binding/tests/test_agon_move_owner_bindings.py
```
