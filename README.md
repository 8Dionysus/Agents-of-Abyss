# Agents of Abyss (AoA)

`Agents-of-Abyss` is the constitutional polis of AoA.

AoA as a whole is the federation: source-owned repositories, derived layers, routing surfaces, supporting consumers, public profile surfaces, and adjacent system anchors. This repository is not that whole federation. It is the polis where the federation is named, mapped, governed, audited, and kept legible.

Federation streams may enter this polis as claims, maps, contracts, release posture, stop-lines, root-surface placement questions, and machine capsules. They must leave with clearer ownership than they had on entry.

This README is human-first and agent-useful. A person should see the city before entering its districts. An agent should know which owner surface to touch before changing anything.

> Current release: `v0.2.3`. See [CHANGELOG](CHANGELOG.md) for release notes.

## Current state and highest aim

| Axis | Current sober status | Highest aim |
|---|---|---|
| Constitutional center | Proven center surface for identity, layer map, federation rules, and program-level direction. | A stable civic root for the AoA federation: clear enough for humans, strict enough for agents. |
| Federation contour | Compact registry v1 names the public AoA contour and adjacent anchors. Supporting consumers are tracked separately. | Every layer can grow without stealing another layer's truth. |
| Root surface governance | The root contains civic docs, public governance docs, indexes, machine folders, and a few legacy leak artifacts that should be moved or narrowed. | The root should stay a city gate: lawful, readable, sparse, and strict about what belongs nearby. |
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
7. [docs/PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md) for what the center may honestly claim and how CI reinforces it.

If you only need the shortest outside overview, stop after step 3. If you are a low-context agent or small model, also inspect [`generated/center_entry_map.min.json`](generated/center_entry_map.min.json).

## How to verify center claims

Use this tree before trusting a claim made by the center:

| Branch | Question | Primary surface | Check |
|---|---|---|---|
| Authority | Is this actually a center-owned claim? | [CHARTER](CHARTER.md) | The claim must fit the center's ownership boundary. |
| Contour | Does the current map name the repo, layer, or adjacent anchor being discussed? | [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) | Cross-check [`generated/ecosystem_registry.min.json`](generated/ecosystem_registry.min.json) and [`generated/federation_supporting_inventory.min.json`](generated/federation_supporting_inventory.min.json). |
| Ownership law | Does the claim preserve source truth, derived truth, routing truth, runtime truth, and ToS-authored meaning as separate things? | [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) | Cross-check [docs/REPO_ROLES](docs/REPO_ROLES.md) and [docs/PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md). |
| Surface placement | Does this object deserve to live in the repository root? | [docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) | If it is a wave receipt, audit artifact, future registry note, or generated object, route it away from root. |
| Direction | Is this current program direction rather than an old contour, wave note, or copied promise? | [ROADMAP](ROADMAP.md) | Cross-check [docs/DIRECTION_SURFACES](docs/DIRECTION_SURFACES.md). |
| Machine contract | Can the compact surfaces still rebuild and validate? | generated capsules and validators | Run the commands below. |
| Mechanic route | Is the claim about a process, engineering philosophy, Agon, Experience, recurrence, quest/RPG, antifragility, or ToS support? | [docs/MECHANICS](docs/MECHANICS.md) | Use the atlas entry for that mechanic before editing the deeper surface. |
| Audit route | Is this cleanup, pruning, or duplicate-meaning review? | [ECOSYSTEM_AUDIT_INDEX](ECOSYSTEM_AUDIT_INDEX.md) and [docs/audits](docs/audits/) | Keep audit evidence reviewable without promoting it into constitutional law. |

```bash
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```


## If you are editing the root

Do not add a root file because a thought feels important. The root is allowed to hold only a few classes of surface.

| Root class | Examples | Rule |
|---|---|---|
| Civic law and map | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md` | keep in root, make human-readable, and cross-check with generated capsules |
| Public governance and legal | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` | keep in root because platforms and contributors expect them there |
| Thin civic indexes | `GLOSSARY.md`, `QUESTBOOK.md`, `ECOSYSTEM_AUDIT_INDEX.md`, `FRAGILITY_BLACKLIST.md` | keep only if they stay compact and route deeper rather than duplicate deeper doctrine |
| Machine and developer districts | `scripts/`, `schemas/`, `generated/`, `tests/`, `config/`, `examples/`, `.github/` | keep by function, not as narrative surfaces |
| Agent lanes | `AGENTS.md`, `.agents/`, `Spark/` | keep under their own lane law; do not use them as general root docs |

