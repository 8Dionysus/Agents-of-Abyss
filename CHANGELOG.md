# Changelog

All notable changes to `Agents-of-Abyss` will be documented in this file.

The format is intentionally simple and human-first.
Tracking starts with the community-docs baseline for this repository.

## [Unreleased]

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
- technical-district routing and validation for `config/`, `examples/`,
  `generated/`, `manifests/`, `schemas/`, `scripts/`, `tests/`, and `Spark/`
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
- `scripts/release_check.py` now runs the expanded repo gate across docs,
  mechanics, questbook, generated surfaces, config, manifests, schemas,
  scripts, tests, Spark, ecosystem validation, and pytest

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

- `aoa skills guard /srv/AbyssOS/Agents-of-Abyss --root /srv/AbyssOS --intent-text "polish unreleased changelog after root docs and mechanics release prep" --mutation-surface public-share --json`
- `python scripts/validate_markdown_shape.py --target CHANGELOG.md`
- `python scripts/validate_links.py`
- `git diff --check`
- `python scripts/release_check.py`

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
