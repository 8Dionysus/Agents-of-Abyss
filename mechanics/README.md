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
repo-wide contracts only. See
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

After the mechanic card, the README should stay a lightweight entry route:
`## Active route`, `## Functioning parts`, `## Owner-request queue`,
`## Historical provenance`, `## Owner boundary`, and `## Growth posture`.
Keep deeper doctrine in the linked owner surfaces instead of expanding the
README into a second manual.

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

Use the validation lane in [mechanics/AGENTS.md](AGENTS.md#validation) for executable commands.

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

Use the validation lane in [mechanics/AGENTS.md](AGENTS.md#validation) for executable commands.

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
| Method and growth refinery | How does repeated work move from donor or checkpoint to candidate, seed, owner landing, proof, method, memory, or derived summary? | active center route package | [Method-growth](method-growth/README.md), [PARTS](method-growth/PARTS.md), [OWNER_MAP](method-growth/OWNER_MAP.md) | center-owned scenario canon or final object truth |
| Distillation | How does heavy source material become active form without losing provenance or inflating authority? | landed center route package | [Distillation](distillation/README.md), [PARTS](distillation/PARTS.md), [OWNER_MAP](distillation/OWNER_MAP.md) | summary-as-proof, memory canon, runtime activation, owner acceptance, or ToS canon |
| Growth Cycle | How does reviewed agent-process work move through checkpoint, closeout, harvest, progression, forks, automation scan, diagnosis, repair, quest promotion, and owner followthrough? | landed center route package | [Growth Cycle](growth-cycle/README.md), [PARTS](growth-cycle/PARTS.md), [OWNER_MAP](growth-cycle/OWNER_MAP.md) | hidden scheduler, proof verdict, memory canon, runtime activation, owner acceptance, or universal progression score |
| Recurrence, return, continuity | How does AoA recover when a route loses its axis and must re-enter through a valid anchor? | bounded return law | [Recurrence](recurrence/README.md), [PARTS](recurrence/PARTS.md), [OWNER_MAP](recurrence/OWNER_MAP.md) | ambient continuity, hidden memory sovereignty, or automatic recursor spawn |
| Checkpoint | How does intermediate state preserve, review, return, bridge, export, or hand off without stealing owner truth? | landed center law | [Checkpoint](checkpoint/README.md), [PARTS](checkpoint/PARTS.md), [OWNER_MAP](checkpoint/OWNER_MAP.md) | checkpoint implementation authority or owner acceptance |
| Experience | Which staged experience contract, office/service posture, seed intake, duel pressure, continuity loom, or runtime boundary is relevant? | planted center contracts through v2.0 | [Experience](experience/README.md) | live workspace runtime or owner-local activation |
| Agon | Which pressure, lawful move, duel, arena, packet, verdict, retention, rank, school, canon, or threshold boundary is relevant? | center-owned pre-protocol law and candidate grammar | [Agon](agon/README.md) | live arena execution or assistant contestant authority |
| Antifragility and subtraction | What stress, degraded mode, evidence, pruning, or anti-authority posture applies? | center doctrine | [Antifragility](antifragility/README.md), [PARTS](antifragility/PARTS.md), [OWNER_MAP](antifragility/OWNER_MAP.md) | one-score health or deletion theater |
| Questbook | What obligation must survive the current diff as a public tracked follow-up? | public obligation model | [QUESTBOOK](../QUESTBOOK.md), [model-spine](questbook/parts/model-spine/README.md) | second roadmap or private scratchpad |
| RPG reflection | How can progression, questlines, campaigns, roles, and feats be read without rewriting ownership? | adjunct reflection layer | [RPG](rpg/README.md), [PARTS](rpg/PARTS.md), [source-boundary](rpg/parts/source-boundary/README.md), [vocabulary-overlay](rpg/parts/vocabulary-overlay/README.md) | hidden ontology or runtime ledger |
| Boundary bridge, ToS support, witness, compost | How can AoA connect owner-owned surfaces without identity collapse or authority transfer? | bridge law and ToS-support doctrine | [Boundary bridge](boundary-bridge/README.md), [PARTS](boundary-bridge/PARTS.md), [tos-support](boundary-bridge/parts/tos-support/README.md) | identity collapse, AoA-authored ToS canon, or owner acceptance without receipt |
| Release, audit, public support | Which transitions or claims can the center support, publish, hand off, or roll back? | state-transition and release posture | [Release support](release-support/README.md), [PARTS](release-support/PARTS.md), [PUBLIC_SUPPORT_POSTURE](release-support/docs/PUBLIC_SUPPORT_POSTURE.md) | GitHub-only release definition or unverified public claim |

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

Use the validation lane in [mechanics/AGENTS.md](AGENTS.md#validation) for executable commands.

## Method, growth, and owner landing

Use this branch when the object is not just a task, but a repeated route that
may become technique, skill, playbook, proof, memory, derived summary, or
owner-local doctrine.

Active package routes:

- [Method-growth](method-growth/README.md): package card and owner boundary.
- [DIRECTION](method-growth/DIRECTION.md): current direction and working standard.
- [PARTS](method-growth/PARTS.md): active functioning parts.
- [OWNER_MAP](method-growth/OWNER_MAP.md): center role and stronger owners.
- [OWNER_REQUESTS](method-growth/OWNER_REQUESTS.md): ready-to-carry request packets.
- [PROVENANCE](method-growth/PROVENANCE.md): source and sibling-evidence bridge.

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
| Reusable practice | `aoa-techniques` |
| Seed staging | `Dionysus` |
| Final object truth | the final owner repo |
| Proof | `aoa-evals` |
| Recurring method | `aoa-playbooks` |
| Derived summary | `aoa-stats` |
| Bounded memory and lessons | `aoa-memo` |

Validation anchors:

Use the validation lane in [mechanics/AGENTS.md](AGENTS.md#validation) for executable commands.

## Distillation

Use this branch when material is too heavy, raw, historical, exploratory,
runtime-shaped, or witness-facing to be an active route, but something inside it
must survive as current function.

Active package routes:

- [Distillation](distillation/README.md): package card and owner boundary.
- [DIRECTION](distillation/DIRECTION.md): current direction and working standard.
- [PARTS](distillation/PARTS.md): active functioning parts.
- [OWNER_MAP](distillation/OWNER_MAP.md): center role and stronger owners.
- [OWNER_REQUESTS](distillation/OWNER_REQUESTS.md): ready-to-carry request packets.
- [PROVENANCE](distillation/PROVENANCE.md): source and future archive bridge.

Core law:

- [DISTILLATION_LAW](distillation/docs/DISTILLATION_LAW.md) keeps the sequence
  source route, review state, active function, and owner boundary explicit.

Owner split:

| Slice | Stronger owner |
|---|---|
| Reusable distillation practice | `aoa-techniques` |
| Executable workflow | `aoa-skills` |
| Recurring scenario | `aoa-playbooks` |
| Runtime distill phase and artifact contract | `aoa-agents` |
| Memory writeback candidates | `aoa-memo` |
| Provenance-preservation proof | `aoa-evals` |
| Typed helpers and readers | `aoa-sdk` |
| Seed and donor staging | `Dionysus` |
| Compost, principle, and canon meaning | `Tree-of-Sophia` |
| Runtime storage and exports | `abyss-stack` |

Validation anchors:

Use the validation lane in [mechanics/AGENTS.md](AGENTS.md#validation) for executable commands.

## Growth Cycle

Use this branch when a reviewed work cycle or agent process needs to move from
checkpoint through closeout, harvest, progression, route choice, automation
opportunity, diagnosis, repair, quest promotion, and owner followthrough.

Active package routes:

- [Growth Cycle](growth-cycle/README.md): package card and owner boundary.
- [DIRECTION](growth-cycle/DIRECTION.md): current direction and working standard.
- [PARTS](growth-cycle/PARTS.md): active functioning parts.
- [OWNER_MAP](growth-cycle/OWNER_MAP.md): center role and stronger owners.
- [OWNER_REQUESTS](growth-cycle/OWNER_REQUESTS.md): ready-to-carry request packets.
- [PROVENANCE](growth-cycle/PROVENANCE.md): source and sibling-evidence bridge.

Core law:

- [GROWTH_CYCLE_LAW](growth-cycle/docs/GROWTH_CYCLE_LAW.md) keeps stage order,
  review law, owner law, and stop-lines explicit.

Owner split:

| Slice | Stronger owner |
|---|---|
| Hooks, ledgers, closeout context, typed helpers | `aoa-sdk` |
| Executable cycle stages | `aoa-skills` |
| Self-agent posture | `aoa-agents` |
| Proof, verdict, and regression | `aoa-evals` |
| Memory writeback and failure lessons | `aoa-memo` |
| Recurring choreography | `aoa-playbooks` |
| Derived visibility | `aoa-stats` |
| Route hints | `aoa-routing` |
| Reviewed snapshots and seeds | `Dionysus` |
| Runtime exports and health receipts | `abyss-stack` |

Validation anchors:

Use the validation lane in [mechanics/AGENTS.md](AGENTS.md#validation) for executable commands.

## Recurrence, return, and continuity

Use this branch when a route lost its axis, must recurse back into a valid
anchor, needs bounded re-entry, or must preserve duration without pretending
that continuity is ambient memory.

Core law:

- [DIRECTION](recurrence/DIRECTION.md): present contour for honest return,
  bounded re-entry, and owner-local follow-through.
- [PARTS](recurrence/PARTS.md): active recurrence parts for Anchor Return,
  Continuity Window, Component Refresh, Control Plane Carry, Reentry Routing,
  Memory Recall, Scenario Choreography, Proof Gates, Runtime Return, and
  Recursor Boundary.
- [OWNER_MAP](recurrence/OWNER_MAP.md): stronger-owner route map.
- [OWNER_REQUESTS](recurrence/OWNER_REQUESTS.md): center-side owner-local
  landing requests.
- [PROVENANCE](recurrence/PROVENANCE.md): source trail and sibling evidence
  bridge.
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
- `aoa-sdk` owns typed recurrence carry, manifests, graph closure, projections,
  and reviewed handoff packets.
- `aoa-routing` may point toward re-entry, but does not own recurrence meaning.
- `aoa-memo` owns checkpoint, recall, and provenance surfaces.
- `aoa-agents` owns role and handoff posture for returns between actors.
- `aoa-playbooks` owns recurring return choreography.
- `aoa-evals` owns drift and recovery-quality proof.
- `aoa-stats` owns derived recurrence visibility.
- `aoa-kag` owns derived regrounding toward stronger source refs.
- `abyss-stack` owns runtime wrappers only after runtime-owner gates.

## Checkpoint

Use this branch when work reaches an intermediate state that must survive
session boundaries, review gates, return and re-entry, closeout bridging,
runtime export, or owner handoff without becoming owner-local truth.

Core law:

- [CHECKPOINT_LAW](checkpoint/docs/CHECKPOINT_LAW.md): checkpoint is a bounded
  intermediate form, not a hidden scheduler, proof verdict, memory canon,
  runtime activation, stats truth, or owner acceptance.
- [CHECKPOINT_OWNER_BOUNDARY](checkpoint/docs/CHECKPOINT_OWNER_BOUNDARY.md):
  AoA owns checkpoint law and route grammar; sibling repositories own local
  controls, protocol, proof, memory, runtime, stats, roles, and snapshots.
- [OWNER_MAP](checkpoint/OWNER_MAP.md): each checkpoint pressure routes to the
  repository that can actually land operational truth.
- [PARTS](checkpoint/PARTS.md): active checkpoint routes are session carry,
  review gate, return re-entry, closeout bridge, runtime export, and owner
  handoff.

Owner split:

- `aoa-sdk` operates checkpoint controls, hooks, local ledgers, typed readers,
  and closeout-context builders.
- `aoa-skills` owns checkpoint-note protocol and explicit closeout bridge
  skills.
- `aoa-agents`, `aoa-memo`, `aoa-playbooks`, `aoa-evals`, `aoa-routing`,
  `aoa-stats`, `Dionysus`, and `abyss-stack` own their local checkpoint
  meanings after owner-local acceptance.

Validation anchors:

Use the validation lane in [mechanics/checkpoint/AGENTS.md](checkpoint/AGENTS.md#validation).

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

Validation starts in [Experience AGENTS](experience/AGENTS.md#validation);
follow its part-specific route for the active part or versioned contract you
changed.

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

### Agon part map

| Part | Role |
|---|---|
| [Imposition Readiness](agon/parts/imposition-readiness/README.md) | conservative boundary, survival lens, and first pressure gate before live protocol |
| [Lawful Move Grammar](agon/parts/lawful-move-grammar/README.md) | center vocabulary and registry contour without execution authority |
| [Owner Binding](agon/parts/owner-binding/README.md) | owner gravity for moves and explicit non-landed requests |
| [Gate Routing](agon/parts/gate-routing/README.md) | handoff to routing without granting route authority |
| [Trial Handoff](agon/parts/trial-handoff/README.md) | handoff to playbook choreography without granting scenario authority |
| [Recurrence Adapter](agon/parts/recurrence-adapter/README.md) | recurrence route pressure without owning continuity runtime |
| [Packet Arena](agon/parts/packet-arena/README.md) | state packets, sessions, seats, pressure, and lifecycle without live arena |
| [Duel Kernel](agon/parts/duel-kernel/README.md) | duel grammar, model-of-other, sealed commit, and mechanical trial pressure |
| [Verdict Retention Rank](agon/parts/verdict-retention-rank/README.md) | verdict, delta, scar, retention, rank, and inscription boundaries |
| [Epistemic KAG](agon/parts/epistemic-kag/README.md) | epistemic contest and KAG promotion candidates without truth ownership |
| [Sophian Threshold](agon/parts/sophian-threshold/README.md) | ToS/Sophian thresholds, canon restraint, and terminal outcome boundaries |
| [Compatibility Bridges](agon/parts/compatibility-bridges/README.md) | law interlocks, schools, lineages, campaigns, contradiction, closure, and summon grammar |

Detailed raw wave and model provenance lives behind
[Agon provenance](agon/PROVENANCE.md), with the full raw index at
[agon/legacy/INDEX.md](agon/legacy/INDEX.md).

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
| [Antifragility package](antifragility/README.md) | active route card |
| [DIRECTION](antifragility/DIRECTION.md) | current growth posture |
| [PARTS](antifragility/PARTS.md) | functioning part index |
| [ANTIFRAGILITY](antifragility/docs/ANTIFRAGILITY.md) | stress should make the system more legible, bounded, and teachable |
| [VIA_NEGATIVA](antifragility/docs/VIA_NEGATIVA.md) | subtraction as doctrine |
| [ANTI_AUTHORITY_RULES](antifragility/docs/ANTI_AUTHORITY_RULES.md) | stop authority inflation |
| [ONE_IN_ONE_OUT](antifragility/docs/ONE_IN_ONE_OUT.md) | sprawl pressure rule |
| [FRAGILITY_BLACKLIST](../FRAGILITY_BLACKLIST.md) | known fragile patterns |
| [DELETION_CANDIDATES](../docs/audits/DELETION_CANDIDATES.json) | deletion candidates |
| [PROVENANCE](antifragility/PROVENANCE.md) | legacy/raw source bridge |

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
- [`quests/`](../quests/): lane-first lifecycle item store for center, Agon, Experience, and future mechanic follow-through work.
- [Questbook model spine](questbook/parts/model-spine/README.md): Questbook spine and route map to lifecycle, execution-passport, harvest, relation, and owner-route parts.
- [Questbook legacy first wave](questbook/legacy/raw/QUESTBOOK_FIRST_WAVE.md): preserved first-contour guardrails.

RPG reflection surfaces:

- [RPG](rpg/README.md): package entry and mechanic card.
- [PARTS](rpg/PARTS.md): active RPG sub-mechanic map.
- [source-boundary](rpg/parts/source-boundary/README.md): source, proof, runtime, and presentation precedence.
- [vocabulary-overlay](rpg/parts/vocabulary-overlay/README.md): stable machine keys and themed labels.
- [PROVENANCE](rpg/PROVENANCE.md): bridge to preserved legacy raw sources when history is needed.

Boundary:

- Questbook is not a second roadmap.
- RPG is not a hidden ontology.
- Progression evidence is not a global score.
- Campaign language must not imply runtime ledger ownership.

## Boundary Bridge, ToS Support, Witness, and Compost

Use this branch when AoA connects owner-owned surfaces without identity
collapse, authority transfer, or AoA-authored ToS meaning.

| Surface | Role |
|---|---|
| [ROOTLINE](method-growth/docs/ROOTLINE.md) | trunk-first AoA x ToS coordination spine |
| [Boundary bridge](boundary-bridge/README.md) | center mechanic card for non-identity bridge law |
| [PARTS](boundary-bridge/PARTS.md) | active operating map for cross-owner bridge work |
| [ToS Support](boundary-bridge/parts/tos-support/README.md) | support Tree-of-Sophia without authoring ToS meaning |
| [COUNTERPART_BRIDGE](boundary-bridge/docs/COUNTERPART_BRIDGE.md) | counterpart mappings stay derived, optional, and non-identity |
| [WITNESS_COMPOST](boundary-bridge/docs/WITNESS_COMPOST.md) | witness and compost pilot doctrine |
| [OWNER_REQUESTS](boundary-bridge/OWNER_REQUESTS.md) | owner-local packets before bridge support is operational |

Rule:

`Tree-of-Sophia` owns authored knowledge meaning.

AoA may route, support, derive, witness, prepare, and hand off, but the bridge
never transfers owner truth.

It does not become ToS canon.

## Release, audit, and support posture

Use this branch when a public claim, release surface, audit route, landing
closeout, owner handoff, checkpoint or quest closeout, direction update, or
rollback-sensitive transition must be checked.

| Surface | Role |
|---|---|
| [Release support](release-support/README.md) | mechanic entry card |
| [DIRECTION](release-support/DIRECTION.md) | release as state-transition direction |
| [PARTS](release-support/PARTS.md) | active operating routes for transition claims |
| [OWNER_MAP](release-support/OWNER_MAP.md) | stronger owner split for release-support moves |
| [OWNER_REQUESTS](release-support/OWNER_REQUESTS.md) | center-side owner handoff packets |
| [PROVENANCE](release-support/PROVENANCE.md) | source trace and legacy bridge |
| [PUBLIC_SUPPORT_POSTURE](release-support/docs/PUBLIC_SUPPORT_POSTURE.md) | what the center may honestly claim |
| [DIRECTION_SURFACES](release-support/docs/DIRECTION_SURFACES.md) | current direction surface per repo |
| [FEDERATION_RELEASE_PROTOCOL](release-support/docs/FEDERATION_RELEASE_PROTOCOL.md) | shared release completeness contract |
| [RELEASING](release-support/docs/RELEASING.md) | center release runbook |
| [ECOSYSTEM_AUDIT_INDEX](../ECOSYSTEM_AUDIT_INDEX.md), [ROOT_SURFACE_AUDIT_2026_04_24](../docs/audits/ROOT_SURFACE_AUDIT_2026_04_24.md) | audit index |
| [CODEX_AUDIT_PROTOCOL](../docs/audits/CODEX_AUDIT_PROTOCOL.md) | Codex audit protocol |
| [CODEX_SKILL_PROOF_AUDIT_BRIDGE](../docs/audits/CODEX_SKILL_PROOF_AUDIT_BRIDGE.md) | skill/proof audit bridge |

Compact validation:

Use the validation lane in [mechanics/AGENTS.md](AGENTS.md#validation) for executable commands.

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
