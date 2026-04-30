# AoA Ecosystem Map

This file is the human-first map of the current documented public AoA federation contour and its adjacent system anchors.

It names the federation. It does not absorb the inner truth of every repository it names.

## Authority

This map owns the public federation contour: which repositories and adjacent
anchors are currently named by the center, what role each one plays, and which
owner boundary protects it.

It does not own owner-local implementation, operational routing, mechanic
detail, or release promises. For those routes, use:

- [CHARTER](CHARTER.md) to decide whether the center may make a claim at all
- [docs/LAYERS](docs/LAYERS.md) to understand the conceptual layer
- [docs/REPO_ROLES](docs/REPO_ROLES.md) to decide where a change belongs
- [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) to preserve source-of-truth discipline

Machine companions:

- [`generated/ecosystem_registry.min.json`](generated/ecosystem_registry.min.json) for the public registry v2 contour
- [`generated/federation_supporting_inventory.min.json`](generated/federation_supporting_inventory.min.json) for supporting consumers outside registry v2

Registry v2 exposes four axes: `visibility`, `maturity`, `relation`, and
`kind`. The tables below keep current maturity separate from growth direction
so readers do not confuse present status with aspiration.

## When to use this file

Use this map when the question is:

- what belongs to the current public AoA contour?
- which repositories are source layers, derived layers, routing layers,
  adjacent anchors, or supporting consumers?
- whether a repository belongs in ecosystem registry v2 or the supporting
  inventory

If the question is "where should I edit?", continue to [docs/REPO_ROLES](docs/REPO_ROLES.md).
If the question is "what kind of layer is this?", continue to [docs/LAYERS](docs/LAYERS.md).
If the question is "does the center have authority to say this?", return to
[CHARTER](CHARTER.md).

## Center

| Repository | Role | Owns | Does not own | Current maturity | Growth direction |
|---|---|---|---|---|---|
| `Agents-of-Abyss` | constitutional polis and ecosystem center | ecosystem identity, layer map, federation rules, program-level direction, center mechanics law, root surface governance, center-entry capsules | technique truth, skill truth, eval truth, memory truth, agent truth, playbook truth, KAG truth, SDK/control-plane implementation, runtime infrastructure, ToS-authored corpus | active | proven center route and validator-backed public map |

## Public source-owned AoA layers

| Repository | Role | Owns | Does not own | Current maturity | Growth direction |
|---|---|---|---|---|---|
| `aoa-techniques` | practice canon | reusable techniques, evidence, examples, checks, and technique-level derived surfaces | skill bundles, eval bundles, global routing, memory objects | active | proven practice canon |
| `aoa-skills` | execution canon | bounded agent-facing workflows, trigger boundaries, verification guidance, and technique composition | primary technique truth, proof doctrine, memory objects | active | proven execution canon |
| `aoa-evals` | proof canon | portable eval bundles, bounded claims, verdict logic, blind spots, and comparison surfaces | workflow execution truth, memory objects, ecosystem routing truth | active | proven proof canon |
| `aoa-memo` | memory layer | memory objects, recall posture, memory interfaces, retention, forgetting, and provenance-aware recall conventions | eval canon, global routing truth, infrastructure internals | bootstrap | seed memory layer |
| `aoa-agents` | role layer | role definitions, persona boundaries, agent posture, handoff contracts, and role-facing memory/eval posture | skill corpus, eval canon, infrastructure internals, ToS-authored corpus truth | bootstrap | seed role layer |
| `aoa-playbooks` | scenario-composition layer | recurring multi-layer scenarios, composition patterns, fallback posture, and orchestration recipes with explicit boundaries | primary technique canon, primary skill canon, proof canon, infrastructure internals | bootstrap | seed scenario-composition layer |

## Public derived or routing-oriented AoA layers

| Repository | Role | Owns | Does not own | Current maturity | Growth direction |
|---|---|---|---|---|---|
| `aoa-stats` | derived observability layer | machine-first summary surfaces, derived windows, shared stats receipt envelopes, and evidence-linked read models | workflow meaning, proof meaning, route authority, quest authority, score authority | bootstrap | seed derived observability layer |
| `aoa-routing` | navigation and dispatch layer | cross-repo routing hints, dispatch surfaces, navigation posture, lightweight indexes, and a thin federation entry ABI | primary authored truth of other layers | bootstrap | seed navigation layer |
| `aoa-kag` | derived knowledge substrate | provenance-aware lifts, graph-ready projections, retrieval-ready structures, and bounded federation readiness surfaces derived from authoritative sources | source-authored truth of ToS or other layer-owned corpora | bootstrap | seed derived knowledge substrate |

## Supporting consumers outside ecosystem registry v2

| Repository | Role | Owns | Does not own | Current maturity | Registry posture |
|---|---|---|---|---|---|
| `aoa-sdk` | typed local-first consumer and control-plane helper spine | loading, integration, compatibility helpers, typed helper seams, controlled orchestration support | constitutional authority, source-layer truth, owner-local implementation acceptance | proven | tracked in `generated/federation_supporting_inventory.min.json`, not ecosystem registry v2 |

## Adjacent system anchors

| Repository | Role | Owns | Does not own | Current maturity | Growth direction |
|---|---|---|---|---|---|
| `Tree-of-Sophia` | source-first knowledge architecture counterpart | ToS-authored knowledge architecture, source-first structural meaning, lineage-aware conceptual discipline, and public tree-first tiny-entry seams | AoA center truth, AoA runtime infrastructure, AoA layer-owned operational truth | concept | seed source-first counterpart |
| `abyss-stack` | infrastructure substrate | runtime, storage, deployment, service composition, system body, lifecycle, and infrastructure security posture | AoA constitutional truth, ToS-authored corpus truth | active | proven runtime substrate |

## Public projection surfaces

| Surface | Role | Owns | Does not own |
|---|---|---|---|
| `8Dionysus` profile surfaces | public route map and selected shared-root projection source | profile orientation, entry posture, public-facing summary, and selected shared-root projection source truth | owner-local truth of AoA layers |
| `Dionysus` seed garden | seed garden and staging surface | intake packs, seeds, staging traces, and planting trace before owner landing | final owner truth |

## Scope note

Ecosystem registry v2 follows the center + public AoA layers + adjacent anchors
contour in this file. Supporting consumer surfaces, such as `aoa-sdk`, remain
outside ecosystem registry v2 by design and appear in the companion
machine-readable supporting inventory at
`generated/federation_supporting_inventory.min.json`.

Registry v2 should stay stable during the current root-document pass. A future
registry v3 belongs after the remaining root surfaces and technical districts
finish their review, so the new contract can reflect the full repository shape
rather than one document's wording.

## Reading rule

When there is ambiguity, use this map as a route back to the owner:

- the center names the federation
- source-owned layers author their primary object class
- derived layers derive from owner-owned evidence
- routing layers dispatch without authoring layer truth
- supporting consumers load, integrate, and activate without authority transfer
- substrate layers run the system body
- adjacent anchors keep their own authorship law
- public projection surfaces orient without overruling owners
