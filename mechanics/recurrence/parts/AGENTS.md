# AGENTS.md

## Applies to

This card applies to `mechanics/recurrence/parts/` and every active recurrence
part under that path.

## Role

Parts hold active, lean recurrence route shapes. They should help an agent pick
the right owner route without pulling sibling inventories or provenance
history into the active path.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/recurrence/AGENTS.md`,
`mechanics/recurrence/README.md`, and `mechanics/recurrence/PARTS.md`.

## Boundaries

- Do not copy owner-local implementation into center parts.
- Do not add raw sibling inventories or old wave receipts to part docs.
- Route source lineage through `mechanics/recurrence/PROVENANCE.md` only when
  an audit needs it.
- Route executable validation here instead of repeating commands inside every
  child `VALIDATION.md`.

## Validation

```bash
python mechanics/recurrence/scripts/validate_recurrence_mechanic.py
python -m pytest -q mechanics/recurrence/tests/test_recurrence_mechanic.py
```

## Closeout

Name changed parts, owner routes affected, whether `PROVENANCE.md` was actually
consulted, checks run, checks skipped, remaining risk, and the next owner route.
