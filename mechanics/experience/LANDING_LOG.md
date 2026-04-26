# Experience Landing Log

This is the canonical landing ledger for center-owned Experience contracts in
`Agents-of-Abyss`.

Use this file when a change needs the landed history, checked surfaces,
validators, and stop-lines for Experience. Use `ROADMAP.md` for program
direction, not for version-by-version ledger detail.

Experience remains planted center law here. It does not activate live workspace
runtime, hidden memory sovereignty, assistant contestant authority, direct ToS
writes, or owner-local implementation.

## Route index for agents

Read this index before scanning the full ledger. It names the current shape of
Experience without requiring every older landing entry to be re-read.

- Current active route: `mechanics/experience/README.md`,
  `mechanics/experience/DIRECTION.md`, `mechanics/experience/PARTS.md`,
  `mechanics/experience/parts/README.md`, and the relevant part README.
- Current proof and placement route: `mechanics/experience/artifact-map.json`,
  `mechanics/experience/provenance-receipts.json`, and the relevant part-local
  schemas, examples, scripts, or tests.
- Current owner pressure route: `mechanics/experience/OWNER_REQUESTS.md`.
- Current future-pressure route: `mechanics/experience/ROADMAP.md`.
- Current archive bridge: `mechanics/experience/PROVENANCE.md`; use it only
  when auditing source provenance or receipt history.

Key recent landings:

