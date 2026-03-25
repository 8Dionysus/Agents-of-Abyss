# AGENTS.md

## Project identity

Agents of Abyss (AoA) is an evolving ecosystem for long-horizon agentic work.

It is not one bot, one workflow, or one narrow automation project.
It is a modular federation of reusable practice, bounded execution, portable proof, memory, routing, agent roles, and supporting infrastructure.

This repository is the constitutional and ecosystem-center repository of AoA.
It is the canonical high-level statement of what AoA is, how its layers relate, and how the federation should grow without collapsing into monolith or confusion.

## Current repository role

Treat `Agents-of-Abyss` as:
- public landing page
- canonical project identity
- ecosystem map
- federation-rule surface
- stable high-level entrypoint for humans and coding agents

This repository is not the full implementation home of AoA.
Its job is not to absorb the ecosystem.
Its job is to keep the ecosystem intelligible.

## Ecosystem map

- `Agents-of-Abyss` = ecosystem identity, layer map, federation rules, program-level direction
- `Tree-of-Sophia` = living knowledge architecture that AoA helps build and operationalize
- `abyss-stack` = runtime, deployment, storage, and service substrate
- `aoa-techniques` = reusable practice canon
- `aoa-skills` = bounded execution canon
- `aoa-evals` = portable proof canon
- `aoa-routing` = navigation and dispatch layer
- `aoa-memo` = memory and recall layer
- `aoa-agents` = role and handoff layer

## Working assumptions

When editing or extending AoA-related material:
- preserve the distinction between ecosystem truth and layer truth
- preserve the distinction between agent operations and knowledge architecture
- prefer reusable patterns over one-off hacks
- prefer modularity over monolithic fusion
- maintain source-of-truth discipline
- keep changes reviewable, explicit, and well-scoped
- make assumptions and uncertainty visible

## What belongs here

Use this repository for:
- charter and principles
- ecosystem map
- layer definitions and relationships
- federation rules and ownership boundaries
- program-level roadmap
- compact registry surfaces that summarize the ecosystem
- contributor and coding-agent entrypoint guidance

## What does not belong here

Do not turn this repository into the primary home of specialized layer content.

Avoid adding or expanding as primary truth:
- technique bundles
- skill bundles
- eval bundles
- memory objects
- agent runtime configurations
- routing datasets as authoritative content
- infrastructure implementation details
- large knowledge corpora that belong in Tree of Sophia or another owning layer

## Routing guidance

If you need implementation or layer-owned detail, check adjacent repositories first:
- `aoa-techniques`
- `aoa-skills`
- `aoa-evals`
- `aoa-routing`
- `aoa-memo`
- `aoa-agents`
- `abyss-stack`
- `Tree-of-Sophia`

If a task mainly strengthens a neighboring layer, route there instead of recreating its meaning here.
Do not invent implementation claims that are not yet public in this repository.

## Editing rules

When changing ecosystem definitions or boundaries:
- update affected center-layer documents coherently
- keep terminology stable unless there is a strong reason to rename
- prefer links and routing guidance over copying layer-owned detail
- keep derived surfaces clearly derived
- avoid vague umbrella language that blurs ownership

When creating new files:
- ask whether the file clarifies the center or belongs in another repository
- prefer compact coordination surfaces over sprawl

## Directory guidance

When working inside a specific center-layer surface, read the nearest local guide first:

- `docs/AGENTS.md`
- `generated/AGENTS.md`
- `schemas/AGENTS.md`
- `scripts/AGENTS.md`

These nested guides tighten the root rules for their directory without replacing them.

## Validation

When changing the center-layer surface, review:
- `README.md`
- `CHARTER.md`
- `ECOSYSTEM_MAP.md`
- `docs/LAYERS.md`
- `docs/FEDERATION_RULES.md`
- `ROADMAP.md`
- `generated/ecosystem_registry.min.json`

If you are editing `docs/`, `generated/`, `schemas/`, or `scripts/`, read the local `AGENTS.md` in that directory before changing files.

Run local validation when relevant:

```bash
python scripts/validate_ecosystem.py
```

## Definition of done

A change is done when:
- AoA is more intelligible after the edit
- source-of-truth boundaries are clearer, not blurrier
- routing to neighboring layers is easier
- no specialized layer was silently absorbed into the ecosystem center
- validation passes, or missing validation is disclosed honestly

## Style for this repository

Prefer:
- clear declarative writing
- explicit boundaries
- compact but durable terminology
- readable maps over abstract grandeur

Avoid:
- mythic vagueness where operational clarity is needed
- inflated manifesto language that hides ownership
- generic summaries that flatten layer distinctions

Human meaning, agent acceleration.
