# AGENTS.md

## Applies to

This card applies to `mechanics/recurrence/parts/` and every active recurrence
part under that path.

## Role

Parts hold active, lean recurrence route shapes. They should help an agent pick
the right owner route without pulling sibling inventories or provenance
history into the active path.

## Read before editing

Select only the source, contract, or owner route that can change the interpretation of the named task.
A nearby human README is on-demand: use it when its explanation, package map, provenance, compatibility, or usage contract is material to the task.
Exact executable checks belong to the applicable `VALIDATION.md`, validated manifest, runner, or stronger owner procedure surface.
## Boundaries

- Do not copy owner-local implementation into center parts.
- Do not add raw sibling inventories or old wave receipts to part docs.
- Route source lineage through `mechanics/recurrence/PROVENANCE.md` only when
  an audit needs it.
- Route executable validation here instead of repeating commands inside every
  child `VALIDATION.md`.

## Validation

## Closeout

Name changed parts, owner routes affected, whether `PROVENANCE.md` was actually
consulted, checks run, checks skipped, remaining risk, and the next owner route.
