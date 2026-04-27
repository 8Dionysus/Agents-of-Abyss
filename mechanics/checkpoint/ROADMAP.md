# Checkpoint Roadmap

Checkpoint is landed as center law and owner map.

The current contour is intentionally small: make intermediate growth states
reviewable and transferable without moving implementation, memory, proof,
runtime, routing, stats, or owner acceptance into the center.

## Current contour

- Center package exists with law, parts, owner map, provenance, and owner
  requests.
- `aoa-sdk` remains the control panel for hooks, ledgers, and closeout context.
- `aoa-skills` remains the owner of checkpoint-note and bridge skill protocol.
- Owner repositories keep local checkpoint meaning.

## Next useful moves

- After checkpoint law stabilizes, consider a compact machine-readable owner map
  only if sibling repos need it.
- When owner repos land checkpoint slices, update `OWNER_REQUESTS.md`,
  `LANDING_LOG.md`, and the owner-request queue instead of expanding center
  doctrine.
- If repeated checkpoint states diverge across owners, define a minimal shared
  state vocabulary here.

## Stop-lines

- Do not make checkpoint a memory object family.
- Do not make checkpoint a proof verdict.
- Do not make checkpoint a hidden automation runner.
- Do not make checkpoint a runtime scheduler.
- Do not make checkpoint a second quest or roadmap system.

## When The Time Comes

- Add owner-local acceptance receipts once sibling repos accept request packets.
- Add part-local examples only after one route repeats enough to justify an
  example.
- Revisit whether checkpoint should influence release-support gates after the
  first owner-local control panel and closeout bridge slices are proven.
