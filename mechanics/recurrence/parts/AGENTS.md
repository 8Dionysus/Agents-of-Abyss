# AGENTS.md

## Applies to

This card applies to `mechanics/recurrence/parts/` and every active recurrence
part under that path.

## Role

Parts hold active, lean recurrence route shapes. They should help an agent pick
the right owner route without pulling sibling inventories or provenance
history into the active path.

## Read before editing

Read the relevant active part contract and owner route only when part semantics change.
## Boundaries

- Do not copy owner-local implementation into center parts.
- Do not add raw sibling inventories or old wave receipts to part docs.
- Route source lineage through `mechanics/recurrence/PROVENANCE.md` only when
  an audit needs it.
- Route executable validation here instead of repeating commands inside every
  child `VALIDATION.md`.

## Validation

The recurrence part routes are defined in the repository [`VALIDATION.md`](../../../VALIDATION.md).
## Closeout

Name changed parts, owner routes affected, whether `PROVENANCE.md` was actually
consulted, checks run, checks skipped, remaining risk, and the next owner route.
