# Agents of Abyss (AoA)

`Agents-of-Abyss` is the constitutional polis of AoA.

AoA as a whole is a federation of source-owned repositories, derived layers, routing surfaces, supporting consumers, and adjacent system anchors. This repository is not that whole federation. It is the polis where the federation is named, mapped, governed, and kept legible.

The root is human-first and agent-useful: a person should see the city before entering its districts; an agent should know which owner surface to touch before changing anything.

> Current release: `v0.2.3`. See [CHANGELOG](CHANGELOG.md) for release notes.

## Current state and highest aim

| Axis | Current sober status | Highest aim |
|---|---|---|
| Constitutional center | Proven center surface for identity, layer map, federation rules, and program-level direction. | Stable civic root for the AoA federation: clear enough for humans, strict enough for agents. |
| Federation map | Compact registry v1 names the public AoA contour and adjacent anchors. | Every layer can grow without stealing another layer's truth. |
| Mechanics | Agon, Experience, recurrence, growth, quest/RPG, antifragility, and ToS support are mostly center contracts, doctrine, or pre-protocol routes. | A readable engineering philosophy where every mechanic has a home, owner split, stop-lines, and verification path. |
| Runtime | The center does not run the body. Runtime belongs to `abyss-stack` or later owner-local gates. | Runtime can enact validated mechanics without becoming the source of law or meaning. |
| Self-agency | Continuity is anchor-bound and reviewable. No permissionless autonomy, hidden memory sovereignty, or live arena authority is claimed here. | Long-horizon agency can preserve continuity, revise method, and return to anchors without losing provenance or human judgment. |

## Start here

Read in this order:

1. [CHARTER](CHARTER.md) for the center's mission and authority boundary.
2. [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) for the current public federation contour.
3. [docs/LAYERS](docs/LAYERS.md) and [docs/REPO_ROLES](docs/REPO_ROLES.md) for layer roles and ownership routing.
4. [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) for source-of-truth discipline.
5. [ROADMAP](ROADMAP.md) for current program-level direction.
6. [docs/PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md) for what the center may honestly claim and how CI reinforces it.

If you only need the shortest outside overview, stop after step 4. If you are a low-context agent or small model, also inspect [`generated/center_entry_map.min.json`](generated/center_entry_map.min.json).

## How to verify center claims

Use this tree before trusting a claim made by the center:

| Step | Question | Root surface | Check |
|---|---|---|---|
| 1. Authority | Is this actually a center-owned claim? | [CHARTER](CHARTER.md) | The claim must fit the center's ownership boundary. |
| 2. Contour | Does the current map name the repo or layer being discussed? | [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) | Cross-check [`generated/ecosystem_registry.min.json`](generated/ecosystem_registry.min.json) and [`generated/federation_supporting_inventory.min.json`](generated/federation_supporting_inventory.min.json). |
| 3. Ownership law | Does the claim preserve source truth, derived truth, routing truth, and runtime truth as separate things? | [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) | Cross-check [docs/PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md). |
| 4. Direction | Is this current direction, not an old contour or copied wave note? | [ROADMAP](ROADMAP.md) | Cross-check [docs/DIRECTION_SURFACES](docs/DIRECTION_SURFACES.md). |
| 5. Machine contract | Can the compact surfaces still rebuild and validate? | generated capsules and validators | Run the commands below. |

