# AoA Mechanics Atlas

This is the single branch point for center-level processes and engineering
philosophy in `Agents-of-Abyss`.

Use it after the first-reading route:

1. `README.md`
2. `CHARTER.md`
3. `ECOSYSTEM_MAP.md`
4. `docs/FEDERATION_RULES.md`

The purpose is simple:

when a human or agent asks **what kind of move is this?**, this atlas points to
the right mechanic, owner split, stop-line, machine companion, and verification
path.

This file does not create new authority.

It keeps the root README human-sized while giving agents a precise map of the
deeper machinery.

Mechanics are not documentation-only packages. When a schema, example, seed
config, generated companion, validator, test, or quest rule belongs to one
mechanic, its source home is the mechanic package. Root technical districts keep
repo-wide contracts and compatibility aliases. See
[ARTIFACT_TOPOLOGY](ARTIFACT_TOPOLOGY.md).

## Canonical route contract

Mechanic work uses the `mechanic-change` route in
[`docs/START_HERE_ROUTE_CONTRACT.md`](../docs/START_HERE_ROUTE_CONTRACT.md).

Mechanic-facing route modes:

| Route mode | Mechanics relevance |
|---|---|
| `first-reading` | enter the center before choosing a process branch |
| `root-editing` | keep root-facing mechanic references thin |
| `direction-change` | update roadmap or release contour without turning history into doctrine |
| `ownership-routing` | decide which owner repository owns operational truth |
| `mechanic-change` | change a process, stop-line, owner split, or mechanic package |
| `public-claim-validation` | check whether a mechanic claim can be publicly supported |
| `district-work` | respect local gates for scripts, schemas, generated capsules, tests, and quests |

## Mechanic card contract

Every `mechanics/<slug>/README.md` is an agent-operable card, not merely a
human overview. The card lets a reader answer: **when do I use this,
what does the center own, who owns the stronger truth, what can enter, what can
leave, what must not be claimed, how do I validate it, and where do I route
next?**

Each package README must include these headings in this order:

| Heading | Purpose |
|---|---|
| `## Mechanic card` | compact status and entry point |
| `### Trigger` | when the mechanic applies |
| `### Center owns` | what `Agents-of-Abyss` may author here |
| `### Stronger owner split` | repositories or districts that own operational truth |
| `### Inputs` | what may enter this mechanic |
| `### Outputs` | what may leave this mechanic |
| `### Must not claim` | stop-lines copied from the registry |
| `### Validation` | exact commands for this mechanic card and topology |
| `### Next route` | where implementation, proof, memory, runtime, role, KAG, or ToS meaning goes next |

Status vocabulary:

| Status | Meaning |
|---|---|
| `planted` | center doctrine and route language exist, but the mechanic must not be claimed as operational truth |
| `landed` | center route, stop-lines, registry entry, card, and validation expectations exist |
| `requested` | a named owner-local landing request exists, but the owner has not yet accepted operational truth |
| `operational` | the stronger owner repository has accepted and validated the relevant implementation, proof, memory, runtime, or canon surface |
| `deprecated` | the route is retained only for compatibility, history, or migration support |

Machine companion:

- [`generated/mechanic_card_index.min.json`](../generated/mechanic_card_index.min.json)

Validation:

```bash
python scripts/validate_mechanic_readme_cards.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_mechanics_topology.py
```

The generated card index reflects `mechanics/registry.json` and the package
README cards. It never authors mechanic meaning.


## Owner-request queue

Mechanic cards name the owner split. The owner-request queue names the exact owner-local landing packets that must exist before a center mechanic can be claimed as operational outside the center.

Use these surfaces when the card output would become owner-local work:

- [`OWNER_REQUEST_PROTOCOL.md`](OWNER_REQUEST_PROTOCOL.md) for status grammar and advancement rules.
- [`OWNER_REQUEST_QUEUE.md`](OWNER_REQUEST_QUEUE.md) for the human request index.
- [`owner-request-queue.json`](owner-request-queue.json) for the source data.
- [`generated/owner_request_queue.min.json`](../generated/owner_request_queue.min.json) for compact machine entry.

Validation:

```bash
python scripts/validate_owner_request_queue.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py
```

A request packet is not owner acceptance. Owner repositories land operational truth; the center keeps the queue honest.

## How to use this atlas

