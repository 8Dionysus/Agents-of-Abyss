# Agon Landing Log

This is the canonical landing ledger for center-owned Agon waves in
`Agents-of-Abyss`.

Use this file when a change needs the landed history, checked surfaces,
validators, and stop-lines for Agon. Use `ROADMAP.md` for program direction,
not for wave-by-wave ledger detail.

Agon remains center-owned here as law, vocabulary, stop-line, and owner-binding
doctrine. It is not live arena execution, not assistant contestant authority,
not runtime substrate, and not ToS canon write authority.

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

## Landed center line

### Agon preparation holding boundary

Status: planted.

Owner boundary: `Agents-of-Abyss` may name the holding boundary and pre-Agon
review posture; live arena work, actor behavior, runtime dispatch, proof,
memory, and ToS promotion remain outside this repository.

Surfaces:

- `docs/AGON_PREPARATION_POSTURE.md`

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

- `docs/AGON_IMPOSITION_POSTURE.md`
- `docs/AGON_SURVIVAL_CRITERIA.md`
- `docs/AGON_DOUBT_AUDIT.md`
- `docs/PRE_AGON_BASELINE.md`
- `docs/AGON_WAVE0_LANDING.md`
- `generated/agon_imposition_readiness.min.json`
- `schemas/agon-imposition-readiness.schema.json`
- `examples/agon_doubt_audit.example.json`
- `scripts/build_agon_imposition_readiness.py`
- `scripts/validate_agon_imposition_readiness.py`
- `tests/test_agon_imposition_readiness.py`

Validation:

- `python scripts/build_agon_imposition_readiness.py --check`
- `python scripts/validate_agon_imposition_readiness.py`
- `python -m pytest -q tests/test_agon_imposition_readiness.py`

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

- `docs/AGON_LAWFUL_MOVE_LANGUAGE.md`
- `docs/AGON_MOVE_REGISTRY_MODEL.md`
- `docs/AGON_MOVE_OWNER_HANDOFFS.md`
- `docs/AGON_WAVE3_LANDING.md`
- `config/agon_lawful_moves.seed.json`
- `generated/agon_lawful_move_registry.min.json`
- `schemas/agon-lawful-move.schema.json`
- `schemas/agon-lawful-move-registry.schema.json`
- `examples/agon_lawful_move.example.json`
- `scripts/build_agon_lawful_move_registry.py`
- `scripts/validate_agon_lawful_moves.py`
- `tests/test_agon_lawful_moves.py`

Validation:

- `python scripts/build_agon_lawful_move_registry.py --check`
- `python scripts/validate_agon_lawful_moves.py`
- `python -m pytest -q tests/test_agon_lawful_moves.py`

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

- `docs/AGON_MOVE_OWNER_BINDING.md`
- `docs/AGON_MOVE_BINDING_MATRIX_MODEL.md`
- `docs/AGON_OWNER_REPO_REQUESTS.md`
- `docs/AGON_PRE_PROTOCOL_STOP_LINES.md`
- `docs/AGON_WAVE4_LANDING.md`
- `config/agon_move_owner_bindings.seed.json`
- `generated/agon_move_owner_binding_registry.min.json`
- `schemas/agon-move-owner-binding.schema.json`
- `schemas/agon-move-owner-binding-registry.schema.json`
- `examples/agon_move_owner_binding.example.json`
- `scripts/build_agon_move_owner_binding_registry.py`
- `scripts/validate_agon_move_owner_bindings.py`
- `tests/test_agon_move_owner_bindings.py`

Validation:

- `python scripts/build_agon_move_owner_binding_registry.py --check`
- `python scripts/validate_agon_move_owner_bindings.py`
- `python -m pytest -q tests/test_agon_move_owner_bindings.py`

Stop-lines: owner requests are not landed practice, workflow, proof, route,
scenario, memory, stats, actor, runtime, or ToS authority.

Next route: bounded handoffs may ask owner repositories to land their own
slices.

### Agon gate routing handoff

Status: handoff landed in `v0.2.3`.

Owner boundary: `Agents-of-Abyss` owns the pre-protocol gate-routing request;
`aoa-routing` owns any future routing implementation after its own review.

Surfaces:

