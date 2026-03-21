# AGENTS.md

## Repository role
This repository is the constitutional center of Agents of Abyss (AoA).

It owns the high-level truth of the AoA federation:
- ecosystem identity
- charter and principles
- layer map
- federation rules
- program-level direction
- compact registry surfaces that describe the ecosystem

Treat this repository as the canonical entrypoint into AoA, not as the place that absorbs the primary content of every neighboring layer.

## Priority of instructions
- Follow direct maintainer instructions first.
- Then follow this file.
- Prefer the source-of-truth repository for each layer over convenience edits in the ecosystem center.
- When a task clearly belongs to another repository, route there instead of recreating its meaning here.

## What belongs here
Use this repository for changes to:
- the public explanation of what AoA is
- ecosystem-level terminology and boundaries
- repository roles across the AoA federation
- layer definitions and their relationships
- federation rules and ownership discipline
- roadmap-level direction
- compact generated or machine-readable registry surfaces that summarize the ecosystem

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

AoA should grow by adding clear layers, not by swelling this repository into a monolith.

## Current reference surfaces
When orienting yourself, review the center-layer documents first:
- `README.md`
- `CHARTER`
- `ECOSYSTEM_MAP`
- `docs/LAYERS`
- `docs/FEDERATION_RULES`
- `ROADMAP`
- `generated/ecosystem_registry.min.json`
- `scripts/validate_ecosystem.py`

If a change touches ecosystem meaning, check whether more than one of these surfaces must move together.

## Working posture
- Preserve the distinction between ecosystem truth and layer truth.
- Prefer clear ownership boundaries over convenience duplication.
- Prefer modular growth over premature fusion.
- Keep the system legible to both humans and smaller models.
- Make assumptions, tradeoffs, and uncertainty explicit.
- Keep public artifacts public-safe. Do not add secrets, sensitive operational details, or private assumptions.
- Favor reviewable, reproducible edits over clever but opaque wording.

## Repository routing guidance
Use the smallest correct destination.

- `Agents-of-Abyss`: ecosystem identity, federation rules, layer map, program-level direction
- `aoa-techniques`: reusable engineering practice
- `aoa-skills`: bounded execution workflows
- `aoa-evals`: portable proof surfaces for bounded claims
- `aoa-routing`: navigation and dispatch surfaces
- `aoa-memo`: memory and recall surfaces
- `aoa-agents`: role contracts and handoff posture
- `aoa-playbooks`: recurring scenario compositions
- `aoa-kag`: derived provenance-aware knowledge substrate
- `abyss-stack`: runtime, deployment, storage, and service substrate
- `Tree-of-Sophia`: living knowledge architecture for philosophy and world thought

If the requested change primarily strengthens a neighboring layer, do not keep it here just because this repository is the center.

## Editing rules
When changing ecosystem definitions or boundaries:
- update all affected center-layer documents coherently
- keep terminology stable unless there is a strong reason to rename
- prefer links, references, and routing guidance over copying layer-owned detail
- keep generated surfaces derived from authoritative documents rather than silently replacing them
- avoid introducing vague umbrella language that blurs distinct layers

When creating new files:
- ask whether the file clarifies the center or whether it actually belongs in another repository
- keep new coordination surfaces compact and justified
- make machine-readable artifacts clearly generated and reviewable

## Validation
Run local validation when changing the center-layer surface:

```bash
python scripts/validate_ecosystem.py
```

Use this especially when changing:
- ecosystem registry data
- repository roles
- layer ownership assumptions
- compact federation surfaces that should remain coherent

Also perform a consistency pass across the human-facing center documents so they do not drift apart.

## Definition of done
A change is done when:
- AoA is more intelligible after the edit, not less
- source-of-truth boundaries remain explicit
- routing to neighboring layers is clearer
- validation passes, or any missing validation is clearly disclosed
- no specialized layer was silently absorbed into the ecosystem center

## Style for this repository
Write with precision and architectural clarity.

Prefer:
- short declarative statements
- explicit boundaries
- concrete repository ownership
- durable terminology

Avoid:
- mythic vagueness that hides responsibility
- inflated manifesto language where operational clarity is needed
- generic summaries that erase layer distinctions

Human meaning, agent acceleration.
