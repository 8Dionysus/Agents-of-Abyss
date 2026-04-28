# AoA Mechanics Atlas

This is the branch point for center-level AoA mechanics.

Use it after the first-reading route:

1. `README.md`
2. `CHARTER.md`
3. `ECOSYSTEM_MAP.md`
4. `docs/FEDERATION_RULES.md`

When a human or agent asks **what kind of move is this?**, this atlas points to
the right mechanic, source split, stop-line, machine companion, owner request,
and verification lane.

This file does not create new authority. It keeps the root README human-sized
and routes deeper machinery back to the package that owns it.

## Root Mechanics Files

The root of `mechanics/` is a dispatcher, not a second doctrine store.

| File | Owns | Must not become |
|---|---|---|
| [`mechanics/AGENTS.md`](AGENTS.md) | local law for the mechanics tree, editing posture, closeout contract, and centralized validation | mechanic doctrine or package-specific meaning |
| [`mechanics/README.md`](README.md) | this atlas, route contract, mechanic compass, and card contract | a duplicate of package `README.md`, `PARTS.md`, `OWNER_MAP.md`, or `LANDING_LOG.md` |
| [`mechanics/ARTIFACT_TOPOLOGY.md`](ARTIFACT_TOPOLOGY.md) | where schemas, examples, config, generated companions, scripts, tests, and quests belong | a migration log or alias map |
| [`mechanics/OWNER_REQUEST_PROTOCOL.md`](OWNER_REQUEST_PROTOCOL.md) | owner-request fields, status vocabulary, priority vocabulary, advancement rules, and stop-lines | the current request index |
| [`mechanics/OWNER_REQUEST_QUEUE.md`](OWNER_REQUEST_QUEUE.md) | human queue index and package request routes | protocol vocabulary source, owner acceptance, or proof |

Generated indexes reflect registry and package cards. They do not author
mechanic truth.

## Canonical Route Contract

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

## Mechanic Card Contract

Every `mechanics/<slug>/README.md` is an agent-operable card, not merely a
human overview. The card lets a reader answer: **when do I use this, what does
the center own, who owns the stronger truth, what can enter, what can leave,
what must not be claimed, how do I validate it, and where do I route next?**

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

After the mechanic card, the package README should stay a lightweight entry
route: `## Active route`, `## Functioning parts`, `## Owner-request queue`,
`## Historical provenance`, `## Owner boundary`, and `## Growth posture`.
Deeper doctrine belongs in `DIRECTION.md`, `PARTS.md`, `OWNER_MAP.md`,
`OWNER_REQUESTS.md`, `PROVENANCE.md`, `LANDING_LOG.md`, `ROADMAP.md`, `docs/`,
or part-local files.

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

## Owner-request Queue

Mechanic cards name the owner split. The owner-request queue names the exact
owner-local landing packets that must exist before a center mechanic can be
claimed as operational outside the center.

Use these surfaces when the card output would become owner-local work:

- [`OWNER_REQUEST_PROTOCOL.md`](OWNER_REQUEST_PROTOCOL.md) for status grammar
  and advancement rules.
- [`OWNER_REQUEST_QUEUE.md`](OWNER_REQUEST_QUEUE.md) for the human request
  index.
- [`owner-request-queue.json`](owner-request-queue.json) for the source data.
- [`generated/owner_request_queue.min.json`](../generated/owner_request_queue.min.json)
  for compact machine entry.

A request packet is not owner acceptance. Owner repositories land operational
truth; the center keeps the queue honest. Derived visibility routes such as
`aoa-stats` summarize receipts after stronger owners land evidence; they do
not turn queue status into proof.

## How to Use This Atlas

1. Name the mechanic you are touching.
2. Read the mechanic card and stop-lines.
3. Identify the owner repository that owns the operational truth.
4. If the output crosses into owner-local work, open the matching owner-request
   packet.
5. Run the validator named by that mechanic and by the owner-request queue when
   validators exist.
6. If ownership is unclear, return to
   [`FEDERATION_RULES`](../docs/FEDERATION_RULES.md) before changing anything.

## Compass

