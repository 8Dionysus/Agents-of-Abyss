# Return Re-entry

Return Re-entry uses checkpoint as a valid anchor for returning to a bounded
route after drift, pause, loss of axis, or context reset.

## Use When

- A route lost its axis and needs a last valid anchor.
- A relaunch should inspect checkpoint evidence before widening recall.
- Re-entry must stay reviewable and owner-routed.

## Do Not Use When

- The checkpoint lacks enough evidence to anchor a return.
- The route wants hidden memory or ambient continuity.
- Runtime wants to continue without owner review.

## Route Check

Ask whether the checkpoint names a valid anchor, bounded re-entry note, and
stronger owner. If any are missing, safe-stop or route to `aoa-memo`.

## Active Outputs

- return anchor
- re-entry note
- safe stop
- recall route
- owner handoff

## Next Route

Route relaunch and recall surfaces to `aoa-memo`, navigation hints to
`aoa-routing`, scenario choreography to `aoa-playbooks`, and actor handoffs to
`aoa-agents`.
