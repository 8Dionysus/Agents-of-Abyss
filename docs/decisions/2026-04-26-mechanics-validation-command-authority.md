# Mechanics Validation Command Authority

Status: accepted
Date: 2026-04-26

## Context

Mechanic packages now have many nested route, part, owner-request, and support
documents. When each child document carries its own validation command list,
future agents must reconcile stale copies, repeated command blocks, and unclear
local authority before making a change.

That creates the same problem the mechanics topology was built to avoid:
active surfaces become heavier than the move they are supposed to guide.

## Options considered

1. Let every active child document carry its own validation command list.
2. Put executable validation in the nearest `AGENTS.md` lane and let child docs
   route there.
3. Move all mechanic validation commands into one repository-root command list.

## Decision

Executable validation commands for active mechanic docs belong in the nearest
`AGENTS.md` validation lane.

Child mechanic docs may point to the nearest `AGENTS.md#validation`, but they
must not own executable command blocks or inline command lists.

Historical `LANDING_LOG.md` and `legacy/` surfaces may retain command evidence
as receipts, because they are provenance surfaces rather than the active
execution route.

## Rationale

The nearest `AGENTS.md` already owns local execution posture. Keeping commands
there lets agents change active docs without reconciling stale copies across
every child surface.

The split also preserves useful historical command evidence where it belongs:
landing logs and legacy records can show what was checked at the time, while
active docs stay light and route-shaped.

## Consequences

- Agents changing a mechanic read the local doc for meaning and the nearest
  `AGENTS.md` for exact checks.
- Child docs stay lighter and less prone to stale command drift.
- `scripts/validate_markdown_shape.py` guards active mechanic docs against
  reintroducing executable validation commands outside `AGENTS.md`.
- Long landing logs can still preserve historical validation evidence without
  becoming the current command surface.

## Source surfaces

- `mechanics/AGENTS.md`
- `mechanics/<slug>/AGENTS.md`
- `scripts/validate_markdown_shape.py`
- `mechanics/<slug>/LANDING_LOG.md`
- `mechanics/<slug>/legacy/`

## Follow-up route

Route future command-placement pressure through `mechanics/AGENTS.md` and
`scripts/validate_markdown_shape.py`; add exceptions only for provenance or
landing evidence surfaces.
