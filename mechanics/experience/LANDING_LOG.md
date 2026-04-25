# Experience Landing Log

This is the canonical landing ledger for center-owned Experience contracts in
`Agents-of-Abyss`.

Use this file when a change needs the landed history, checked surfaces,
validators, and stop-lines for Experience. Use `ROADMAP.md` for program
direction, not for version-by-version ledger detail.

Experience remains planted center law here. It does not activate live workspace
runtime, hidden memory sovereignty, assistant contestant authority, direct ToS
writes, or owner-local implementation.

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

### Experience Wave 1 kernel

Status: planted.

Owner boundary: `Agents-of-Abyss` names the first experience-capture kernel;
owner-local runtime and memory activation remain outside the center.

Surfaces:

- `mechanics/experience/parts/capture-kernel/README.md`
- `schemas/experience-wave1-flow.schema.json`
- `examples/experience_wave1_flow.example.json`
- `scripts/validate_experience_wave1.py`
- `tests/test_experience_wave1.py`

Validation:

- `python scripts/validate_experience_wave1.py`
- `python -m pytest -q tests/test_experience_wave1.py`

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
- `schemas/experience-wave2-certification-watchtower.schema.json`
- `examples/experience_wave2_certification_watchtower.example.json`
- `scripts/validate_experience_wave2.py`
- `tests/test_experience_wave2.py`

Validation:

- `python scripts/validate_experience_wave2.py`
- `python -m pytest -q tests/test_experience_wave2.py`

Stop-lines: no autonomous certification, no proof authority transfer, no
runtime watchtower activation.

Next route: federation adoption posture.

### Experience Wave 3 federation adoption

Status: planted.

Owner boundary: `Agents-of-Abyss` names federation harvest and adoption gates;
owner repositories decide whether adoption lands locally.

Surfaces:

- `mechanics/experience/parts/adoption-federation/README.md`
- `schemas/experience-wave3-federation-adoption.schema.json`
- `examples/experience_wave3_federation_adoption.example.json`
- `scripts/validate_experience_wave3.py`
- `tests/test_experience_wave3.py`

Validation:

- `python scripts/validate_experience_wave3.py`
- `python -m pytest -q tests/test_experience_wave3.py`

Stop-lines: no owner-truth theft, no federation adoption without owner review.

Next route: polis constitution posture.

### Experience Wave 4 polis constitution

Status: planted.

Owner boundary: `Agents-of-Abyss` names polis governance, sealed decisions,
stays, appeals, and replayable precedent as center contracts; runtime
implementation stays outside the center.

Surfaces:

- `mechanics/experience/parts/governance-polis/README.md`
- `schemas/experience-wave4-polis-constitution.schema.json`
- `examples/experience_wave4_polis_constitution.example.json`
- `scripts/validate_experience_wave4.py`
- `tests/test_experience_wave4.py`
- `tests/test_experience_wave4_seed_contracts.py`

Validation:

- `python scripts/validate_experience_wave4.py`
- `python -m pytest -q tests/test_experience_wave4.py`
- `python -m pytest -q tests/test_experience_wave4_seed_contracts.py`

Stop-lines: no constitution runtime activation, no hidden precedent ledger, no
unreviewed authority resolver.

Next route: sovereign office posture.

### Experience Wave 5 sovereign office

Status: planted.

Owner boundary: `Agents-of-Abyss` names installable sovereign release and first
live-office contour; owner-local repositories own any live-office activation.

Surfaces:

- `mechanics/experience/parts/office-operations/README.md`
- `schemas/experience-wave5-sovereign-office.schema.json`
- `examples/experience_wave5_sovereign_office.example.json`
- `scripts/validate_experience_wave5.py`
- `tests/test_experience_wave5.py`
- `tests/test_experience_wave5_seed_contracts.py`

Validation:

- `python scripts/validate_experience_wave5.py`
- `python -m pytest -q tests/test_experience_wave5.py`
- `python -m pytest -q tests/test_experience_wave5_seed_contracts.py`

Stop-lines: no live office without owner-local authority, no sovereign runtime
claim from center docs.

Next route: v1.2 to v2.0 planting line.

### Experience v1.2 to v2.0 bridge

Status: planted.

Owner boundary: `Agents-of-Abyss` bridges `Dionysus` intake into future
owner-local planting waves; it does not own future runtime activation.

Surfaces:

