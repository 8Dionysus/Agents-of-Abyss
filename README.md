# Agents of Abyss (AoA)

![Agents of Abyss expedition crossing the abyss toward a lit citadel](assets/agents-of-abyss-readme-banner.png)

`Agents-of-Abyss` is the constitutional polis of AoA.

AoA as a whole is the federation: source-owned repositories, derived layers, routing surfaces, supporting consumers, public profile surfaces, and adjacent system anchors. This repository is not that whole federation. It is the polis where the federation is named, mapped, governed, audited, and kept legible.

Federation streams may enter this polis as claims, maps, contracts, release posture, stop-lines, root-surface placement questions, and machine capsules. They must leave with clearer ownership than they had on entry.

This README is human-first and agent-useful. A person should see the city before entering its districts. An agent should know which owner surface to touch before changing anything.

> Current release: `v0.2.3`. See [CHANGELOG](CHANGELOG.md) for release notes.

## Current state and highest aim

| Axis | Current sober status | Highest aim |
|---|---|---|
| Constitutional center | Proven center surface for identity, layer map, federation rules, and program-level direction. | A stable civic root for the AoA federation: clear enough for humans, strict enough for agents. |
| Federation contour | Ecosystem registry v2 names the public AoA contour through separate visibility, maturity, relation, and kind axes. Supporting consumers are tracked separately. | Every layer can grow without stealing another layer's truth. |
| Root surface governance | Root surface law is planted, first root-leak cleanup is defined, and technical districts now get local gates. | The root should stay a city gate: lawful, readable, sparse, and strict about what belongs nearby. |
| Mechanics | Agon, Experience, recurrence/return, growth, quest/RPG reflection, antifragility, and ToS support are mostly center contracts, doctrine, or pre-protocol routes. | A readable engineering philosophy where every mechanic has a home, owner split, stop-line, and verification path. |
| Runtime | The center does not run the body. Runtime belongs to `abyss-stack` or later owner-local gates. | Runtime can enact validated mechanics without becoming the source of law or meaning. |
| Self-agency | Continuity is anchor-bound and reviewable. No permissionless autonomy, hidden memory sovereignty, or live arena authority is claimed here. | Long-horizon agency can preserve continuity, revise method, and return to anchors without losing provenance or human judgment. |

## Start here

Read in this order:

1. [CHARTER](CHARTER.md) for the center's mission and authority boundary.
2. [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) for the current public federation contour.
3. [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) for source-of-truth discipline.
4. [docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) before adding, moving, deleting, or renaming any root-level file.
5. [ROADMAP](ROADMAP.md) for current program-level direction.
6. [docs/LAYERS](docs/LAYERS.md) and [docs/REPO_ROLES](docs/REPO_ROLES.md) for layer roles and ownership routing.
7. [release-support/PUBLIC_SUPPORT_POSTURE](mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md) for what the center may honestly claim and how CI reinforces it.

If you only need the shortest outside overview, stop after step 3. If you are
a low-context agent or small model, also inspect
[`generated/center_entry_map.min.json`](generated/center_entry_map.min.json).
The route modes behind this entry surface are governed by
[`docs/START_HERE_ROUTE_CONTRACT.md`](docs/START_HERE_ROUTE_CONTRACT.md).

## Route modes

Every public entry surface must expose the same route-mode vocabulary:

| Route mode | Use when | Start surface |
|---|---|---|
| `first-reading` | you need the shortest honest center overview | `README.md` |
| `root-editing` | you will add, move, delete, rename, or rewrite a root surface | `docs/ROOT_SURFACE_LAW.md` |
| `direction-change` | you will change roadmap, phase, maturity, release contour, or declared direction | `ROADMAP.md` |
| `ownership-routing` | you need to decide which repository owns a change | `docs/REPO_ROLES.md` |
| `mechanic-change` | you will touch Agon, Experience, recurrence, method/growth, antifragility, quest/RPG, release-support, or ToS support | `mechanics/README.md` |
| `public-claim-validation` | a sentence sounds like a public promise | `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md` |
| `low-context-agent` | you need a compact machine-facing route before full reading | `generated/center_entry_map.min.json` |
| `district-work` | you are already inside a technical district | nearest local `README.md` |

## How to verify center claims

Use this tree before trusting a claim made by the center:

