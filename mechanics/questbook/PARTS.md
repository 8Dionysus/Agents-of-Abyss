# Questbook Parts

This file is the active map of functioning Questbook parts. Each part owns a
real slice of the mechanic: purpose, boundary, validation, and next route.
Legacy source contours stay outside the working path.

## Part Map

| Part | Center function | Stronger owner route |
|---|---|---|
| [Model Spine](parts/model-spine/README.md) | compact Questbook model, source-of-truth map, and shared stop-lines | owner repositories keep quest meaning; center only names common law |
| [Public Index](parts/public-index/README.md) | root public frontier and near-obligation index posture | source quest objects own detail |
| [Quest Store](parts/quest-store/README.md) | lane-first source object layout under `quests/<lane>/<state>/AOA-Q-*` | lanes and owner repositories keep acceptance evidence |
| [Source Contract](parts/source-contract/README.md) | reviewability contract for YAML and strict Markdown quest objects | source files carry obligation meaning; generated views only reflect them |
| [Lifecycle Law](parts/lifecycle-law/README.md) | lifecycle states, lane placement, promotion protocol, and bands | owner repositories prove acceptance and closure |
| [Generated Views](parts/generated-views/README.md) | compact index, frontier, and relation read models | generated views never author quest meaning |
| [Relation Shape](parts/relation-shape/README.md) | `parent`, `sidequest`, dependency-style, and reanchor relation vocabulary | relations do not transfer ownership or close quests |
| [Execution Passport](parts/execution-passport/README.md) | difficulty, risk, control, delegation, and reviewability vocabulary | proof and acceptance stay with owner-local evidence |
| [Harvest Route](parts/harvest-route/README.md) | repeated-pattern thresholds and promotion targets | reusable practice, proof, playbook, skill, memo, or route truth lands with stronger owners |
| [Owner Handoffs](parts/owner-handoffs/README.md) | center-side owner request packets and queue route | stronger owners accept, reject, land, or prove the request |
| [Lane Owner Routes](parts/lane-owner-routes/README.md) | ready quest to owner-request registries and generated route tables | owner repositories still own acceptance, proof, landing, and closure |

## Active Part Contract

Every part keeps three working surfaces:

- `README.md`: what the part is for and where to start.
- `CONTRACT.md`: owner boundary, stop-lines, and allowed outputs.
- `VALIDATION.md`: short route back to the central validation matrix.

The part list is machine-checked through
[`parts/registry.json`](parts/registry.json). Add or retire a part there only
when the matching README, contract, validation, indexes, and provenance route
are ready together.

A part may grow, split, merge, shrink, or retire when that improves its
function and keeps the route cleaner. The move should leave the active path
easier to follow, not merely smaller.

## Provenance Bridge

Historical source accounting is deliberately outside part docs. Use
[PROVENANCE](PROVENANCE.md) when a task must audit which old contour fed an
active part. Active part docs should not grow source-file inventories.

## Validation

Use the central Questbook validation matrix in [Questbook AGENTS](AGENTS.md#validation).