```bash
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

When the claim concerns a process, mechanic, or engineering philosophy, branch through the single process gate: [docs/MECHANICS](docs/MECHANICS.md). It routes Agon, Experience, recurrence/return, growth refinery, antifragility, quest/RPG reflection, ToS support, release posture, and related stop-lines without crowding this root page.

## Branch by mechanism

Use [docs/MECHANICS](docs/MECHANICS.md) when the question is "what kind of move is this?" rather than "which repository is this?" The atlas branches into:

| Mechanic | Use it when |
|---|---|
| Method and growth refinery | A repeated pattern needs to move from donor or checkpoint into candidate, seed, owner landing, proof, playbook, memory, or derived summary. |
| Recurrence, return, and continuity | A route lost its axis, needs re-entry, or must preserve bounded duration across revision windows. |
| Experience | A staged experience contract from Wave 1 through the v1.2 -> v2.0 planting line needs orientation, validation, or stop-line review. |
| Agon | A pressure, duel, lawful move, arena, verdict, retention, rank, canon, or routing-gate concept needs center-owned pre-protocol law and owner split. |
| Antifragility and via negativa | Stress, degraded mode, failure evidence, pruning, one-in-one-out pressure, or anti-authority cleanup is the relevant frame. |
| Questbook and RPG reflection | Deferred obligations, quest IDs, campaign reading, progression evidence, or adjunct RPG vocabulary needs a public route without inventing runtime state. |
| ToS bridge, witness, and compost | AoA supports `Tree-of-Sophia` work without authoring ToS meaning. |

## Quick route table

| Surface | Owns | Go here when | Not for |
|---|---|---|---|
| `Agents-of-Abyss` | ecosystem identity, layer map, federation rules, program-level direction, center-entry capsules | you need the constitutional polis, the public map, or center-level claim verification | technique, skill, eval, memo, agent, playbook, KAG, runtime, or ToS-authored source truth |
| `aoa-techniques` | reusable engineering practice | you need durable practice rather than a one-off fix | executable skill bundles or proof verdicts |
| `aoa-skills` | bounded agent-facing execution workflows | an agent needs an executable workflow with triggers, procedure, risks, and verification | primary technique canon or eval doctrine |
| `aoa-evals` | portable proof surfaces for bounded claims | quality, boundaries, regressions, verdicts, or defensible claims must be checked | workflow execution or memory truth |
| `aoa-stats` | derived observability and machine-first summaries | you need evidence-linked movement summaries without turning stats into authority | proof, route, score, quest, or verdict authority |
| `aoa-routing` | navigation, dispatch, thin federation entry ABI | a human or model needs the smallest next route across AoA surfaces | authored truth of any layer |
| `aoa-memo` | explicit memory, recall, provenance, re-entry support | memory, checkpoint, recall, retention, forgetting, or witness posture is the object | proof canon, route authority, or runtime persistence |
| `aoa-agents` | role contracts, persona boundaries, handoff posture | you need to define who acts and under what role contract | skill corpus, runtime identity, or memory store |
| `aoa-playbooks` | recurring scenario composition and method routes | a repeated multi-layer scenario needs choreography, fallback posture, and expected evidence | single-skill execution or proof canon |
| `aoa-kag` | derived knowledge substrate and retrieval/graph-ready lifts | authoritative sources need provenance-aware derived structures | source-authored meaning or ToS canon |
| `aoa-sdk` | typed local-first consumer and helper spine | you need loading, integration, compatibility, or controlled orchestration helpers | constitutional authority or compact registry membership |
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

The center currently names a growing set of mechanics while keeping most of them below live authority. Treat this as a map of planted law, not as proof that all downstream owner repos have landed implementation.

| Contour | Current status | Primary surfaces |
|---|---|---|
| Public center map | landed public route and registry v1 | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md`, generated registry capsules |
| Method and growth | center doctrine and cross-owner route, not a new lineage layer | `docs/METHOD_SPINE.md`, `docs/REVIEWABLE_GROWTH_REFINERY.md`, `docs/CANDIDATE_LINEAGE_CROSSWALK.md`, `docs/OWNER_LANDING_AND_PRUNING.md` |
| Recurrence and continuity | bounded return to valid anchors, not ambient continuity or runtime autonomy | `docs/RECURRENCE_PRINCIPLE.md`, `docs/SELF_AGENCY_CONTINUITY.md`, `docs/COMPONENT_REFRESH_LAW.md` |
| Agon | center-owned pre-protocol law, imposition, move language, owner binding, routing/playbook handoffs, and later arena grammar | `docs/MECHANICS.md#agon` and the linked `AGON_*` surfaces |
| Experience | staged center contracts through Wave 1-5 and v1.2 -> v2.0, with strict no-live-runtime and owner-split boundaries | `docs/MECHANICS.md#experience` and the linked `EXPERIENCE_*` surfaces |
| Antifragility and subtraction | stress should leave evidence, degraded-mode discipline, and pruning pressure | `docs/ANTIFRAGILITY.md`, `docs/VIA_NEGATIVA.md`, `docs/ANTI_AUTHORITY_RULES.md`, `docs/ONE_IN_ONE_OUT.md` |
| Quest/RPG reflection | public quest model and adjunct RPG reading layer, not runtime state or global score | `QUESTBOOK.md`, `docs/QUESTBOOK_MODEL.md`, `docs/RPG_LAYER_MODEL.md` |
| ToS support and counterpart work | AoA may support, route, witness, and derive, but not author ToS meaning | `docs/COUNTERPART_BRIDGE.md`, `docs/WITNESS_COMPOST.md`, `docs/TOS_GROWTH_SUPPORT.md`, `docs/TOS_TEMPLATE_SUPPORT.md`, `docs/TOS_LINEAGE_PILOT_SUPPORT.md`, `docs/TOS_SOIL_PREP_SUPPORT.md` |
| Release and support | public claims must align across human docs, generated capsules, and validators | `docs/PUBLIC_SUPPORT_POSTURE.md`, `docs/FEDERATION_RELEASE_PROTOCOL.md`, `docs/RELEASING.md` |

## Working rule

AoA should grow by making the polis clearer, not fatter. Add reviewable layers, owner-local contracts, and machine-checkable surfaces. Do not turn the center into a warehouse for every future object.
