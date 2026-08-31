# AGENTS.md

## Applies to

This card applies to `schemas/` and every nested path under that scope until a
nearer `AGENTS.md` narrows the lane.

## Role

`schemas/` owns root-level JSON schema contracts and the registry that routes
agents to schema homes. It keeps root shape contracts visible without absorbing
mechanic-owned schemas.

The authoritative registry is `schemas/registry.json`.

## Read before editing

Select only the source, contract, or owner route that can change the interpretation of the named task.
A nearby human README is on-demand: use it when its explanation, package map, provenance, compatibility, or usage contract is material to the task.
Exact executable checks belong to the applicable `VALIDATION.md`, validated manifest, runner, or stronger owner procedure surface.
## Boundaries

- Root `schemas/` owns root center contracts.
- Mechanic schemas belong with the owning mechanic or part.
- `ecosystem-registry.schema.json` is a public center registry contract; any
  contract change to `$id`, visibility, maturity, relation, kind, or required
  fields must stay aligned with `validate_ecosystem.py`.
- Do not widen a schema just to make weak or inconsistent data pass.
- Do not use schema names or fields to create runtime authority, owner
  acceptance, or source meaning.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

For release-facing schema changes, also run:

## Closeout

Report schema registry entries changed, root schemas touched, source surfaces
consulted, generated files rebuilt or intentionally left untouched, checks run,
checks skipped, and the owner route when a schema belongs outside root.