- [Experience root route surface cleanup](#experience-root-route-surface-cleanup)
  clarifies the roles of root Experience markdown surfaces.
- [Experience provenance receipt indirection](#experience-provenance-receipt-indirection)
  keeps source packets behind receipt IDs instead of active-path clutter.
- [Experience active artifact naming cleanup](#experience-active-artifact-naming-cleanup)
  removes wave and version names from active artifact identities.
- [Experience part artifact homes](#experience-part-artifact-homes) moves
  schemas, examples, validators, and tests into functioning part homes.
- [Experience active parts plus provenance bridge](#experience-active-parts-plus-provenance-bridge)
  is the main distillation line from old flat docs into active parts.

Older wave and version entries remain historical landing receipts. They should
not be the first route for new work unless a task specifically audits the
original landing contour.

## How to update this log

Every landing entry uses the same shape:

- `Status:`
- `Owner boundary:`
- `Surfaces:`
- `Validation:`
- `Stop-lines:`
- `Next route:`

When a change touches Experience docs, generated capsules, schemas, examples,
validators, or tests, update the relevant entry here or explain in the PR why
the change is not a landing change.

## Landed center line

### Experience root route surface cleanup

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps root Experience markdown surfaces
role-specific: direction names the current operating line, parts map active
functions, roadmap tracks future pressure, provenance bridges receipts and
archive evidence, and owner requests stay center-side handoff packets.

Surfaces:

- `mechanics/experience/AGENTS.md`
- `mechanics/experience/DIRECTION.md`
- `mechanics/experience/PARTS.md`
- `mechanics/experience/LANDING_LOG.md`
- `mechanics/experience/ROADMAP.md`
- `mechanics/experience/OWNER_REQUESTS.md`
- `mechanics/experience/PROVENANCE.md`

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `python scripts/validate_markdown_shape.py`
- `python scripts/validate_mechanic_readme_cards.py --mechanic experience`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`

Stop-lines: root markdown surfaces must not become competing part maps,
validation ledgers, archive inventories, or owner-acceptance receipts.

Next route: future root-md changes should update only the surface whose role
actually moved, then run the narrow Experience distillation and shape checks.

### Experience provenance receipt indirection

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps active Experience schemas, examples,
validators, and tests on functional receipt IDs. Exact source packets, staged
seed paths, sibling surfaces, and owner surfaces stay behind the package
provenance bridge and receipt registry.

Surfaces:

- `mechanics/experience/provenance-receipts.json`
- `mechanics/experience/PROVENANCE.md`
- `mechanics/experience/README.md`
- `mechanics/experience/DIRECTION.md`
- `mechanics/experience/PARTS.md`
- `mechanics/experience/AGENTS.md`
- `mechanics/experience/scripts/validate_experience_distillation.py`
- `mechanics/experience/parts/*/schemas/`
- `mechanics/experience/parts/*/examples/`
- `mechanics/experience/parts/*/scripts/`
- `mechanics/experience/parts/*/tests/`

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `for script in $(find mechanics/experience/parts -path '*/scripts/*.py' -type f | sort); do python "$script"; done`
- `python -m pytest -q mechanics/experience/tests mechanics/experience/parts`

Stop-lines: active part artifacts may not carry direct archival, staged seed,
or sibling-source paths when a receipt ID can name the evidence. Receipt IDs do
not make an old packet, seed, or sibling surface active authority.

Next route: future Experience source citations add or reuse a receipt in
`mechanics/experience/provenance-receipts.json`, then keep active part
contracts focused on current function and owner route.

### Experience active artifact naming cleanup

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps active Experience artifact names,
contract IDs, bridge IDs, and validator/test identities functional by part.
Historical wave and version contours remain available only through
`mechanics/experience/PROVENANCE.md` and artifact-map receipts; they are not
active coordinates for future work.

Surfaces:

- `mechanics/experience/artifact-map.json`
- `mechanics/experience/scripts/validate_experience_distillation.py`
- `mechanics/experience/tests/test_experience_distillation.py`
- `mechanics/experience/parts/*/schemas/`
- `mechanics/experience/parts/*/examples/`
- `mechanics/experience/parts/*/scripts/`
- `mechanics/experience/parts/*/tests/`

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `for script in $(find mechanics/experience/parts -path '*/scripts/*.py' -type f | sort); do python "$script"; done`
- `python -m pytest -q mechanics/experience/tests mechanics/experience/parts`

Stop-lines: no active artifact filename, contract identity, bridge identity,
or validator/test identity may use wave or release-contour naming as the
working route.

Next route: keep source-contour details in provenance and receipts; future
artifact work should use the owning part name, not the landing campaign name.

### Experience part artifact homes

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps Experience schemas, examples,
validators, and tests in the active part homes that use them. The map preserves
the old flat artifact paths as migration receipts only; it does not reactivate a
flat artifact district or owner-local runtime behavior.

Surfaces:

- `mechanics/experience/artifact-map.json`
- `mechanics/experience/scripts/validate_experience_distillation.py`
- `mechanics/experience/tests/test_experience_distillation.py`
- `mechanics/experience/parts/capture-kernel/schemas/`
- `mechanics/experience/parts/capture-kernel/examples/`
- `mechanics/experience/parts/capture-kernel/scripts/`
- `mechanics/experience/parts/capture-kernel/tests/`
- `mechanics/experience/parts/certification-proof/schemas/`
- `mechanics/experience/parts/certification-proof/examples/`
- `mechanics/experience/parts/certification-proof/scripts/`
- `mechanics/experience/parts/certification-proof/tests/`
- `mechanics/experience/parts/adoption-federation/schemas/`
- `mechanics/experience/parts/adoption-federation/examples/`
- `mechanics/experience/parts/adoption-federation/scripts/`
- `mechanics/experience/parts/adoption-federation/tests/`
- `mechanics/experience/parts/governance-polis/schemas/`
- `mechanics/experience/parts/governance-polis/examples/`
- `mechanics/experience/parts/governance-polis/scripts/`
- `mechanics/experience/parts/governance-polis/tests/`
- `mechanics/experience/parts/release-deployment/schemas/`
- `mechanics/experience/parts/release-deployment/examples/`
- `mechanics/experience/parts/release-deployment/scripts/`
- `mechanics/experience/parts/release-deployment/tests/`
- `mechanics/experience/parts/office-operations/schemas/`
- `mechanics/experience/parts/office-operations/examples/`
- `mechanics/experience/parts/office-operations/scripts/`
- `mechanics/experience/parts/office-operations/tests/`
- `mechanics/experience/parts/service-mesh/schemas/`
- `mechanics/experience/parts/service-mesh/examples/`
- `mechanics/experience/parts/service-mesh/scripts/`
- `mechanics/experience/parts/service-mesh/tests/`
- `mechanics/experience/parts/continuity-context/schemas/`
- `mechanics/experience/parts/continuity-context/examples/`
- `mechanics/experience/parts/continuity-context/scripts/`
- `mechanics/experience/parts/continuity-context/tests/`
- `mechanics/experience/parts/runtime-boundary/schemas/`
- `mechanics/experience/parts/runtime-boundary/examples/`
- `mechanics/experience/parts/runtime-boundary/scripts/`
- `mechanics/experience/parts/runtime-boundary/tests/`
- `mechanics/experience/parts/compatibility-bridges/schemas/`
- `mechanics/experience/parts/compatibility-bridges/examples/`
- `mechanics/experience/parts/compatibility-bridges/scripts/`
- `mechanics/experience/parts/compatibility-bridges/tests/`

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `python scripts/validate_mechanic_artifact_topology.py --mechanic experience`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`
- `python -m pytest -q mechanics/experience/tests mechanics/experience/parts`

Stop-lines: no flat Experience artifact aliases, no hidden legacy-first route,
no generated or example surface becoming owner truth.

Next route: future Experience artifacts land inside the active part that uses
them, then update `mechanics/experience/artifact-map.json`, this ledger, and the
relevant part validation.

### Experience Wave 1 kernel

Status: planted.

Owner boundary: `Agents-of-Abyss` names the first experience-capture kernel;
owner-local runtime and memory activation remain outside the center.

Surfaces:

- `mechanics/experience/parts/capture-kernel/README.md`
- `mechanics/experience/parts/capture-kernel/schemas/experience-capture-flow.schema.json`
- `mechanics/experience/parts/capture-kernel/examples/experience_capture_flow.example.json`
- `mechanics/experience/parts/capture-kernel/scripts/validate_capture_kernel.py`
- `mechanics/experience/parts/capture-kernel/tests/test_capture_kernel.py`

Validation:

- `python mechanics/experience/parts/capture-kernel/scripts/validate_capture_kernel.py`
- `python -m pytest -q mechanics/experience/parts/capture-kernel/tests/test_capture_kernel.py`

Stop-lines: no live runtime, no hidden memory sovereignty, no inert projection
pretending to be activation.

Next route: certification/watchtower posture.

### Experience Wave 2 certification watchtower

Status: planted.

Owner boundary: `Agents-of-Abyss` names certification discipline and gated
watchtower contracts; certification authority remains bounded by explicit
owner-local review.

Surfaces:

- `mechanics/experience/parts/certification-proof/README.md`
- `mechanics/experience/parts/certification-proof/schemas/experience-certification-watchtower.schema.json`
- `mechanics/experience/parts/certification-proof/examples/experience_certification_watchtower.example.json`
- `mechanics/experience/parts/certification-proof/scripts/validate_certification_proof.py`
- `mechanics/experience/parts/certification-proof/tests/test_certification_proof.py`

Validation:

- `python mechanics/experience/parts/certification-proof/scripts/validate_certification_proof.py`
- `python -m pytest -q mechanics/experience/parts/certification-proof/tests/test_certification_proof.py`

Stop-lines: no autonomous certification, no proof authority transfer, no
runtime watchtower activation.

Next route: federation adoption posture.

### Experience Wave 3 federation adoption

Status: planted.

Owner boundary: `Agents-of-Abyss` names federation harvest and adoption gates;
owner repositories decide whether adoption lands locally.

Surfaces:

- `mechanics/experience/parts/adoption-federation/README.md`
- `mechanics/experience/parts/adoption-federation/schemas/experience-federation-adoption.schema.json`
- `mechanics/experience/parts/adoption-federation/examples/experience_federation_adoption.example.json`
- `mechanics/experience/parts/adoption-federation/scripts/validate_adoption_federation.py`
- `mechanics/experience/parts/adoption-federation/tests/test_adoption_federation.py`

Validation:

- `python mechanics/experience/parts/adoption-federation/scripts/validate_adoption_federation.py`
- `python -m pytest -q mechanics/experience/parts/adoption-federation/tests/test_adoption_federation.py`

Stop-lines: no owner-truth theft, no federation adoption without owner review.

Next route: polis constitution posture.

### Experience Wave 4 polis constitution

Status: planted.

Owner boundary: `Agents-of-Abyss` names polis governance, sealed decisions,
stays, appeals, and replayable precedent as center contracts; runtime
implementation stays outside the center.

Surfaces:

- `mechanics/experience/parts/governance-polis/README.md`
- `mechanics/experience/parts/governance-polis/schemas/experience-polis-constitution.schema.json`
- `mechanics/experience/parts/governance-polis/examples/experience_polis_constitution.example.json`
- `mechanics/experience/parts/governance-polis/scripts/validate_governance_polis.py`
- `mechanics/experience/parts/governance-polis/tests/test_governance_polis.py`
- `mechanics/experience/parts/governance-polis/tests/test_governance_polis_seed_contracts.py`

Validation:

- `python mechanics/experience/parts/governance-polis/scripts/validate_governance_polis.py`
- `python -m pytest -q mechanics/experience/parts/governance-polis/tests/test_governance_polis.py`
- `python -m pytest -q mechanics/experience/parts/governance-polis/tests/test_governance_polis_seed_contracts.py`

Stop-lines: no constitution runtime activation, no hidden precedent ledger, no
unreviewed authority resolver.

Next route: sovereign office posture.

### Experience Wave 5 sovereign office

Status: planted.

Owner boundary: `Agents-of-Abyss` names installable sovereign release and first
live-office contour; owner-local repositories own any live-office activation.

Surfaces:

- `mechanics/experience/parts/office-operations/README.md`
- `mechanics/experience/parts/office-operations/schemas/experience-sovereign-office.schema.json`
- `mechanics/experience/parts/office-operations/examples/experience_sovereign_office.example.json`
- `mechanics/experience/parts/office-operations/scripts/validate_office_operations.py`
- `mechanics/experience/parts/office-operations/tests/test_office_operations.py`
- `mechanics/experience/parts/office-operations/tests/test_office_operations_seed_contracts.py`

Validation:

- `python mechanics/experience/parts/office-operations/scripts/validate_office_operations.py`
- `python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_operations.py`
- `python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_operations_seed_contracts.py`

Stop-lines: no live office without owner-local authority, no sovereign runtime
claim from center docs.

Next route: v1.2 to v2.0 planting line.

### Experience v1.2 to v2.0 bridge

Status: planted.

Owner boundary: `Agents-of-Abyss` bridges `Dionysus` intake into future
owner-local planting waves; it does not own future runtime activation.

Surfaces:

- `mechanics/experience/parts/runtime-boundary/README.md`
- `mechanics/experience/parts/runtime-boundary/schemas/experience-runtime-boundary-bridge.schema.json`
- `mechanics/experience/parts/runtime-boundary/examples/experience_runtime_boundary_bridge.example.json`
- `mechanics/experience/parts/runtime-boundary/scripts/validate_runtime_boundary_bridge.py`
- `mechanics/experience/parts/runtime-boundary/tests/test_runtime_boundary_bridge.py`

Validation:

- `python mechanics/experience/parts/runtime-boundary/scripts/validate_runtime_boundary_bridge.py`
- `python -m pytest -q mechanics/experience/parts/runtime-boundary/tests/test_runtime_boundary_bridge.py`

Stop-lines: no future owner-local wave is considered landed by center bridge
language alone.

Next route: version-specific v1.2 through v2.0 entries.

### Experience v1.2 service mesh operations

Status: planted.

Owner boundary: `Agents-of-Abyss` names service mesh operations drills and
no-runtime stop-lines; runtime service ownership remains outside the center.

Surfaces:

- `mechanics/experience/parts/service-mesh/README.md`
- `mechanics/experience/parts/service-mesh/schemas/experience-service-mesh-operations.schema.json`
- `mechanics/experience/parts/service-mesh/examples/experience_service_mesh_operations.example.json`
- `mechanics/experience/parts/service-mesh/scripts/validate_service_mesh.py`
- `mechanics/experience/parts/service-mesh/tests/test_service_mesh.py`

Validation:

- `python mechanics/experience/parts/service-mesh/scripts/validate_service_mesh.py`
- `python -m pytest -q mechanics/experience/parts/service-mesh/tests/test_service_mesh.py`

Stop-lines: no live service mesh, no runtime dispatch, no owner-local activation.

Next route: office foundry role pairs.

### Experience v1.3 office foundry role pairs

Status: planted.

Owner boundary: `Agents-of-Abyss` names office foundry and role-pair split; it
does not create hybrid-agent authority.

Surfaces:

- `mechanics/experience/parts/office-operations/README.md`
- `mechanics/experience/parts/office-operations/schemas/experience-office-foundry-role-pairs.schema.json`
- `mechanics/experience/parts/office-operations/examples/experience_office_foundry_role_pairs.example.json`
- `mechanics/experience/parts/office-operations/scripts/validate_office_role_pairs.py`
- `mechanics/experience/parts/office-operations/tests/test_office_role_pairs.py`

Validation:

- `python mechanics/experience/parts/office-operations/scripts/validate_office_role_pairs.py`
- `python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_role_pairs.py`

Stop-lines: no hidden hybrid agent, no office activation by center docs.

Next route: mechanical arena kernel.

### Experience v1.4 mechanical arena kernel

Status: planted.

Owner boundary: `Agents-of-Abyss` names the mechanical arena kernel contour;
Agon law, arena operation, verdicts, scars, and retention remain unactivated.

Surfaces:

- `mechanics/experience/parts/compatibility-bridges/README.md`
- `mechanics/experience/parts/compatibility-bridges/schemas/experience-agonic-pair-trials-arena-kernel.schema.json`
- `mechanics/experience/parts/compatibility-bridges/examples/experience_agonic_pair_trials_arena_kernel.example.json`
- `mechanics/experience/parts/compatibility-bridges/scripts/validate_agonic_pair_trials_bridge.py`
- `mechanics/experience/parts/compatibility-bridges/tests/test_agonic_pair_trials_bridge.py`

Validation:

- `python mechanics/experience/parts/compatibility-bridges/scripts/validate_agonic_pair_trials_bridge.py`
- `python -m pytest -q mechanics/experience/parts/compatibility-bridges/tests/test_agonic_pair_trials_bridge.py`

Stop-lines: no live arena, no verdicts, no scars, no assistant contestants.

Next route: epistemic duel model-of-other forge.

### Experience v1.5 epistemic duel model-of-other forge

Status: planted.

Owner boundary: `Agents-of-Abyss` names sealed prediction, reveal scoring,
countermodel pressure, revision, and bifurcation quality; truth verdicts and
standing mutation remain outside the center.

Surfaces:

- `mechanics/experience/parts/compatibility-bridges/README.md`
- `mechanics/experience/parts/compatibility-bridges/schemas/experience-epistemic-duel-model-forge.schema.json`
- `mechanics/experience/parts/compatibility-bridges/examples/experience_epistemic_duel_model_forge.example.json`
- `mechanics/experience/parts/compatibility-bridges/scripts/validate_epistemic_duel_bridge.py`
- `mechanics/experience/parts/compatibility-bridges/tests/test_epistemic_duel_bridge.py`

Validation:

- `python mechanics/experience/parts/compatibility-bridges/scripts/validate_epistemic_duel_bridge.py`
- `python -m pytest -q mechanics/experience/parts/compatibility-bridges/tests/test_epistemic_duel_bridge.py`

Stop-lines: no live duel authority, no truth verdict, no standing or memory
mutation.

Next route: epistemic memory, rank, and reputation candidates.

### Experience v1.6 epistemic memory rank reputation engine

Status: planted.

Owner boundary: `Agents-of-Abyss` names rank, reputation, standing, and
jurisdiction candidates; memory truth and live rank mutation remain outside.

Surfaces:

- `mechanics/experience/parts/continuity-context/README.md`
- `mechanics/experience/parts/continuity-context/schemas/experience-memory-rank-reputation.schema.json`
- `mechanics/experience/parts/continuity-context/examples/experience_memory_rank_reputation.example.json`
- `mechanics/experience/parts/continuity-context/scripts/validate_memory_rank_reputation.py`
- `mechanics/experience/parts/continuity-context/tests/test_memory_rank_reputation.py`

Validation:

- `python mechanics/experience/parts/continuity-context/scripts/validate_memory_rank_reputation.py`
- `python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_memory_rank_reputation.py`

Stop-lines: no live rank mutation, no hidden memory truth, no reputation
authority.

Next route: affective economy and honor treasury.

### Experience v1.7 affective economy honor treasury

Status: planted.

Owner boundary: `Agents-of-Abyss` names affect and honor grammar; consciousness,
rights, and honor treasury activation remain outside the center.

Surfaces:

- `mechanics/experience/parts/continuity-context/README.md`
- `mechanics/experience/parts/continuity-context/schemas/experience-affective-economy-honor-treasury.schema.json`
- `mechanics/experience/parts/continuity-context/examples/experience_affective_economy_honor_treasury.example.json`
- `mechanics/experience/parts/continuity-context/scripts/validate_affective_economy.py`
- `mechanics/experience/parts/continuity-context/tests/test_affective_economy.py`

Validation:

- `python mechanics/experience/parts/continuity-context/scripts/validate_affective_economy.py`
- `python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_affective_economy.py`

Stop-lines: no consciousness claim, no rights authority, no live treasury.

Next route: context routing nervous system.

### Experience v1.8 context routing nervous system

Status: planted.

Owner boundary: `Agents-of-Abyss` names context routing, salience, budget, and
route receipt grammar; live router engine and owner override remain outside.

Surfaces:

- `mechanics/experience/parts/continuity-context/README.md`
- `mechanics/experience/parts/continuity-context/schemas/experience-context-routing.schema.json`
- `mechanics/experience/parts/continuity-context/examples/experience_context_routing.example.json`
- `mechanics/experience/parts/continuity-context/scripts/validate_context_routing.py`
- `mechanics/experience/parts/continuity-context/tests/test_context_routing.py`

Validation:

- `python mechanics/experience/parts/continuity-context/scripts/validate_context_routing.py`
- `python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_context_routing.py`

Stop-lines: no live router engine, no owner override, no route receipt as
authority.

Next route: context memory weaving continuity loom.

### Experience v1.9 context memory weaving continuity loom

Status: planted.

Owner boundary: `Agents-of-Abyss` names bounded continuity weave and re-entry
grammar; private memory sovereignty and runtime installation remain outside.

Surfaces:

- `mechanics/experience/parts/continuity-context/README.md`
- `mechanics/experience/parts/continuity-context/schemas/experience-continuity-loom.schema.json`
- `mechanics/experience/parts/continuity-context/examples/experience_continuity_loom.example.json`
- `mechanics/experience/parts/continuity-context/scripts/validate_context_memory_weaving.py`
- `mechanics/experience/parts/continuity-context/tests/test_context_memory_weaving.py`

Validation:

- `python mechanics/experience/parts/continuity-context/scripts/validate_context_memory_weaving.py`
- `python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_context_memory_weaving.py`

Stop-lines: no private memory sovereignty, no runtime installation, no ambient
continuity.

Next route: living workspace continuity runtime boundary.

### Experience v2.0 living workspace continuity runtime

Status: planted.

Owner boundary: `Agents-of-Abyss` names the final center boundary before
future owner-local living-workspace hardening; runtime ownership remains
outside the center.

Surfaces:

- `mechanics/experience/parts/runtime-boundary/README.md`
- `mechanics/experience/parts/continuity-context/schemas/experience-living-workspace-continuity-runtime.schema.json`
- `mechanics/experience/parts/continuity-context/examples/experience_living_workspace_continuity_runtime.example.json`
- `mechanics/experience/parts/continuity-context/scripts/validate_living_workspace_continuity.py`
- `mechanics/experience/parts/continuity-context/tests/test_living_workspace_continuity.py`

Validation:

- `python mechanics/experience/parts/continuity-context/scripts/validate_living_workspace_continuity.py`
- `python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_living_workspace_continuity.py`

Stop-lines: no live workspace runtime from center docs, no owner-local
activation, no hidden memory sovereignty.

Next route: owner-local hardening must land in the owning repository before
any runtime claim becomes public truth.

### Experience active parts plus provenance bridge

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps Experience direction, functioning
part contracts, owner requests, landing history, and archival accounting bridge;
runtime, memory, proof, routing, KAG, ToS meaning, and live office authority
remain with stronger owner repositories.

Surfaces:

- `mechanics/experience/DIRECTION.md`
- `mechanics/experience/PARTS.md`
- `mechanics/experience/parts/README.md`
- `mechanics/experience/PROVENANCE.md`
- `mechanics/experience/OWNER_REQUESTS.md`
- `mechanics/experience/scripts/validate_experience_distillation.py`
- `mechanics/experience/tests/test_experience_distillation.py`

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`
- `python -m pytest -q mechanics/experience/tests/test_experience_distillation.py`

Stop-lines: no archived packet becomes the primary active route by
accumulation, no provenance is deleted to make the active surface look clean,
and no owner activation is claimed from center distillation alone.

Next route: future Experience waves update the active part they pressure,
preserve archival accounting through `mechanics/experience/PROVENANCE.md`, and
route owner-local activation through `mechanics/experience/OWNER_REQUESTS.md`.

### Experience active docs provenance-load cleanup

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps active Experience parts concise while
preserving archival source accounting behind one bridge; no active part owns the
archive inventory itself.

Surfaces:

- `mechanics/experience/PROVENANCE.md`
- `mechanics/experience/README.md`
- `mechanics/experience/DIRECTION.md`
- `mechanics/experience/PARTS.md`
- `mechanics/experience/parts/README.md`
- `mechanics/experience/OWNER_REQUESTS.md`
- `mechanics/experience/scripts/validate_experience_distillation.py`
- `mechanics/experience/tests/test_experience_distillation.py`

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`
- `python -m pytest -q mechanics/experience/tests/test_experience_distillation.py`

Stop-lines: active part docs must not carry archival inventories, per-source
lists, or old packet filenames; archive detail remains accessible only through
the provenance bridge and archive district.

Next route: keep future part docs clean, functional, and free of source-list
load; when historical accounting matters, use
`mechanics/experience/PROVENANCE.md` instead of adding source lists to active
contracts.

### Experience route discipline hardening

Status: landed.

Owner boundary: `Agents-of-Abyss` owns the Experience working route, part
contracts, and center stop-lines; stronger owners keep runtime, memory, proof,
routing, actor, KAG, and ToS authority.

Surfaces:

- `mechanics/AGENTS.md`
- `mechanics/experience/AGENTS.md`
- `mechanics/experience/README.md`
- `mechanics/experience/DIRECTION.md`
- `mechanics/experience/PARTS.md`
- `mechanics/experience/ROADMAP.md`
- `mechanics/experience/parts/AGENTS.md`
- `mechanics/experience/parts/README.md`
- `mechanics/experience/parts/*/CONTRACT.md`
- `mechanics/experience/parts/*/VALIDATION.md`
- `mechanics/registry.json`
- `docs/thematic_districts.json`
- `mechanics/experience/scripts/validate_experience_distillation.py`
- `mechanics/experience/tests/test_experience_distillation.py`

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `python scripts/validate_mechanic_readme_cards.py --mechanic experience`
- `python scripts/validate_mechanics_topology.py --mechanic experience`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`
- `python scripts/release_check.py`

Stop-lines: active route surfaces must not carry stale flat-doc routes,
service-model notes, source-list load, or duplicated paths; owner-request
stop-lines must stay visible in the Experience card and part contracts.

Next route: future Experience changes perform a post-change route review across
direction, parts, roadmap, landing log, owner requests, registry, validators,
and generated surfaces, updating only the surfaces whose meaning truly moved.

### Experience provenance-gate hardening

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps archival Experience source accounting in
the package-level provenance gate. Active part validators check their living
contracts, schemas, examples, and tests without reading the archive district
directly.

Surfaces:

- `mechanics/experience/scripts/validate_experience_distillation.py`
- `mechanics/experience/tests/test_experience_distillation.py`
- `mechanics/experience/parts/*/scripts/*.py`
- `mechanics/experience/parts/release-deployment/VALIDATION.md`
- `mechanics/experience/parts/release-deployment/scripts/validate_release_deployment.py`
- `mechanics/experience/parts/release-deployment/tests/test_release_deployment.py`
- `mechanics/experience/artifact-map.json`

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `python mechanics/experience/parts/release-deployment/scripts/validate_release_deployment.py`
- `python scripts/validate_mechanic_artifact_topology.py --mechanic experience`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`
- `python -m pytest -q mechanics/experience/tests mechanics/experience/parts`

Stop-lines: active part validators must not read the archival packet district
directly, archival token drift must fail at the package gate, and
release-deployment must not sit as schema/example-only without a local active
validation route.

Next route: future archival-packet audits update the package provenance gate and
`mechanics/experience/PROVENANCE.md` bridge; future part behavior changes update
the owning part validator, tests, artifact map, and this ledger when the landing
surface moves.
