# Changelog

All notable changes to `Agents-of-Abyss` will be documented in this file.

The format is intentionally simple and human-first.
Tracking starts with the community-docs baseline for this repository.

## [Unreleased]

### Added

- `docs/START_HERE_ROUTE_CONTRACT.md` as the canonical route-mode contract for
  public entry, root editing, direction changes, ownership routing, mechanic
  changes, public claim validation, low-context agents, and district work
- `mechanics/` as the canonical root topology for center mechanics, with a
  shared mechanics `AGENTS.md`, per-mechanic packages, `README.md`,
  `ROADMAP.md`, `LANDING_LOG.md`, and `docs/` surfaces for each canonical
  mechanic
- `mechanics/registry.json` and `scripts/validate_mechanics_topology.py` to
  machine-check mechanic slugs, required package files, owner boundaries,
  compatibility routes, and moved-path cleanup
- `mechanics/agon/LANDING_LOG.md` and
  `mechanics/experience/LANDING_LOG.md` as mechanic-level landing ledgers for
  checked surfaces, validators, owner boundaries, stop-lines, and next routes
- `scripts/validate_mechanic_landing_logs.py` and regression coverage for the
  Agon and Experience LANDING_LOG surfaces
- mechanic card contracts for every root mechanic package, plus
  `generated/mechanic_card_index.min.json`,
  `scripts/build_mechanic_card_index.py`,
  `scripts/validate_mechanic_card_index.py`, and
  `scripts/validate_mechanic_readme_cards.py`
- `mechanics/OWNER_REQUEST_PROTOCOL.md`,
  `mechanics/OWNER_REQUEST_QUEUE.md`,
  `mechanics/owner-request-queue.json`, per-mechanic
  `*OWNER_REPO_REQUESTS.md` packets, `generated/owner_request_queue.min.json`,
  and owner-request validators for center-side handoff tracking
- docs thematic district cleanup law through
  `docs/THEMATIC_DISTRICT_PROTOCOL.md`, `docs/CURRENT_SURFACE_INDEX.md`,
  `docs/thematic_districts.json`, `generated/docs_thematic_index.min.json`,
  district README gates, and docs-thematic validators
- Wave E link and shape hygiene guardrails through
  `docs/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md`,
  `docs/HYGIENE_GUARDRAIL_INDEX.md`,
  `config/link_shape_hygiene.json`, `generated/link_shape_hygiene.min.json`,
  local-link/status/freshness validators, and exact known-repair traces
- Wave F AGENTS mesh guardrails through `docs/AGENTS_MESH_PROTOCOL.md`,
  `docs/AGENTS_MESH_INDEX.md`, `config/agents_mesh.json`,
  `generated/agents_mesh.min.json`, local `AGENTS.md` district cards, mesh
  validators, and regression tests
- Experience active-part distillation through `mechanics/experience/DIRECTION.md`,
  `mechanics/experience/PARTS.md`, `mechanics/experience/parts/`,
  `mechanics/experience/PROVENANCE.md`, archived source packets, and
  `mechanics/experience/scripts/validate_experience_distillation.py`
- Agon active-part distillation through `mechanics/agon/DIRECTION.md`,
  `mechanics/agon/PARTS.md`, `mechanics/agon/parts/`,
  `mechanics/agon/PROVENANCE.md`, `mechanics/agon/OWNER_REQUESTS.md`, and
  `mechanics/agon/scripts/validate_agon_distillation.py`
- `mechanics/ARTIFACT_TOPOLOGY.md` and
  `scripts/validate_mechanic_artifact_topology.py` for mechanic-owned schemas,
  examples, config, generated companions, scripts, and tests
- Questbook lane-first lifecycle validation through
  `mechanics/questbook/scripts/validate_questbook_lifecycle.py`,
  `mechanics/questbook/scripts/build_questbook_index.py`,
  `mechanics/questbook/scripts/validate_questbook_index.py`,
  `mechanics/questbook/scripts/validate_quest_relations.py`,
  `generated/questbook_index.min.json`,
  `generated/questbook_frontier.min.json`, and checks that reject top-level
  `AOA-Q-*` aliases plus root lifecycle source directories
- Questbook relation law through
  `mechanics/questbook/parts/relation-shape/README.md` and
  `generated/questbook_relations.min.json`, using `parent`, `sidequest`,
  `blocked_by`, and related route metadata without moving quest ownership
- Questbook narrow source docs for lifecycle law, execution-passport fields,
  harvest thresholds, and lane owner-route contracts, plus
  `mechanics/questbook/parts/lane-owner-routes/experience-ready-owner-routes.json` and
  `mechanics/questbook/scripts/build_ready_owner_routes.py` for
  registry-backed ready-route projections
- Questbook `parts/`, `legacy/`, and `PROVENANCE.md` surfaces so active
  obligation mechanics have functioning part packages while first-contour
  source history stays behind an explicit provenance bridge
