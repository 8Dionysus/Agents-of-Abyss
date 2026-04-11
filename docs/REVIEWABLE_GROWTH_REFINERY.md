# Reviewable Growth Refinery

This document names the current center-level doctrine for the growth-refinery
route across AoA.

It does not create a new sovereign layer.
It names one reviewable route that crosses existing owner layers without
replacing them.

## Purpose

AoA already has:

- checkpoint-aware local carry in `aoa-sdk`
- reviewed donor harvest in `aoa-skills`
- seed staging in `Dionysus`
- derived observability in `aoa-stats`
- proof in `aoa-evals`
- recurring method in `aoa-playbooks`
- bounded writeback in `aoa-memo`

What was missing was one explicit, narrow, non-sovereign biography for a growth
object moving across those layers.

The growth refinery supplies that biography.

## Canonical chain

The canonical chain is:

`cluster_ref -> candidate_ref -> seed_ref -> object_ref`

This is a route, not a new layer.

## Boundary rule

Keep each stage in its existing owner:

- `aoa-sdk` may carry `cluster_ref` as provisional checkpoint and reviewed-closeout context
- `aoa-skills` may mint `candidate_ref` only after reviewed donor harvest
- `Dionysus` may mint `seed_ref` only in seed staging and dispatch
- final owner repos mint or resolve `object_ref`

The center names the chain and its boundaries.
It does not mint the identities inside that chain.

## Owner-first route

The honest owner-first route is:

1. center doctrine and crosswalk in `Agents-of-Abyss`
2. provisional lineage carry in `aoa-sdk`
3. reviewed candidate identity in `aoa-skills`
4. seed identity and planting trace in `Dionysus`
5. derived funnel summary in `aoa-stats`
6. lineage proof bundles in `aoa-evals`
7. recurring session-growth method in `aoa-playbooks`
8. lineage-aware writeback in `aoa-memo`

This order keeps doctrine, carry, candidate identity, seed identity, derived
views, proof, recurring method, and memory writeback from collapsing into one
surface.

## Negative rules

Do not:

- create a new sovereign lineage repository or layer
- mint `candidate_ref` in `aoa-sdk`
- mint `seed_ref` outside `Dionysus`
- let `aoa-stats` become route or proof authority
- let `aoa-memo` become lineage authority
- let `aoa-routing` or `aoa-kag` become first-authoring homes for this route
- use one total score as the readout of growth

## What this doctrine is for

Use this doctrine when a growth object must stay legible across:

- checkpoint carry
- reviewed harvest
- seed staging
- owner landing
- proof
- recurring playbook use
- bounded failure or recovery writeback

Use narrower owner docs when the question is already local to one layer.