1. Name the mechanic you are touching.
2. Read the mechanic's center entry and stop-lines.
3. Identify the owner repository that owns the operational truth.
4. If the output crosses into owner-local work, open the matching owner-request packet.
5. Run the validator named by that mechanic and by the owner-request queue when validators exist.
6. If ownership is unclear, return to [FEDERATION_RULES](../docs/FEDERATION_RULES.md) before changing anything.

## Compass

| Mechanic | Center question | Current status | Start here | Must not claim |
|---|---|---|---|---|
| Constitutional polis | What does the center own, and what must stay outside it? | landed center law | [CHARTER](../CHARTER.md), [ECOSYSTEM_MAP](../ECOSYSTEM_MAP.md), [FEDERATION_RULES](../docs/FEDERATION_RULES.md), [ROOT_SURFACE_LAW](../docs/ROOT_SURFACE_LAW.md) | layer-owned truth or root-surface inflation |
| Layer ownership | Which repository owns this object class? | landed route map | [LAYERS](../docs/LAYERS.md), [REPO_ROLES](../docs/REPO_ROLES.md) | convenience ownership transfer |
| Method and growth refinery | How does repeated work move from donor or checkpoint to candidate, seed, owner landing, proof, method, memory, or derived summary? | center doctrine and cross-owner route | [METHOD_SPINE](method-growth/docs/METHOD_SPINE.md), [REVIEWABLE_GROWTH_REFINERY](method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md) | center-owned scenario canon |
| Recurrence, return, continuity | How does AoA recover when a route loses its axis and must re-enter through a valid anchor? | bounded return law | [RECURRENCE_PRINCIPLE](recurrence/docs/RECURRENCE_PRINCIPLE.md), [SELF_AGENCY_CONTINUITY](recurrence/docs/SELF_AGENCY_CONTINUITY.md) | ambient continuity or hidden memory sovereignty |
| Experience | Which staged experience contract, office/service posture, seed intake, duel pressure, continuity loom, or runtime boundary is relevant? | planted center contracts through v2.0 | [Experience](experience/README.md) | live workspace runtime or owner-local activation |
| Agon | Which pressure, lawful move, duel, arena, packet, verdict, retention, rank, school, canon, or threshold boundary is relevant? | center-owned pre-protocol law and candidate grammar | [Agon](agon/README.md) | live arena execution or assistant contestant authority |
| Antifragility and subtraction | What stress, degraded mode, evidence, pruning, or anti-authority posture applies? | center doctrine | [ANTIFRAGILITY](antifragility/docs/ANTIFRAGILITY.md), [VIA_NEGATIVA](antifragility/docs/VIA_NEGATIVA.md) | one-score health or deletion theater |
| Questbook | What obligation must survive the current diff as a public tracked follow-up? | public obligation model | [QUESTBOOK](../QUESTBOOK.md), [QUESTBOOK_MODEL](questbook/docs/QUESTBOOK_MODEL.md) | second roadmap or private scratchpad |
| RPG reflection | How can progression, questlines, campaigns, roles, and feats be read without rewriting ownership? | adjunct reflection layer | [RPG_LAYER_MODEL](rpg/docs/RPG_LAYER_MODEL.md), [RPG_ARCHITECTURE_RFC](rpg/docs/RPG_ARCHITECTURE_RFC.md) | hidden ontology or runtime ledger |
| ToS bridge, witness, compost | How can AoA support ToS without authoring ToS meaning? | support doctrine and seams | [COUNTERPART_BRIDGE](tos-bridge/docs/COUNTERPART_BRIDGE.md), [WITNESS_COMPOST](tos-bridge/docs/WITNESS_COMPOST.md) | AoA-authored ToS canon |
| Release, audit, public support | Which claims can the center publicly support? | release and CI posture | [PUBLIC_SUPPORT_POSTURE](release-support/docs/PUBLIC_SUPPORT_POSTURE.md), [FEDERATION_RELEASE_PROTOCOL](release-support/docs/FEDERATION_RELEASE_PROTOCOL.md), [RELEASING](release-support/docs/RELEASING.md) | unverified public claim |

## Constitutional polis

The polis owns the civic map, not every district's inner law.

Read:

