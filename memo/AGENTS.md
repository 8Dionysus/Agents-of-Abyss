# AGENTS.md

## Applies to

This card applies to `memo/`.

## Role

`memo/` is the Agents-of-Abyss local memory port. It holds center-local memory
candidates, receipts, exports, and local notes before reviewed landing in
`aoa-memo`.

## Read before editing

Read `PORT.yaml` and the relevant candidate or export route only when memory-port behavior changes.
## Boundaries

Use this port for `write_candidate_only` work. Do not turn local notes into
center doctrine or durable memory without `aoa-memo` review.

Use `PORT.yaml` for the local port contract and `INDEX.md` / `index.min.json`
as generated read models. Use `candidates/` for proposed memory, `receipts/`
for review or handoff traces, `exports/` for packets meant for `aoa-memo`, and
`local/` for center-local memory that should stay here for now.

## Candidate Route

The candidate route for creating center-local candidates through the stack MCP helper from the `abyss-stack` source checkout is defined in the repository [`VALIDATION.md`](../VALIDATION.md).

The emitted candidate path is validated through the candidate route in the repository [`VALIDATION.md`](../VALIDATION.md).

## Reviewed Landing Route

When an export is ready to move from this local port toward durable reviewed
memory, inspect it through the same MCP access plane:

The landing plan is a readiness/dry-run route. The actual durable memory object
lands only in `aoa-memo` through its reviewed intake script, generated read
models, validators, and review.

## Validation

The local candidate-check route through the stack MCP access plane is defined in the repository [`VALIDATION.md`](../VALIDATION.md).

The release route for release-facing center changes is defined in the repository [`VALIDATION.md`](../VALIDATION.md).

## Closeout

Report candidate path, evidence refs, validation result, and whether the item
stayed local, was exported for reviewed intake, or was landed in `aoa-memo`.
