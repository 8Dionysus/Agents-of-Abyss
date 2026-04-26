# Mechanics Validation Command Authority

Date: 2026-04-26

## Status

Accepted

## Context

Mechanic packages now have many nested route, part, owner-request, and support
documents. When each child document carries its own validation command list,
future agents must reconcile stale copies, repeated command blocks, and unclear
local authority before making a change.

That creates the same problem the mechanics topology was built to avoid:
active surfaces become heavier than the move they are supposed to guide.

## Decision

Executable validation commands for active mechanic docs belong in the nearest
`AGENTS.md` validation lane.

Child mechanic docs may point to the nearest `AGENTS.md#validation`, but they
must not own executable command blocks or inline command lists.

Historical `LANDING_LOG.md` and `legacy/` surfaces may retain command evidence
as receipts, because they are provenance surfaces rather than the active
execution route.

## Consequences

- Agents changing a mechanic read the local doc for meaning and the nearest
  `AGENTS.md` for exact checks.
- Child docs stay lighter and less prone to stale command drift.
- `scripts/validate_markdown_shape.py` guards active mechanic docs against
  reintroducing executable validation commands outside `AGENTS.md`.
- Long landing logs can still preserve historical validation evidence without
  becoming the current command surface.
