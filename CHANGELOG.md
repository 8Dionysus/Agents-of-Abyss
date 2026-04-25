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
  `scripts/validate_experience_distillation.py`

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
- `python scripts/build_agon_imposition_readiness.py --check`
- `python scripts/validate_agon_imposition_readiness.py`
- `python -m pytest -q tests/test_agon_imposition_readiness.py`
- `python scripts/build_agon_lawful_move_registry.py --check`
- `python scripts/validate_agon_lawful_moves.py`
- `python -m pytest -q tests/test_agon_lawful_moves.py`
- `python scripts/build_agon_move_owner_binding_registry.py --check`
- `python scripts/validate_agon_move_owner_bindings.py`
- `python -m pytest -q tests/test_agon_move_owner_bindings.py`
- `python scripts/build_agon_gate_routing_handoff_request.py --check`
- `python scripts/validate_agon_gate_routing_handoff_request.py`
- `python -m pytest -q tests/test_agon_gate_routing_handoff_request.py`

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
