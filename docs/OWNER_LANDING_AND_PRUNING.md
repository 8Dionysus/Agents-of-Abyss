# Owner Landing And Pruning

This document names the center-level doctrine for what happens after reviewed
candidate identity already exists.

It does not create a new owner-status layer.
It names one tracked, reviewable, non-sovereign follow-through posture across
existing owners.

## Purpose

Wave 1 made the growth route legible through:

`cluster_ref -> candidate_ref -> seed_ref -> object_ref`

Wave 2 added derived funnel summaries, proof bundles, recurring method, and
bounded memo support.

What still needed a center law was the route after `candidate_ref` exists:

- where the candidate lands first
- how reanchor, merge, defer, or drop stays explicit
- how tracked owner status stays weaker than final owner truth

## Owner Status Surfaces

An owner status surface is a reviewed, bounded owner-local record that says
what is currently happening to a reviewed candidate on the way toward honest
landing or honest pruning.

It is weaker than a landed owner object.

That means:

- it may say a route is being landed, reanchored, merged, deferred, or dropped
- it does not become the final object
- it does not rewrite the earlier lineage stages
- it does not outrank the final owner repository once `object_ref` is real

## Allowed Outcomes

The route may end in one of these bounded outcomes:

- `landed`
- `reanchored`
- `merged`
- `deferred`
- `dropped`

These outcomes keep post-candidate movement reviewable without pretending that
every route must resolve into a planted owner object immediately.

## Boundary Rule

Keep the post-candidate route owner-first:

- `aoa-skills` may carry reviewed owner landing and bounded follow-through
  decisions
- `Dionysus` may trace how a `seed_ref` did or did not lead into owner landing
- final owner repos still own landed objects and `object_ref`

The center names the doctrine and vocabulary.
It does not become the home of owner status surfaces themselves.

## Negative Rules

Do not:

- let `aoa-stats` infer owner truth from seed staging or turnover summaries
- let `aoa-memo` turn prune or recovery writeback into landing authority
- let `aoa-routing` treat owner-status hints as stronger than owner-local review
- let `Dionysus` pretend seed staging is the same thing as final owner landing
- let the center claim that tracked status is equivalent to landed object truth

## Reading Rule

When the route is post-candidate but not yet final:

1. use `docs/REVIEWABLE_GROWTH_REFINERY.md` to restore the route
2. use `docs/CANDIDATE_LINEAGE_CROSSWALK.md` to restore stage ownership
3. use the owner repo's reviewed status surface to read the next honest move
4. use the final owner object only when landed object truth is actually present

Pruning should stay explicit, owner-aware, and reviewable.
It should not disappear into runtime carry, chat memory, stats summaries, or
memo writeback.
