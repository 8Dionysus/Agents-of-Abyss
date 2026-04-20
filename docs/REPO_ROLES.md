# Repository Roles

This file is the compact operational guide to repository ownership across the AoA ecosystem, distinguishing ecosystem-level stewardship from specialized corpus and runtime artifacts.

Use it when the question is not only "what exists?" but also:
- where should this change go?
- what repository owns this truth?
- what repository should stay out of it?

## Core repositories

| repository | role | owns | does not own | primary artifacts | main question |
|---|---|---|---|---|---|
| `Agents-of-Abyss` | ecosystem center | ecosystem identity, charter, layer map, federation rules, ecosystem registry, program-level roadmap | specialized corpus truth, runtime infra, technique bundles, skill bundles, eval bundles, memory objects | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md`, `generated/ecosystem_registry.min.json` | what is AoA as a whole? |
| `aoa-techniques` | practice canon | reusable techniques, origin evidence, checks, examples, technique-level derived surfaces | skill truth, eval truth, memory truth, cross-repo routing truth | `TECHNIQUE.md`, notes, checks, examples, technique catalogs | what practice is genuinely reusable? |
| `aoa-skills` | execution canon | bounded agent-facing workflows, trigger boundaries, verification guidance, technique composition manifests | primary technique meaning, proof doctrine, memory objects, ecosystem-center governance | `SKILL.md`, `techniques.yaml`, agent policy files, skill support artifacts | how should an agent execute bounded work? |
| `aoa-evals` | proof canon | bounded proof surfaces, verdict logic, scoring guidance, comparison modes, blind spots | workflow execution truth, technique truth, memory truth, ecosystem routing truth | `EVAL.md`, `eval.yaml`, evidence/support artifacts | what bounded claim can we honestly defend? |
| `aoa-routing` | navigation layer | cross-repo dispatch, lightweight entrypoints, recommended paths, model-facing access surfaces | authored technique, skill, eval, or memory truth | router manifests, path surfaces, dispatch registries, `generated/federation_entrypoints.min.json`, `docs/FEDERATION_ENTRY_ABI.md` | where should a model or human go next? |
| `aoa-stats` | derived observability layer | machine-first summaries, derived windows, shared stats event envelope, and bounded summary builders | workflow meaning, proof meaning, live route authority, quest-state authority | `generated/*.json`, `generated/summary_surface_catalog.min.json`, `schemas/stats-event-envelope.schema.json`, stats builders and validators | what movement is visible across owner-local evidence without turning stats into authority? |

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

| repository | role in the wider system | compact registry v1 note |
|---|---|---|
| `aoa-sdk` | typed local-first consumer and orchestration surface for source-owned AoA repositories | routed from the center, but intentionally outside compact registry v1 |

## Routing rule of thumb

When deciding where something belongs:

1. If it defines reusable practice, it probably belongs in `aoa-techniques`.
2. If it defines bounded execution for agents, it probably belongs in `aoa-skills`.
3. If it defines proof or claim discipline, it probably belongs in `aoa-evals`.
4. If it defines recall, provenance, or temporal memory, it probably belongs in `aoa-memo`.
5. If it defines role-bearing agents, it probably belongs in `aoa-agents`.
6. If it defines dispatch across layers, it probably belongs in `aoa-routing`.
7. If it defines machine-first summary surfaces or derived observability windows, it probably belongs in `aoa-stats`.
8. If it defines ecosystem-level identity or federation boundaries, it belongs here.
9. If it defines future Agon law, imposition audit, owner binding law, arena
   lifecycle, lawful moves, gate-routing handoff, contradiction-ledger posture, or promotion
   discipline, route it here first as center-owned protocol preparation and
   imposition unless a later reviewed center decision narrows that contour. If
   it defines agonic actor form, civil/service assistant variants, requested
   owner landings, routing gates, trial scenarios, verdicts, scars, derived
   summaries, SDK helpers, runtime services, or ToS canonization, route that
   slice to the owning layer named in `docs/AGON_PREPARATION_POSTURE.md`,
   `docs/AGON_IMPOSITION_POSTURE.md`, `docs/AGON_LAWFUL_MOVE_LANGUAGE.md`,
   `docs/AGON_MOVE_OWNER_BINDING.md`, `docs/AGON_GATE_ROUTING_HANDOFF.md`,
   and `docs/AGON_OWNER_REPO_REQUESTS.md`.

## Compact rule

Source repositories own meaning.
Meta repositories own maps.
Derived repositories own bounded lifts, views, and access layers.

Compact registry v1 covers the center, the public AoA layers, and the adjacent system anchors listed in the ecosystem map.
Supporting consumer surfaces stay routable from the center but remain outside compact registry v1 until a later map version says otherwise.
