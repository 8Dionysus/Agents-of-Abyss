# Agon Landing Log

This is the canonical landing ledger for center-owned Agon waves in
`Agents-of-Abyss`.

Use this file when a change needs the landed history, checked surfaces,
validators, and stop-lines for Agon. Use `ROADMAP.md` for program direction,
not for wave-by-wave ledger detail.

Agon remains center-owned here as law, vocabulary, stop-line, and owner-binding
doctrine. It is not live arena execution, not assistant contestant authority,
not runtime substrate, and not ToS canon write authority.

## Route index for agents

Read this index before scanning the full ledger. It names the current Agon
shape without requiring every older landing entry to be re-read.

- Current active route: `mechanics/agon/README.md`,
  `mechanics/agon/DIRECTION.md`, `mechanics/agon/PARTS.md`,
  `mechanics/agon/parts/README.md`, and the relevant part README.
- Current proof and placement route: `mechanics/agon/artifact-map.json` and the
  relevant part-local schemas, examples, config, generated capsules, scripts,
  or tests.
- Current owner pressure route: `mechanics/agon/OWNER_REQUESTS.md`.
- Current future-pressure route: `mechanics/agon/ROADMAP.md`.
- Current provenance bridge: `mechanics/agon/PROVENANCE.md`; use it only when
  auditing source provenance or receipt history.

Key recent landings:

