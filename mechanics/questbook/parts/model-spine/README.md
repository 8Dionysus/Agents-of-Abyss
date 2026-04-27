# Questbook Model Spine

## Purpose

`QUESTBOOK` is the public tracked surface for deferred obligations across the
AoA ecosystem.

It exists so that:

- new seeds can be captured without breaking roadmap hierarchy
- deferred follow-ups receive stable IDs
- agents can locate the right open obligation without rereading raw history
- repeated routes can be harvested into durable canon instead of rotting as
  backlog noise

## What QUESTBOOK Is Not

`QUESTBOOK` is not:

- a replacement for source-owned meaning
- a global monolithic backlog
- a private scratchpad
- a second roadmap
- a promise that every microstep deserves an object

## Core Rule

A quest exists only when a work item survives the current bounded diff.

Use a quest when the item:

- creates a follow-up
- creates a seam or dependency
- leaves debt or risk
- needs a separate verification pass
- should be harvested later into a more durable object class

If the work dies inside the current diff, keep it in the active plan or
checklist instead.

## Ownership

Each source repo owns its own quest meaning.

The center may:

- define the common model
- define the first contour rollout shape
- carry federation-level cross-repo quests
- route readers toward source-owned questbooks

The center must not:

- absorb repo-local quest detail
- make `aoa-routing` the author of quest meaning
- confuse memory writeback with source truth
- rename every local TODO into a tracked quest

## Authoritative Surfaces

| Concern | Source |
|---|---|
| Human index | [`QUESTBOOK.md`](../../../../QUESTBOOK.md) |
| Source item store | [`quests/`](../../../../quests/) |
| Source object reviewability | [`source-contract`](../source-contract/README.md) |
| Lifecycle, lanes, promotion, and bands | [`lifecycle-law`](../lifecycle-law/README.md) |
| Relation vocabulary and relation read model | [`relation-shape`](../relation-shape/README.md) |
| Difficulty, risk, control, and delegation | [`execution-passport`](../execution-passport/README.md) |
| Harvest thresholds and promotion targets | [`harvest-route`](../harvest-route/README.md) |
| Lane owner-route maps | [`lane-owner-routes`](../lane-owner-routes/README.md) |
| RPG playable obligation reading | [`RPG_PLAYABLE_READING.md`](RPG_PLAYABLE_READING.md) |

Generated read models:

- `generated/questbook_index.min.json`
- `generated/questbook_frontier.min.json`
- `generated/questbook_relations.min.json`

Generated surfaces summarize, transport, or validate source objects. They do
not author quest meaning.

## Object Names

- human surface: `QUESTBOOK.md`
- canonical object: `work_quest_v1`
- thin delegation projection: `quest_dispatch_v1`
- source item store: `quests/<lane>/<state>/AOA-Q-*`

This naming avoids conflating the human-facing Questbook concept with
repo-specific operator intents such as `open_quest_book`.

## Stop-Lines

- Do not turn quests into private TODOs.
- Do not use generated Questbook views as source truth.
- Do not place repo-local task truth in AoA center unless it is a federation
  obligation.
- Do not route a quest to a lane only because the title sounds similar; owner
  boundary wins.
- Do not treat `sidequest` as dependency, owner transfer, acceptance, or
  closure proof.

## Validation

Use the central Questbook validation matrix in [Questbook AGENTS](../../AGENTS.md#validation).