- `docs/AGON_GATE_ROUTING_HANDOFF.md`
- `docs/AGON_GATE_ROUTING_OWNER_REQUEST.md`
- `docs/AGON_GATE_ROUTING_STOP_LINES.md`
- `docs/AGON_WAVE5_CENTER_HANDOFF.md`
- `config/agon_gate_routing_handoff_request.seed.json`
- `generated/agon_gate_routing_handoff_request.min.json`
- `schemas/agon-gate-routing-handoff-request.schema.json`
- `examples/agon_gate_routing_handoff_request.example.json`
- `scripts/build_agon_gate_routing_handoff_request.py`
- `scripts/validate_agon_gate_routing_handoff_request.py`
- `tests/test_agon_gate_routing_handoff_request.py`

Validation:

- `python scripts/build_agon_gate_routing_handoff_request.py --check`
- `python scripts/validate_agon_gate_routing_handoff_request.py`
- `python -m pytest -q tests/test_agon_gate_routing_handoff_request.py`

Stop-lines: routing hints are not arena activation, verdicts, scars, retention,
rank mutation, runtime dispatch, or ToS promotion.

Next route: scenario choreography belongs in `aoa-playbooks` after owner-local
landing.

### Agon trial playbook handoff

Status: handoff landed in `v0.2.3`.

Owner boundary: `Agents-of-Abyss` owns the pre-protocol trial-playbook request;
`aoa-playbooks` owns recurring trial choreography only after its own landing.

Surfaces:

- `docs/AGON_TRIAL_PLAYBOOK_HANDOFF.md`
- `docs/AGON_TRIAL_PLAYBOOK_OWNER_REQUEST.md`
- `docs/AGON_TRIAL_PLAYBOOK_STOP_LINES.md`
- `docs/AGON_WAVE6_CENTER_HANDOFF.md`
- `config/agon_trial_playbook_request.seed.json`
- `generated/agon_trial_playbook_request.min.json`
- `schemas/agon-trial-playbook-request.schema.json`
- `examples/agon_trial_playbook_request.example.json`
- `scripts/build_agon_trial_playbook_request.py`
- `scripts/validate_agon_trial_playbook_request.py`
- `tests/test_agon_trial_playbook_request.py`

Validation:

- `python scripts/build_agon_trial_playbook_request.py --check`
- `python scripts/validate_agon_trial_playbook_request.py`
- `python -m pytest -q tests/test_agon_trial_playbook_request.py`

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

- `docs/AGON_WAVE7_CENTER_HANDOFF.md`
- `docs/AGON_WAVE8_LANDING.md`
- `docs/AGON_WAVE9_LANDING.md`
- `docs/AGON_WAVE10_LANDING.md`
- `docs/AGON_WAVE10_STOP_LINES.md`
- `docs/AGON_WAVE11_LANDING.md`
- `docs/AGON_WAVE11_STOP_LINES.md`
- `docs/AGON_WAVE12_LANDING.md`
- `docs/AGON_WAVE12_STOP_LINES.md`
- `docs/AGON_WAVE13_LANDING.md`
- `docs/AGON_WAVE13_STOP_LINES.md`
- `docs/AGON_WAVE14_LANDING.md`
- `docs/AGON_WAVE14_STOP_LINES.md`
- `docs/AGON_WAVE15_LANDING.md`
- `docs/AGON_WAVE15_STOP_LINES.md`
- `docs/AGON_WAVE16_LANDING.md`
- `docs/AGON_WAVE16_STOP_LINES.md`
- `docs/AGON_WAVE17_LANDING.md`
- `docs/AGON_WAVE17_STOP_LINES.md`
- `docs/AGON_WAVE18_LANDING.md`
- `docs/AGON_WAVE18_STOP_LINES.md`
- `docs/AGON_INTERLUDE_R4_LANDING.md`

Validation:

- `python scripts/release_check.py`
- nearest `scripts/validate_agon_*.py` named by the changed generated surface
- nearest `python -m pytest -q tests/test_agon_*.py`

Stop-lines: later center waves still do not create live arena authority,
assistant contestants, live rank mutation, runtime dispatch, hidden memory
sovereignty, or direct ToS canon writes.

Next route: update this log when a later wave becomes the active release
contour or when its owner-request surface changes.