- [Agon root route surface cleanup](#agon-root-route-surface-cleanup) clarifies
  the roles of root Agon markdown surfaces.
- [Agon active artifact lineage polish](#agon-active-artifact-lineage-polish)
  keeps active technical artifacts on functional part lineage names.
- [Agon active route distillation](#agon-active-route-distillation) is the main
  route from source families into active parts and owner requests.
- [Agon part artifact homes](#agon-part-artifact-homes) keeps schemas,
  examples, config, generated capsules, validators, and tests beside their
  owning parts.
- [Agon legacy raw provenance district](#agon-legacy-raw-provenance-district)
  preserves detailed source history without making it the working route.

Older source-contour entries remain historical landing receipts. They should
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

When a change touches Agon docs, generated capsules, schemas, seed config,
examples, validators, or tests, update the relevant entry here or explain in
the PR why the change is not a landing change.

### Agon root route surface cleanup

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps root Agon markdown surfaces
role-specific: direction names the current operating line, parts map active
functions, roadmap tracks future pressure, provenance bridges receipt history,
and owner requests stay center-side handoff packets.

Surfaces:

- `mechanics/agon/AGENTS.md`
- `mechanics/agon/README.md`
- `mechanics/agon/DIRECTION.md`
- `mechanics/agon/PARTS.md`
- `mechanics/agon/LANDING_LOG.md`
- `mechanics/agon/ROADMAP.md`
- `mechanics/agon/OWNER_REQUESTS.md`
- `mechanics/agon/PROVENANCE.md`

Validation:

- `python mechanics/agon/scripts/validate_agon_distillation.py`
- `python scripts/validate_markdown_shape.py`
- `python scripts/validate_mechanic_readme_cards.py --mechanic agon`
- `python scripts/validate_mechanic_landing_logs.py --mechanic agon`

Stop-lines: root markdown surfaces must not become competing part maps,
technical artifact ledgers, source-file inventories, or owner-acceptance
receipts.

Next route: future root-md changes should update only the surface whose role
actually moved, then run the narrow Agon distillation and shape checks.

### Agon legacy raw provenance district

Status: landed.

Owner boundary: `Agents-of-Abyss` preserves raw Agon wave and model provenance
while the current operating route stays in active part contracts, owner
requests, and the provenance bridge; live arena execution, actor authority,
runtime behavior, proof verdicts, memory objects, KAG source truth, and ToS
canon remain stronger-owner concerns.

Surfaces:

- `mechanics/agon/docs/README.md`
- `mechanics/agon/docs/AGENTS.md`
- `mechanics/agon/legacy/README.md`
- `mechanics/agon/legacy/AGENTS.md`
- `mechanics/agon/legacy/INDEX.md`
- `mechanics/agon/legacy/DISTILLATION_LOG.md`
- `mechanics/agon/legacy/raw/README.md`
- `mechanics/agon/legacy/raw/AGON_*.md`
- `mechanics/agon/legacy/raw/PRE_AGON_BASELINE.md`
- `mechanics/agon/scripts/validate_agon_distillation.py`

Validation:

- `python mechanics/agon/scripts/validate_agon_distillation.py`
- `python scripts/validate_mechanic_landing_logs.py --mechanic agon`
- `python scripts/validate_mechanics_topology.py --mechanic agon`
- `python scripts/validate_links.py`

Stop-lines: do not make `mechanics/agon/legacy/raw/` the normal first route,
do not delete raw provenance after distillation, and do not let raw packets
become the only place current active Agon rules live.

Next route: future Agon packet landings update the relevant active part first,
then this landing log and `mechanics/agon/legacy/INDEX.md` when the raw
provenance map changes.

### Agon part artifact homes

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps current Agon technical artifacts beside
their owning active parts; package-level distillation validation remains at the
mechanic root, while live arena execution, proof verdicts, durable memory,
runtime behavior, KAG promotion, and ToS canon remain stronger-owner concerns.

Surfaces:

- `mechanics/agon/artifact-map.json`
- `mechanics/agon/legacy/artifacts/README.md`
- `mechanics/agon/parts/*/config/agon_*.seed.json`
- `mechanics/agon/parts/*/generated/agon_*.min.json`
- `mechanics/agon/parts/*/schemas/agon-*.schema.json`
- `mechanics/agon/parts/*/examples/agon_*.example.json`
- `mechanics/agon/parts/*/scripts/*agon*.py`
- `mechanics/agon/parts/*/tests/test_agon_*.py`
- `mechanics/agon/scripts/validate_agon_distillation.py`
- `mechanics/agon/tests/test_agon_distillation.py`
- `scripts/validate_mechanic_artifact_topology.py`

Validation:

- `python mechanics/agon/scripts/validate_agon_distillation.py`
- `python scripts/validate_mechanic_artifact_topology.py --mechanic agon`
- `python scripts/validate_mechanic_landing_logs.py --mechanic agon`
- `python -m pytest -q mechanics/agon/tests mechanics/agon/parts`

Stop-lines: do not recreate flat aliases, do not let old wave names become the
working route, and do not move package-level or repo-level validators into a
part unless that part actually owns the behavior.

Next route: when a part gains new schemas, config, generated capsules,
validators, or tests, land them in that part home and update
`mechanics/agon/artifact-map.json` only if the move changes artifact topology.

### Agon active artifact lineage polish

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps active Agon seeds, schemas, examples,
generated capsules, validators, and tests expressed through functional part
lineage names; historical wave source labels remain receipt/provenance
language, not the operating vocabulary inside active part artifacts.

Surfaces:

- `mechanics/agon/parts/*/config/agon_*.seed.json`
- `mechanics/agon/parts/*/generated/agon_*.min.json`
- `mechanics/agon/parts/*/schemas/agon-*.schema.json`
- `mechanics/agon/parts/*/examples/agon_*.example.json`
- `mechanics/agon/parts/*/scripts/*agon*.py`
- `mechanics/agon/parts/*/tests/test_agon_*.py`
- `mechanics/agon/scripts/validate_agon_distillation.py`
- `mechanics/agon/ROADMAP.md`

Validation:

- `find mechanics/agon/parts -path '*/scripts/build_agon_*.py' -exec python {} --check \;`
- `find mechanics/agon/parts -path '*/scripts/validate_agon_*.py' -exec python {} \;`
- `python mechanics/agon/scripts/validate_agon_distillation.py`
- `python scripts/validate_mechanic_artifact_topology.py --mechanic agon`
- `python -m pytest -q mechanics/agon/tests mechanics/agon/parts`

Stop-lines: do not let active part artifacts direct agents into legacy raw
sources, do not expose old wave labels as the active route vocabulary, and do
not collapse generated schema versions or model versions into landing history.

Next route: if a future source contour changes part behavior, update the
owning part artifacts first, then the generated capsules and package
distillation validator.

### Agon active route distillation

Status: landed.

Owner boundary: `Agents-of-Abyss` owns the active Agon route, part contracts,
center-side owner requests, and provenance bridge; detailed wave documents stay
receipts, and proof, memory, KAG, route behavior, runtime, actor posture,
scenario choreography, rank, and ToS canon authority remain owner-local.

Surfaces:

- `mechanics/agon/README.md`
- `mechanics/agon/DIRECTION.md`
- `mechanics/agon/PARTS.md`
- `mechanics/agon/OWNER_REQUESTS.md`
- `mechanics/agon/PROVENANCE.md`
- `mechanics/agon/artifact-map.json`
- `mechanics/agon/parts/README.md`
- `mechanics/agon/parts/AGENTS.md`
- `mechanics/agon/parts/imposition-readiness/README.md`
- `mechanics/agon/parts/lawful-move-grammar/README.md`
- `mechanics/agon/parts/owner-binding/README.md`
- `mechanics/agon/parts/gate-routing/README.md`
- `mechanics/agon/parts/trial-handoff/README.md`
- `mechanics/agon/parts/recurrence-adapter/README.md`
- `mechanics/agon/parts/packet-arena/README.md`
- `mechanics/agon/parts/duel-kernel/README.md`
- `mechanics/agon/parts/verdict-retention-rank/README.md`
- `mechanics/agon/parts/epistemic-kag/README.md`
- `mechanics/agon/parts/sophian-threshold/README.md`
- `mechanics/agon/parts/compatibility-bridges/README.md`
- `mechanics/agon/scripts/validate_agon_distillation.py`
- `mechanics/agon/tests/test_agon_distillation.py`
- `mechanics/registry.json`
- `mechanics/owner-request-queue.json`
- `mechanics/OWNER_REQUEST_QUEUE.md`
- `generated/owner_request_queue.min.json`

Validation:

- `python mechanics/agon/scripts/validate_agon_distillation.py`
- `python scripts/validate_mechanic_landing_logs.py --mechanic agon`
- `python scripts/validate_mechanics_topology.py --mechanic agon`
- `python scripts/validate_mechanic_artifact_topology.py --mechanic agon`
- `python scripts/validate_owner_request_queue.py --mechanic agon`
- `python scripts/build_owner_request_queue.py --check`
- `python scripts/validate_generated_owner_request_queue.py`
- `python scripts/validate_owner_request_docs.py --mechanic agon`
- `python -m pytest -q mechanics/agon/tests/test_agon_distillation.py`

Stop-lines: active parts do not supersede owner repositories, activate a live
arena, grant contestant authority, mutate memory or rank, convert KAG
projections into source truth, or write ToS canon.

Next route: distill detailed Agon source families into part-owned artifacts
only when a part behavior changes; keep old wave documents behind
`mechanics/agon/PROVENANCE.md` and use `mechanics/agon/OWNER_REQUESTS.md`
for stronger-owner asks.

## Landed center line

### Agon preparation holding boundary

Status: planted.

Owner boundary: `Agents-of-Abyss` may name the holding boundary and pre-Agon
review posture; live arena work, actor behavior, runtime dispatch, proof,
memory, and ToS promotion remain outside this repository.

Surfaces:

- `mechanics/agon/legacy/raw/AGON_PREPARATION_POSTURE.md`

Validation:

- `python scripts/release_check.py`

Stop-lines: not a planted wave package, not a new sibling repository, no direct
arena write path.

Next route: later Agon work must enter through the specific wave or handoff
entry below.

### Agon imposition gate

Status: landed in `v0.2.3`.

Owner boundary: `Agents-of-Abyss` owns Agon as an imposed review lens and
survival audit, not as a live arena, sibling repository, or runtime contour.

Surfaces:

- `mechanics/agon/legacy/raw/AGON_IMPOSITION_POSTURE.md`
- `mechanics/agon/legacy/raw/AGON_SURVIVAL_CRITERIA.md`
- `mechanics/agon/legacy/raw/AGON_DOUBT_AUDIT.md`
- `mechanics/agon/legacy/raw/PRE_AGON_BASELINE.md`
- `mechanics/agon/legacy/raw/AGON_WAVE0_LANDING.md`
- `mechanics/agon/parts/imposition-readiness/generated/agon_imposition_readiness.min.json`
- `mechanics/agon/parts/imposition-readiness/schemas/agon-imposition-readiness.schema.json`
- `mechanics/agon/parts/imposition-readiness/examples/agon_doubt_audit.example.json`
- `mechanics/agon/parts/imposition-readiness/scripts/build_agon_imposition_readiness.py`
- `mechanics/agon/parts/imposition-readiness/scripts/validate_agon_imposition_readiness.py`
- `mechanics/agon/parts/imposition-readiness/tests/test_agon_imposition_readiness.py`

Validation:

- `python mechanics/agon/parts/imposition-readiness/scripts/build_agon_imposition_readiness.py --check`
- `python mechanics/agon/parts/imposition-readiness/scripts/validate_agon_imposition_readiness.py`
- `python -m pytest -q mechanics/agon/parts/imposition-readiness/tests/test_agon_imposition_readiness.py`

Stop-lines: survive, recharter, defer, prune, or quarantine review does not
grant actor, proof, memory, routing, runtime, or ToS authority.

Next route: lawful move vocabulary may be named only as pre-protocol legal
language.

### Agon lawful move language

Status: landed in `v0.2.3`.

Owner boundary: `Agents-of-Abyss` owns the lawful tongue and registry contour;
execution, proof, memory, routing, scenario, and runtime follow-through remain
owner-local.

Surfaces:

- `mechanics/agon/legacy/raw/AGON_LAWFUL_MOVE_LANGUAGE.md`
- `mechanics/agon/legacy/raw/AGON_MOVE_REGISTRY_MODEL.md`
- `mechanics/agon/legacy/raw/AGON_MOVE_OWNER_HANDOFFS.md`
- `mechanics/agon/legacy/raw/AGON_WAVE3_LANDING.md`
- `mechanics/agon/parts/lawful-move-grammar/config/agon_lawful_moves.seed.json`
- `mechanics/agon/parts/lawful-move-grammar/generated/agon_lawful_move_registry.min.json`
- `mechanics/agon/parts/lawful-move-grammar/schemas/agon-lawful-move.schema.json`
- `mechanics/agon/parts/lawful-move-grammar/schemas/agon-lawful-move-registry.schema.json`
- `mechanics/agon/parts/lawful-move-grammar/examples/agon_lawful_move.example.json`
- `mechanics/agon/parts/lawful-move-grammar/scripts/build_agon_lawful_move_registry.py`
- `mechanics/agon/parts/lawful-move-grammar/scripts/validate_agon_lawful_moves.py`
- `mechanics/agon/parts/lawful-move-grammar/tests/test_agon_lawful_moves.py`

Validation:

- `python mechanics/agon/parts/lawful-move-grammar/scripts/build_agon_lawful_move_registry.py --check`
- `python mechanics/agon/parts/lawful-move-grammar/scripts/validate_agon_lawful_moves.py`
- `python -m pytest -q mechanics/agon/parts/lawful-move-grammar/tests/test_agon_lawful_moves.py`

Stop-lines: every move remains pre-protocol with `live_protocol: false` and
`runtime_effect: none`.

Next route: owner gravity must be explicit before move requests can point
toward sibling repositories.

### Agon move owner binding

Status: landed in `v0.2.3`.

Owner boundary: `Agents-of-Abyss` owns pre-protocol owner-binding law; practice,
workflow, proof, routing, scenario, memory, stats, and actor slices stay
`requested_not_landed` until owner repositories accept them.

Surfaces:

- `mechanics/agon/legacy/raw/AGON_MOVE_OWNER_BINDING.md`
- `mechanics/agon/legacy/raw/AGON_MOVE_BINDING_MATRIX_MODEL.md`
- `mechanics/agon/legacy/raw/AGON_OWNER_REPO_REQUESTS.md`
- `mechanics/agon/legacy/raw/AGON_PRE_PROTOCOL_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE4_LANDING.md`
- `mechanics/agon/parts/owner-binding/config/agon_move_owner_bindings.seed.json`
- `mechanics/agon/parts/owner-binding/generated/agon_move_owner_binding_registry.min.json`
- `mechanics/agon/parts/owner-binding/schemas/agon-move-owner-binding.schema.json`
- `mechanics/agon/parts/owner-binding/schemas/agon-move-owner-binding-registry.schema.json`
- `mechanics/agon/parts/owner-binding/examples/agon_move_owner_binding.example.json`
- `mechanics/agon/parts/owner-binding/scripts/build_agon_move_owner_binding_registry.py`
- `mechanics/agon/parts/owner-binding/scripts/validate_agon_move_owner_bindings.py`
- `mechanics/agon/parts/owner-binding/tests/test_agon_move_owner_bindings.py`

Validation:

- `python mechanics/agon/parts/owner-binding/scripts/build_agon_move_owner_binding_registry.py --check`
- `python mechanics/agon/parts/owner-binding/scripts/validate_agon_move_owner_bindings.py`
- `python -m pytest -q mechanics/agon/parts/owner-binding/tests/test_agon_move_owner_bindings.py`

Stop-lines: owner requests are not landed practice, workflow, proof, route,
scenario, memory, stats, actor, runtime, or ToS authority.

Next route: bounded handoffs may ask owner repositories to land their own
slices.

### Agon gate routing handoff

Status: handoff landed in `v0.2.3`.

Owner boundary: `Agents-of-Abyss` owns the pre-protocol gate-routing request;
`aoa-routing` owns any future routing implementation after its own review.

Surfaces:

- `mechanics/agon/legacy/raw/AGON_GATE_ROUTING_HANDOFF.md`
- `mechanics/agon/legacy/raw/AGON_GATE_ROUTING_OWNER_REQUEST.md`
- `mechanics/agon/legacy/raw/AGON_GATE_ROUTING_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE5_CENTER_HANDOFF.md`
- `mechanics/agon/parts/gate-routing/config/agon_gate_routing_handoff_request.seed.json`
- `mechanics/agon/parts/gate-routing/generated/agon_gate_routing_handoff_request.min.json`
- `mechanics/agon/parts/gate-routing/schemas/agon-gate-routing-handoff-request.schema.json`
- `mechanics/agon/parts/gate-routing/examples/agon_gate_routing_handoff_request.example.json`
- `mechanics/agon/parts/gate-routing/scripts/build_agon_gate_routing_handoff_request.py`
- `mechanics/agon/parts/gate-routing/scripts/validate_agon_gate_routing_handoff_request.py`
- `mechanics/agon/parts/gate-routing/tests/test_agon_gate_routing_handoff_request.py`

Validation:

- `python mechanics/agon/parts/gate-routing/scripts/build_agon_gate_routing_handoff_request.py --check`
- `python mechanics/agon/parts/gate-routing/scripts/validate_agon_gate_routing_handoff_request.py`
- `python -m pytest -q mechanics/agon/parts/gate-routing/tests/test_agon_gate_routing_handoff_request.py`

Stop-lines: routing hints are not arena activation, verdicts, scars, retention,
rank mutation, runtime dispatch, or ToS promotion.

Next route: scenario choreography belongs in `aoa-playbooks` after owner-local
landing.

### Agon trial playbook handoff

Status: handoff landed in `v0.2.3`.

Owner boundary: `Agents-of-Abyss` owns the pre-protocol trial-playbook request;
`aoa-playbooks` owns recurring trial choreography only after its own landing.

Surfaces:

- `mechanics/agon/legacy/raw/AGON_TRIAL_PLAYBOOK_HANDOFF.md`
- `mechanics/agon/legacy/raw/AGON_TRIAL_PLAYBOOK_OWNER_REQUEST.md`
- `mechanics/agon/legacy/raw/AGON_TRIAL_PLAYBOOK_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE6_CENTER_HANDOFF.md`
- `mechanics/agon/parts/trial-handoff/config/agon_trial_playbook_request.seed.json`
- `mechanics/agon/parts/trial-handoff/generated/agon_trial_playbook_request.min.json`
- `mechanics/agon/parts/trial-handoff/schemas/agon-trial-playbook-request.schema.json`
- `mechanics/agon/parts/trial-handoff/examples/agon_trial_playbook_request.example.json`
- `mechanics/agon/parts/trial-handoff/scripts/build_agon_trial_playbook_request.py`
- `mechanics/agon/parts/trial-handoff/scripts/validate_agon_trial_playbook_request.py`
- `mechanics/agon/parts/trial-handoff/tests/test_agon_trial_playbook_request.py`

Validation:

- `python mechanics/agon/parts/trial-handoff/scripts/build_agon_trial_playbook_request.py --check`
- `python mechanics/agon/parts/trial-handoff/scripts/validate_agon_trial_playbook_request.py`
- `python -m pytest -q mechanics/agon/parts/trial-handoff/tests/test_agon_trial_playbook_request.py`

Stop-lines: trial playbooks rehearse the arena; they do not open it or grant
verdict, scar, retention, rank, runtime, or ToS authority.

Next route: later Agon waves stay center-law and owner-request surfaces until
their owner repositories land implementation.

### Later Agon center waves

Status: planted and indexed.

Owner boundary: `Agents-of-Abyss` may keep center law, models, handoff requests,
stop-lines, and generated registries; sibling repositories own operational
workflow, proof, memory, stats, routing, runtime, KAG, and ToS canon work.

Surfaces:

- `mechanics/agon/legacy/raw/AGON_WAVE7_CENTER_HANDOFF.md`
- `mechanics/agon/legacy/raw/AGON_WAVE8_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE9_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE10_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE10_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE11_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE11_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE12_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE12_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE13_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE13_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE14_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE14_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE15_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE15_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE16_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE16_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE17_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE17_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE18_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE18_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_INTERLUDE_R4_LANDING.md`

Validation:

- `python scripts/release_check.py`
- nearest `scripts/validate_agon_*.py` named by the changed generated surface
- nearest `python -m pytest -q/test_agon_*.py`

Stop-lines: later center waves still do not create live arena authority,
assistant contestants, live rank mutation, runtime dispatch, hidden memory
sovereignty, or direct ToS canon writes.

Next route: update this log when a later wave becomes the active release
contour or when its owner-request surface changes.
