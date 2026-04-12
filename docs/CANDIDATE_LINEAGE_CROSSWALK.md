# Candidate Lineage Crosswalk

This document records the center-level crosswalk for the growth-refinery chain.

It exists so contributors can name the route without confusing route stages for
new sovereign object classes.

## Crosswalk

| stage | identifier | owner repo | scope | authority posture | must not do |
|---|---|---|---|---|---|
| checkpoint carry | `cluster_ref` | `aoa-sdk` | local checkpoint and reviewed-closeout preparation | provisional control-plane carry only | mint reviewed candidate identity or seed identity |
| reviewed candidate | `candidate_ref` | `aoa-skills` | reviewed reusable candidate after donor harvest | reviewed candidate carry, not final owner truth | act as planted object truth |
| seed staging | `seed_ref` | `Dionysus` | seed staging, dispatch, planting trace | seed-garden and dispatch identity only | replace final owner object identity |
| owner landing | `object_ref` | final owning repo | landed source-owned object | final owner truth for that object class | retroactively rewrite earlier stage meaning |

After `candidate_ref` exists, tracked owner status surfaces may record whether
the route landed, reanchored, merged, deferred, or dropped.
Those surfaces stay weaker than landed objects; see
`docs/OWNER_LANDING_AND_PRUNING.md`.

## Metadata that should survive or update across stages

Each stronger stage should preserve or explicitly update:

- `owner_hypothesis`
- `owner_shape`
- `nearest_wrong_target`
- `evidence_refs`
- `axis_pressure`
- `supersedes`
- `merged_into`
- `drop_reason`
- `status_posture`

## Status posture

Use one bounded posture grammar across the route:

- `early`
- `reanchor`
- `thin-evidence`
- `stable`

This posture helps keep route state legible without inventing one global score.

## Shared lifecycle language

The route may pass through:

- `checkpointed`
- `reviewed`
- `harvested`
- `seeded`
- `planted`
- `proved`
- `promoted`
- `superseded`
- `dropped`

Not every lineage must reach every state.

## Derivative-layer rule

`aoa-routing` and `aoa-kag` may later consume or summarize parts of this route.

They stay derivative:

- they do not mint stage identity
- they do not become the first authoring home
- they do not outrank owner repositories

## Reading rule

When there is ambiguity:

- use the center docs to restore the route
- use the owner repo to restore local truth
- treat derived, routing, and memory surfaces as weaker than the owner layer
