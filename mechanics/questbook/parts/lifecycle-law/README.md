# Quest Lifecycle

This document owns Questbook lifecycle states, lane placement, promotion, and
placement bands.

## Lifecycle States

- `captured`
- `triaged`
- `ready`
- `active`
- `blocked`
- `reanchor`
- `done`
- `dropped`

The lifecycle state is not only prose. Quest source files live in the matching
state directory under a lane in `quests/`. Top-level `quests/AOA-Q-*` aliases
and root lifecycle directories such as `quests/triaged/` are intentionally
absent so every route lands on `quests/<lane>/<state>/AOA-Q-*`.

## Lanes

The lane names the owner route before the lifecycle state names the current
posture.

- `center`
- `agon`
- `experience`
- `rpg`
- `recurrence`
- `checkpoint`
- `questbook`
- `antifragility`
- `method-growth`
- `release-support`
- `tos-bridge`

Use `center` for federation-level obligations that are not owned by a more
specific mechanic lane. Use mechanic lanes when the quest ID family and owning
route are already clear, such as `AOA-Q-AGON-*` or `AOA-Q-EXP-*`.

## Promotion Protocol

Promotion is a source move, not only a label change. Move the quest file to the
matching lifecycle directory and update the quest's `state` field in the same
diff.

Before promoting:

- read the quest source file, the lane README, and the named anchor surface
- confirm the lane is still the honest owner route
- confirm the next action can be understood without raw session history
- keep public-safe wording; do not paste private local notes into quest source

State transitions:

- `captured` -> `triaged` when the owner lane, band, and rough acceptance are
  known
- `triaged` -> `ready` when the next action can be taken from the quest, its
  lane README, and its anchor
- `ready` -> `active` only while an owner lane is actually advancing it
- `active` -> `done`, `blocked`, `reanchor`, or `dropped` when the current move
  ends
- `blocked` -> `ready` only after the named dependency changes
- `reanchor` -> `captured` or `triaged` after the route is honestly reset

After promoting:

- update root `QUESTBOOK.md` only when the public frontier or near contour
  changes
- update the mechanic `LANDING_LOG.md` when the promotion changes Questbook
  mechanics or proves a new route
- rebuild the generated Questbook read models
- run lifecycle, generated-index, and relation validators

Do not promote a quest just because it is old. Age is a review signal, not
proof of readiness.

## Placement Bands

- `frontier`
- `near`
- `latent`
- `parked`

Use bands instead of fixed calendar horizons when the build tempo is
event-driven.

## Validation

Use the central Questbook validation matrix in [Questbook AGENTS](../../AGENTS.md#validation).