| Mechanic | Center question | Current status | Start here | Must not claim |
|---|---|---|---|---|
| Constitutional polis | What does the center own, and what must stay outside it? | landed center law | [CHARTER](../CHARTER.md), [ECOSYSTEM_MAP](../ECOSYSTEM_MAP.md), [FEDERATION_RULES](../docs/FEDERATION_RULES.md), [ROOT_SURFACE_LAW](../docs/ROOT_SURFACE_LAW.md) | layer-owned truth or root-surface inflation |
| Layer ownership | Which repository owns this object class? | landed route map | [LAYERS](../docs/LAYERS.md), [REPO_ROLES](../docs/REPO_ROLES.md) | convenience ownership transfer |
| Method-growth | How does repeated work become candidate, seed, proof, method, memory, derived summary, or owner landing? | landed center route package | [README](method-growth/README.md), [PARTS](method-growth/PARTS.md), [OWNER_MAP](method-growth/OWNER_MAP.md), [OWNER_REQUESTS](method-growth/OWNER_REQUESTS.md) | center-owned final object truth, proof verdict, or memory canon |
| Distillation | How does heavy source material become active form without losing provenance or inflating authority? | landed center route package | [README](distillation/README.md), [PARTS](distillation/PARTS.md), [OWNER_MAP](distillation/OWNER_MAP.md), [OWNER_REQUESTS](distillation/OWNER_REQUESTS.md) | summary-as-proof, memory canon, runtime activation, owner acceptance, or ToS canon |
| Growth Cycle | How does reviewed agent-process work move through checkpoint, closeout, harvest, progression, repair, quest promotion, and owner followthrough? | landed center route package | [README](growth-cycle/README.md), [PARTS](growth-cycle/PARTS.md), [OWNER_MAP](growth-cycle/OWNER_MAP.md), [OWNER_REQUESTS](growth-cycle/OWNER_REQUESTS.md) | hidden scheduler, proof verdict, memory canon, runtime activation, owner acceptance, or universal progression score |
| Recurrence | How does AoA recover when a route loses its axis and must re-enter through a valid anchor? | landed return law | [README](recurrence/README.md), [PARTS](recurrence/PARTS.md), [OWNER_MAP](recurrence/OWNER_MAP.md), [OWNER_REQUESTS](recurrence/OWNER_REQUESTS.md) | ambient continuity, hidden memory sovereignty, or automatic recursor spawn |
| Checkpoint | How does intermediate state preserve, review, return, bridge, export, or hand off without stealing owner truth? | landed center law | [README](checkpoint/README.md), [PARTS](checkpoint/PARTS.md), [OWNER_MAP](checkpoint/OWNER_MAP.md), [OWNER_REQUESTS](checkpoint/OWNER_REQUESTS.md) | checkpoint implementation authority or owner acceptance |
| Experience | Which staged experience contract, office/service posture, seed intake, duel pressure, continuity loom, or runtime boundary is relevant? | planted center contracts through v2.0 | [README](experience/README.md), [PARTS](experience/PARTS.md), [PROVENANCE](experience/PROVENANCE.md), [OWNER_REQUESTS](experience/OWNER_REQUESTS.md) | live workspace runtime or owner-local activation |
| Agon | Which pressure, lawful move, duel, arena, packet, verdict, retention, rank, school, canon, or threshold boundary is relevant? | landed center law and pre-protocol grammar | [README](agon/README.md), [PARTS](agon/PARTS.md), [PROVENANCE](agon/PROVENANCE.md), [OWNER_REQUESTS](agon/OWNER_REQUESTS.md) | live arena execution, assistant contestant authority, rank mutation, or ToS canon write authority |
| Antifragility | What stress, degraded mode, evidence, pruning, or anti-authority posture applies? | landed center doctrine | [README](antifragility/README.md), [PARTS](antifragility/PARTS.md), [OWNER_MAP](antifragility/OWNER_MAP.md), [OWNER_REQUESTS](antifragility/OWNER_REQUESTS.md) | one-score health, deletion theater, or owner-local cleanup authority |
| Questbook | What obligation must survive the current diff as a public tracked follow-up? | landed public obligation model | [README](questbook/README.md), [PARTS](questbook/PARTS.md), [model-spine](questbook/parts/model-spine/README.md), [QUESTBOOK](../QUESTBOOK.md) | second roadmap or private scratchpad |
| RPG | How can progression, questlines, campaigns, roles, and feats be read without rewriting ownership? | landed adjunct reflection layer | [README](rpg/README.md), [PARTS](rpg/PARTS.md), [source-boundary](rpg/parts/source-boundary/README.md), [vocabulary-overlay](rpg/parts/vocabulary-overlay/README.md) | hidden ontology, runtime ledger, or decorative game skin |
| Boundary-bridge | How can AoA connect owner-owned surfaces without identity collapse or authority transfer? | landed bridge law | [README](boundary-bridge/README.md), [PARTS](boundary-bridge/PARTS.md), [tos-support](boundary-bridge/parts/tos-support/README.md), [OWNER_REQUESTS](boundary-bridge/OWNER_REQUESTS.md) | identity collapse, AoA-authored ToS canon, or owner acceptance without receipt |
| Release-support | Which transitions or claims can the center support, publish, hand off, or roll back? | landed state-transition posture | [README](release-support/README.md), [PARTS](release-support/PARTS.md), [PUBLIC_SUPPORT_POSTURE](release-support/docs/PUBLIC_SUPPORT_POSTURE.md), [OWNER_REQUESTS](release-support/OWNER_REQUESTS.md) | GitHub-only release definition or unverified public claim |

