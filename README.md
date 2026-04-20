# Agents of Abyss (AoA)

Agents of Abyss (AoA) is the operational federation of explicit layers used to build, route, validate, and run long-horizon agentic systems.

It is not one bot, one workflow, or one narrow automation project. It is a modular federation with distinct public layers for reusable practice, bounded execution, portable proof, derived observability, navigation, memory, agent roles, scenario composition, derived knowledge substrate work, and infrastructure.

This repository is the constitutional and ecosystem-center repository of AoA. It names the federation, maps its layers, states the growth rules, and routes readers toward the repositories that own specialized meaning. It should keep the ecosystem intelligible without absorbing it.

> Current release: `v0.2.2`. See [CHANGELOG](CHANGELOG.md) for release notes.

## Start here

Read in this order:

1. [CHARTER](CHARTER.md) for mission and ownership boundaries
2. [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) for current repository roles
3. [docs/LAYERS](docs/LAYERS.md) for the layer model
4. [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) for source-of-truth discipline
5. [ROADMAP](ROADMAP.md) for program-level direction
6. [docs/PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md) for the current public onboarding, support, release, and CI posture of the center

If you only need the shortest outsider overview, stop after step 4 and return here for the route table below.
For low-context agents and machine-facing entry, inspect `generated/center_entry_map.min.json`.

## How to verify center claims

Read in this order when you need to check a public claim coming from the center:

1. [CHARTER](CHARTER.md) for what this repository owns and does not own
2. [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) for the current documented public federation contour
3. [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) for source-of-truth discipline
4. [ROADMAP](ROADMAP.md) for declared direction and current phase
5. [generated/center_entry_map.min.json](generated/center_entry_map.min.json), `python scripts/build_center_entry_map.py --check`, and `python scripts/validate_center_entry_map.py` for the compact machine-facing center-entry capsule
6. [generated/ecosystem_registry.min.json](generated/ecosystem_registry.min.json), [generated/federation_supporting_inventory.min.json](generated/federation_supporting_inventory.min.json), `python scripts/validate_ecosystem.py`, and `python -m pytest -q tests` for the compact v1 registry, the companion supporting inventory, and the current bounded center battery

Then branch by need:

- **structural trunk**: [docs/ROOTLINE](docs/ROOTLINE.md)
- **cross-repo direction surfaces and roadmap alternatives**: [docs/DIRECTION_SURFACES](docs/DIRECTION_SURFACES.md)
- **antifragility doctrine and first-wave boundary**: [docs/ANTIFRAGILITY](docs/ANTIFRAGILITY.md) and [docs/ANTIFRAGILITY_FIRST_WAVE](docs/ANTIFRAGILITY_FIRST_WAVE.md)
- **via negativa and anti-authority pruning posture**: [docs/VIA_NEGATIVA.md](docs/VIA_NEGATIVA.md), [docs/ANTI_AUTHORITY_RULES.md](docs/ANTI_AUTHORITY_RULES.md), [docs/ONE_IN_ONE_OUT.md](docs/ONE_IN_ONE_OUT.md), [FRAGILITY_BLACKLIST.md](FRAGILITY_BLACKLIST.md), and [DELETION_CANDIDATES.json](DELETION_CANDIDATES.json)
- **method and maturity**: [docs/METHOD_SPINE](docs/METHOD_SPINE.md)
- **growth refinery and candidate lineage**: [docs/REVIEWABLE_GROWTH_REFINERY](docs/REVIEWABLE_GROWTH_REFINERY.md), [docs/CANDIDATE_LINEAGE_CROSSWALK](docs/CANDIDATE_LINEAGE_CROSSWALK.md), [docs/OWNER_LANDING_AND_PRUNING](docs/OWNER_LANDING_AND_PRUNING.md), `python scripts/validate_candidate_lineage_contract.py --workspace-root /srv`, and `python scripts/validate_wave4_kernel_automation.py --workspace-root /srv`
- **self-agency continuity and bounded long-arc return**: [docs/SELF_AGENCY_CONTINUITY](docs/SELF_AGENCY_CONTINUITY.md)
- **component refresh and owner-owned self-maintenance**: [docs/COMPONENT_REFRESH_LAW](docs/COMPONENT_REFRESH_LAW.md)
- **counterpart bridge and KAG restraint**: [docs/COUNTERPART_BRIDGE](docs/COUNTERPART_BRIDGE.md)
- **witness and compost pilot**: [docs/WITNESS_COMPOST](docs/WITNESS_COMPOST.md)
- **ToS support waves**: [docs/TOS_GROWTH_SUPPORT](docs/TOS_GROWTH_SUPPORT.md), [docs/TOS_TEMPLATE_SUPPORT](docs/TOS_TEMPLATE_SUPPORT.md), [docs/TOS_LINEAGE_PILOT_SUPPORT](docs/TOS_LINEAGE_PILOT_SUPPORT.md), [docs/TOS_SOIL_PREP_SUPPORT](docs/TOS_SOIL_PREP_SUPPORT.md)
- **Agon preparation holding boundary**: [docs/AGON_PREPARATION_POSTURE](docs/AGON_PREPARATION_POSTURE.md)
- **Agon imposition gate**: [docs/AGON_IMPOSITION_POSTURE](docs/AGON_IMPOSITION_POSTURE.md), [docs/AGON_SURVIVAL_CRITERIA](docs/AGON_SURVIVAL_CRITERIA.md), [docs/AGON_DOUBT_AUDIT](docs/AGON_DOUBT_AUDIT.md), [docs/PRE_AGON_BASELINE](docs/PRE_AGON_BASELINE.md), [generated/agon_imposition_readiness.min.json](generated/agon_imposition_readiness.min.json), `python scripts/build_agon_imposition_readiness.py --check`, `python scripts/validate_agon_imposition_readiness.py`, and `python -m pytest -q tests/test_agon_imposition_readiness.py`
- **Agon lawful move language**: [docs/AGON_LAWFUL_MOVE_LANGUAGE](docs/AGON_LAWFUL_MOVE_LANGUAGE.md), [docs/AGON_MOVE_REGISTRY_MODEL](docs/AGON_MOVE_REGISTRY_MODEL.md), [docs/AGON_MOVE_OWNER_HANDOFFS](docs/AGON_MOVE_OWNER_HANDOFFS.md), [docs/AGON_WAVE3_LANDING](docs/AGON_WAVE3_LANDING.md), [generated/agon_lawful_move_registry.min.json](generated/agon_lawful_move_registry.min.json), `python scripts/build_agon_lawful_move_registry.py --check`, `python scripts/validate_agon_lawful_moves.py`, and `python -m pytest -q tests/test_agon_lawful_moves.py`
- **adjunct RPG reflection contour**: [docs/RPG_LAYER_MODEL](docs/RPG_LAYER_MODEL.md), [docs/RPG_FIRST_WAVE](docs/RPG_FIRST_WAVE.md), [docs/RPG_SECOND_WAVE](docs/RPG_SECOND_WAVE.md), [docs/RPG_SKILLS_AND_FEATS](docs/RPG_SKILLS_AND_FEATS.md), [docs/RPG_ARCHITECTURE_RFC](docs/RPG_ARCHITECTURE_RFC.md), [docs/RPG_CANONICAL_TERMINOLOGY](docs/RPG_CANONICAL_TERMINOLOGY.md), [docs/RPG_BOUNDARY_MAP](docs/RPG_BOUNDARY_MAP.md)
- **public onboarding, support, release, and CI posture**: [docs/PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md)

