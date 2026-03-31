# QUESTBOOK model

## Purpose

`QUESTBOOK` is the public tracked surface for deferred obligations across the AoA ecosystem.

It exists so that:
- new seeds can be captured without breaking roadmap hierarchy
- deferred follow-ups receive stable IDs
- agents can locate the right open obligation without rereading raw history
- repeated routes can be harvested into durable canon instead of rotting as backlog noise

## What QUESTBOOK is not

`QUESTBOOK` is not:
- a replacement for source-owned meaning
- a global monolithic backlog
- a private scratchpad
- a second roadmap
- a promise that every microstep deserves an object

## Core rule

A quest exists only when a work item survives the current bounded diff.

Use a quest when the item:
- creates a follow-up
- creates a seam or dependency
- leaves debt or risk
- needs a separate verification pass
- should be harvested later into a more durable object class

If the work dies inside the current diff, keep it in the active plan or checklist instead.

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

## Human and machine surfaces

- human surface: `QUESTBOOK.md`
- canonical object: `work_quest_v1`
- thin delegation projection: `quest_dispatch_v1`

This naming avoids conflating the human-facing questbook concept with repo-specific operator intents such as `open_quest_book`.

## Position model

QUESTBOOK uses two axes.

### Lifecycle state

- `captured`
- `triaged`
- `ready`
- `active`
- `blocked`
- `reanchor`
- `done`
- `dropped`

### Placement band

- `frontier`
- `near`
- `latent`
- `parked`

Use bands instead of fixed calendar horizons when the build tempo is event-driven.

## Execution passport

Every quest carries:
- `difficulty`
- `risk`
- `control_mode`
- `delegate_tier`
- optional `wrapper_class`

These fields do not answer "when".
They answer "who may touch this, under what leash, and how expensive a mistake would be".

## Difficulty ladder

- `d0_probe` — bounded reading, triage, listing, no write
- `d1_patch` — one small bounded change in one surface
- `d2_slice` — one bounded slice across a few files in one owner surface
- `d3_seam` — contract or layer seam inside one repo or between adjacent repos
- `d4_architecture` — broad architectural or policy route
- `d5_doctrine` — rule-birth, ownership-boundary, or public-canon work

## Risk ladder

- `r0_readonly`
- `r1_repo_local`
- `r2_contract`
- `r3_side_effect`

## Delegation rule

Do not hand `d3+` quests directly to smaller local wrappers.
Split them into honest `d0-d2` leaves first.

## Harvest rule

Repeated quest patterns should not remain as permanent open work if they are really signs of missing canon.

Default harvest thresholds:
- same route appears twice in one repo -> open a harvest quest
- same route appears three times across repo boundaries -> promote a cross-repo harvest decision

Promotion targets:
- repeated reusable practice -> `aoa-techniques`
- repeated bounded execution recipe -> `aoa-skills`
- repeated proof posture -> `aoa-evals`
- repeated scenario route -> `aoa-playbooks`
- repeated role or handoff contract -> `aoa-agents`
- repeated memory/writeback pattern -> `aoa-memo`
- repeated thin navigation pattern -> `aoa-routing`

## Public-safety rule

Tracked quest surfaces are public-safe by default.

Do not store:
- secrets
- private system paths
- hidden incident detail that belongs elsewhere
- raw local planning noise

If richer local notes are needed, keep them in ignored local overlays and reference the public quest ID.