## Package Route Standard

For a mechanic package, start with the package `README.md`. Then use only the
surface that matches the work:

| Surface | Use for |
|---|---|
| `AGENTS.md` | local law, post-change route review, closeout, validation |
| `DIRECTION.md` | current operating contour |
| `PARTS.md` | active functioning parts and part routes |
| `OWNER_MAP.md` | center role and stronger owner split |
| `OWNER_REQUESTS.md` | ready-to-carry owner-local request packets |
| `PROVENANCE.md` | active-first bridge to historical or sibling evidence |
| `LANDING_LOG.md` | checked landings, validation anchors, and stop-lines |
| `ROADMAP.md` | next contour and condition-based future work |
| `docs/` | detailed mechanic-owned doctrine and support notes |
| `parts/` | functioning sub-mechanics and part-local artifacts |
| `legacy/` | preserved source history that should not burden active routes |

If a package has a part-local `AGENTS.md`, follow it after the package card.

## Package Anchors

Use this section only to jump to the right package. Do not treat these short
notes as substitutes for package-local truth.

| Package | Active anchors |
|---|---|
| `method-growth` | [ROOTLINE](method-growth/docs/ROOTLINE.md), [METHOD_SPINE](method-growth/docs/METHOD_SPINE.md), [REVIEWABLE_GROWTH_REFINERY](method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md), [CANDIDATE_LINEAGE_CROSSWALK](method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md), `mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md` |
| `distillation` | [DISTILLATION_LAW](distillation/docs/DISTILLATION_LAW.md), [PARTS](distillation/PARTS.md), [PROVENANCE](distillation/PROVENANCE.md) |
| `growth-cycle` | [GROWTH_CYCLE_LAW](growth-cycle/docs/GROWTH_CYCLE_LAW.md), [PARTS](growth-cycle/PARTS.md), [PROVENANCE](growth-cycle/PROVENANCE.md) |
| `recurrence` | `mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md`, `mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md`, [RECURRENCE_PRINCIPLE](recurrence/docs/RECURRENCE_PRINCIPLE.md), [PARTS](recurrence/PARTS.md) |
| `checkpoint` | [CHECKPOINT_LAW](checkpoint/docs/CHECKPOINT_LAW.md), [CHECKPOINT_OWNER_BOUNDARY](checkpoint/docs/CHECKPOINT_OWNER_BOUNDARY.md), [PARTS](checkpoint/PARTS.md) |
| `experience` | [DIRECTION](experience/DIRECTION.md), [PARTS](experience/PARTS.md), [LANDING_LOG](experience/LANDING_LOG.md), [PROVENANCE](experience/PROVENANCE.md), [OWNER_REQUESTS](experience/OWNER_REQUESTS.md) |
| `agon` | [DIRECTION](agon/DIRECTION.md), [PARTS](agon/PARTS.md), [LANDING_LOG](agon/LANDING_LOG.md), [agon/PROVENANCE.md](agon/PROVENANCE.md), [agon/legacy/INDEX.md](agon/legacy/INDEX.md) |
| `antifragility` | [ANTIFRAGILITY](antifragility/docs/ANTIFRAGILITY.md), [VIA_NEGATIVA](antifragility/docs/VIA_NEGATIVA.md), [ANTI_AUTHORITY_RULES](antifragility/docs/ANTI_AUTHORITY_RULES.md), [ONE_IN_ONE_OUT](antifragility/docs/ONE_IN_ONE_OUT.md), [FRAGILITY_BLACKLIST](../FRAGILITY_BLACKLIST.md), [DELETION_CANDIDATES.json](../docs/audits/DELETION_CANDIDATES.json) |
| `questbook` | [model-spine](questbook/parts/model-spine/README.md), [source-contract](questbook/parts/source-contract/README.md), [relation-shape](questbook/parts/relation-shape/README.md), [`quests/`](../quests/) |
| `rpg` | [source-boundary](rpg/parts/source-boundary/README.md), [vocabulary-overlay](rpg/parts/vocabulary-overlay/README.md), [quest-campaign](rpg/parts/quest-campaign/README.md), [USAGE](rpg/USAGE.md) |
| `boundary-bridge` | [ToS Support](boundary-bridge/parts/tos-support/README.md), [COUNTERPART_BRIDGE](boundary-bridge/docs/COUNTERPART_BRIDGE.md), [WITNESS_COMPOST](boundary-bridge/docs/WITNESS_COMPOST.md) |
| `release-support` | [PUBLIC_SUPPORT_POSTURE](release-support/docs/PUBLIC_SUPPORT_POSTURE.md), [DIRECTION_SURFACES](release-support/docs/DIRECTION_SURFACES.md), [FEDERATION_RELEASE_PROTOCOL](release-support/docs/FEDERATION_RELEASE_PROTOCOL.md), [RELEASING](release-support/docs/RELEASING.md) |

