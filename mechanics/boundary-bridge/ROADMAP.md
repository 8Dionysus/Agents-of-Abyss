# Boundary Bridge Roadmap

## Current Contour

Boundary bridge is landed as the center mechanic for crossing owner boundaries
without identity collapse or authority transfer.

The current strongest slice is ToS support: counterpart policy, witness and
compost support, ToS growth support, template support, lineage pilot support,
and soil preparation support.

## Next Work

- Keep ToS-specific support inside `parts/tos-support/` and source doctrine
  under `docs/`.
- Add a new part only when another bridge shape repeats across owner
  boundaries and cannot be handled by an existing part.
- Keep owner requests portable enough to seed `Tree-of-Sophia`, `aoa-kag`,
  `aoa-routing`, `aoa-memo`, `aoa-evals`, and `aoa-playbooks` without claiming
  acceptance.
- If sibling repositories later create local `mechanics/boundary-bridge/`
  packages, keep their local scope narrower than this center doctrine.

## When The Time Comes

Add future bridge contours here when the route is real but not ready to land.
Each note should name the condition that means the time has come.

- When `aoa-kag` starts carrying counterpart projections operationally, add a
  derived-projection handoff contour with required proof and source-owner refs.
- When `Tree-of-Sophia` accepts an owner-local ToS support receipt, add the
  ToS-support adoption contour and update owner-request status.
- When SDK or routing bridge helpers become stable, add a compatibility-route
  contour that separates adapter behavior from meaning authority.

## Out Of Scope

- AoA-authored ToS canon.
- Owner-local implementation truth.
- Identity claims between bridged surfaces.
- KAG projections as source authority.
- Routing, SDK, memory, runtime, or public projection as bridge authority.
