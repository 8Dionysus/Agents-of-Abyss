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

## Validation witness

The center keeps one witness-shaped validator for the live example chain:

Use the validation lane in [mechanics/method-growth/docs/AGENTS.md](AGENTS.md#validation) for executable commands.

That check reads owner-repo examples in `aoa-sdk`, `aoa-skills`, and
`Dionysus`.
It may detect drift in the chain, but it does not make this repository the
owner of checkpoint carry, reviewed candidate identity, seed identity, or final
object identity.

The center-level example at `mechanics/method-growth/examples/lineage_contract_chain.example.json` is
a crosswalk witness only.

For the wave-four next-kernel and reviewed automation seam, the center keeps a
second witness-shaped validator:

Use the validation lane in [mechanics/method-growth/docs/AGENTS.md](AGENTS.md#validation) for executable commands.

That check confirms the reviewed closeout hint in `aoa-sdk`, the kernel
maturity example set in `aoa-skills`, the review-governed playbook home in
`aoa-playbooks`, and the derived branch/follow-through summaries in
`aoa-stats` still line up without giving the center scheduler or owner
authority.

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

For the tracked owner-status and pruning law after reviewed candidate identity
already exists, use `mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md`.
For owner-owned maintenance of one drifting internal technical surface, use
`mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md`.

Use narrower owner docs when the question is already local to one layer.
