# Agents of Abyss (AoA)

Agents of Abyss (AoA) is the operational federation of explicit layers used to build, route, validate, and run long-horizon agentic systems.

It is not one bot, one workflow, or one narrow automation project. It is a modular federation with distinct public layers for reusable practice, bounded execution, portable proof, navigation, memory, agent roles, scenario composition, derived knowledge substrate work, and infrastructure.

This repository is the constitutional and ecosystem-center repository of AoA. It names the federation, maps its layers, states the growth rules, and routes readers toward the repositories that own specialized meaning. It should keep the ecosystem intelligible without absorbing it.

## Start here

Read in this order:

1. [CHARTER](CHARTER.md) for mission and ownership boundaries
2. [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) for current repository roles
3. [docs/LAYERS](docs/LAYERS.md) for the layer model
4. [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) for source-of-truth discipline
5. [ROADMAP](ROADMAP.md) for program-level direction
6. [docs/PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md) for the current public onboarding, support, release, and CI posture of the center

If you only need the shortest outsider overview, stop after step 4 and return here for the route table below.

## How to verify center claims

Read in this order when you need to check a public claim coming from the center:

1. [CHARTER](CHARTER.md) for what this repository owns and does not own
2. [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) for the current documented public federation contour
3. [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) for source-of-truth discipline
4. [ROADMAP](ROADMAP.md) for declared direction and current phase
5. [generated/ecosystem_registry.min.json](generated/ecosystem_registry.min.json), [generated/federation_supporting_inventory.min.json](generated/federation_supporting_inventory.min.json), `python scripts/validate_ecosystem.py`, and `python -m pytest -q tests` for the compact v1 registry, the companion supporting inventory, and the current bounded center battery

Then branch by need:

- **structural trunk**: [docs/ROOTLINE](docs/ROOTLINE.md)
- **method and maturity**: [docs/METHOD_SPINE](docs/METHOD_SPINE.md)
- **counterpart bridge and KAG restraint**: [docs/COUNTERPART_BRIDGE](docs/COUNTERPART_BRIDGE.md)
- **witness and compost pilot**: [docs/WITNESS_COMPOST](docs/WITNESS_COMPOST.md)
- **ToS support waves**: [docs/TOS_GROWTH_SUPPORT](docs/TOS_GROWTH_SUPPORT.md), [docs/TOS_TEMPLATE_SUPPORT](docs/TOS_TEMPLATE_SUPPORT.md), [docs/TOS_LINEAGE_PILOT_SUPPORT](docs/TOS_LINEAGE_PILOT_SUPPORT.md), [docs/TOS_SOIL_PREP_SUPPORT](docs/TOS_SOIL_PREP_SUPPORT.md)
- **adjunct RPG reflection contour**: [docs/RPG_LAYER_MODEL](docs/RPG_LAYER_MODEL.md), [docs/RPG_FIRST_WAVE](docs/RPG_FIRST_WAVE.md), [docs/RPG_SECOND_WAVE](docs/RPG_SECOND_WAVE.md), [docs/RPG_SKILLS_AND_FEATS](docs/RPG_SKILLS_AND_FEATS.md), [docs/RPG_ARCHITECTURE_RFC](docs/RPG_ARCHITECTURE_RFC.md), [docs/RPG_CANONICAL_TERMINOLOGY](docs/RPG_CANONICAL_TERMINOLOGY.md), [docs/RPG_BOUNDARY_MAP](docs/RPG_BOUNDARY_MAP.md)
- **public onboarding, support, release, and CI posture**: [docs/PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md)

## Quick route table

| repository | owns | go here when |
|---|---|---|
| `Agents-of-Abyss` | ecosystem identity, layer map, federation rules, program-level direction | you need the center, the map, or the constitutional view of AoA |
| `aoa-techniques` | reusable engineering practice | you need durable techniques rather than one-off fixes |
| `aoa-skills` | bounded agent-facing execution workflows | you need an executable workflow built from reusable techniques |
| `aoa-evals` | portable proof surfaces for bounded claims | you need to check quality, boundaries, regressions, or defensible claims |
| `aoa-routing` | navigation and dispatch surfaces plus a thin federation entry ABI | you need the smallest next route across AoA surfaces without promoting routing into authority |
| `aoa-memo` | explicit memory and recall surfaces | you need reviewable memory, provenance, or recall posture |
| `aoa-agents` | role contracts, persona boundaries, handoff posture | you need to define who acts and under what role contract |
| `aoa-playbooks` | scenario composition and method surfaces | you need recurring cross-layer operational scenarios |
| `aoa-kag` | derived knowledge substrate and bounded federation readiness surfaces | you need provenance-aware, retrieval-ready, or graph-ready structures without replacing source-owned meaning |
| `abyss-stack` | runtime, deployment, storage, and service substrate | you need the body the system runs on |
| `Tree-of-Sophia` | source-first living knowledge architecture for philosophy and world thought | you need the knowledge world AoA helps build and support |

## Current contour

The current center-level framing and declared near-term direction are:

- **trunk-first structure** to reduce meaning drift, archive inflation, and autonomy rhetoric
- **method-centered growth** with scenario-level method routed into `aoa-playbooks`
- **source-first donor refinement** along `donor -> technique/skill -> playbook -> eval`
- **bounded counterpart bridges** with `aoa-kag` remaining derived and conceptual origin remaining in `Tree-of-Sophia`
- **contract-first witness and compost** before any deeper runtime instrumentation wave
- **explicit, reviewable ToS support** for growth law, corpus scaffold, lineage pilot, and soil prep without AoA authoring ToS meaning

The linked wave notes above hold the compact doctrine for each declared move.

## What this repository owns

- ecosystem identity
- layer map
- federation rules
- program-level direction
- compact ecosystem-level registry surfaces

## Public support and release posture

For the shortest public statement of what the center may claim, how those claims are verified, and which CI tiers reinforce them, use [docs/PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md).

## What this repository does not own

- technique truth
- skill truth
- eval truth
- memo truth
- agent-role truth
- playbook truth
- KAG-derived truth as authored source
- runtime implementation detail
- ToS-authored knowledge truth

## Related public surfaces

- [`abyss-stack`](https://github.com/8Dionysus/abyss-stack) owns runtime, deployment, storage, and service posture
- [`Tree-of-Sophia`](https://github.com/8Dionysus/Tree-of-Sophia) owns source-first knowledge architecture and authored ToS meaning
- [`aoa-sdk`](https://github.com/8Dionysus/aoa-sdk) is the typed local-first consumer and orchestration spine for source-owned AoA surfaces; it is a supporting consumer surface, not the constitutional center, and it stays outside the compact registry v1 by design while remaining visible in the supporting machine-readable inventory

AoA should grow by adding clear, reviewable layers rather than collapsing everything into the center.