1. [CHARTER](../CHARTER.md) for mission and ownership boundary.
2. [ECOSYSTEM_MAP](../ECOSYSTEM_MAP.md) for the public contour.
3. [LAYERS](../docs/LAYERS.md) for conceptual layer definitions.
4. [REPO_ROLES](../docs/REPO_ROLES.md) for compact ownership routing.
5. [FEDERATION_RULES](../docs/FEDERATION_RULES.md) for source-of-truth law.
6. [ROOT_SURFACE_LAW](../docs/ROOT_SURFACE_LAW.md) for repository-root placement and cleanup law.
7. [PUBLIC_SUPPORT_POSTURE](release-support/docs/PUBLIC_SUPPORT_POSTURE.md) for public claim and CI posture.

Machine companions:

- [`generated/README.md`](../generated/README.md)
- [`scripts/README.md`](../scripts/README.md)
- [`schemas/README.md`](../schemas/README.md)
- [`generated/center_entry_map.min.json`](../generated/center_entry_map.min.json)
- [`generated/ecosystem_registry.min.json`](../generated/ecosystem_registry.min.json)
- [`generated/federation_supporting_inventory.min.json`](../generated/federation_supporting_inventory.min.json)

Validation:

```bash
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
python scripts/validate_owner_request_queue.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

## Method, growth, and owner landing

Use this branch when the object is not just a task, but a repeated route that
may become technique, skill, playbook, proof, memory, derived summary, or
owner-local doctrine.

Core law:

- [ROOTLINE](method-growth/docs/ROOTLINE.md) keeps the trunk-first coordination spine.
- [METHOD_SPINE](method-growth/docs/METHOD_SPINE.md) says recurring scenario-level method belongs in `aoa-playbooks`.
- [REVIEWABLE_GROWTH_REFINERY](method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md) names the non-sovereign chain `cluster_ref -> candidate_ref -> seed_ref -> object_ref`.
- [CANDIDATE_LINEAGE_CROSSWALK](method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md) maps stages to owners.
- [OWNER_LANDING_AND_PRUNING](method-growth/docs/OWNER_LANDING_AND_PRUNING.md) handles post-candidate landing and pruning.
- [COMPONENT_REFRESH_LAW](recurrence/docs/COMPONENT_REFRESH_LAW.md) handles owner-owned maintenance of one drifting technical component.

Owner split:

| Stage | Stronger owner |
|---|---|
| Provisional carry and typed helper hints | `aoa-sdk` |
| Reviewed candidate identity | `aoa-skills` |
| Seed staging | `Dionysus` |
| Final object truth | the final owner repo |
| Proof | `aoa-evals` |
| Recurring method | `aoa-playbooks` |
| Derived summary | `aoa-stats` |
| Bounded memory and lessons | `aoa-memo` |

Validation anchors:

```bash
python scripts/validate_candidate_lineage_contract.py --workspace-root /srv
python scripts/validate_wave4_kernel_automation.py --workspace-root /srv
```

## Recurrence, return, and continuity

Use this branch when a route lost its axis, must recurse back into a valid
anchor, needs bounded re-entry, or must preserve duration without pretending
that continuity is ambient memory.

Core law:

- [RECURRENCE_PRINCIPLE](recurrence/docs/RECURRENCE_PRINCIPLE.md): when a route loses its axis, return to the last valid anchor before continuing.
- [SELF_AGENCY_CONTINUITY](recurrence/docs/SELF_AGENCY_CONTINUITY.md): continuity means bounded duration with explicit anchors and reviewable return, not permissionless autonomy.
- [COMPONENT_REFRESH_LAW](recurrence/docs/COMPONENT_REFRESH_LAW.md): drifting components refresh through owner-owned receipts, not mystical self-healing.
- [METHOD_SPINE](method-growth/docs/METHOD_SPINE.md): recurring return routes should become playbook-owned method.

Vocabulary:

| Term | Meaning |
|---|---|
| axis | goal, phase, owner source, expected artifact, and proof boundary that make the next step legitimate |
| drift | loss, blurring, or substitution of that axis |
| anchor | last reviewable object that still preserves enough of the axis |
| return | stepping back to the anchor |
| re-entry | explicit next step from the anchor |
| safe stop | honest halt when no bounded re-entry is justified |

Owner split:

- `Agents-of-Abyss` owns center law and stop-lines.
- `aoa-routing` may point toward re-entry, but does not own recurrence meaning.
- `aoa-memo` owns checkpoint, recall, and provenance surfaces.
- `aoa-agents` owns role and handoff posture for returns between actors.
- `aoa-playbooks` owns recurring return choreography.
- `aoa-evals` owns drift and recovery-quality proof.
- `abyss-stack` owns runtime wrappers only after runtime-owner gates.

## Experience

Use this branch when working with staged experience contracts, office/service
posture, seed intake, epistemic duel pressure, continuity loom, or the
living-workspace runtime boundary.

Read this as planted center law, not live authority.

These surfaces repeatedly forbid live runtime activation, hidden memory
sovereignty, assistant contestant authority, direct ToS writes, and owner-truth
theft unless a later owner-local gate lands the slice.

Active direction, functioning parts, landing history, archival bridge, and
owner requests live in [Experience](experience/README.md),
[DIRECTION](experience/DIRECTION.md), [PARTS](experience/PARTS.md),
[LANDING_LOG](experience/LANDING_LOG.md), [PROVENANCE](experience/PROVENANCE.md),
and [OWNER_REQUESTS](experience/OWNER_REQUESTS.md).

This atlas stays a route surface rather than the canonical Experience ledger.
Historical source packets stay behind the provenance bridge; use them for
audits, not as the first active route.

### Experience active parts

| Part | Role |
|---|---|
| [Capture Kernel](experience/parts/capture-kernel/README.md) | friction, incident, candidate, verdict route, memory gate, and inert projection intake |
| [Certification Proof](experience/parts/certification-proof/README.md) | certification, watchtower, canary, smoke, regression, and proof handoff discipline |
| [Adoption Federation](experience/parts/adoption-federation/README.md) | federation harvest, adoption gates, owner consent, rollback, and retention routes |
| [Governance Polis](experience/parts/governance-polis/README.md) | polis governance, constitution boundary, appeals, stays, policy, and precedent |
| [Release Deployment](experience/parts/release-deployment/README.md) | installation, deployment, release train, rollout, rollback, semver, and landing order |
| [Office Operations](experience/parts/office-operations/README.md) | sovereign office posture, operator routes, assistant invariants, roles, and handoffs |
| [Service Mesh](experience/parts/service-mesh/README.md) | service mesh operations and no-runtime service boundaries |
| [Continuity Context](experience/parts/continuity-context/README.md) | context routing grammar, continuity loom, replay, memory routes, and re-entry |
| [Runtime Boundary](experience/parts/runtime-boundary/README.md) | living-workspace runtime stop-lines, authority resolver boundaries, and case queues |
| [Compatibility Bridges](experience/parts/compatibility-bridges/README.md) | cross-mechanic, ToS, KAG, and Agon bridge language without authority transfer |

Validation starts with `python scripts/validate_experience_distillation.py`,
then the matching `scripts/validate_experience_*.py` and
`tests/test_experience_*.py` for the active part or versioned contract you changed.

## Agon

Use this branch when pressure, contest, survival, lawful moves, arena sessions,
sealed commitments, state packets, verdicts, scars, retention, rank, schools,
canon promotion, or ToS thresholds are involved.

Agon is center-owned as law, vocabulary, stop-line, and owner-binding doctrine.

It is not live arena execution in this repository.

Owner repos must land their own slices before practice, workflows, proof,
memory, stats, routing, actors, runtime, or ToS canon become operational truth.

Landing history, checked surfaces, validators, and stop-lines live in
[AGON_LANDING_LOG](agon/LANDING_LOG.md).

This atlas stays a route surface rather than the canonical Agon ledger.

### Agon phase map

| Phase | Start here | Role |
|---|---|---|
| Baseline and imposition | [AGON_PREPARATION_POSTURE](agon/docs/AGON_PREPARATION_POSTURE.md), [AGON_IMPOSITION_POSTURE](agon/docs/AGON_IMPOSITION_POSTURE.md), [AGON_SURVIVAL_CRITERIA](agon/docs/AGON_SURVIVAL_CRITERIA.md) | conservative boundary, survival lens, and first pressure gate before live protocol |
| Lawful move language | [AGON_LAWFUL_MOVE_LANGUAGE](agon/docs/AGON_LAWFUL_MOVE_LANGUAGE.md), [AGON_MOVE_REGISTRY_MODEL](agon/docs/AGON_MOVE_REGISTRY_MODEL.md) | center vocabulary and registry contour without execution authority |
| Owner binding | [AGON_MOVE_OWNER_BINDING](agon/docs/AGON_MOVE_OWNER_BINDING.md), [AGON_MOVE_BINDING_MATRIX_MODEL](agon/docs/AGON_MOVE_BINDING_MATRIX_MODEL.md), [AGON_PRE_PROTOCOL_STOP_LINES](agon/docs/AGON_PRE_PROTOCOL_STOP_LINES.md) | owner gravity for moves and explicit non-landed requests |
| Gate, playbook, recurrence, prebinding | [AGON_GATE_ROUTING_HANDOFF](agon/docs/AGON_GATE_ROUTING_HANDOFF.md), [AGON_TRIAL_PLAYBOOK_HANDOFF](agon/docs/AGON_TRIAL_PLAYBOOK_HANDOFF.md), [AGON_RECURRENCE_ADAPTER](agon/docs/AGON_RECURRENCE_ADAPTER.md), [AGON_COURT_MEMO_STATS_PREBINDING_HANDOFF](agon/docs/AGON_COURT_MEMO_STATS_PREBINDING_HANDOFF.md) | handoffs to routing, playbooks, recurrence, proof, memory, and stats without granting authority |
| Arena, seats, pressure, sessions | [AGON_ARENA_SESSION_MODEL](agon/docs/AGON_ARENA_SESSION_MODEL.md), [AGON_SESSION_LIFECYCLE_MODEL](agon/docs/AGON_SESSION_LIFECYCLE_MODEL.md), [AGON_CHARTER_AND_SEAT_MODEL](agon/docs/AGON_CHARTER_AND_SEAT_MODEL.md) | future session frame, seating, lifecycle, and pressure profile without live arena |
| Packets and commitments | [AGON_STATE_PACKET_MODEL](agon/docs/AGON_STATE_PACKET_MODEL.md), [AGON_PACKET_SEQUENCE_MODEL](agon/docs/AGON_PACKET_SEQUENCE_MODEL.md), [AGON_SEALED_COMMIT_MODEL](agon/docs/AGON_SEALED_COMMIT_MODEL.md) | declaration, reveal, revision, packet sequence, and owner handoff grammar |
| Contradiction, closure, summon | [AGON_CONTRADICTION_LAW_MODEL](agon/docs/AGON_CONTRADICTION_LAW_MODEL.md), [AGON_CONTRADICTION_CLOSURE_SUMMON_LAW](agon/docs/AGON_CONTRADICTION_CLOSURE_SUMMON_LAW.md), [AGON_LAW_INTERLOCKS](agon/docs/AGON_LAW_INTERLOCKS.md) | contradiction handling and closure/summon law without unbounded escalation |
| Verdict, delta, scars, inscription | [AGON_VERDICT_DRAFT_MODEL](agon/docs/AGON_VERDICT_DRAFT_MODEL.md), [AGON_VERDICT_DELTA_SCAR_BRIDGE](agon/docs/AGON_VERDICT_DELTA_SCAR_BRIDGE.md), [AGON_INSCRIPTION_BUNDLE_MODEL](agon/docs/AGON_INSCRIPTION_BUNDLE_MODEL.md) | draft verdicts, deltas, scars, receipts, concept-map candidates, and inscription bundles without runtime mutation |
| Duel kernel and model-of-other | [AGON_DUEL_KERNEL_MODEL](agon/docs/AGON_DUEL_KERNEL_MODEL.md), [AGON_DUEL_KERNEL_EVENT_MODEL](agon/docs/AGON_DUEL_KERNEL_EVENT_MODEL.md), [AGON_MODEL_OF_OTHER_LAW](agon/docs/AGON_MODEL_OF_OTHER_LAW.md) | duel kernel grammar, event model, seats, model-of-other law, and bifurcation pressure without live duel authority |
| Mechanical trials | [AGON_MECHANICAL_TRIALS_OVER_DUEL_KERNEL](agon/docs/AGON_MECHANICAL_TRIALS_OVER_DUEL_KERNEL.md), [AGON_MECHANICAL_TRIAL_RUN_MODEL](agon/docs/AGON_MECHANICAL_TRIAL_RUN_MODEL.md) | trial-suite grammar and outcome candidates without proof sovereignty |
| Epistemic Agon | [AGON_EPISTEMIC_AGON](agon/docs/AGON_EPISTEMIC_AGON.md), [AGON_EPISTEMIC_MOVE_EXTENSION_MODEL](agon/docs/AGON_EPISTEMIC_MOVE_EXTENSION_MODEL.md) | epistemic contest grammar and handoffs without truth ownership |
| Retention, rank, standing | [AGON_RETENTION_RANK_ECONOMY](agon/docs/AGON_RETENTION_RANK_ECONOMY.md), [AGON_RETENTION_CHECK_MODEL](agon/docs/AGON_RETENTION_CHECK_MODEL.md), [AGON_RANK_JURISDICTION_MODEL](agon/docs/AGON_RANK_JURISDICTION_MODEL.md) | retention, standing, rank, jurisdiction, and mutation candidates without live rank authority |
| Schools, lineages, campaigns | [AGON_SCHOOL_MODEL](agon/docs/AGON_SCHOOL_MODEL.md), [AGON_LINEAGE_MODEL](agon/docs/AGON_LINEAGE_MODEL.md), [AGON_CAMPAIGN_MODEL](agon/docs/AGON_CAMPAIGN_MODEL.md) | school, lineage, and campaign grammar without hidden hierarchy |
| KAG, canon, Sophian threshold | [AGON_KAG_PROMOTION_PATH](agon/docs/AGON_KAG_PROMOTION_PATH.md), [AGON_CANON_RESTRAINT_MODEL](agon/docs/AGON_CANON_RESTRAINT_MODEL.md), [AGON_SOPHIAN_THRESHOLD](agon/docs/AGON_SOPHIAN_THRESHOLD.md) | promotion candidates, canon restraint, ToS/Sophian thresholds, and terminal outcome boundaries without direct canon write |

### Agon wave landings

Use the landing and stop-line document for the wave you touch.

Known center waves live in the Agon package and its `LANDING_LOG`.

Generated companions live under `generated/agon_*.min.json`.

Use the matching builder, validator, and test for the generated surface you
changed.

## Antifragility, via negativa, and pruning

Use this branch when the system is under stress, sprawl, authority inflation, or
cleanup pressure.

| Surface | Role |
|---|---|
| [ANTIFRAGILITY](antifragility/docs/ANTIFRAGILITY.md) | stress should make the system more legible, bounded, and teachable |
| [ANTIFRAGILITY_FIRST_WAVE](antifragility/docs/ANTIFRAGILITY_FIRST_WAVE.md) | first-wave antifragility scope |
| [VIA_NEGATIVA](antifragility/docs/VIA_NEGATIVA.md) | subtraction as doctrine |
| [ANTI_AUTHORITY_RULES](antifragility/docs/ANTI_AUTHORITY_RULES.md) | stop authority inflation |
| [ONE_IN_ONE_OUT](antifragility/docs/ONE_IN_ONE_OUT.md) | sprawl pressure rule |
| [FRAGILITY_BLACKLIST](../FRAGILITY_BLACKLIST.md) | known fragile patterns |
| [DELETION_CANDIDATES](../docs/audits/DELETION_CANDIDATES.json) | deletion candidates |

Review questions:

1. Where was stress bounded?
2. What owner-local evidence exists?
3. Did the degraded mode remain weaker than normal mode?
4. What later change can cite the event?
5. Did cleanup reduce authority drift or merely move it?

## Questbook and RPG reflection

Use this branch when work becomes a tracked obligation, questline, campaign,
progression path, or readable adjunct reflection.

Quest surfaces:

- [QUESTBOOK](../QUESTBOOK.md): public tracked surface for deferred obligations.
- [`quests/`](../quests/): lifecycle item store for center, Agon, and Experience follow-through work.
- [QUESTBOOK_MODEL](questbook/docs/QUESTBOOK_MODEL.md): quest lifecycle, placement bands, risk, difficulty, and harvest rules.
- [QUESTBOOK_FIRST_WAVE](questbook/docs/QUESTBOOK_FIRST_WAVE.md): first-wave guardrails.

RPG reflection surfaces:

- [RPG_LAYER_MODEL](rpg/docs/RPG_LAYER_MODEL.md): adjunct RPG reflection layer.
- [RPG_FIRST_WAVE](rpg/docs/RPG_FIRST_WAVE.md) and [RPG_SECOND_WAVE](rpg/docs/RPG_SECOND_WAVE.md): staged reflection contours.
- [RPG_SKILLS_AND_FEATS](rpg/docs/RPG_SKILLS_AND_FEATS.md): skill/feat reading, not skill ownership.
- [RPG_ARCHITECTURE_RFC](rpg/docs/RPG_ARCHITECTURE_RFC.md): four-plane split of source meaning, proof/witness, runtime/session, and presentation/theme.
- [RPG_CANONICAL_TERMINOLOGY](rpg/docs/RPG_CANONICAL_TERMINOLOGY.md) and [RPG_BOUNDARY_MAP](rpg/docs/RPG_BOUNDARY_MAP.md): terms and boundaries.

Boundary:

- Questbook is not a second roadmap.
- RPG is not a hidden ontology.
- Progression evidence is not a global score.
- Campaign language must not imply runtime ledger ownership.

## ToS bridge, witness, and compost

Use this branch when AoA supports `Tree-of-Sophia` or derived knowledge work
without authoring ToS meaning.

| Surface | Role |
|---|---|
| [ROOTLINE](method-growth/docs/ROOTLINE.md) | trunk-first AoA x ToS coordination spine |
| [COUNTERPART_BRIDGE](tos-bridge/docs/COUNTERPART_BRIDGE.md) | counterpart mappings stay derived, optional, and non-identity |
| [WITNESS_COMPOST](tos-bridge/docs/WITNESS_COMPOST.md) | witness and compost pilot doctrine |
| [TOS_GROWTH_SUPPORT](tos-bridge/docs/TOS_GROWTH_SUPPORT.md) | narrow support for ToS-owned growth law |
| [TOS_TEMPLATE_SUPPORT](tos-bridge/docs/TOS_TEMPLATE_SUPPORT.md) | support around ToS templates without owning ToS scaffold truth |
| [TOS_LINEAGE_PILOT_SUPPORT](tos-bridge/docs/TOS_LINEAGE_PILOT_SUPPORT.md) | support around ToS lineage pilot work |
| [TOS_SOIL_PREP_SUPPORT](tos-bridge/docs/TOS_SOIL_PREP_SUPPORT.md) | soil-preparation support without ToS authorship |

Rule:

`Tree-of-Sophia` owns authored knowledge meaning.

AoA may route, support, derive, witness, or prepare.

It does not become ToS canon.

## Release, audit, and support posture

Use this branch when a public claim, release surface, or audit route must be
checked.

| Surface | Role |
|---|---|
| [PUBLIC_SUPPORT_POSTURE](release-support/docs/PUBLIC_SUPPORT_POSTURE.md) | what the center may honestly claim |
| [DIRECTION_SURFACES](release-support/docs/DIRECTION_SURFACES.md) | current direction surface per repo |
| [FEDERATION_RELEASE_PROTOCOL](release-support/docs/FEDERATION_RELEASE_PROTOCOL.md) | shared release completeness contract |
| [RELEASING](release-support/docs/RELEASING.md) | center release runbook |
| [ECOSYSTEM_AUDIT_INDEX](../ECOSYSTEM_AUDIT_INDEX.md), [ROOT_SURFACE_AUDIT_2026_04_24](../docs/audits/ROOT_SURFACE_AUDIT_2026_04_24.md) | audit index |
| [CODEX_AUDIT_PROTOCOL](../docs/audits/CODEX_AUDIT_PROTOCOL.md) | Codex audit protocol |
| [CODEX_SKILL_PROOF_AUDIT_BRIDGE](../docs/audits/CODEX_SKILL_PROOF_AUDIT_BRIDGE.md) | skill/proof audit bridge |

Compact validation:

```bash
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
python scripts/validate_owner_request_queue.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

If you touched a generated Agon or Experience capsule, run that surface's
builder, validator, and test as well.

## Future growth rule

Mechanics may grow only when they make owner routing easier, not when they make
the center feel more powerful.

A new mechanic branch must name:

- trigger
- center-owned law
- stronger owner
- stop-line
- generated or validation companion, when one exists
- current status
- owner-local landing route

A planted mechanic is not operational merely because it is named.

A landed mechanic is not runtime merely because it has a validator.

An operational mechanic must land in the owner repository that owns its truth.

## Final rule

The mechanic is only healthy when it makes ownership clearer.

If a mechanic makes AoA feel powerful while making owners, proof, or stop-lines
harder to name, return to the last valid anchor and re-enter through a smaller
route.
