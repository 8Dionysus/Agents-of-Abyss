# AGENTS.md

## Applies to

This card applies to `mechanics/agon/parts/` and every descendant active part.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/agon/AGENTS.md`,
`mechanics/agon/DIRECTION.md`, and `mechanics/agon/PARTS.md` before changing an
active part.

## Boundaries

Active parts are concise working contracts. Do not turn them into source-doc
inventories, wave ledgers, proof verdicts, memory objects, runtime activation,
or ToS canon.

If a task needs detailed source accounting, route through
`mechanics/agon/PROVENANCE.md`.

## Validation

```bash
python mechanics/agon/scripts/validate_agon_distillation.py
python scripts/validate_mechanic_artifact_topology.py --mechanic agon
```

Run the nearest Agon builder, validator, and test when a part-specific model
artifact changes.

## Closeout

Report active parts changed, whether `PROVENANCE.md` was consulted, owner
requests affected, checks run, checks skipped, remaining risk, and the next
owner route if this lane was only a waypoint.