| Branch | Question | Primary surface | Check |
|---|---|---|---|
| Authority | Is this actually a center-owned claim? | [CHARTER](CHARTER.md) | The claim must fit the center's ownership boundary. |
| Contour | Does the current map name the repo, layer, or adjacent anchor being discussed? | [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) | Cross-check [`generated/ecosystem_registry.min.json`](generated/ecosystem_registry.min.json) and [`generated/federation_supporting_inventory.min.json`](generated/federation_supporting_inventory.min.json). |
| Ownership law | Does the claim preserve source truth, derived truth, routing truth, runtime truth, and ToS-authored meaning as separate things? | [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) | Cross-check [docs/REPO_ROLES](docs/REPO_ROLES.md) and [release-support/PUBLIC_SUPPORT_POSTURE](mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md). |
| Surface placement | Does this object deserve to live in the repository root? | [docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) | If it is a wave receipt, audit artifact, design note, or generated object, route it away from root. |
| Direction | Is this current program direction rather than an old contour, wave note, or copied promise? | [ROADMAP](ROADMAP.md) | Cross-check [release-support/DIRECTION_SURFACES](mechanics/release-support/docs/DIRECTION_SURFACES.md). |
| Release support | Is a draft, quest, checkpoint, landing, handoff, public claim, or GitHub release becoming a supportable state transition? | [release-support](mechanics/release-support/README.md) | Use [release-support/PARTS](mechanics/release-support/PARTS.md) before public wording hardens. |
| Machine contract | Can the compact surfaces and AGENTS mesh still rebuild and validate? | generated capsules, AGENTS cards, and validators | Run the commands below. |
| Mechanic route | Is the claim about a process, engineering philosophy, Agon, Experience, recurrence, quest/RPG, antifragility, or ToS support? | [mechanics/README](mechanics/README.md) | Use the package entry for that mechanic before editing the deeper surface. |
| Audit route | Is this cleanup, pruning, drift, or duplicate-meaning review? | [ECOSYSTEM_AUDIT_INDEX](ECOSYSTEM_AUDIT_INDEX.md) and [audit](mechanics/audit/README.md) | Keep audit evidence reviewable without promoting it into constitutional law. |

```bash
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_docs_thematic_districts.py
python scripts/validate_docs_migration_map.py
python scripts/validate_traces_district.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
python scripts/validate_config_registry.py
python scripts/validate_schema_registry.py
python scripts/validate_manifests_registry.py
python scripts/validate_scripts_district.py
python scripts/validate_tests_district.py
python scripts/repair_known_link_drifts.py --check
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python scripts/validate_status_vocabulary.py
python scripts/build_link_shape_hygiene_index.py --check
python scripts/validate_link_shape_hygiene_index.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_entry_surface_sync.py
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_mechanics_topology.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python scripts/validate_ecosystem.py
python -m pytest -q
```


## If you are editing the root

Do not add a root file because a thought feels important. The root is allowed to hold only a few classes of surface.

| Root class | Examples | Rule |
|---|---|---|
| Civic law and map | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md` | keep in root, make human-readable, and cross-check with generated capsules |
| Public governance and legal | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` | keep in root because platforms and contributors expect them there |
| Thin civic indexes | `GLOSSARY.md`, `QUESTBOOK.md`, `ECOSYSTEM_AUDIT_INDEX.md`, `FRAGILITY_BLACKLIST.md` | keep only if they stay compact and route deeper rather than duplicate deeper doctrine |
| Machine and developer districts | `scripts/`, `schemas/`, `generated/`, `tests/`, `config/`, `examples/`, `manifests/`, `quests/`, `.github/` | keep by function, give each district a local README gate, and do not let generated or executable surfaces become source truth |
| Agent lanes | `AGENTS.md`, `.agents/`, `Spark/` | keep under their own lane law; do not use them as general root docs |

Everything else must justify its place through [docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md).

## Branch by mechanism

Use [mechanics/README](mechanics/README.md) as the single process gate when
the question is **what kind of move is this?** rather than **which repository
is this?** The atlas routes method/growth, recurrence/return/continuity, Agon,
Experience, antifragility/subtraction, quest/RPG reflection, boundary bridge
and ToS-support work, release posture, machine companions, validators, owner
splits, and stop-lines. Detailed mechanic landing history lives in
[Agon LANDING_LOG](mechanics/agon/LANDING_LOG.md) and
[Experience LANDING_LOG](mechanics/experience/LANDING_LOG.md), not in the root
roadmap. The root deliberately keeps those branches behind one door so the
polis remains a city gate, not a warehouse.

