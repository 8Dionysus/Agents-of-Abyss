# Decision Note: Reviewable Growth Refinery Uses A Narrow Cross-Layer Lineage Route

Status: accepted
Date: 2026-04-11

## Context

AoA already had real owner-layer surfaces for checkpoint carry, reviewed donor
harvest, seed staging, derived observability, proof, recurring method, and
writeback support.

But one growth object still lost identity as it moved between those layers.

The center needed to name that route without creating a new layer or quietly
promoting derived neighbors into first-authoring homes.

## Options considered

1. Leave the route implicit and let owner repos describe the handoffs only in
   local prose.
2. Name one center-level lineage route and crosswalk while keeping each stage
   in its existing owner repo.
3. Create a new dedicated lineage or refinery layer.

## Decision

AoA now names one narrow reviewable growth-refinery route:

`cluster_ref -> candidate_ref -> seed_ref -> object_ref`

The center records the route in:

- `mechanics/method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md`
- `mechanics/method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md`
- `mechanics/method-growth/docs/METHOD_SPINE.md`

This route does **not** create a new sovereign layer.

Stage ownership stays split:

- `aoa-sdk` carries provisional `cluster_ref`
- `aoa-skills` mints reviewed `candidate_ref`
- `Dionysus` mints `seed_ref`
- the final owner repo owns `object_ref`

`aoa-routing` and `aoa-kag` remain derivative.
`aoa-stats` remains derived-only.
`aoa-memo` remains memory-only.

## Why this path

- The route needed a shared name before cross-repo rollout could stay honest.
- Existing owner repos already had the right boundary posture.
- A new dedicated layer would make the federation less legible, not more.
- Naming the nearest-wrong target and route posture explicitly preserves
  diagnostic value without inflating derived or routing layers.

## Consequences

- future center docs may name the growth-refinery route, but they must not mint
  stage identity themselves
- owner repos must keep the chain narrow and bounded rather than widening it
  into score, routing, or memory sovereignty
- cross-repo rollout can now use one shared route grammar without inventing a
  new lineage empire
