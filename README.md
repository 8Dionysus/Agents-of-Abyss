# Agents of Abyss (AoA)

Agents of Abyss (AoA) is an evolving ecosystem for long-horizon agentic work.

It is not one bot, one workflow, or one narrow automation project.
It is a modular federation of layers for reusable practice, bounded execution, portable proof, memory, routing, and agent roles.

This repository is the constitutional and ecosystem-center repository of AoA.
It should remain the canonical high-level statement of what AoA is, how its layers relate, and how the federation should grow without collapsing into monolith or confusion.

## Start here

If you are new to AoA, use this path:

1. Read [CHARTER](CHARTER.md) for the mission and ownership boundaries.
2. Read [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) for the current repository roles.
3. Read [docs/LAYERS](docs/LAYERS.md) for the layer model.
4. Read [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) for source-of-truth discipline.
5. Read [ROADMAP](ROADMAP.md) for program-level direction.

## What this repository is for

`Agents-of-Abyss` exists to keep the AoA ecosystem intelligible.

It owns ecosystem-level truth about:
- what AoA is
- which layers belong to AoA
- what role each layer plays
- how the layers connect
- what federation rules should remain stable as AoA grows

It is the right place for:
- charter and principles
- ecosystem map
- layer model
- federation rules
- program-level roadmap
- compact machine-readable ecosystem registry

## What this repository is not for

This repository should not become the main corpus home of specialized AoA layers.

It should not absorb:
- technique bundles
- skill bundles
- eval bundles
- memory objects
- agent runtime configs
- routing datasets as primary truth
- infrastructure implementation details

AoA grows by adding clear layers, not by swallowing them into one root repository.

## Layer map

AoA currently consists of current and emerging layers with different ownership boundaries.

| layer | repository | main question |
|---|---|---|
| ecosystem center | `Agents-of-Abyss` | what is AoA as a whole? |
| practice canon | `aoa-techniques` | what practice is genuinely reusable? |
| execution canon | `aoa-skills` | how should an agent execute bounded work? |
| proof canon | `aoa-evals` | what bounded claim can we honestly defend? |
| navigation layer | `aoa-routing` | where should a model or human go next? |
| memory layer | `aoa-memo` | what should be remembered and how should it be recalled? |
| agent layer | `aoa-agents` | who acts under what role contract? |
| infrastructure substrate | `abyss-stack` | on what body does the system run? |
| knowledge architecture counterpart | `Tree-of-Sophia` | what knowledge world is being cultivated? |

See [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) and [docs/LAYERS](docs/LAYERS.md) for the fuller version.

## Local validation

This repository now includes a compact machine-readable ecosystem registry at:
- `generated/ecosystem_registry.min.json`

To validate the current center-layer surface locally, run:

```bash
python scripts/validate_ecosystem.py
```

Use this check when changing:
- the ecosystem registry
- repository roles
- center-layer ownership assumptions
- other compact federation surfaces that should stay coherent

## Relationship to Tree of Sophia

AoA is the operational and agentic side of the broader ecosystem.

Tree of Sophia (ToS) is the living knowledge architecture that AoA helps build, maintain, and operationalize.

In short:
- **AoA** = agents, techniques, workflows, proof, memory, routing, infrastructure
- **ToS** = living knowledge architecture, texts, concepts, lineages, interpretation layers

## Core principles

- truth and reproducibility over legend
- human meaning, agent acceleration
- modular growth over brittle fusion
- source-of-truth boundaries must stay explicit
- reviewability matters at every layer
- new tools should become new layers, not chaos multipliers

## Related repositories

### Current public pillars

- `aoa-techniques` — reusable techniques for coding agents and humans
- `aoa-skills` — bounded agent-facing execution workflows
- `aoa-evals` — bounded proof surfaces for agent quality and behavior
- `aoa-routing` — emerging navigation and dispatch layer

### Related system repositories

- `abyss-stack` — modular local and hybrid infrastructure substrate
- `Tree-of-Sophia` — living knowledge architecture counterpart

### Emerging repositories

- `aoa-memo` — planned memory and recall layer
- `aoa-agents` — planned role and persona layer

## For contributors and coding agents

Treat this repository as the canonical high-level entrypoint into AoA.

When in doubt:
- preserve the distinction between ecosystem truth and layer truth
- prefer clear ownership boundaries over convenience duplication
- prefer modular growth over premature fusion
- keep the ecosystem legible to both humans and smaller models

## Current status

AoA is moving from a loose project cluster toward a clearer public federation.
The specialized layers are maturing in parallel, while this repository becomes the stable center that names the whole.

## Maintainer

Dionysus
