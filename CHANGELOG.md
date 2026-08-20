# Changelog

All notable changes to `Agents-of-Abyss` will be documented in this file.

The format is intentionally simple and human-first.
Tracking starts with the community-docs baseline for this repository.

## [Unreleased]

### Changed

- Active routing, dispatch, Agon gate, and owner-request surfaces now target the
  canonical typed routing/control-plane home in `aoa-sdk`. `aoa-routing`
  remains a deprecated maintenance predecessor for history and rollback; this
  succession does not archive or delete it.
- The broad release gate now executes each owned leaf command once, retains
  generated-output and builder-declaration checks through a non-reentrant
  `validate_generated_freshness.py --inputs-only` step, and keeps the full
  generated-freshness and hygiene aggregate routes available for focused use.
- The federation no longer routes candidates, donor residue, checkpoints, or
  recurrence through `Dionysus` as a seed-stage intermediary. Method-growth
  now uses `cluster_ref -> candidate_ref -> owner-local intake -> object_ref`;
  decision `AOA-CENTER-D-0033` records the supersession boundary.
- The current `Dionysus` route now names its conversational interview,
  consent, evidence, review, and personal portrait projection role.
- The AbyssOS organ contract now defines deny-by-default access admission,
  access-form-specific evidence chains, exact-target approval for external
  effects, and separate protocol and authority rollback. Decision
  `AOA-CENTER-D-0032` records the owner split and links its bounded pre-change
  evidence ledger.
- `.agents/` now states the owner-home and projection boundary explicitly:
  shared AoA skills come from the user profile, while a future repository
  projection requires a separately admitted owner skill home.

### Added

- `aoa-dashboard` is now registered as a bounded public bootstrap derived organ
  for Goal Space/operator projections, with explicit source-owner separation,
  SDK discovery, public route mapping, and no private organ-access admission.
- Decision `AOA-CENTER-D-0038` selects Reduced Federated Two-Speed Organ R1:
  reviewed public pull-only is the admitted core, while selective proactive
  and agent-local contours remain disabled and separately gated.
- Decision `AOA-CENTER-D-0037` keeps training and model memory at explicit
  consumer-zero until nonparametric natural benefit, a 30-day soak, a separate
  owner, purge and unlearning contracts, frozen-predecessor proof, rollback,
  and a new sole-operator decision all exist.
- C25 `OperatorDecisionPacket` under Experience Governance Polis: one
  hash-bound constitutional envelope for sole-operator `approve`, `reject`,
  `defer`, `narrow`, or `quarantine` decisions after procedurally separated AI
  review. It fails closed on unresolved or mismatched manifests and grants no
  automatic effect, production, payload, proof, memory, or routing authority.
- Decision `AOA-CENTER-D-0036` records why C25 is distinct from the
  emergency-stay-only office contract and existing polis case/council packets.

### Removed

- Removed four obsolete Dionysus owner requests and the Method-growth
  cross-repository validator dependency on a Dionysus seed example.
- Removed 25 copied shared skill bundles from `.agents/skills/` and the root
  test that treated one copied helper as center-owned behavior. The
  constitutional center currently has no independently justified home skill.

## [0.5.0] - 2026-07-13

### Summary

- This release advances the AoA constitutional center from the `v0.4.0`
  route-law and mechanic-package baseline into an explicitly designed,
  agent-readable center with bounded memo, eval, artifact-trust, and KAG
  ports.
- Root and generated routes now distinguish center doctrine, compact read
  models, host-machine artifact enforcement, runtime substrate ownership,
  derived KAG publication, and sibling-owner truth instead of leaving those
  boundaries implicit.
- The release was reconstructed from Git rather than from the old
  `[Unreleased]` prose: all 60 first-parent commits from `v0.4.0` through
  `c9d7282` are accounted for below, spanning 601 changed paths and 62,446
  additions / 2,098 deletions. Only 13 of those 60 commits touched this
  changelog at all, and the earlier release preparation stopped before the
  final center-local stats change.

### Added

- `DESIGN.md` as the root system-form surface for AoA's long-horizon shape
  toward OS Abyss, plus `DESIGN.AGENTS.md` for agent-facing guidance, AGENTS
  mesh growth, closeout posture, and portable agent guidance.