- Questbook parts registry and distillation validator through
  `mechanics/questbook/parts/registry.json`,
  `mechanics/questbook/scripts/validate_questbook_distillation.py`, and
  package tests that keep active part contracts, validation files, index
  coverage, and legacy provenance routing synchronized
- Questbook source object contract runway through
  `mechanics/questbook/parts/source-contract/`,
  `mechanics/questbook/scripts/validate_questbook_source_contract.py`, and tests
  that validate rich YAML quest sources plus strict Markdown quest contracts
- Questbook post-change route review and validation centralization through
  `mechanics/questbook/AGENTS.md`, with lane/state default compression for
  Agon and Experience quest sources
- Questbook source-contract hardening that rejects direct `legacy/raw`
  references from source quest objects and routes preserved raw provenance
  through mechanic `PROVENANCE.md` or `legacy/INDEX.md` bridges
- RPG active parts and legacy provenance distillation through `mechanics/rpg/PARTS.md`,
  `mechanics/rpg/PROVENANCE.md`, `mechanics/rpg/legacy/`, and
  `mechanics/rpg/scripts/validate_rpg_distillation.py`
- RPG dual-vocabulary overlay validation through
  `mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py`
  and part-local tests that keep terminology, schema, example, and generated
  overlay keys in lockstep
- `mechanics/rpg/DIRECTION.md` to define RPG as world grammar for agent work,
  not a toy layer or decorative game skin
- RPG active-route polish that gives every part `README.md` the same
  `Use When` / `Do Not Use When` / `Active Outputs` / `Next Route` shape and
  rejects wave-era language from active RPG routes, with ecosystem validation
  aligned to the distilled active wording
- RPG usage contract through `mechanics/rpg/USAGE.md`, with validator coverage
  for when to use RPG language, when to stay plain, and which owner route keeps
  source truth
- RPG and Questbook playable obligation bridge through
  `mechanics/rpg/parts/quest-campaign/PLAYABLE_OBLIGATION.md` and
  `mechanics/questbook/parts/model-spine/RPG_PLAYABLE_READING.md`, keeping
  Questbook source ownership separate from derived RPG readings
- RPG part usability guardrails through a part-local playable-obligation
  worked route, `Route Check` sections in active part READMEs, and
  `Required Before Output` gates in active part contracts
- RPG ready-to-carry owner request packets in `mechanics/rpg/OWNER_REQUESTS.md`,
  with validator coverage that keeps sibling-owner handoff cards requested,
  receipt-linked, and distinct from owner acceptance

### Changed

- `generated/center_entry_map.min.json` and its schema now publish the
  `aoa_center_entry_map_v2` route contract with route modes, human paths,
  machine companions, and explicit `must_not_claim` stop-lines
- `docs/MECHANICS.md` is now a compatibility route to
  `mechanics/README.md`; the full mechanics atlas lives under the root
  mechanics topology
- `ROADMAP.md` now keeps strategic direction and current contour while
  detailed Agon and Experience landing history lives in mechanic LANDING_LOG
  surfaces
- route surfaces, schemas, generated maps, examples, manifests, validators,
  and tests now resolve Agon, Experience, RPG, recurrence, questbook,
  antifragility, ToS-bridge, method-growth, and release-support references
  through `mechanics/`
- release validation now runs Markdown shape checks, mechanics topology
  validation, and mechanic landing-log validation through
  `scripts/release_check.py`
- `scripts/release_check.py` now also checks docs thematic cleanup, mechanic
  card indexes, and generated owner-request queues before running tests
- `scripts/release_check.py` now also checks known link repairs, local
  Markdown links, status vocabulary, generated freshness, and the Wave E
  hygiene suite before release acceptance
- `scripts/release_check.py`, center-entry sync, generated freshness, and
  contributor guidance now include AGENTS mesh shape, coverage, and generated
  index validation before release acceptance
- Experience now keeps functioning direction and part contracts in active
  package surfaces, while long Wave 1-5 and v1.2-v2.0 source packets are
  preserved behind a single provenance bridge instead of being listed in
  active part docs
- Experience schemas, examples, part validators, and part tests now live under
  their owning `mechanics/experience/parts/<part>/` homes, with
  `mechanics/experience/artifact-map.json` preserving old flat-path receipts
  and artifact topology validation enforcing the route
- Experience active part artifacts now use functional part names instead of
  wave or release-contour artifact identities; source contours remain in
  provenance and receipts, and the distillation validator guards against
  active naming drift
- Experience active schemas, examples, validators, and tests now cite older
  packets, staged seed inputs, and sibling-owner surfaces through
  `mechanics/experience/provenance-receipts.json` receipt IDs instead of
  direct archive or source paths
- Experience root markdown surfaces now separate direction, part map, roadmap,
  owner-request, provenance, and landing-log roles with less validation and
  route duplication, plus a bounded roadmap route for deferred trigger notes
- Experience provenance checks now live in the package-level distillation
  validator, active part validators no longer direct-read `legacy/raw`, and
  `release-deployment` now has a local validator and test route
