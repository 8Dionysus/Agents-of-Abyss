# Questbook Roadmap

## Current Contour

Questbook has landed its lane-first source layout, generated read models,
center relation model, model-spine split, and registry-backed Experience ready
owner-route index. Active parts are now machine-checked through
`parts/registry.json` and
`mechanics/questbook/scripts/validate_questbook_distillation.py`.

Current source placement is `quests/<lane>/<state>/AOA-Q-*`. Generated
Questbook views are read models. Relation shape is explicit through `parent`,
`sidequest`, and dependency-style relations without transferring lane
ownership. `parts/model-spine/` is now the short source-of-truth spine;
lifecycle, execution-passport, harvest, and lane-owner route contract details
live in narrow part packages. `legacy/` preserves first-contour provenance
behind `PROVENANCE.md`.

## Next Work

- Keep quest lifecycle law aligned with the root public index.
- Keep `ready` lanes mapped to explicit owner-request packets before claiming
  they are execution-ready.
- Keep ready owner-route maps generated from registry JSON instead of editing
  route tables directly.
- Keep part packages as the normal working route; use `PROVENANCE.md` only
  when older source contours must be audited.
- Keep `parts/registry.json` synchronized with `PARTS.md`, `parts/README.md`,
  per-part contracts, validation routes, and the legacy index.
- Keep relation visibility useful while preventing `sidequest` from becoming
  ownership, dependency, or automatic closure.
- Tighten markdown quest object shape after the lane-first source layout proves
  stable across several real promotions.
- Harvest repeated quest families into owner-local mechanics, playbooks, evals,
  or memo surfaces instead of letting open quest lists become noisy.

## Review Routes

- Center lane: use the center promotion pilot as the proof shape before broad
  promotion passes.
- Agon lane: keep done contour quests split from ready owner-followthrough
  quests, then close only from reviewed owner acceptance.
- Experience lane: keep the ready owner-route index current while AoA remains
  the active work lane, then update queue status only from owner-local
  receipts.
- Future lanes: add lane README route notes before a lane becomes difficult to
  scan from `quests/README.md` alone.

## Time Has Come When

- Add lane README route notes when a lane gains enough active quests to need
  local orientation.
- Open the next lane activation pass when a lane has enough triaged pressure
  that readers can no longer tell which quest can honestly move next.
- Review `quests/<lane>/ready/` when ready items start mixing owner-acceptance
  review, owner-request updates, and true execution work in one pile.
- Add a lane route registry when a second ready lane needs the same
  quest-to-owner-request coverage as Experience.
- Promote a related cluster into lane-local quest objects when `sidequest`
  visibility is no longer enough to explain owner action cleanly.
- Promote a recurring quest pattern when it appears twice in one lane or three
  times across lanes.
- Add a stricter markdown quest contract when title/path review no longer gives
  enough closure confidence.
- Prepare sibling-repo questbooks when owner repositories are ready to accept
  local quest truth without copying the AoA root index.

## Out Of Scope

- Private scratchpad content.
- Owner-local task lists from sibling repositories.
- Replacing `ROADMAP.md`.
