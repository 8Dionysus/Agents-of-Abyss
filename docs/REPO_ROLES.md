# Repository Roles

This file is the compact operational guide to repository ownership across the AoA ecosystem.

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

## Routing rule of thumb

When deciding where something belongs:

1. If it defines reusable practice, it probably belongs in `aoa-techniques`.
2. If it defines bounded execution for agents, it probably belongs in `aoa-skills`.
3. If it defines proof or claim discipline, it probably belongs in `aoa-evals`.
4. If it defines recall, provenance, or temporal memory, it probably belongs in `aoa-memo`.
5. If it defines role-bearing agents, it probably belongs in `aoa-agents`.
6. If it defines dispatch across layers, it probably belongs in `aoa-routing`.
7. If it defines ecosystem-level identity or federation boundaries, it belongs here.

## Compact rule

Source repositories own meaning.
Meta repositories own maps.
Derived repositories own access layers.