## Quick route table

| repository | owns | go here when |
|---|---|---|
| `Agents-of-Abyss` | ecosystem identity, layer map, federation rules, program-level direction | you need the center, the map, or the constitutional view of AoA |
| `aoa-techniques` | reusable engineering practice | you need durable techniques rather than one-off fixes |
| `aoa-skills` | bounded agent-facing execution workflows | you need an executable workflow built from reusable techniques |
| `aoa-evals` | portable proof surfaces for bounded claims | you need to check quality, boundaries, regressions, or defensible claims |
| `aoa-stats` | derived observability and machine-first summary layer | you need evidence-linked summaries of movement without promoting stats into workflow, proof, or quest authority |
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
- **reviewable growth refinery** with one narrow route kept legible across checkpoint carry, reviewed candidate identity, seed staging, and owner landing
- **self-agency continuity** with explicit anchors, bounded revision windows, and governed reanchor rather than runtime-autonomy mythology
- **owner-owned component refresh** for internal technical surfaces through reviewed drift hints, owner receipts, and explicit refresh boundaries rather than mystical self-healing
- **source-first donor refinement** along `donor -> technique/skill -> playbook -> eval`
- **bounded counterpart bridges** with `aoa-kag` remaining derived and conceptual origin remaining in `Tree-of-Sophia`
- **contract-first witness and compost** before any deeper runtime instrumentation wave
- **explicit, reviewable ToS support** for growth law, corpus scaffold, lineage pilot, and soil prep without AoA authoring ToS meaning
- **Agon preparation holding boundary** that keeps Agon inside the center as a provisional future protocol contour, not a new sibling repo, not ToS canon, and not runtime substrate
- **Agon imposition gate** that places the current system under Agon survival scrutiny without starting a live arena protocol, a sibling repo, ToS canon, or runtime substrate
- **Agon lawful move language** that gives the center a first pre-protocol legal vocabulary without turning lawful moves into runtime packets, verdict law, scars, retention, or ToS authority

The linked wave notes above hold the compact doctrine for each declared move.

## What this repository owns

- ecosystem identity
- layer map
- federation rules
- program-level direction
- compact center-entry capsule surfaces
- compact ecosystem-level registry surfaces

## Public support and release posture

For the shortest public statement of what the center may claim, how those claims are verified, and which CI tiers reinforce them, use [docs/PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md).

## What this repository does not own

- technique truth
- skill truth
- eval truth
- stats-layer derived view truth
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
