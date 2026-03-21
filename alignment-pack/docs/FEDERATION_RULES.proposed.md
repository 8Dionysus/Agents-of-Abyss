# Proposed replacement for `docs/FEDERATION_RULES.md`

# AoA Federation Rules

This document records the most important ownership rules across the AoA ecosystem.

## Rule 1: source repositories own meaning

A specialized source repository owns the primary meaning of its object class.

Examples:
- `aoa-techniques` owns technique meaning
- `aoa-skills` owns skill meaning
- `aoa-evals` owns eval meaning
- `aoa-memo` owns memory meaning
- `aoa-agents` owns role and persona meaning
- `aoa-playbooks` owns scenario-composition meaning
- `Tree-of-Sophia` owns ToS authored knowledge-architecture meaning

## Rule 2: navigation layers do not become source-of-truth layers

`aoa-routing` should remain a navigation and dispatch surface.

It may aggregate, compress, and route.

It should not become the primary authoring home of techniques, skills, evals, memory objects, playbooks, or ToS corpus material.

## Rule 3: derived knowledge substrate is not authored source truth

`aoa-kag` may hold provenance-aware lifts, graph-ready projections, and retrieval-ready structures.

It must not silently replace source-authored meaning from `Tree-of-Sophia` or other source repositories.

## Rule 4: scenario composition is not execution canon

`aoa-playbooks` may compose recurring multi-layer scenarios.

It should not silently replace the bounded execution canon owned by `aoa-skills`.

## Rule 5: the center names the federation, not every object inside it

`Agents-of-Abyss` owns ecosystem-level truth, not the primary detail of every layer.

The center should map, govern, and route. It should not absorb layer-owned objects as a matter of convenience.

## Rule 6: infrastructure runs systems, but does not author their meaning

`abyss-stack` may run services beneath AoA and ToS.

It does not own AoA constitutional truth or ToS-authored corpus truth.

## Rule 7: profile and mirrors should follow the center

The public profile and other mirror surfaces may summarize the ecosystem.

They should not silently outrun the center on core definitions, repository roles, or federation boundaries.

## Rule 8: growth should increase legibility

If a new repository, layer, or surface makes AoA less legible, it has not yet been integrated properly.

Growth should sharpen ownership, routing, and reviewability rather than blur them.