## Quick route table

| Surface | Owns | Go here when | Not for |
|---|---|---|---|
| `Agents-of-Abyss` | ecosystem identity, layer map, federation rules, program-level direction, center-entry capsules | you need the constitutional polis, public map, center claim verification, or center-level mechanic law | technique, skill, eval, memo, role, playbook, KAG, runtime, or ToS-authored source truth |
| `aoa-techniques` | reusable engineering practice | you need durable practice rather than a one-off fix | executable skill bundles or proof verdicts |
| `aoa-skills` | bounded agent-facing execution workflows | an agent needs an executable workflow with triggers, procedure, risks, and verification | primary technique canon or eval doctrine |
| `aoa-evals` | portable proof surfaces for bounded claims | quality, boundaries, regressions, verdicts, or defensible claims must be checked | workflow execution or memory truth |
| `aoa-stats` | derived observability and machine-first summaries | you need evidence-linked movement summaries without turning stats into authority | proof, route, score, quest, or verdict authority |
| `aoa-routing` | navigation, dispatch, thin federation entry ABI | a human or model needs the smallest next route across AoA surfaces | authored truth of any layer |
| `aoa-memo` | explicit memory, recall, provenance, re-entry support | memory, checkpoint, recall, retention, forgetting, or witness posture is the object | proof canon, route authority, or runtime persistence |
| `aoa-agents` | role contracts, persona boundaries, handoff posture | you need to define who acts and under what role contract | skill corpus, runtime identity, or memory store |
| `aoa-playbooks` | recurring scenario composition and method routes | a repeated multi-layer scenario needs choreography, fallback posture, and expected evidence | single-skill execution or proof canon |
| `aoa-kag` | derived knowledge substrate and retrieval/graph-ready lifts | authoritative sources need provenance-aware derived structures | source-authored meaning or ToS canon |
| `aoa-sdk` | typed local-first consumer and helper spine | you need loading, integration, compatibility, or controlled orchestration helpers | constitutional authority or ecosystem registry membership |
| `Dionysus` | seed garden and staging surface | an intake pack, seed, or staging trace must be preserved before owner landing | final owner truth |
| `Tree-of-Sophia` | source-first living knowledge architecture and authored ToS meaning | the work concerns source-linked knowledge, concept nodes, lineage, or ToS growth law | AoA operational authority |
| `abyss-stack` | runtime, deployment, storage, services, lifecycle | the question is about the body the system runs on | AoA constitutional truth or ToS-authored meaning |
| `8Dionysus` | public route map, profile, and selected shared-root projection surfaces | the question concerns public entry posture or shared-root projection law | owner-local truth of AoA layers |

## What this repository owns and does not own

| Owned by `Agents-of-Abyss` | Not owned here | Stronger owner |
|---|---|---|
| ecosystem identity and naming | reusable practice truth | `aoa-techniques` |
| layer map and repository-role routing | executable workflow truth | `aoa-skills` |
| federation and source-of-truth rules | proof, scoring, verdict, and regression truth | `aoa-evals` |
| program-level direction and maturity crosswalks | derived summary truth as authority | `aoa-stats` owns derived views, not authority |
| compact center-entry and ecosystem registry surfaces | navigation truth as authored meaning | `aoa-routing` routes, source owners author |
| center-level mechanics, stop-lines, and owner-split law | memory, retention, recall, or witness objects as primary truth | `aoa-memo` |
| Agon and Experience center contracts before owner-local landing | role, persona, standing, jurisdiction, or assistant posture truth | `aoa-agents` |
| public support posture and center claim verification | scenario choreography and recurring method once operational | `aoa-playbooks` |
| narrow AoA support doctrine for ToS-owned work | graph/retrieval projections as source canon | `aoa-kag` stays derived, `Tree-of-Sophia` owns ToS meaning |
| constitutional boundary of future runtime-related claims | runtime implementation, services, storage, workers, daemons | `abyss-stack` |

## Current contour

Treat this contour as a map of planted law, contracts, candidates, and proof surfaces. It is not proof that all downstream owner repos have landed implementation.