- Agon now routes active work through concise functioning parts, a single
  provenance bridge, and `legacy/raw` provenance accounting; `docs/` is only a
  compatibility route, while `mechanics/agon/OWNER_REQUESTS.md` and the central
  owner-request queue carry the current stronger-owner asks
- Experience owner-request coverage now includes playbooks, SDK helpers, stats
  summaries, skills, and reusable techniques, so Questbook `ready` items route
  through explicit request packets instead of implicit sibling-owner hints
- Questbook now keeps an AoA-side Experience ready owner-route index and
  validator, mapping each ready Experience quest to `ORQ-EXPERIENCE-*` packets
  without mutating or overclaiming sibling-owner acceptance
- Agon config seeds, generated capsules, schemas, examples, part validators,
  and part tests now live under their owning
  `mechanics/agon/parts/<part>/` homes, with
  `mechanics/agon/artifact-map.json` and `mechanics/agon/legacy/artifacts/`
  preserving the flat-path receipt
- Agon active part artifacts now use functional part lineage names instead of
  historical wave labels, while the distillation validator rejects legacy/raw
  route leakage and wave-era vocabulary inside active part files
- Agon root markdown surfaces now have a route index and cleaner active-source
  split, with source-contour history routed through `PROVENANCE.md` and
  `LANDING_LOG.md` instead of active entry docs
- Agon, Experience, RPG, antifragility, and method-growth mechanic artifacts now
  live in mechanic-owned homes; root technical districts keep repo-wide
  contracts only and no longer carry mechanic artifact aliases
- Questbook now uses lane-first lifecycle source placement instead of a flat
  quest pile: `quests/center/`, `quests/agon/`, `quests/experience/`, and the
  remaining mechanic lanes hold state directories such as `triaged`, `ready`,
  `active`, `blocked`, `reanchor`, `done`, and `dropped`
- Questbook now has its first center lane promotion pilot: the source-owned
  dispatch seam quest is closed with sibling-owner evidence, the next contour
  quest is unblocked into triage, and active lane README gates explain promotion
  and stop-lines before broad Agon or Experience passes
- Questbook now activates the Agon lane by moving center-landed Agon contour
  quests into `done` and owner-followthrough obligations into `ready`, leaving
  the next Agon work focused on owner acceptance and receipt review rather than
  a flat historical triage pile
- Questbook now activates the Experience lane by moving center-planted
  Experience contract quests into `done` and stronger-owner follow-through into
  `ready`, preserving runtime, proof, memory, KAG, ToS, SDK, stats, and office
  acceptance as owner-local routes instead of center claims
- Questbook center quests now carry explicit relation metadata: the foundation
  contour links `AOA-Q-0001` through `AOA-Q-0003`, and RPG-shaped center
  quests `AOA-Q-0004` through `AOA-Q-0008` remain center-owned while visible as
  `sidequest` routes from the next-contour quest
- Questbook root entry surfaces now split route-card, direction, roadmap,
  parts, and landing-ledger roles more cleanly, with a top landing-log index
  and refreshed AGENTS guidance for relation, generated, and owner-request
  edits
- Questbook `QUESTBOOK_MODEL.md` is now a compact model spine; lifecycle,
  execution, harvest, relation, and ready owner-route details live in focused
  package-local sources, and the Experience ready owner-route table is rebuilt
  from JSON instead of edited by hand
- Questbook active guidance now routes through `mechanics/questbook/parts/`;
  `docs/` is compatibility-only, `QUESTBOOK_FIRST_WAVE.md` moved to
  `legacy/raw/`, and Questbook owner request packets moved to
  `mechanics/questbook/OWNER_REQUESTS.md`
- Questbook part additions, retirements, validation routes, and direct
  legacy/raw references are now blocked by a package-level distillation gate
  that is also run from `scripts/release_check.py`
- Questbook release validation now requires source object reviewability checks
  for rich YAML quests and strict Markdown contracts; all Markdown quest
  sources have been promoted to `quest_markdown_contract_v1`
- Questbook Markdown sources now point generic owner-route, next-action,
  acceptance-evidence, and stop-line defaults to lane README sections instead
  of repeating the same route text in every quest file
- RPG root surfaces now separate entry card, roadmap, landing ledger,
  vocabulary overlay, owner requests, and wave contours, with RPG included in
  mechanic landing-log validation and release checks
- RPG now has explicit direction for when game language should deepen routing,
  judgment, memory, proof, and consequence, and when it should stay silent
- active mechanic child docs now route executable validation through the
  nearest `AGENTS.md`, with Markdown shape validation guarding against command
  drift back into child docs
- detailed agent-lane and Codex audit references now live under
  `docs/agent-lane/` and `docs/audits/`, while `docs/MECHANICS.md` remains a
  narrow compatibility route into `mechanics/README.md`
- stale links from old flat docs paths into mechanic packages and root docs
  audit surfaces now route through exact, manifest-backed repair rules

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
