# AoA Ecosystem Map

This file is the human-first map of the current documented public AoA federation contour and its adjacent system anchors.

It names the federation. It does not absorb the inner truth of every repository it names.

## Center

| Repository | Role | Owns | Does not own | Maturity crosswalk |
|---|---|---|---|---|
| `Agents-of-Abyss` | constitutional polis and ecosystem center | ecosystem identity, layer map, federation rules, program-level direction, center mechanics, root surface governance | technique truth, skill truth, eval truth, memory truth, agent truth, playbook truth, KAG truth, runtime infrastructure, ToS-authored corpus | active -> proven |

## Public source-owned AoA layers

| Repository | Role | Owns | Does not own | Maturity crosswalk |
|---|---|---|---|---|
| `aoa-techniques` | practice canon | reusable techniques, evidence, examples, checks, and technique-level derived surfaces | skill bundles, eval bundles, global routing, memory objects | active -> proven |
| `aoa-skills` | execution canon | bounded agent-facing workflows, trigger boundaries, verification guidance, and technique composition | primary technique truth, proof doctrine, memory objects | active -> proven |
| `aoa-evals` | proof canon | portable eval bundles, bounded claims, verdict logic, blind spots, and comparison surfaces | workflow execution truth, memory objects, ecosystem routing truth | active -> proven |
| `aoa-memo` | memory layer | memory objects, recall posture, memory interfaces, retention, forgetting, and provenance-aware recall conventions | eval canon, global routing truth, infrastructure internals | bootstrap -> seed |
| `aoa-agents` | role layer | role definitions, persona boundaries, agent posture, handoff contracts, and role-facing memory/eval posture | skill corpus, eval canon, infrastructure internals, ToS-authored corpus truth | bootstrap -> seed |
| `aoa-playbooks` | scenario-composition layer | recurring multi-layer scenarios, composition patterns, fallback posture, and orchestration recipes with explicit boundaries | primary technique canon, primary skill canon, proof canon, infrastructure internals | bootstrap -> seed |

## Public derived or routing-oriented AoA layers

| Repository | Role | Owns | Does not own | Maturity crosswalk |
|---|---|---|---|---|
| `aoa-stats` | derived observability layer | machine-first summary surfaces, derived windows, shared stats receipt envelopes, and evidence-linked read models | workflow meaning, proof meaning, route authority, quest authority, score authority | bootstrap -> seed |
| `aoa-routing` | navigation and dispatch layer | cross-repo routing hints, dispatch surfaces, navigation posture, lightweight indexes, and a thin federation entry ABI | primary authored truth of other layers | bootstrap -> seed |
| `aoa-kag` | derived knowledge substrate | provenance-aware lifts, graph-ready projections, retrieval-ready structures, and bounded federation readiness surfaces derived from authoritative sources | source-authored truth of ToS or other layer-owned corpora | bootstrap -> seed |

## Supporting consumers outside ecosystem registry v2

| Repository | Role | Owns | Registry posture |
|---|---|---|---|
| `aoa-sdk` | typed local-first consumer and helper spine | loading, integration, compatibility helpers, typed helper seams, and controlled orchestration support | tracked in `generated/federation_supporting_inventory.min.json`, not ecosystem registry v2 |

## Adjacent system anchors

| Repository | Role | Owns | Does not own | Maturity crosswalk |
|---|---|---|---|---|
| `Tree-of-Sophia` | source-first knowledge architecture counterpart | ToS-authored knowledge architecture, source-first structural meaning, lineage-aware conceptual discipline, and public tree-first tiny-entry seams | AoA center truth, AoA runtime infrastructure, AoA layer-owned operational truth | active-conceptual -> seed |
| `abyss-stack` | infrastructure substrate | runtime, storage, deployment, service composition, system body, lifecycle, and infrastructure security posture | AoA constitutional truth, ToS-authored corpus truth | active -> proven |

## Public projection surfaces

| Surface | Role | Owns | Does not own |
|---|---|---|---|
| `8Dionysus` profile surfaces | public route map and selected shared-root projection | orientation, entry posture, and public-facing summary of selected surfaces | owner-local truth of AoA layers |
| `Dionysus` seed garden | seed garden and staging surface | intake packs, seeds, and staging traces before owner landing | final owner truth |

## Scope note

Ecosystem registry v2 follows the center + public AoA layers + adjacent anchors contour in this file. It splits public naming into `visibility`, `maturity`, `relation`, and `kind` axes so status, role, and ownership do not collapse into one field. Supporting consumer surfaces, such as `aoa-sdk`, remain outside ecosystem registry v2 by design and appear in the companion machine-readable supporting inventory at `generated/federation_supporting_inventory.min.json`.

## Reading rule

When there is ambiguity:

- the center names the federation
- source-owned layers own their primary object class
- derived layers stay derived
- routing layers stay routing
- substrate layers run the system but do not author meaning
- adjacent anchors keep their own authorship law
- public projection surfaces orient, but do not overrule owners
