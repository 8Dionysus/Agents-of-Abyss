# AGENTS.md

## Applies to

This card applies to `mechanics/agon/legacy/` and every raw or accounting
surface inside it.

## Role

Legacy preserves Agon provenance. `legacy/raw/` holds long wave, model,
handoff, stop-line, and support documents after their active route has been
distilled into `parts/`.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/agon/AGENTS.md`,
`mechanics/agon/DIRECTION.md`, `mechanics/agon/PARTS.md`, and `INDEX.md`
before changing legacy files.

## Boundaries

Do not treat raw legacy files as the primary active route. Do not delete
provenance to make the active surface look clean. Do not add new raw packets
without indexing them and naming the active part they pressure.

## Validation

Run:

```bash
python mechanics/agon/scripts/validate_agon_distillation.py
python scripts/validate_mechanic_landing_logs.py --mechanic agon
python scripts/validate_links.py
```

## Closeout

Report raw files moved or edited, index and distillation-log updates, active
part surfaces updated, and checks run or skipped.