## Agon Quick Map

Agon has many active parts, so this atlas keeps a name index for route
discovery only. Use [Agon PARTS](agon/PARTS.md) and part-local files for
meaning.

| Part | Route |
|---|---|
| Imposition Readiness | [imposition-readiness](agon/parts/imposition-readiness/README.md) |
| Lawful Move Grammar | [lawful-move-grammar](agon/parts/lawful-move-grammar/README.md) |
| Owner Binding | [owner-binding](agon/parts/owner-binding/README.md) |
| Gate Routing | [gate-routing](agon/parts/gate-routing/README.md) |
| Trial Handoff | [trial-handoff](agon/parts/trial-handoff/README.md) |
| Recurrence Adapter | [recurrence-adapter](agon/parts/recurrence-adapter/README.md) |
| Packet Arena | [packet-arena](agon/parts/packet-arena/README.md) |
| Duel Kernel | [duel-kernel](agon/parts/duel-kernel/README.md) |
| Verdict Retention Rank | [verdict-retention-rank](agon/parts/verdict-retention-rank/README.md) |
| Epistemic KAG | [epistemic-kag](agon/parts/epistemic-kag/README.md) |
| Sophian Threshold | [sophian-threshold](agon/parts/sophian-threshold/README.md) |
| Compatibility Bridges | [compatibility-bridges](agon/parts/compatibility-bridges/README.md) |

## Artifact Placement

Mechanics are not documentation-only packages. When a schema, example, seed
config, generated companion, validator, test, or quest rule belongs to one
mechanic, its source home is the mechanic package or the nearest owning part.
Root technical districts keep repo-wide contracts only.

Use [`ARTIFACT_TOPOLOGY`](ARTIFACT_TOPOLOGY.md) before moving artifacts between
root districts and mechanic homes.

## Validation

Executable commands for this atlas live in
[mechanics/AGENTS.md](AGENTS.md#validation).

For package-local work, start with the nearest package `AGENTS.md` and add the
central validation lane only when the change touches registry, owner queue,
generated indexes, public route surfaces, or release-bound claims.

## Future Growth Rule

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

## Final Rule

The mechanic is only healthy when it makes ownership clearer.

If a mechanic makes AoA feel powerful while making owners, proof, or stop-lines
harder to name, return to the last valid anchor and re-enter through a smaller
route.
