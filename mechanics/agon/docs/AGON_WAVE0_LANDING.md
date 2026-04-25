# Agon Wave 0 Landing

This note describes how to land the Agon Imposition Gate without accidentally starting the arena.

## Target

Land in `Agents-of-Abyss`.

Do not create a new sibling repository.

Do not modify owner repositories from this patch.

## Landing order

1. Add the Wave 0 documents.
2. Add the schema and generated readiness capsule.
3. Add builder, validator, and test.
4. Run the Wave 0 validation commands.
5. Decide whether to wire the validator into broader center validation immediately or leave it as explicit Wave 0 validation until the next center release cut.

## Validation commands

```bash
python mechanics/agon/scripts/build_agon_imposition_readiness.py --check
python mechanics/agon/scripts/validate_agon_imposition_readiness.py
python -m pytest -q mechanics/agon/tests/test_agon_imposition_readiness.py
```

## Recommended follow-through

After this seed lands cleanly, update public route surfaces only if the release contour is ready to name Agon imposition publicly.

Suggested future edits, not included in this seed:

- add `mechanics/agon/docs/AGON_IMPOSITION_POSTURE.md` to the README route table;
- add the generated readiness capsule to the machine-facing center entry route if desired;
- add a roadmap note that Agon has moved from preparation to imposition audit;
- open Wave I in `aoa-agents` as Agonic Actor Rechartering.

## Forbidden follow-through in this wave

Do not add arena session schemas.

Do not add lawful move registries.

Do not add contradiction ledger schemas.

Do not add verdict packet schemas.

Do not add scar write schemas.

Do not wire runtime services.

Do not write into `Tree-of-Sophia`.

Wave 0 is the hammer raised over the old shape. It is not yet the sword fight.
