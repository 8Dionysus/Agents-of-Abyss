# AGENTS.md

## Applies to

This card applies to `memo/`.

## Role

`memo/` is the Agents-of-Abyss local memory port. It holds center-local memory
candidates, receipts, exports, and local notes before reviewed landing in
`aoa-memo`.

## Read before editing

Select only the source, contract, or owner route that can change the interpretation of the named task.
A nearby human README is on-demand: use it when its explanation, package map, provenance, compatibility, or usage contract is material to the task.
Exact executable checks belong to the applicable `VALIDATION.md`, validated manifest, runner, or stronger owner procedure surface.
## Boundaries

Use this port for `write_candidate_only` work. Do not turn local notes into
center doctrine or durable memory without `aoa-memo` review.

Use `PORT.yaml` for the local port contract and `INDEX.md` / `index.min.json`
as generated read models. Use `candidates/` for proposed memory, `receipts/`
for review or handoff traces, `exports/` for packets meant for `aoa-memo`, and
`local/` for center-local memory that should stay here for now.

## Candidate Route

Create center-local candidates through the stack MCP helper from the
`abyss-stack` source checkout:

Then validate the emitted candidate path:

## Reviewed Landing Route

When an export is ready to move from this local port toward durable reviewed
memory, inspect it through the same MCP access plane:

The landing plan is a readiness/dry-run route. The actual durable memory object
lands only in `aoa-memo` through its reviewed intake script, generated read
models, validators, and review.

## Validation

For local candidate checks through the stack MCP access plane:

For release-facing center changes, run:

## Closeout

Report candidate path, evidence refs, validation result, and whether the item
stayed local, was exported for reviewed intake, or was landed in `aoa-memo`.
