# RPG Parts

This file is the active map of functioning RPG parts. Each part owns a real slice of the mechanic: purpose, boundary, validation, and next route. Historical source contours stay outside the working path.

Use [USAGE](USAGE.md) before choosing a part. It decides whether RPG language belongs in the task at all.

## Part Map

| Part | Center function | Stronger owner route |
|---|---|---|
| [World Grammar](parts/world-grammar/README.md) | when RPG language improves action, judgment, memory, proof, or consequence | owning mechanic or repository keeps the underlying truth |
| [Source Boundary](parts/source-boundary/README.md) | reflection law, source precedence, and no-hidden-ontology boundary | source repositories keep durable meaning |
| [Vocabulary Overlay](parts/vocabulary-overlay/README.md) | canonical machine keys, themed labels, and checked dual-vocabulary overlay | `abyss-stack` owns runtime projection; UI labels never replace canonical keys |
| [Quest Campaign](parts/quest-campaign/README.md) | quest, questline, campaign, party, and chronicle reading | Questbook owns quest objects; `aoa-playbooks` owns campaign choreography; `aoa-memo` owns chronicles |
| [Progression Unlocks](parts/progression-unlocks/README.md) | rank, mastery axes, ability/feat reflections, reputation, and unlock posture | `aoa-agents`, `aoa-skills`, `aoa-techniques`, `aoa-evals`, and `aoa-stats` own proof and object truth |
| [Runtime Projection](parts/runtime-projection/README.md) | runtime/frontend projection needs and transport contours | `abyss-stack` owns live runtime, state, service, and projection delivery |
| [Owner Handoffs](parts/owner-handoffs/README.md) | stronger-owner request route and no-acceptance boundary | target owner repositories accept or reject operational slices |

## Active Part Contract

Every part keeps three working surfaces:

- `README.md`: what the part is for and where to start.
- `CONTRACT.md`: owner boundary, stop-lines, and allowed outputs.
- `VALIDATION.md`: validation route, with executable commands centralized in `AGENTS.md`.

Every part `README.md` should stay short and use the same active-route shape:

- `## Use When`
- `## Do Not Use When`
- `## Route Check`
- `## Active Outputs`
- `## Next Route`

Every part `CONTRACT.md` should name what must be true before the part emits an
output:

- `## Center Owns`
- `## Must Not Claim`
- `## Allowed Outputs`
- `## Required Before Output`

A part may grow, split, merge, shrink, or retire when that improves the world grammar and keeps the route cleaner. The move should leave agent action easier to judge, not merely smaller.

## Provenance Bridge

Detailed source-doc accounting is deliberately outside part docs. Use [PROVENANCE](PROVENANCE.md) when a task must audit which RFC, preserved contour, boundary map, or runtime projection fed a part. Active part docs should not grow source-file inventories.

## Validation

Use the validation lane in [mechanics/rpg/AGENTS.md](AGENTS.md#validation) for executable commands.

Use `OWNER_REQUESTS.md` for owner-request queue validation and `parts/vocabulary-overlay/` for the checked dual-vocabulary overlay.