Everything else must justify its place through [docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md).

## Branch by mechanism

Use [docs/MECHANICS](docs/MECHANICS.md) as the single process gate when the question is **what kind of move is this?** rather than **which repository is this?** The atlas routes method/growth, recurrence/return/continuity, Agon, Experience, antifragility/subtraction, quest/RPG reflection, ToS bridge/witness/compost, release posture, machine companions, validators, owner splits, and stop-lines. The root deliberately keeps those branches behind one door so the polis remains a city gate, not a warehouse.

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

Treat this contour as a map of planted law, contracts, candidates, and proof surfaces. It is not proof that all downstream owner repos have landed implementation.

| Contour | Current status | Do not read as | Primary surfaces |
|---|---|---|---|
| Public center map | landed public route and registry v1 | a claim that the center owns every object it names | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md`, generated registry capsules |
| Root surface governance | civic root law plus first cleanup route for leaked historical, audit, and design-note artifacts | permission to hide history or delete without review | `docs/ROOT_SURFACE_LAW.md`, `docs/audits/ROOT_SURFACE_AUDIT_2026_04_24.md` |
| Method and growth | center doctrine and cross-owner route | a new lineage layer or center-owned method corpus | `docs/METHOD_SPINE.md`, `docs/REVIEWABLE_GROWTH_REFINERY.md`, `docs/CANDIDATE_LINEAGE_CROSSWALK.md`, `docs/OWNER_LANDING_AND_PRUNING.md` |
| Recurrence and continuity | bounded return to valid anchors | ambient continuity, hidden memory, or runtime autonomy | `docs/RECURRENCE_PRINCIPLE.md`, `docs/SELF_AGENCY_CONTINUITY.md`, `docs/COMPONENT_REFRESH_LAW.md` |
| Agon | center-owned pre-protocol law, move language, owner binding, handoffs, arena grammar, consequence candidates, and threshold restraint | live arena execution, assistant contestant authority, live rank mutation, or canon write authority | `docs/MECHANICS.md#agon` and linked `AGON_*` surfaces |
| Experience | staged center contracts through Wave 1-5 and v1.2 to v2.0 | live workspace runtime, hidden memory sovereignty, or owner-local activation | `docs/MECHANICS.md#experience` and linked `EXPERIENCE_*` surfaces |
| Antifragility and subtraction | stress discipline, degraded-mode evidence, pruning, and anti-authority cleanup | one-score health, deletion theater, or authority transfer | `docs/ANTIFRAGILITY.md`, `docs/VIA_NEGATIVA.md`, `FRAGILITY_BLACKLIST.md`, `docs/audits/DELETION_CANDIDATES.json` |
| Quest/RPG reflection | public quest model and adjunct progression reading layer | runtime ledger, global score, or hidden ontology | `QUESTBOOK.md`, `quests/`, `docs/QUESTBOOK_MODEL.md`, `docs/RPG_LAYER_MODEL.md` |
| ToS support and counterpart work | AoA may route, support, witness, derive, and prepare ToS-adjacent seams | AoA-authored ToS meaning or direct ToS canon write | `docs/COUNTERPART_BRIDGE.md`, `docs/WITNESS_COMPOST.md`, `docs/TOS_GROWTH_SUPPORT.md`, `docs/TOS_TEMPLATE_SUPPORT.md`, `docs/TOS_LINEAGE_PILOT_SUPPORT.md`, `docs/TOS_SOIL_PREP_SUPPORT.md` |
| Release and support | public claims must align across human docs, generated capsules, and validators | release glamour without claim verification | `docs/PUBLIC_SUPPORT_POSTURE.md`, `docs/FEDERATION_RELEASE_PROTOCOL.md`, `docs/RELEASING.md`, `scripts/`, `tests/` |

## Working rule

AoA should grow by making the polis clearer, not fatter. Add reviewable layers, owner-local contracts, and machine-checkable surfaces. Do not turn the center into a warehouse for every future object.