- A portable `.agents/skills/` foundation, session-growth skill set, shared
  skill refresh route, and hardened dry-run, traceability, summon,
  self-diagnosis, and automation-opportunity support contracts.
- A center-local `memo/` port with candidate, reviewed-landing, MCP service,
  portability, and validation routes that keep durable memory authority in
  `aoa-memo`.
- A bounded local `evals/` port and center-entry route that expose local eval
  pressure without moving verdict authority out of `aoa-evals`.
- Canonical `AOA-CENTER-D-####` decision records and generated decision
  indexes, including modeled-surface contracts that detect unknown or invalid
  decision lanes.
- Artifact identity for the compact center entry map, the OS Abyss artifact
  trust-plane decision and posture matrix, and an explicit
  `center_entry_route_readmodel` class for the generated center capsule.
- A center-local KAG provider home and canonical seven-index repository family
  for source surfaces, entities, artifacts, anchors, events, assertions, and
  relations, with source-return boundaries back to center doctrine.
- Host-machine artifact enforcement is now routed explicitly to
  `abyss-machine`, while runtime substrate composition remains with
  `abyss-stack`; the center route map also exposes the local KAG district.
- A center-local `stats/` port now publishes the reference-only
  `public-registry-active-maturity-ratio` over the owner-validated ecosystem
  registry v2 while leaving shared measurement grammar and cross-owner
  composition in `aoa-stats`.

### Changed

- First-reading, root-surface law, center authority, repository-role routing,
  roadmap, and generated entry-map routes now include `DESIGN.md`; AGENTS mesh
  law routes agent-card form through `DESIGN.AGENTS.md`.
- The Codex Spark lane now lives at `.agents/spark/`, with release, pytest,
  registry, and AGENTS mesh routes updated to that home.
- Markdown hygiene validators track matching fence delimiter type, projected
  session-growth skill contracts are refreshed from their owner source, and
  root Python commands now live in family-scoped `scripts/<family>/` homes.
- Owner-request status and receipt handling now distinguish landed, accepted,
  and packet-local evidence, preserve H3 packet boundaries, and reject
  malformed or out-of-scope owner-request material.
- RPG overlay/schema checks, Agon numbered-wave detection, Experience living
  workspace continuity, wave4 scheduler authority markers, Method-growth
  rootline invariants, docs migration boundaries, and current audit validators
  are regression-checked rather than prose-only.
- Repo-local KAG generation is CI-enforced, pinned, deterministic, complete
  across the seven-index family, and published in compact canonical form.
- Release-support direction now routes `abyss-stack` through its repository
  roadmap, while Checkpoint and Recurrence stats provenance returns to current
  part-local owner docs.
- Validation and test command blocks now route to executable owners and local
  `AGENTS.md` cards instead of being duplicated across weaker Markdown docs.

### Fixed

- Dry-run helpers retain malformed preview shapes for explicit validation
  instead of normalizing evidence away.
- Decision guidance and modeled decision paths now follow the family-scoped
  script topology and reject unmodeled surfaces.
- External docs migration checks no longer treat unrelated districts as local
  migration targets.
- Center-entry schema validation now constrains artifact `surface_state` to
  the canonical `generated` value.

### First-Parent Reconciliation (60/60)

The ordered pre-release history is recorded explicitly so the 47 original
commits absent from the old changelog, the earlier release-preparation commit,
and the post-preparation stats change all remain discoverable:

1. `c8ba825` — Add root design surface.
2. `2e7b5d5` — Sync aoa-skills owner request statuses.
3. `9a233e7` — Install portable AoA skill foundation.
4. `8110f35` — Roll out session-growth skills (#206).
5. `c1462ec` — Harden portable skills and traceability (#207).
6. `527c6cc` — Refresh session growth refs and readiness guard (#208).
7. `9e692f4` — Guard dry run preview step shape (#209).
8. `94d1efe` — Preserve dry run helper malformed shapes (#210).
9. `1621f51` — Refresh shared AoA skill pack (#211).
10. `aee5d0f` — Add agent surface design.
11. `0716bdf` — Move Spark lane under agents.
12. `d27df4e` — Address current Agents audit findings.
13. `f997e71` — Refresh shared AoA skill pack (#215).
14. `79be8a2` — Tighten markdown fence hygiene and skill projections (#216).
15. `c0a325d` — Refresh aoa-summon skill export (#217).
16. `f417436` — Refresh self-diagnose skill export.
17. `7f528d4` — Validate RPG overlay against schema (#219).
18. `1378ba5` — Refresh automation opportunity skill contracts (#220).
19. `f997fe0` — Harden current Agents audit validators (#221).
20. `b672571` — Add local memo port route (#222).
21. `9a61028` — Update aoa memo MCP service route (#223).
22. `5435a6a` — Wire center memo port route (#224).
23. `5f24de0` — Add center memo candidate route (#225).
24. `07fc51e` — Route memo reviewed landing.
25. `4966661` — Make memo validation route portable (#227).
26. `ab16e4c` — Canonicalize center decision indexes.
27. `73d4f48` — Refactor scripts into family topology.
28. `91fcb7d` — Fix decision guidance command paths (#230).
29. `3b8776d` — Detect unmodeled decision lane surfaces (#231).
30. `554ad39` — Honor modeled decision lane surfaces (#232).
31. `e9890e1` — Normalize modeled decision surface paths (#233).
32. `6c13ea6` — Add local eval port skeleton.
33. `5fc0d18` — Register evals district in center entry routes (#235).
34. `e242215` — Align RPG skills owner request status (#236).
35. `a7eac64` — Register recurrence parts AGENTS in mesh (#237).
36. `8e5bb4d` — Catch numbered Agon wave tokens in artifacts (#238).
37. `35d65ae` — Add living workspace checks to continuity validation (#239).
38. `9aa897b` — Constrain external docs migration districts (#240).
39. `a8a822e` — Fix Experience runtime observability core law (#241).
40. `d1f97c3` — Clarify RPG owner request receipt status (#242).
41. `7a98bc2` — Scope owner request receipt validation to packets (#243).
42. `8c3d693` — Harden owner request packet parsing (#244).
43. `e6389ac` — Preserve owner request H3 packet boundaries (#245).
44. `f084fb3` — Document evals district route (#246).
45. `5beaf7c` — Add artifact identity to center entry map (#247).
46. `d730f17` — Add OS Abyss artifact trust plane decision (#248).
47. `3fc6c57` — Add center KAG provider home (#249).
48. `ba0722f` — Align KAG provider validation route (#250).
49. `1a37738` — Add OS artifact trust posture matrix (#252).
50. `5e7ea38` — Add repo-local KAG indexes (#253).
51. `e591f59` — Route abyss-stack direction through repo roadmap (#254).
52. `314fec3` — Harden wave4 scheduler authority markers (#255).
53. `f974095` — Align method spine rootline doctrine (#256).
54. `e4e1925` — Enforce repo-local KAG index parity (#257).
55. `9eab44d` — Pin deterministic repo-local KAG index gate (#258).
56. `76e6272` — Add repository KAG index family (#259).
57. `2646a3d` — Reroute stats documentation provenance (#261).
58. `49f9943` — Publish canonical repository KAG indexes (#260).
59. `62d62bd` — Prepare Agents-of-Abyss v0.5.0 (#262).
60. `c9d7282` — Add center-local stats port (#263).

### Validation

- Release preparation reconciled the exact `v0.4.0..c9d7282` first-parent
  history, changed-path inventory, old dirty-tree evidence, source/generated
  center-entry parity, decision and district topology, owner-request and
  mechanic invariants, artifact-trust boundaries, and all seven KAG indexes
  rather than trusting `[Unreleased]` alone.
- The root release gate validates docs, mechanics, local ports, generated
  capsules, schemas, scripts, tests, decisions, KAG provider parity, and the
  complete pytest suite through the executable owner routes recorded in this
  repository.

### Notes

- Memo, eval, KAG, portable skill, and artifact-trust surfaces remain bounded
  center ports or read models; they do not transfer durable memory, proof,
  shared skill, graph, host enforcement, runtime, or sibling source authority
  into this repository.
- The earlier release-preparation commit added the explicit host/runtime owner
  split, center readmodel class, KAG district route and manifest provenance,
  strict generated surface-state schema test, `v0.5.0` banners, changelog
  reconciliation, and regenerated derived indexes; it is explicitly item 59
  above instead of being hidden outside the history count.
- This final reconciliation moves the landed stats work into `v0.5.0`, updates
  the exact Git inventory, and regenerates derived indexes. Its own bounded
  release-only commit is described here rather than misclassified as an
  additional product change.

## [0.4.0] - 2026-04-30

### Summary

- this release turns `Agents-of-Abyss` from a flat, docs-heavy center into a
  route-law, mechanic-package, and validator-backed center repository
- public root surfaces now explain the center without becoming archives:
  `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md`, `AGENTS.md`,
  `CONTRIBUTING.md`, `GLOSSARY.md`, `QUESTBOOK.md`,
  `ECOSYSTEM_AUDIT_INDEX.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` have
  been shaped as compact entry, policy, and routing surfaces
- center mechanics now live in `mechanics/<slug>/` packages with active parts,
  provenance bridges, owner-request packets, roadmaps, landing logs, and local
  validation instead of spreading wave-era source material through flat docs
- technical districts now own their repo-level role: docs guardrails,
  decisions, traces, config, examples, generated surfaces, manifests, schemas,
  scripts, tests, and Spark routes all point to their active function
- release validation now exercises the center entry map, mechanics topology,
  mechanic artifact placement, mechanic landing logs, questbook lifecycle,
  generated freshness, district validators, and the test suite through the
  root release gate

### Added

- public entry and route-law surfaces: `docs/START_HERE_ROUTE_CONTRACT.md`,
  `assets/agents-of-abyss-cycle-map.svg`, the `aoa_center_entry_map_v2`
  generated capsule, route-mode schema/build/validation support, and the
  entry-surface validation baseline under `docs/guardrails/`
- root mechanics topology: `mechanics/README.md`, `mechanics/AGENTS.md`,
  `mechanics/registry.json`, mechanic cards, shared owner-request protocol and
  queue, artifact topology law, and validators for mechanics, mechanic cards,
  owner requests, landing logs, and artifact placement
- mechanic package distillation for Agon, Experience, Questbook, RPG,
  Checkpoint, Recurrence, Method-growth, Antifragility, Release-support,
  Boundary-bridge, Distillation, Growth Cycle, and Audit, with each package
  carrying active route surfaces, parts, provenance, owner requests, and
  release-check coverage
- Questbook lane-first source lifecycle, relation metadata, generated indexes,
  source-object contracts, ready owner-route projections, and strict Markdown
  quest contracts; root `QUESTBOOK.md` remains only the compact public index
- RPG world-grammar route surfaces, part contracts, dual-vocabulary validation,
  playable-obligation examples, Questbook bridge readings, and ready-to-carry
  owner handoff packets
- Checkpoint, Distillation, Growth Cycle, and Audit as new center mechanics for
  bounded intermediate state, raw-to-active extraction, reviewed growth loops,
  and evidence-led audit routes
- docs guardrail, decision-record, and traces districts with local `AGENTS.md`,
  README routing, validators, generated indexes, and release-check coverage
- repo-level `docs/RELEASING.md` release route so federation release preflight
  can verify the GitHub release entry while the release-support mechanic owns
  the active runbook
- AbyssOS organ-contract district with `organ-alignment` route mode, surface
  state vocabulary, first-cycle route, system event vocabulary, and validation
- technical-district routing and validation for `config/`, `examples/`,
  `generated/`, `manifests/`, `schemas/`, `scripts/`, `tests/`, and the Spark lane
  so repo-level artifacts stay discoverable without becoming mechanic storage

### Changed

- `README.md` is now a compact public front door that routes readers through
  claim checks, route modes, mechanics, proof districts, machine companions,
  and the AoA cycle diagram without duplicating Charter, Map, or Roadmap
- root `AGENTS.md` now separates first-reading from agent editing, records the
  current squash-merge GitHub landing route, names post-change route review,
  and keeps full validation behind `scripts/release_check.py`
- `CHARTER.md`, `ECOSYSTEM_MAP.md`, and `ROADMAP.md` now split constitutional
  authority, ecosystem contour, current maturity, growth direction, and future
  triggers instead of making the root roadmap carry mechanic-level detail
- center entry routing now includes `organ-alignment` so downstream
  repository descent has a checked route without making AoA a control-plane,
  routing, runtime, or owner-local implementation repository
- `CONTRIBUTING.md` now faces contributors rather than duplicating agent law;
  `GLOSSARY.md` stays a compact vocabulary route; `QUESTBOOK.md` stays a root
  index rather than a task pile; `ECOSYSTEM_AUDIT_INDEX.md` routes audit work
  to owner surfaces instead of storing audit doctrine
- `SECURITY.md` and `CODE_OF_CONDUCT.md` now define public reporting and public
  collaboration routes while routing sensitive material to private security
  handling
- `docs/MECHANICS.md` is now a compatibility route to `mechanics/README.md`;
  active mechanic direction, maps, logs, and raw history live inside owning
  mechanic packages
- Agon and Experience active artifacts now live under part-local mechanic homes
  with artifact maps and provenance receipts preserving old flat-path history
- Questbook sources now live in lane-first lifecycle directories with relation
  metadata and generated indexes instead of top-level `AOA-Q-*` aliases
- RPG, Questbook, Agon, Experience, Antifragility, and Method-growth active
  docs now use functioning part routes and keep legacy history behind
  `PROVENANCE.md` or `legacy/` bridges
- root technical folders now document and validate repo-level function instead
  of holding mechanic-owned artifacts; mechanic-owned schemas, examples,
  manifests, scripts, and tests are routed to their packages where appropriate
- `pytest.ini` now collects active tests from root `tests/`, `mechanics/`, and
  the Spark lane while excluding legacy, cache, and build directories from the
  default root pytest run
- `scripts/release_check.py` now runs the expanded repo gate across docs,
  mechanics, questbook, generated surfaces, config, manifests, schemas,
  scripts, tests, the Spark lane, ecosystem validation, and pytest
- mechanics topology validation now permits `docs/RELEASING.md` only as a
  bounded repo-level route into the release-support runbook

### Removed

- root `FRAGILITY_BLACKLIST.md`; fragile-pattern routing now belongs in
  `mechanics/antifragility/FRAGILITY_BLACKLIST.md`
- empty or misleading docs doors such as flat Agon, Experience, legacy,
  landing, audit, postmortem, registry, and agent-lane routes after their useful
  material was distilled into mechanics, guardrails, decisions, traces, or root
  route surfaces
- flat mechanic artifact aliases and top-level quest aliases that encouraged
  agents to bypass owner packages or lane-first Questbook lifecycle routes
- direct active references from functioning mechanic docs to raw legacy sources
  where a `PROVENANCE.md`, receipt index, or `legacy/INDEX.md` bridge now owns
  that history

### Validation

The release passed the then-current repository release gate and public landing
checks. Exact command and session receipts remain in Git and CI history rather
than in this release-history surface.

### Notes

- this release remains center-owned: sibling repositories still own runtime,
  SDK helpers, skills, techniques, evals, memory, KAG, routing, playbooks,
  stats, agents, and ToS-authored source truth
- mechanic `LANDING_LOG.md` and `PROVENANCE.md` surfaces keep detailed landing
  and source-history receipts; this changelog records the repository release
  contour

## [0.2.3] - 2026-04-23

### Summary

- this patch lands the Agon pre-protocol center line from imposition,
  lawful-move vocabulary, owner binding, and gate routing through trial
  handoffs, recurrence, contradiction closure, duel kernels, mechanical
  trials, epistemic agon, rank economy, schools, lineages, campaigns, and
  ToS/KAG threshold posture
- the Experience program advances from wave1-wave5 (external v0.1-v1.1)
  into the v1.2-v2.0 planting line: service mesh operations, office foundry,
  mechanical arena, epistemic duel, reputation, affect, context routing,
  continuity loom, and living workspace runtime doctrine are now visible from
  the center
- `Agents-of-Abyss` remains the constitutional center: it records law,
  stop-lines, handoffs, and review contracts without taking over runtime,
  proof, skill, memory, KAG, or ToS authored truth

### Added

- Agon Wave 0 imposition doctrine, readiness capsule, and explicit builder /
  validator / test surfaces for the center repository
- Agon Wave III lawful move doctrine, move registry seed, and explicit builder
  / validator / test surfaces for the center repository
- Agon Wave IV move owner binding doctrine, binding registry seed, and
  explicit builder / validator / test surfaces for the center repository
- Agon Wave V gate routing handoff doctrine, center handoff request seed, and
  explicit builder / validator / test surfaces for the center repository
- center-owned Agon doctrine, registries, and owner-request surfaces for trial
  playbooks, recurrence adapters, contradiction closure, verdict delta scars,
  duel kernels, mechanical trials, epistemic agon, retention rank, schools,
  lineages, campaigns, KAG promotion, and Sophian thresholds
- Experience center doctrine for the external v0.1-v1.1 seed line
  (kernel, certification/watchtower, federation/adoption, polis/constitution,
  and sovereign office) plus the v1.2-v2.0 bridge and versioned center
  contracts for service mesh, office foundry, arena, duel, rank, affect,
  routing, continuity, and living workspace runtime

### Changed

- center route docs and roadmap now distinguish the historical Agon
  preparation holding boundary from the new Agon imposition gate
- center route docs, layer map, and local guide surfaces now distinguish the
  Agon imposition gate from the first pre-protocol lawful move vocabulary
- center route docs, layer map, and local guide surfaces now distinguish the
  first pre-protocol lawful move vocabulary from the next owner-binding turn
- center route docs, layer map, and local guide surfaces now distinguish the
  owner-binding turn from the next gate-routing handoff into `aoa-routing`
- review follow-up validators, ordering checks, generated registry checks,
  and contract guards were tightened across the Agon and Experience center
  surfaces
- center route docs, layer maps, seed manifests, and generated registry
  surfaces now keep Agon, Experience, and sibling-owner handoffs legible
  without moving specialized implementation authority into the center

### Validation

- `python scripts/release_check.py`
- `python mechanics/agon/parts/imposition-readiness/scripts/build_agon_imposition_readiness.py --check`
- `python mechanics/agon/parts/imposition-readiness/scripts/validate_agon_imposition_readiness.py`
- `python -m pytest -q mechanics/agon/parts/imposition-readiness/tests/test_agon_imposition_readiness.py`
- `python mechanics/agon/parts/lawful-move-grammar/scripts/build_agon_lawful_move_registry.py --check`
- `python mechanics/agon/parts/lawful-move-grammar/scripts/validate_agon_lawful_moves.py`
- `python -m pytest -q mechanics/agon/parts/lawful-move-grammar/tests/test_agon_lawful_moves.py`
- `python mechanics/agon/parts/owner-binding/scripts/build_agon_move_owner_binding_registry.py --check`
- `python mechanics/agon/parts/owner-binding/scripts/validate_agon_move_owner_bindings.py`
- `python -m pytest -q mechanics/agon/parts/owner-binding/tests/test_agon_move_owner_bindings.py`
- `python mechanics/agon/parts/gate-routing/scripts/build_agon_gate_routing_handoff_request.py --check`
- `python mechanics/agon/parts/gate-routing/scripts/validate_agon_gate_routing_handoff_request.py`
- `python -m pytest -q mechanics/agon/parts/gate-routing/tests/test_agon_gate_routing_handoff_request.py`

### Notes

- this release is a center-owned doctrine and routing release; sibling repos
  still own execution workflows, proof bundles, runtime records, memory
  objects, derived KAG structures, and source-authored ToS meaning

## [0.2.2] - 2026-04-19

### Summary

- this patch tightens center release posture, pre-Agon preparation guidance,
  and roadmap/current-direction routing around the active center wave
- CI and protection surfaces are aligned through Node24 workflow refs, pull
  request template coverage, and the required-check contract
- `Agents-of-Abyss` remains the center doctrine and route map without
  absorbing sdk, runtime, memory, or proof ownership

### Added

- component refresh center law and pre-Agon preparation posture surfaces for
  the center repository
- a GitHub pull request template for bounded contribution intake

### Changed

- roadmap/current-direction docs, aoa-sdk guard wording, and required-check
  plus Actions wiring are aligned with the current center release path

### Validation

- `python scripts/release_check.py`

### Notes

- this patch stays on center-owned doctrine, release posture, and routing
  surfaces; implementation ownership remains in sibling repositories

## [0.2.1] - 2026-04-12

### Summary

- this patch lands lineage validator work, owner-landing doctrine, and
  self-agency continuity updates in the center repo
- roadmap continuity and scheduler authority checks are tightened for the
  current kernel wave
- `Agents-of-Abyss` remains the center doctrine and route map, not a sink for
  specialized layer truth

### Added

- growth-refinery doctrine and lineage crosswalk surfaces, a candidate-lineage
  contract validator, owner-landing center doctrine, and self-agency
  continuity center doctrine.
- a wave-4 kernel automation validator for the center-owned automation
  posture.

### Changed

- roadmap continuity direction and scheduler-authority checks are tightened
  around the current kernel wave.

### Validation

- `python scripts/release_check.py`

### Notes

- detailed lineage-validator, owner-landing doctrine, and self-agency continuity changes for this patch remain enumerated below under `Added` and `Changed`

## [0.2.0] - 2026-04-10

### Summary

- this release adds center entry capsules, public support posture, and center-owned project-foundation/session-harvest follow-through surfaces
- center validation is tighter around `aoa-stats` promotion, questbook placement, and machine-readable federation support maps
- `Agents-of-Abyss` remains the center doctrine and routing home without absorbing specialized layer truth

### Validation

- `python scripts/release_check.py`

### Notes

- detailed corpus, documentation, and generated-surface coverage for this release remains enumerated below under `Added`, `Changed`, and `Included in this release`

### Added

- `generated/center_entry_map.min.json` as the center-owned zero-entry capsule
  plus `generated/federation_supporting_inventory.min.json` and the matching
  validation lane
- first-wave antifragility and via negativa center doctrine together with
  `docs/PUBLIC_SUPPORT_POSTURE.md` for bounded public onboarding, support, and
  release posture
- repo-local project-foundation, session-harvest, and automation-opportunity
  skill surfaces for center-owned review and closeout follow-through

### Changed

- promoted `aoa-stats` into the documented public federation contour and aligned the compact registry, center maps, and validator-backed documentation around that boundary
- tightened questbook and center validation around unmapped bullets, quest-band
  placement, JSON-schema-backed center-entry checks, and current verify routes

### Included in this release

- center doctrine, audit, and contributor-safety refreshes across `README.md`,
  `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md`,
  `ECOSYSTEM_AUDIT_INDEX.md`,
  `FRAGILITY_BLACKLIST.md`, `DELETION_CANDIDATES.json`, `AGENTS.md`, and
  `docs/`, including the RPG architecture, bridge, and runtime projection wave
- regenerated center-entry and federation-supporting machine surfaces plus CI
  and validation support under `.agents/`, `.github/`, `QUESTBOOK.md`,
  `quests/`, `generated/`, `schemas/`, `examples/`, `scripts/`, and `tests/`

## [0.1.0] - 2026-04-01

First public baseline release of `Agents-of-Abyss` as the constitutional and ecosystem-center repository of AoA.

This changelog entry uses the release-prep merge date.

### Summary

- first public baseline release of `Agents-of-Abyss` as the ecosystem center for AoA
- the public center now ships charter, ecosystem map, layer model, federation rules, program direction, and a compact generated center registry
- this release keeps center truth bounded to ecosystem identity, layer map, federation rules, and program-level direction rather than absorbing specialized layer meaning

### Added

- community-docs baseline established for this repository
- `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md`
- `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md`, and `ROADMAP.md` as the baseline constitutional route for public readers
- current center doctrine surfaces under `docs/`, including rootline, method-spine, counterpart-bridge, witness/compost, ToS-support, questbook, and RPG-adjunct notes
- `generated/ecosystem_registry.min.json` plus the local validator path in `scripts/validate_ecosystem.py`

### Validation

- `python scripts/validate_ecosystem.py`

### Notes

- this is a repository release of center doctrine and routing surfaces, not a claim that specialized layer truth has moved into the center
