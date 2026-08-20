# Repository Roles

This file is the compact operational guide to repository ownership across the AoA ecosystem, distinguishing ecosystem-level stewardship from specialized corpus and runtime artifacts.

Use it when the question is not only "what exists?" but also:
- where should this change go?
- what repository owns this truth?
- what repository should stay out of it?

## Core repositories

| repository | role | owns | does not own | primary artifacts | main question |
|---|---|---|---|---|---|
| `Agents-of-Abyss` | ecosystem center | ecosystem identity, system form, charter, layer map, federation rules, ecosystem registry, program-level roadmap | specialized corpus truth, runtime infra, technique bundles, skill bundles, eval bundles, memory objects | `README.md`, `CHARTER.md`, `DESIGN.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md`, `generated/ecosystem_registry.min.json` | what is AoA as a whole? |
| `aoa-techniques` | practice canon | reusable techniques, origin evidence, checks, examples, technique-level derived surfaces | skill truth, eval truth, memory truth, cross-repo routing truth | `TECHNIQUE.md`, notes, checks, examples, technique catalogs | what practice is genuinely reusable? |
| `aoa-skills` | execution canon | bounded agent-facing workflows, trigger boundaries, verification guidance, technique composition manifests | primary technique meaning, proof doctrine, memory objects, ecosystem-center governance | `SKILL.md`, `techniques.yaml`, agent policy files, skill support artifacts | how should an agent execute bounded work? |
| `aoa-evals` | proof canon | bounded proof surfaces, verdict logic, scoring guidance, comparison modes, blind spots | workflow execution truth, technique truth, memory truth, ecosystem routing truth | `EVAL.md`, `eval.yaml`, evidence/support artifacts | what bounded claim can we honestly defend? |
| `aoa-routing` | deprecated routing predecessor | preserved route history, rollback evidence, and maintenance-only compatibility | new dispatch authority, new route contracts, or authored technique, skill, eval, or memory truth | frozen predecessor manifests, release receipts, and historical route surfaces | what must remain reversible until a separate archive decision? |
| `aoa-stats` | derived observability layer | machine-first summaries, derived windows, shared stats event envelope, and bounded summary builders | workflow meaning, proof meaning, live route authority, quest-state authority | `generated/*.json`, `generated/summary_surface_catalog.min.json`, `schemas/stats-event-envelope.schema.json`, stats builders and validators | what movement is visible across owner-local evidence without turning stats into authority? |
| `aoa-dashboard` | Goal Space/operator derived layer | owner-bounded derived Goal Space projections, provenance/freshness/missingness views, Pressure Inbox, actor activity, annotations, and non-executing action intents | roles, responsibility, task DAG, RunPlan, runtime, proof, memory, stats meaning, KAG authority, owner acceptance, or execution | `contracts/organ_contract.json`, `docs/ORGAN_CONTRACT.md`, projection contracts, and local validators | what can an operator see and route without creating a second authority plane? |

## Emerging repositories

| repository | intended role | likely owned surfaces | should avoid becoming |
|---|---|---|---|
| `aoa-memo` | memory and recall layer | memory objects, provenance threads, temporal relevance, recall policies, salience-oriented retrieval surfaces | proof canon, workflow canon, or routing center |
| `aoa-agents` | role and persona layer | agent profiles, role contracts, preferred skill families, handoff rules, model-fit notes | duplicate skill corpus, routing layer, or memory store |
| `aoa-playbooks` | scenario-composition layer | recurring multi-layer routes, handoff-aware scenarios, fallback posture, expected evidence posture | single-skill home, hidden orchestration sprawl, or proof canon |
| `aoa-kag` | derived knowledge substrate | provenance-aware lifts, chunk maps, node and edge projections, retrieval-ready surfaces, bounded federation readiness surfaces | authored source truth, routing center, or hidden graph empire |

## Related repositories

| repository | role in the wider system |
|---|---|
| `abyss-stack` | infrastructure substrate and implementation body for AoA-oriented systems |
| `Tree-of-Sophia` | living knowledge architecture that AoA helps build and operationalize, including source-authored node law and the public tiny-entry seam |

## Supporting consumer surfaces

| repository | role in the wider system | registry posture |
|---|---|---|
| `aoa-sdk` | canonical typed routing/control-plane and local-first consumer for source-owned AoA repositories | routed from the center through `generated/federation_supporting_inventory.min.json`; routing authority does not transfer source meaning or runtime execution |

## OS Abyss artifact trust-plane route

The OS-level artifact trust contract is named in
[`FEDERATION_RULES`](FEDERATION_RULES.md) as
`os_abyss_artifact_trust_plane_v1`.

The center organ-by-organ posture matrix lives in
[`ARTIFACT_TRUST_POSTURE`](ARTIFACT_TRUST_POSTURE.md). Use it to decide which
minimum artifact controls fit each repository before entering the owner-local
producer route or the `abyss-machine` trust-gate.

| organ or repository | trust-plane role | first question |
|---|---|---|
| `Agents-of-Abyss` | center doctrine and owner split | what is the OS-wide authority boundary? |
| `abyss-machine` | host enforcement, durable registry, trust-gate, trust root modes, update/transparency lane | may this host consume this artifact now? |
| `.aoa` | session evidence routing, rehydration, graph/index projections, generated/export surfaces when machine-consumable | what evidence or session context routes to an owner, without becoming law? |
| `aoa-sdk` | typed read/assert API for trust-plane JSON surfaces | how can an agent read the trust verdict safely? |
| `aoa-evals` | proof scenarios and regression claims | which trust-plane behavior has been proven, and what blind spots remain? |
| source-owner repositories | producer profiles, artifact sidecars, owner validators, release/export triggers | what artifact does this owner produce, and under what controls? |

GitHub is only one producer adapter in this route. Host/runtime/workspace trust
must remain legible outside GitHub as well.

## Routing rule of thumb

When deciding where something belongs:

1. If it defines reusable practice, it probably belongs in `aoa-techniques`.
2. If it defines bounded execution for agents, it probably belongs in `aoa-skills`.
3. If it defines proof or claim discipline, it probably belongs in `aoa-evals`.
4. If it defines recall, provenance, or temporal memory, it probably belongs in `aoa-memo`.
5. If it defines role-bearing agents, it probably belongs in `aoa-agents`.
6. If it defines dispatch across layers, it probably belongs in the routing
   control plane in `aoa-sdk`.
7. If it defines machine-first summary surfaces or derived observability windows, it probably belongs in `aoa-stats`.
8. If it defines ecosystem-level identity, system form, or federation boundaries, it belongs here.
9. If it is mechanic-shaped, start with `mechanics/README.md` and the owning
   mechanic package. Use the package `README.md`, `PARTS.md`,
   `OWNER_REQUESTS.md`, and `PROVENANCE.md` when those surfaces exist.

## Compact rule

Source repositories own meaning.
Meta repositories own maps.
Derived repositories own bounded lifts, views, and access layers.

Ecosystem registry v2 covers the center, the public AoA layers, and the adjacent system anchors listed in the ecosystem map.
It uses separate `visibility`, `maturity`, `relation`, and `kind` axes so public contour, maturity posture, and repository relationship stay legible.
Supporting consumer surfaces stay routable from the center but remain in the companion supporting inventory unless a later public map explicitly promotes them into the ecosystem registry.