- `mechanics/experience/parts/runtime-boundary/README.md`
- `schemas/experience-v1-2-v2-0-bridge.schema.json`
- `examples/experience_v1_2_to_v2_0_bridge.example.json`
- `scripts/validate_experience_v1_2_to_v2_0_bridge.py`
- `tests/test_experience_v1_2_to_v2_0_bridge.py`

Validation:

- `python scripts/validate_experience_v1_2_to_v2_0_bridge.py`
- `python -m pytest -q tests/test_experience_v1_2_to_v2_0_bridge.py`

Stop-lines: no future owner-local wave is considered landed by center bridge
language alone.

Next route: version-specific v1.2 through v2.0 entries.

### Experience v1.2 service mesh operations

Status: planted.

Owner boundary: `Agents-of-Abyss` names service mesh operations drills and
no-runtime stop-lines; runtime service ownership remains outside the center.

Surfaces:

- `mechanics/experience/parts/service-mesh/README.md`
- `schemas/experience-v1-2-service-mesh-operations.schema.json`
- `examples/experience_v1_2_service_mesh_operations.example.json`
- `scripts/validate_experience_v1_2_service_mesh_operations.py`
- `tests/test_experience_v1_2_service_mesh_operations.py`

Validation:

- `python scripts/validate_experience_v1_2_service_mesh_operations.py`
- `python -m pytest -q tests/test_experience_v1_2_service_mesh_operations.py`

Stop-lines: no live service mesh, no runtime dispatch, no owner-local activation.

Next route: office foundry role pairs.

### Experience v1.3 office foundry role pairs

Status: planted.

Owner boundary: `Agents-of-Abyss` names office foundry and role-pair split; it
does not create hybrid-agent authority.

Surfaces:

- `mechanics/experience/parts/office-operations/README.md`
- `schemas/experience-v1-3-office-foundry-role-pairs.schema.json`
- `examples/experience_v1_3_office_foundry_role_pairs.example.json`
- `scripts/validate_experience_v1_3_office_foundry_role_pairs.py`
- `tests/test_experience_v1_3_office_foundry_role_pairs.py`

Validation:

- `python scripts/validate_experience_v1_3_office_foundry_role_pairs.py`
- `python -m pytest -q tests/test_experience_v1_3_office_foundry_role_pairs.py`

Stop-lines: no hidden hybrid agent, no office activation by center docs.

Next route: mechanical arena kernel.

### Experience v1.4 mechanical arena kernel

Status: planted.

Owner boundary: `Agents-of-Abyss` names the mechanical arena kernel contour;
Agon law, arena operation, verdicts, scars, and retention remain unactivated.

Surfaces:

- `mechanics/experience/parts/compatibility-bridges/README.md`
- `schemas/experience-v1-4-agonic-pair-trials-mechanical-arena-kernel.schema.json`
- `examples/experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.example.json`
- `scripts/validate_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py`
- `tests/test_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py`

Validation:

- `python scripts/validate_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py`
- `python -m pytest -q tests/test_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py`

Stop-lines: no live arena, no verdicts, no scars, no assistant contestants.

Next route: epistemic duel model-of-other forge.

### Experience v1.5 epistemic duel model-of-other forge

Status: planted.

Owner boundary: `Agents-of-Abyss` names sealed prediction, reveal scoring,
countermodel pressure, revision, and bifurcation quality; truth verdicts and
standing mutation remain outside the center.

Surfaces:

- `mechanics/experience/parts/compatibility-bridges/README.md`
- `schemas/experience-v1-5-epistemic-duel-model-of-other-forge.schema.json`
- `examples/experience_v1_5_epistemic_duel_model_of_other_forge.example.json`
- `scripts/validate_experience_v1_5_epistemic_duel_model_of_other_forge.py`
- `tests/test_experience_v1_5_epistemic_duel_model_of_other_forge.py`

Validation:

- `python scripts/validate_experience_v1_5_epistemic_duel_model_of_other_forge.py`
- `python -m pytest -q tests/test_experience_v1_5_epistemic_duel_model_of_other_forge.py`

Stop-lines: no live duel authority, no truth verdict, no standing or memory
mutation.

Next route: epistemic memory, rank, and reputation candidates.

### Experience v1.6 epistemic memory rank reputation engine

Status: planted.

Owner boundary: `Agents-of-Abyss` names rank, reputation, standing, and
jurisdiction candidates; memory truth and live rank mutation remain outside.

Surfaces:

- `mechanics/experience/parts/continuity-context/README.md`
- `schemas/experience-v1-6-epistemic-memory-rank-reputation-engine.schema.json`
- `examples/experience_v1_6_epistemic_memory_rank_reputation_engine.example.json`
- `scripts/validate_experience_v1_6_epistemic_memory_rank_reputation_engine.py`
- `tests/test_experience_v1_6_epistemic_memory_rank_reputation_engine.py`

Validation:

- `python scripts/validate_experience_v1_6_epistemic_memory_rank_reputation_engine.py`
- `python -m pytest -q tests/test_experience_v1_6_epistemic_memory_rank_reputation_engine.py`

Stop-lines: no live rank mutation, no hidden memory truth, no reputation
authority.

Next route: affective economy and honor treasury.

### Experience v1.7 affective economy honor treasury

Status: planted.

Owner boundary: `Agents-of-Abyss` names affect and honor grammar; consciousness,
rights, and honor treasury activation remain outside the center.

Surfaces:

- `mechanics/experience/parts/continuity-context/README.md`
- `schemas/experience-v1-7-affective-economy-honor-treasury.schema.json`
- `examples/experience_v1_7_affective_economy_honor_treasury.example.json`
- `scripts/validate_experience_v1_7_affective_economy_honor_treasury.py`
- `tests/test_experience_v1_7_affective_economy_honor_treasury.py`

Validation:

- `python scripts/validate_experience_v1_7_affective_economy_honor_treasury.py`
- `python -m pytest -q tests/test_experience_v1_7_affective_economy_honor_treasury.py`

Stop-lines: no consciousness claim, no rights authority, no live treasury.

Next route: context routing nervous system.

### Experience v1.8 context routing nervous system

Status: planted.

Owner boundary: `Agents-of-Abyss` names context routing, salience, budget, and
route receipt grammar; live router engine and owner override remain outside.

Surfaces:

- `mechanics/experience/parts/continuity-context/README.md`
- `schemas/experience-v1-8-context-routing-nervous-system.schema.json`
- `examples/experience_v1_8_context_routing_nervous_system.example.json`
- `scripts/validate_experience_v1_8_context_routing_nervous_system.py`
- `tests/test_experience_v1_8_context_routing_nervous_system.py`

Validation:

- `python scripts/validate_experience_v1_8_context_routing_nervous_system.py`
- `python -m pytest -q tests/test_experience_v1_8_context_routing_nervous_system.py`

Stop-lines: no live router engine, no owner override, no route receipt as
authority.

Next route: context memory weaving continuity loom.

### Experience v1.9 context memory weaving continuity loom

Status: planted.

Owner boundary: `Agents-of-Abyss` names bounded continuity weave and re-entry
grammar; private memory sovereignty and runtime installation remain outside.

Surfaces:

- `mechanics/experience/parts/continuity-context/README.md`
- `schemas/experience-v1-9-context-memory-weaving-continuity-loom.schema.json`
- `examples/experience_v1_9_context_memory_weaving_continuity_loom.example.json`
- `scripts/validate_experience_v1_9_context_memory_weaving_continuity_loom.py`
- `tests/test_experience_v1_9_context_memory_weaving_continuity_loom.py`

Validation:

- `python scripts/validate_experience_v1_9_context_memory_weaving_continuity_loom.py`
- `python -m pytest -q tests/test_experience_v1_9_context_memory_weaving_continuity_loom.py`

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
- `schemas/experience-v2-0-living-workspace-continuity-runtime.schema.json`
- `examples/experience_v2_0_living_workspace_continuity_runtime.example.json`
- `scripts/validate_experience_v2_0_living_workspace_continuity_runtime.py`
- `tests/test_experience_v2_0_living_workspace_continuity_runtime.py`

Validation:

- `python scripts/validate_experience_v2_0_living_workspace_continuity_runtime.py`
- `python -m pytest -q tests/test_experience_v2_0_living_workspace_continuity_runtime.py`

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
- `scripts/validate_experience_distillation.py`
- `tests/test_experience_distillation.py`

Validation:

- `python scripts/validate_experience_distillation.py`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`
- `python -m pytest -q tests/test_experience_distillation.py`

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
- `scripts/validate_experience_distillation.py`
- `tests/test_experience_distillation.py`

Validation:

- `python scripts/validate_experience_distillation.py`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`
- `python -m pytest -q tests/test_experience_distillation.py`

Stop-lines: active part docs must not carry archival inventories, per-source
lists, or old packet filenames; archive detail remains accessible only through
the provenance bridge and archive district.

Next route: keep future part docs small; when historical accounting matters,
use `mechanics/experience/PROVENANCE.md` instead of adding source lists to
active contracts.
