# AoA Mechanics Atlas

This is the single branch point for center-level processes and engineering philosophy in `Agents-of-Abyss`.

Use it after the root `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/FEDERATION_RULES.md`, and `docs/REPO_ROLES.md`. The purpose is simple: when a human or agent asks **what kind of move is this?**, this atlas points to the right mechanic, owner split, stop-line, machine companion, and verification path.

This file does not create new authority. It keeps the root README human-sized while giving agents a precise map of the deeper machinery.

## How to use this atlas

1. Name the mechanic you are touching.
2. Read the mechanic's center entry and stop-lines.
3. Identify the owner repository that owns the operational truth.
4. Run the validator named by that mechanic when a validator exists.
5. If ownership is unclear, return to [FEDERATION_RULES](FEDERATION_RULES.md) before changing anything.

## Compass

| Mechanic | Center question | Current status | Start here | Must not claim |
|---|---|---|---|---|
| Constitutional polis | What does the center own, and what must stay outside it? | landed center law | [CHARTER](../CHARTER.md), [ECOSYSTEM_MAP](../ECOSYSTEM_MAP.md), [FEDERATION_RULES](FEDERATION_RULES.md), [ROOT_SURFACE_LAW](ROOT_SURFACE_LAW.md) | layer-owned truth or root-surface inflation |
| Layer ownership | Which repository owns this object class? | landed route map | [LAYERS](LAYERS.md), [REPO_ROLES](REPO_ROLES.md) | convenience ownership transfer |
| Method and growth refinery | How does repeated work move from donor or checkpoint to candidate, seed, owner landing, proof, method, memory, or derived summary? | center doctrine and cross-owner route | [METHOD_SPINE](METHOD_SPINE.md), [REVIEWABLE_GROWTH_REFINERY](REVIEWABLE_GROWTH_REFINERY.md) | center-owned scenario canon |
| Recursion, recurrence, return, continuity | How does AoA recover when a route loses its axis and must re-enter through a valid anchor? | bounded return law | [RECURRENCE_PRINCIPLE](RECURRENCE_PRINCIPLE.md), [SELF_AGENCY_CONTINUITY](SELF_AGENCY_CONTINUITY.md) | ambient continuity or hidden memory sovereignty |
| Experience | Which staged experience contract, office/service posture, seed intake, duel pressure, continuity loom, or runtime boundary is relevant? | planted center contracts through v2.0 | [Experience](#experience) | live workspace runtime or owner-local activation |
| Agon | Which pressure, lawful move, duel, arena, packet, verdict, retention, rank, school, canon, or threshold boundary is relevant? | center-owned pre-protocol law and candidate grammar | [Agon](#agon) | live arena execution or assistant contestant authority |
| Antifragility and subtraction | What stress, degraded mode, evidence, pruning, or anti-authority posture applies? | center doctrine | [ANTIFRAGILITY](ANTIFRAGILITY.md), [VIA_NEGATIVA](VIA_NEGATIVA.md) | one-score health or deletion theater |
| Questbook | What obligation must survive the current diff as a public tracked follow-up? | public obligation model | [QUESTBOOK](../QUESTBOOK.md), [QUESTBOOK_MODEL](QUESTBOOK_MODEL.md) | second roadmap or private scratchpad |
| RPG reflection | How can progression, questlines, campaigns, roles, and feats be read without rewriting ownership? | adjunct reflection layer | [RPG_LAYER_MODEL](RPG_LAYER_MODEL.md), [RPG_ARCHITECTURE_RFC](RPG_ARCHITECTURE_RFC.md) | hidden ontology or runtime ledger |
| ToS bridge, witness, compost | How can AoA support ToS without authoring ToS meaning? | support doctrine and seams | [COUNTERPART_BRIDGE](COUNTERPART_BRIDGE.md), [WITNESS_COMPOST](WITNESS_COMPOST.md) | AoA-authored ToS canon |
| Release, audit, public support | Which claims can the center publicly support? | release and CI posture | [PUBLIC_SUPPORT_POSTURE](PUBLIC_SUPPORT_POSTURE.md), [FEDERATION_RELEASE_PROTOCOL](FEDERATION_RELEASE_PROTOCOL.md), [RELEASING](RELEASING.md) | unverified public claim |

## Constitutional polis

The polis owns the civic map, not every district's inner law.

Read:

1. [CHARTER](../CHARTER.md) for mission and ownership boundary.
2. [ECOSYSTEM_MAP](../ECOSYSTEM_MAP.md) for the public contour.
3. [LAYERS](LAYERS.md) for conceptual layer definitions.
4. [REPO_ROLES](REPO_ROLES.md) for compact ownership routing.
5. [FEDERATION_RULES](FEDERATION_RULES.md) for source-of-truth law.
6. [ROOT_SURFACE_LAW](ROOT_SURFACE_LAW.md) for repository-root placement and cleanup law.
7. [PUBLIC_SUPPORT_POSTURE](PUBLIC_SUPPORT_POSTURE.md) for public claim and CI posture.

Machine companions:

- [`generated/README.md`](../generated/README.md)
- [`scripts/README.md`](../scripts/README.md)
- [`schemas/README.md`](../schemas/README.md)
- [`generated/center_entry_map.min.json`](../generated/center_entry_map.min.json)
- [`generated/ecosystem_registry.min.json`](../generated/ecosystem_registry.min.json)
- [`generated/federation_supporting_inventory.min.json`](../generated/federation_supporting_inventory.min.json)

Validation:

```bash
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_ecosystem.py
python scripts/validate_markdown_shape.py
python -m pytest -q tests
```

## Method, growth, and owner landing

Use this branch when the object is not just a task, but a repeated route that may become technique, skill, playbook, proof, memory, derived summary, or owner-local doctrine.

Core law:

- [ROOTLINE](ROOTLINE.md) keeps the trunk-first coordination spine.
- [METHOD_SPINE](METHOD_SPINE.md) says recurring scenario-level method belongs in `aoa-playbooks`.
- [REVIEWABLE_GROWTH_REFINERY](REVIEWABLE_GROWTH_REFINERY.md) names the non-sovereign chain `cluster_ref -> candidate_ref -> seed_ref -> object_ref`.
- [CANDIDATE_LINEAGE_CROSSWALK](CANDIDATE_LINEAGE_CROSSWALK.md) maps stages to owners.
- [OWNER_LANDING_AND_PRUNING](OWNER_LANDING_AND_PRUNING.md) handles post-candidate landing and pruning. Canonical route path: `docs/OWNER_LANDING_AND_PRUNING.md`.
- [COMPONENT_REFRESH_LAW](COMPONENT_REFRESH_LAW.md) handles owner-owned maintenance of one drifting technical component.

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

## Recursion, recurrence, return, and continuity

Use this branch when a route lost its axis, must recurse back into a valid anchor, needs bounded re-entry, or must preserve duration without pretending that continuity is magic ambient memory.

Core law:

- [RECURRENCE_PRINCIPLE](RECURRENCE_PRINCIPLE.md): when a route loses its axis, return to the last valid anchor before continuing.
- [SELF_AGENCY_CONTINUITY](SELF_AGENCY_CONTINUITY.md): continuity means bounded duration with explicit anchors and reviewable return, not permissionless autonomy.
- [COMPONENT_REFRESH_LAW](COMPONENT_REFRESH_LAW.md): drifting components refresh through owner-owned receipts, not mystical self-healing.
- [METHOD_SPINE](METHOD_SPINE.md): recurring return routes should become playbook-owned method.

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

- `Agents-of-Abyss` owns the center law and stop-lines.
- `aoa-routing` may point toward re-entry, but does not own recurrence meaning.
- `aoa-memo` owns checkpoint, recall, and provenance surfaces.
- `aoa-agents` owns role and handoff posture for returns between actors.
- `aoa-playbooks` owns recurring return choreography.
- `aoa-evals` owns drift and recovery-quality proof.
- `abyss-stack` owns runtime wrappers only after runtime-owner gates.

## Experience

Use this branch when working with staged experience contracts, office/service posture, seed intake, epistemic duel pressure, continuity loom, or the living-workspace runtime boundary.

Read this as planted center law, not live authority. These surfaces repeatedly forbid live runtime activation, hidden memory sovereignty, assistant contestant authority, direct ToS writes, and owner-truth theft unless a later owner-local gate lands the slice.

### Experience Wave 1-5

| Surface | Role |
|---|---|
| [EXPERIENCE_WAVE1_KERNEL](EXPERIENCE_WAVE1_KERNEL.md) | first experience-capture kernel for friction, recurrence, candidate, verdict, memory gate, owner route, and inert projection |
| [EXPERIENCE_WAVE2_CERTIFICATION_WATCHTOWER](EXPERIENCE_WAVE2_CERTIFICATION_WATCHTOWER.md) | certification discipline and gated watchtower contracts |
| [EXPERIENCE_WAVE3_FEDERATION_ADOPTION](EXPERIENCE_WAVE3_FEDERATION_ADOPTION.md) | federation harvest and owner-local adoption gates |
| [EXPERIENCE_WAVE4_POLIS_CONSTITUTION](EXPERIENCE_WAVE4_POLIS_CONSTITUTION.md) | polis governance, constitution runtime, sealed decisions, stays, appeals, and replayable precedent |
| [EXPERIENCE_WAVE5_SOVEREIGN_OFFICE](EXPERIENCE_WAVE5_SOVEREIGN_OFFICE.md) | installable sovereign release and first live-office contour, still bounded by owner-local authority |

### Experience v1.2 to v2.0 planting line

| Surface | Role |
|---|---|
| [EXPERIENCE_V1_2_TO_V2_0_BRIDGE](EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md) | center bridge from `Dionysus` intake into future owner-local planting waves |
| [EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS](EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md) | service mesh operations drills and no-runtime stop-lines |
| [EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS](EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS.md) | office foundry and role-pair split without hybrid-agent authority |
| [EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL](EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL.md) | mechanical arena kernel contour without live arena, verdicts, scars, retention, or assistant contestants |
| [EXPERIENCE_V1_5_EPISTEMIC_DUEL_MODEL_OF_OTHER_FORGE](EXPERIENCE_V1_5_EPISTEMIC_DUEL_MODEL_OF_OTHER_FORGE.md) | sealed model-of-other prediction, reveal scoring, countermodel pressure, revision, and bifurcation quality without live duel authority |
| [EXPERIENCE_V1_6_EPISTEMIC_MEMORY_RANK_REPUTATION_ENGINE](EXPERIENCE_V1_6_EPISTEMIC_MEMORY_RANK_REPUTATION_ENGINE.md) | rank, reputation, standing, and jurisdiction candidates without live rank mutation or memory truth |
| [EXPERIENCE_V1_7_AFFECTIVE_ECONOMY_HONOR_TREASURY](EXPERIENCE_V1_7_AFFECTIVE_ECONOMY_HONOR_TREASURY.md) | affect and honor grammar without consciousness claims, honor treasury activation, or rights authority |
| [EXPERIENCE_V1_8_CONTEXT_ROUTING_NERVOUS_SYSTEM](EXPERIENCE_V1_8_CONTEXT_ROUTING_NERVOUS_SYSTEM.md) | context routing, salience, budget, and route receipt grammar without live router engine or owner override |
| [EXPERIENCE_V1_9_CONTEXT_MEMORY_WEAVING_CONTINUITY_LOOM](EXPERIENCE_V1_9_CONTEXT_MEMORY_WEAVING_CONTINUITY_LOOM.md) | bounded continuity weave and re-entry grammar without private memory sovereignty or runtime installation |
| [EXPERIENCE_V2_0_LIVING_WORKSPACE_CONTINUITY_RUNTIME](EXPERIENCE_V2_0_LIVING_WORKSPACE_CONTINUITY_RUNTIME.md) | final center boundary before future owner-local living-workspace continuity hardening, still not live runtime |

Validation is version-specific. Use the matching `scripts/validate_experience_*.py` and `tests/test_experience_*.py` named by the surface you changed.

## Agon

Use this branch when pressure, contest, survival, lawful moves, arena sessions, sealed commitments, state packets, verdicts, scars, retention, rank, schools, canon promotion, or ToS thresholds are involved.

Agon is center-owned as law, vocabulary, stop-line, and owner-binding doctrine. It is not live arena execution in this repository. Owner repos must land their own slices before practice, workflows, proof, memory, stats, routing, actors, runtime, or ToS canon become operational truth.

### Agon phase map

This table names the branch, points to its first anchors, and keeps the full surface chain out of the root-facing atlas rows.

| Phase | Start here | Role |
|---|---|---|
| Baseline and imposition | [AGON_PREPARATION_POSTURE](AGON_PREPARATION_POSTURE.md), [AGON_IMPOSITION_POSTURE](AGON_IMPOSITION_POSTURE.md), [AGON_SURVIVAL_CRITERIA](AGON_SURVIVAL_CRITERIA.md) | conservative boundary, survival lens, and first pressure gate before live protocol |
| Lawful move language | [AGON_LAWFUL_MOVE_LANGUAGE](AGON_LAWFUL_MOVE_LANGUAGE.md), [AGON_MOVE_REGISTRY_MODEL](AGON_MOVE_REGISTRY_MODEL.md) | center vocabulary and registry contour without execution authority |
| Owner binding | [AGON_MOVE_OWNER_BINDING](AGON_MOVE_OWNER_BINDING.md), [AGON_MOVE_BINDING_MATRIX_MODEL](AGON_MOVE_BINDING_MATRIX_MODEL.md), [AGON_PRE_PROTOCOL_STOP_LINES](AGON_PRE_PROTOCOL_STOP_LINES.md) | owner gravity for moves and explicit non-landed requests |
| Gate, playbook, recurrence, prebinding | [AGON_GATE_ROUTING_HANDOFF](AGON_GATE_ROUTING_HANDOFF.md), [AGON_TRIAL_PLAYBOOK_HANDOFF](AGON_TRIAL_PLAYBOOK_HANDOFF.md), [AGON_RECURRENCE_ADAPTER](AGON_RECURRENCE_ADAPTER.md), [AGON_COURT_MEMO_STATS_PREBINDING_HANDOFF](AGON_COURT_MEMO_STATS_PREBINDING_HANDOFF.md) | handoffs to routing, playbooks, recurrence, proof, memory, and stats without granting authority |
| Arena, seats, pressure, sessions | [AGON_ARENA_SESSION_MODEL](AGON_ARENA_SESSION_MODEL.md), [AGON_SESSION_LIFECYCLE_MODEL](AGON_SESSION_LIFECYCLE_MODEL.md), [AGON_CHARTER_AND_SEAT_MODEL](AGON_CHARTER_AND_SEAT_MODEL.md) | future session frame, seating, lifecycle, and pressure profile without live arena |
| Packets and commitments | [AGON_STATE_PACKET_MODEL](AGON_STATE_PACKET_MODEL.md), [AGON_PACKET_SEQUENCE_MODEL](AGON_PACKET_SEQUENCE_MODEL.md), [AGON_SEALED_COMMIT_MODEL](AGON_SEALED_COMMIT_MODEL.md) | declaration, reveal, revision, packet sequence, and owner handoff grammar |
| Contradiction, closure, summon | [AGON_CONTRADICTION_LAW_MODEL](AGON_CONTRADICTION_LAW_MODEL.md), [AGON_CONTRADICTION_CLOSURE_SUMMON_LAW](AGON_CONTRADICTION_CLOSURE_SUMMON_LAW.md), [AGON_LAW_INTERLOCKS](AGON_LAW_INTERLOCKS.md) | contradiction handling and closure/summon law without unbounded escalation |
| Verdict, delta, scars, inscription | [AGON_VERDICT_DRAFT_MODEL](AGON_VERDICT_DRAFT_MODEL.md), [AGON_VERDICT_DELTA_SCAR_BRIDGE](AGON_VERDICT_DELTA_SCAR_BRIDGE.md), [AGON_INSCRIPTION_BUNDLE_MODEL](AGON_INSCRIPTION_BUNDLE_MODEL.md) | draft verdicts, deltas, scars, receipts, concept-map candidates, and inscription bundles without runtime mutation |
| Duel kernel and model-of-other | [AGON_DUEL_KERNEL_MODEL](AGON_DUEL_KERNEL_MODEL.md), [AGON_DUEL_KERNEL_EVENT_MODEL](AGON_DUEL_KERNEL_EVENT_MODEL.md), [AGON_MODEL_OF_OTHER_LAW](AGON_MODEL_OF_OTHER_LAW.md) | duel kernel grammar, event model, seats, model-of-other law, and bifurcation pressure without live duel authority |
| Mechanical trials | [AGON_MECHANICAL_TRIALS_OVER_DUEL_KERNEL](AGON_MECHANICAL_TRIALS_OVER_DUEL_KERNEL.md), [AGON_MECHANICAL_TRIAL_RUN_MODEL](AGON_MECHANICAL_TRIAL_RUN_MODEL.md) | trial-suite grammar and outcome candidates without proof sovereignty |
| Epistemic Agon | [AGON_EPISTEMIC_AGON](AGON_EPISTEMIC_AGON.md), [AGON_EPISTEMIC_MOVE_EXTENSION_MODEL](AGON_EPISTEMIC_MOVE_EXTENSION_MODEL.md) | epistemic contest grammar and handoffs without truth ownership |
| Retention, rank, standing | [AGON_RETENTION_RANK_ECONOMY](AGON_RETENTION_RANK_ECONOMY.md), [AGON_RETENTION_CHECK_MODEL](AGON_RETENTION_CHECK_MODEL.md), [AGON_RANK_JURISDICTION_MODEL](AGON_RANK_JURISDICTION_MODEL.md) | retention, standing, rank, jurisdiction, and mutation candidates without live rank authority |
| Schools, lineages, campaigns | [AGON_SCHOOL_MODEL](AGON_SCHOOL_MODEL.md), [AGON_LINEAGE_MODEL](AGON_LINEAGE_MODEL.md), [AGON_CAMPAIGN_MODEL](AGON_CAMPAIGN_MODEL.md) | school, lineage, and campaign grammar without hidden hierarchy |
| KAG, canon, Sophian threshold | [AGON_KAG_PROMOTION_PATH](AGON_KAG_PROMOTION_PATH.md), [AGON_CANON_RESTRAINT_MODEL](AGON_CANON_RESTRAINT_MODEL.md), [AGON_SOPHIAN_THRESHOLD](AGON_SOPHIAN_THRESHOLD.md) | promotion candidates, canon restraint, ToS/Sophian thresholds, and terminal outcome boundaries without direct canon write |

### Agon wave landings

Use the landing and stop-line document for the wave you touch.

Known center waves include:

- [AGON_WAVE0_LANDING](AGON_WAVE0_LANDING.md)
- [AGON_WAVE3_LANDING](AGON_WAVE3_LANDING.md)
- [AGON_WAVE4_LANDING](AGON_WAVE4_LANDING.md)
- [AGON_WAVE5_CENTER_HANDOFF](AGON_WAVE5_CENTER_HANDOFF.md)
- [AGON_WAVE6_CENTER_HANDOFF](AGON_WAVE6_CENTER_HANDOFF.md)
- [AGON_WAVE7_CENTER_HANDOFF](AGON_WAVE7_CENTER_HANDOFF.md)
- [AGON_WAVE8_LANDING](AGON_WAVE8_LANDING.md)
- [AGON_WAVE9_LANDING](AGON_WAVE9_LANDING.md)
- [AGON_WAVE10_LANDING](AGON_WAVE10_LANDING.md) and [AGON_WAVE10_STOP_LINES](AGON_WAVE10_STOP_LINES.md)
- [AGON_WAVE11_LANDING](AGON_WAVE11_LANDING.md) and [AGON_WAVE11_STOP_LINES](AGON_WAVE11_STOP_LINES.md)
- [AGON_WAVE12_LANDING](AGON_WAVE12_LANDING.md) and [AGON_WAVE12_STOP_LINES](AGON_WAVE12_STOP_LINES.md)
- [AGON_WAVE13_LANDING](AGON_WAVE13_LANDING.md) and [AGON_WAVE13_STOP_LINES](AGON_WAVE13_STOP_LINES.md)
- [AGON_WAVE14_LANDING](AGON_WAVE14_LANDING.md) and [AGON_WAVE14_STOP_LINES](AGON_WAVE14_STOP_LINES.md)
- [AGON_WAVE15_LANDING](AGON_WAVE15_LANDING.md) and [AGON_WAVE15_STOP_LINES](AGON_WAVE15_STOP_LINES.md)
- [AGON_WAVE16_LANDING](AGON_WAVE16_LANDING.md) and [AGON_WAVE16_STOP_LINES](AGON_WAVE16_STOP_LINES.md)
- [AGON_WAVE17_LANDING](AGON_WAVE17_LANDING.md) and [AGON_WAVE17_STOP_LINES](AGON_WAVE17_STOP_LINES.md)
- [AGON_WAVE18_LANDING](AGON_WAVE18_LANDING.md)
- [AGON_INTERLUDE_R4_LANDING](AGON_INTERLUDE_R4_LANDING.md)

Generated companions live under `generated/agon_*.min.json`. Use the matching builder, validator, and test for the generated surface you changed.

## Antifragility, via negativa, and pruning

Use this branch when the system is under stress, sprawl, authority inflation, or cleanup pressure.

| Surface | Role |
|---|---|
| [ANTIFRAGILITY](ANTIFRAGILITY.md) | stress should make the system more legible, bounded, and teachable |
| [ANTIFRAGILITY_FIRST_WAVE](ANTIFRAGILITY_FIRST_WAVE.md) | first-wave antifragility scope |
| [VIA_NEGATIVA](VIA_NEGATIVA.md) | subtraction as doctrine |
| [ANTI_AUTHORITY_RULES](ANTI_AUTHORITY_RULES.md) | stop authority inflation |
| [ONE_IN_ONE_OUT](ONE_IN_ONE_OUT.md) | sprawl pressure rule |
| [FRAGILITY_BLACKLIST](../FRAGILITY_BLACKLIST.md) | known fragile patterns |
| [DELETION_CANDIDATES](audits/DELETION_CANDIDATES.json) | deletion candidates |

Review questions:

1. Where was stress bounded?
2. What owner-local evidence exists?
3. Did the degraded mode remain weaker than normal mode?
4. What later change can cite the event?
5. Did cleanup reduce authority drift or merely move it?

## Questbook and RPG reflection

Use this branch when work becomes a tracked obligation, questline, campaign, progression path, or readable adjunct reflection.

Quest surfaces:

- [QUESTBOOK](../QUESTBOOK.md): public tracked surface for deferred obligations.
- [`quests/`](../quests/): public quest files, including center, Agon, and Experience follow-through work.
- [QUESTBOOK_MODEL](QUESTBOOK_MODEL.md): quest lifecycle, placement bands, risk, difficulty, and harvest rules.
- [QUESTBOOK_FIRST_WAVE](QUESTBOOK_FIRST_WAVE.md): first-wave guardrails.

RPG reflection surfaces:

- [RPG_LAYER_MODEL](RPG_LAYER_MODEL.md): adjunct RPG reflection layer.
- [RPG_FIRST_WAVE](RPG_FIRST_WAVE.md) and [RPG_SECOND_WAVE](RPG_SECOND_WAVE.md): staged reflection contours.
- [RPG_SKILLS_AND_FEATS](RPG_SKILLS_AND_FEATS.md): skill/feat reading, not skill ownership.
- [RPG_ARCHITECTURE_RFC](RPG_ARCHITECTURE_RFC.md): four-plane split of source meaning, proof/witness, runtime/session, and presentation/theme.
- [RPG_CANONICAL_TERMINOLOGY](RPG_CANONICAL_TERMINOLOGY.md) and [RPG_BOUNDARY_MAP](RPG_BOUNDARY_MAP.md): terms and boundaries.

Boundary:

- Questbook is not a second roadmap.
- RPG is not a hidden ontology.
- Progression evidence is not a global score.
- Campaign language must not imply runtime ledger ownership.

## ToS bridge, witness, and compost

Use this branch when AoA supports `Tree-of-Sophia` or derived knowledge work without authoring ToS meaning.

| Surface | Role |
|---|---|
| [ROOTLINE](ROOTLINE.md) | trunk-first AoA x ToS coordination spine |
| [COUNTERPART_BRIDGE](COUNTERPART_BRIDGE.md) | counterpart mappings stay derived, optional, and non-identity |
| [WITNESS_COMPOST](WITNESS_COMPOST.md) | witness and compost pilot doctrine |
| [TOS_GROWTH_SUPPORT](TOS_GROWTH_SUPPORT.md) | narrow support for ToS-owned growth law |
| [TOS_TEMPLATE_SUPPORT](TOS_TEMPLATE_SUPPORT.md) | support around ToS templates without owning ToS scaffold truth |
| [TOS_LINEAGE_PILOT_SUPPORT](TOS_LINEAGE_PILOT_SUPPORT.md) | support around ToS lineage pilot work |
| [TOS_SOIL_PREP_SUPPORT](TOS_SOIL_PREP_SUPPORT.md) | soil-preparation support without ToS authorship |

Rule: `Tree-of-Sophia` owns authored knowledge meaning. AoA may route, support, derive, witness, or prepare. It does not become ToS canon.

## Release, audit, and support posture

Use this branch when a public claim, release surface, or audit route must be checked.

| Surface | Role |
|---|---|
| [PUBLIC_SUPPORT_POSTURE](PUBLIC_SUPPORT_POSTURE.md) | what the center may honestly claim |
| [DIRECTION_SURFACES](DIRECTION_SURFACES.md) | current direction surface per repo |
| [FEDERATION_RELEASE_PROTOCOL](FEDERATION_RELEASE_PROTOCOL.md) | shared release completeness contract |
| [RELEASING](RELEASING.md) | center release runbook |
| [ECOSYSTEM_AUDIT_INDEX](../ECOSYSTEM_AUDIT_INDEX.md), [ROOT_SURFACE_AUDIT_2026_04_24](audits/ROOT_SURFACE_AUDIT_2026_04_24.md) | audit index |
| [CODEX_AUDIT_PROTOCOL](CODEX_AUDIT_PROTOCOL.md) | Codex audit protocol |
| [CODEX_SKILL_PROOF_AUDIT_BRIDGE](CODEX_SKILL_PROOF_AUDIT_BRIDGE.md) | skill/proof audit bridge |

Compact validation:

```bash
python scripts/validate_ecosystem.py
python scripts/validate_markdown_shape.py
python -m pytest -q tests
```

If you touched a generated Agon or Experience capsule, run that surface's builder, validator, and test as well.

## Final rule

The mechanic is only healthy when it makes ownership clearer. If a mechanic makes AoA feel powerful while making owners, proof, or stop-lines harder to name, return to the last valid anchor and re-enter through a smaller route.
