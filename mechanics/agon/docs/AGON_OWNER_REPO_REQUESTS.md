# Agon Owner-repo Requests

This is the center-side request packet list for `agon`.

It names the stronger owner slices that must land outside `Agents-of-Abyss` before `agon` may be treated as operational beyond center doctrine, routes, and stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance. It may be copied into an owner-local issue, document, branch, or receipt, but it remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../../../mechanics/owner-request-queue.json)

Generated companion: [`generated/owner_request_queue.min.json`](../../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-AGON-PLAYBOOKS-001` | `aoa-playbooks` | `requested` | `P0` | Agon trial choreography and repeatable duel routes | Trial playbook with setup, roles, moves, fallback posture, expected evidence, and closure path. | Trial outcomes and verdict claims route to `aoa-evals`. |
| `ORQ-AGON-EVALS-001` | `aoa-evals` | `requested` | `P0` | Verdict proof, evaluation discipline, and regression evidence | Eval bundle for verdict boundaries, comparison modes, blind spots, and regression evidence. | Proof lives in `aoa-evals` before rank, verdict, or public claims. |
| `ORQ-AGON-MEMO-001` | `aoa-memo` | `requested` | `P0` | Scars, retention memory, and bounded lessons | Memory surfaces for scars, retained lessons, provenance, forgetting, and re-entry conditions. | Retention quality routes to `aoa-evals` where needed. |
| `ORQ-AGON-STATS-001` | `aoa-stats` | `requested` | `P2` | Aggregate rank and reputation projections after proof gates | Derived observability view that summarizes owner-local proof and memory without authority transfer. | Stats claims must cite eval and owner-local receipts. |
| `ORQ-AGON-ROUTING-001` | `aoa-routing` | `requested` | `P1` | Gates, handoffs, and arena route behavior | Dispatch and gate surfaces that route between trial, proof, memory, role, runtime, and ToS thresholds. | Route behavior proof may route to `aoa-evals`. |
| `ORQ-AGON-AGENTS-001` | `aoa-agents` | `requested` | `P0` | Actor seats, role contracts, and contestant posture | Role contracts for actor seats, contestant posture, civil/service assistant variants, and handoff boundaries. | Actor-role claims route to `aoa-evals` if public or operational. |
| `ORQ-AGON-STACK-001` | `abyss-stack` | `requested` | `P2` | Runtime session bodies after runtime-owner gates | Infrastructure body for sessions, logs, lifecycle, and storage after all owner gates and proof routes are named. | Runtime evidence must remain infrastructure evidence and route to evals for claims. |
| `ORQ-AGON-TOS-001` | `Tree-of-Sophia` | `requested` | `P0` | ToS threshold and canonization questions | ToS-owned threshold decision or canon process when Agon pressure touches Sophian meaning. | AoA may provide threshold packets; ToS owns canon acceptance. |

## Center sources

- [README.md](../../../mechanics/agon/README.md)
- [AGON_IMPOSITION_POSTURE.md](../../../mechanics/agon/docs/AGON_IMPOSITION_POSTURE.md)
- [AGON_MOVE_OWNER_BINDING.md](../../../mechanics/agon/docs/AGON_MOVE_OWNER_BINDING.md)
- [AGON_GATE_ROUTING_HANDOFF.md](../../../mechanics/agon/docs/AGON_GATE_ROUTING_HANDOFF.md)
- [AGON_TRIAL_PLAYBOOK_HANDOFF.md](../../../mechanics/agon/docs/AGON_TRIAL_PLAYBOOK_HANDOFF.md)
- [AGON_TOS_THRESHOLD_PACKET_MODEL.md](../../../mechanics/agon/docs/AGON_TOS_THRESHOLD_PACKET_MODEL.md)

## Stop-lines

- `ORQ-AGON-PLAYBOOKS-001`: The center must not claim live arena execution or scenario authority.
- `ORQ-AGON-EVALS-001`: The center must not treat Agon law as a verdict engine inside the center.
- `ORQ-AGON-MEMO-001`: The center must not mutate memory or retention.
- `ORQ-AGON-STATS-001`: `aoa-stats` must not become score, verdict, or rank authority.
- `ORQ-AGON-ROUTING-001`: Routing must not become arena execution or verdict authority.
- `ORQ-AGON-AGENTS-001`: The center must not grant assistant contestant authority.
- `ORQ-AGON-STACK-001`: The center must not claim live arena runtime.
- `ORQ-AGON-TOS-001`: The center must not write ToS canon or threshold authority.

## Validation

```bash
python scripts/validate_owner_request_queue.py --mechanic agon
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic agon
python scripts/validate_mechanics_topology.py --mechanic agon
```

## Next route

Carry the request ID into the owner repository. Do not promote center language to owner-local truth without owner acceptance, owner landing, and proof where proof is required.
