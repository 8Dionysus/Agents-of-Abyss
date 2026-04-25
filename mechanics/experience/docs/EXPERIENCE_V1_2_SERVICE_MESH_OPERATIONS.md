# Experience v1.2 Service Mesh Operations

This surface lands the v1.2 service mesh operations contour after the
`Dionysus` intake pack and the `Experience v1.2-v2.0 Bridge`.

It is Wave 2 of the current v1.2-v2.0 planting campaign. It is not `Experience Wave 2`; that name already belongs to
`EXPERIENCE_WAVE2_CERTIFICATION_WATCHTOWER.md`. It is not a runtime service
launch, not a new `aoa-experience` repository, and not raw archive replay.

## Source Frame

The source transport artifact is:

- `aoa-experience-service-mesh-operations-seed-v1_2.zip`

The `Dionysus` intake records its SHA-256 as:

- `df829241ac629770635290e5da2742b81e4d5575270c94a92c34a95f4bbacb85`

The archive-local seed validator and tests passed during intake and were
rerun before this landing. That evidence proves archive readability and local
coherence only. It does not grant owner readiness, runtime safety, or authority
to activate services.

## Predecessor Law

This surface depends on and remains subordinate to:

- `EXPERIENCE_WAVE5_SOVEREIGN_OFFICE.md`
- `EXPERIENCE_V1_1_LIVE_OFFICE_EXPANSION.md`
- `EXPERIENCE_SERVICE_MESH_LAW.md`
- `EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md`
- `EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md`
- `AGON_PRE_PROTOCOL_STOP_LINES.md`

The v1.1 service mesh law defines the office mesh. This v1.2 surface does not
expand that mesh. It tests whether the released offices preserve mandate,
handoff integrity, receipts, scope, alarms, rollback readiness, and
service-to-Agon escalation discipline under pressure.

## Office Contour

The primary offices under drill are:

- `notary.assistant`
- `concierge.assistant`
- `courier.assistant`
- `monitor.assistant`

Prepared but not primary offices remain:

- `librarian.assistant`
- `steward.assistant`
- `scheduler.assistant`

Prepared offices do not become primary through this landing.

## Operations Flow

The center flow is:

```text
service_mesh_release_received
  -> drill_plan_declared
  -> scenario_injected
  -> office_integrity_checked
  -> bounded_verdict_recorded
  -> memory_gate_evaluated
  -> incident_reentry_routed
  -> retention_or_patch_proposal_declared
```

The flow is a contract for rehearsal and evidence routing. It does not execute
a live drill by itself.

## Failure Laws

The non-negotiable v1.2 failure laws are:

- `no_hidden_assistant_self_heal`
- `no_courier_meaning_edit`
- `no_concierge_scope_expansion`
- `no_notary_closure_without_receipt`
- `no_monitor_material_alarm_without_verdict_path`
- `no_service_to_agon_escalation_without_trigger`
- `no_drill_pass_by_codex`
- `no_direct_tree_of_sophia_runtime_write`

Those laws route failures back through verdict, memory gate, incident reentry,
and owner landing. They do not make assistants into agonic contestants and do
not make service drills into live arena sessions.

## Owner Split

- `Agents-of-Abyss` owns this center law, operations flow, source bridge, and
  authority stop-lines.
- `aoa-agents` owns assistant office posture, failure posture, and recovery
  contracts after a separate owner-local landing.
- `aoa-evals` owns bounded drill verdict bundles, not drill pass authority.
- `aoa-playbooks` owns drill choreography and scenario injection playbooks, not
  runtime execution.
- `aoa-memo` owns memory gates, lesson candidates, and retention readiness, not
  memory truth or retention execution.
- `aoa-stats` owns derived dashboards and summaries only.
- `aoa-routing` owns advisory escalation and incident reentry routes only.
- `aoa-sdk` owns typed helper contracts only.
- `aoa-kag` owns service pattern candidates only.
- `abyss-stack` owns runtime jobs, workers, storage, and drill substrate only
  after a separate runtime-owner gate.
- `Tree-of-Sophia` owns canon and interpretive review only through its own
  path; it receives no runtime writes.
- `Dionysus` owns source lineage and harvest trace only.
- `8Dionysus` owns shared-root projection law only where later workspace
  projection surfaces are affected.
- `aoa-skills` and `aoa-techniques` own reusable workflows and practices
  extracted from owner-accepted patterns only.

## Stop-Lines

This landing must not:

- activate live services, host ports, scheduler loops, runtime workers, or
  deployment daemons
- certify, seal, or pass a drill by Codex
- rewrite assistant policy or repair persistent assistant mandates by assistant
  self-heal
- allow courier meaning edits, concierge scope expansion, or notary closure
  without receipt
- treat monitor alarms as material without a verdict path
- turn service-to-Agon escalation into live summon authority
- create live arena sessions, live verdicts, scars, retention execution, rank
  mutation, trust mutation, or honor mutation
- write directly to `Tree-of-Sophia`
- let stats become proof, memo become truth, routing become owner, KAG become canon,
  SDK become authority, or runtime become doctrine

## Validation

The structural anchor is:

- `schemas/experience-v1-2-service-mesh-operations.schema.json`
- `examples/experience_v1_2_service_mesh_operations.example.json`

Run:

```bash
python scripts/validate_experience_v1_2_service_mesh_operations.py
python -m pytest -q tests/test_experience_v1_2_service_mesh_operations.py
```
