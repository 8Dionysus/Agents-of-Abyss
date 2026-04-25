# Agon Wave IV Landing

## Wave name

Agon Wave IV: Move Owner Binding.

## Primary repository

`Agents-of-Abyss`.

## Companion owner candidate repositories

- `aoa-techniques`
- `aoa-skills`

The companion seeds are optional first landings. They only hold candidate requests. They do not promote techniques or skills.

## Validation

From `Agents-of-Abyss`:

```bash
python scripts/build_agon_move_owner_binding_registry.py --check
python scripts/validate_agon_move_owner_bindings.py
python -m pytest -q tests/test_agon_move_owner_bindings.py
```

From `aoa-techniques` after companion landing:

```bash
python scripts/build_agon_technique_binding_candidates.py --check
python scripts/validate_agon_technique_binding_candidates.py
python -m pytest -q tests/test_agon_technique_binding_candidates.py
```

From `aoa-skills` after companion landing:

```bash
python scripts/build_agon_skill_binding_candidates.py --check
python scripts/validate_agon_skill_binding_candidates.py
python -m pytest -q tests/test_agon_skill_binding_candidates.py
```

## Exit criteria

Wave IV is ready when:

- all Wave III lawful moves have exactly one owner binding;
- each binding names `Agents-of-Abyss` as center law owner;
- non-center owner refs remain `requested_not_landed`;
- companion candidate indexes exist for techniques and skills;
- no binding creates live arena behavior;
- assistant boundaries remain explicit;
- generated surfaces are deterministic.

## What Wave IV unlocks

Wave V may begin routing gate work because moves now have owner-aware future surfaces.

Wave VI may begin trial playbook work because moves now have scenario hooks.

Wave VII may begin eval/memo/stats prebinding because proof, memory, and observability slots are no longer hidden in center text.