| Contour | Current status | Do not read as | Primary surfaces |
|---|---|---|---|
| Public center map | landed public route and registry v2 | a claim that the center owns every object it names | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md`, generated registry capsules |
| Root surface governance | civic root law, completed root-leak cleanup route, district gates, link/shape hygiene, and AGENTS mesh guardrails | permission to hide history, delete without review, or turn district READMEs or AGENTS cards into doctrine catalogs | `docs/ROOT_SURFACE_LAW.md`, `docs/guardrails/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md`, `docs/guardrails/AGENTS_MESH_PROTOCOL.md`, `mechanics/audit/PROVENANCE.md`, `scripts/validate_hygiene_suite.py`, local district READMEs and AGENTS cards |
| Method and growth | center doctrine and cross-owner route | a new lineage layer or center-owned method corpus | `mechanics/method-growth/docs/METHOD_SPINE.md`, `mechanics/method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md`, `mechanics/method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md`, `mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md` |
| Recurrence and continuity | bounded return to valid anchors | ambient continuity, hidden memory, or runtime autonomy | `mechanics/recurrence/docs/RECURRENCE_PRINCIPLE.md`, `mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md`, `mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md` |
| Agon | center-owned pre-protocol law, move language, owner binding, handoffs, arena grammar, consequence candidates, and threshold restraint | live arena execution, assistant contestant authority, live rank mutation, or canon write authority | `mechanics/agon/README.md`, `mechanics/agon/PARTS.md`, `mechanics/agon/OWNER_REQUESTS.md`, and `mechanics/agon/PROVENANCE.md` |
| Experience | staged center contracts through active parts, Wave 1-5 lineage, and v1.2 to v2.0 planting contours | live workspace runtime, hidden memory sovereignty, or owner-local activation | `mechanics/experience/README.md`, `mechanics/experience/PARTS.md`, and `mechanics/experience/PROVENANCE.md` |
| Antifragility and subtraction | stress discipline, degraded-mode evidence, pruning, and anti-authority cleanup | one-score health, deletion theater, or authority transfer | `mechanics/antifragility/docs/ANTIFRAGILITY.md`, `mechanics/antifragility/docs/VIA_NEGATIVA.md`, `FRAGILITY_BLACKLIST.md`, `mechanics/audit/PROVENANCE.md` |
| Quest/RPG reflection | public quest model, lifecycle quest board, and adjunct progression reading layer | runtime ledger, global score, or hidden ontology | `QUESTBOOK.md`, `quests/`, `mechanics/questbook/parts/model-spine/README.md`, `mechanics/questbook/parts/lifecycle-law/README.md`, `mechanics/rpg/PARTS.md` |
| Boundary bridge and ToS support | AoA may route, support, witness, derive, and prepare cross-owner seams without authority transfer | AoA-authored ToS meaning, identity collapse, or owner acceptance without owner-local receipt | `mechanics/boundary-bridge/README.md`, `mechanics/boundary-bridge/PARTS.md`, `mechanics/boundary-bridge/parts/tos-support/README.md`, `mechanics/boundary-bridge/docs/COUNTERPART_BRIDGE.md`, `mechanics/boundary-bridge/docs/WITNESS_COMPOST.md` |
| Release and support | transition and public claims must align across human docs, generated capsules, validators, owner evidence, and rollback routes | release glamour without claim verification or GitHub-only release thinking | `mechanics/release-support/README.md`, `mechanics/release-support/PARTS.md`, `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md`, `mechanics/release-support/docs/FEDERATION_RELEASE_PROTOCOL.md`, `mechanics/release-support/docs/RELEASING.md`, `scripts/`, `tests/` |

## Technical district gates

Root-adjacent technical districts now have their own local gates: `generated/README.md`, `scripts/README.md`, `schemas/README.md`, `tests/README.md`, `config/README.md`, `examples/README.md`, `manifests/README.md`, and `quests/README.md`.

Use them when the question is no longer constitutional, but district-local: how builders, validators, generated capsules, schemas, manifests, tests, examples, or quest obligations should be handled.

Spark has its own agent-lane gate at `Spark/README.md` for standalone fast
sessions that must finish as done or handoff.

## Working rule

AoA should grow by making the polis clearer, not fatter. Add reviewable layers, owner-local contracts, and machine-checkable surfaces. Do not turn the center into a warehouse for every future object.
