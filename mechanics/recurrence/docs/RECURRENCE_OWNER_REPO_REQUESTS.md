# Recurrence Owner-repo Requests

This is the center-side request packet list for `recurrence`.

It names the stronger owner slices that must land outside `Agents-of-Abyss` before `recurrence` may be treated as operational beyond center doctrine, routes, and stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance. It may be copied into an owner-local issue, document, branch, or receipt, but it remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../../../mechanics/owner-request-queue.json)

Generated companion: [`generated/owner_request_queue.min.json`](../../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-RECURRENCE-ROUTING-001` | `aoa-routing` | `requested` | `P1` | Re-entry route graph and return dispatch | Navigation surface that points from drift to last valid anchor and explicit re-entry without authoring recurrence meaning. | Route behavior proof should go to `aoa-evals` when public claims are made. |
| `ORQ-RECURRENCE-MEMO-001` | `aoa-memo` | `requested` | `P0` | Anchor checkpoints, recall, and provenance for bounded continuity | Memory surfaces for anchors, checkpoints, recall eligibility, forgetting, and re-entry provenance. | Continuity evidence routes to `aoa-evals` before durability claims. |
| `ORQ-RECURRENCE-AGENTS-001` | `aoa-agents` | `requested` | `P1` | Role and handoff posture for returns between actors | Role-facing handoff contract that says who may resume, under what seat, and with which anchor. | Handoff quality proof routes to `aoa-evals` where needed. |
| `ORQ-RECURRENCE-PLAYBOOKS-001` | `aoa-playbooks` | `requested` | `P1` | Recurring return choreography | Repeatable return scenario with safe stops, anchor checks, fallback posture, and expected evidence. | Scenario proof routes to `aoa-evals`. |
| `ORQ-RECURRENCE-EVALS-001` | `aoa-evals` | `requested` | `P1` | Drift and recovery-quality proof | Eval bundle for drift detection, anchor validity, recovery quality, and regression evidence. | Proof lives in `aoa-evals` and informs other owners. |
| `ORQ-RECURRENCE-STACK-001` | `abyss-stack` | `requested` | `P2` | Runtime wrappers for bounded re-entry after owner gates | Runtime wrapper or service boundary that can enact validated re-entry without authoring meaning. | Runtime evidence routes to `aoa-evals` and infrastructure receipts. |

## Center sources

- [README.md](../../../mechanics/recurrence/README.md)
- [RECURRENCE_PRINCIPLE.md](../../../mechanics/recurrence/docs/RECURRENCE_PRINCIPLE.md)
- [SELF_AGENCY_CONTINUITY.md](../../../mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md)
- [COMPONENT_REFRESH_LAW.md](../../../mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md)

## Stop-lines

- `ORQ-RECURRENCE-ROUTING-001`: `aoa-routing` may dispatch but must not become source meaning.
- `ORQ-RECURRENCE-MEMO-001`: The center must not claim hidden memory sovereignty or ambient continuity.
- `ORQ-RECURRENCE-AGENTS-001`: Continuity must not mutate role authority inside the center.
- `ORQ-RECURRENCE-PLAYBOOKS-001`: The center must not own recurring continuity choreography once it is operational.
- `ORQ-RECURRENCE-EVALS-001`: The center must not treat return doctrine as proof of successful recovery.
- `ORQ-RECURRENCE-STACK-001`: Runtime must not be presented as self-healing or ambient autonomy.

## Validation

Use the validation lane in [mechanics/recurrence/docs/AGENTS.md](AGENTS.md#validation) for executable commands.

## Next route

Carry the request ID into the owner repository. Do not promote center language to owner-local truth without owner acceptance, owner landing, and proof where proof is required.
