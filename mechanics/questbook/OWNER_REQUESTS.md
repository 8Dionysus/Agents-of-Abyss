# Questbook Owner-repo Requests

This is the center-side request packet list for `questbook`.

It names the stronger owner slices that must land outside `Agents-of-Abyss` before `questbook` may be treated as operational beyond center doctrine, routes, and stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance. It may be copied into an owner-local issue, document, branch, or receipt, but it remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../owner-request-queue.json)

Generated companion: [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-QUESTBOOK-PLAYBOOKS-001` | `aoa-playbooks` | `requested` | `P1` | Recurring quest choreography and public obligation routes | Playbook for recurring quest intake, review, fallback, closure, and evidence posture. | Closure proof routes to `aoa-evals` as needed. |
| `ORQ-QUESTBOOK-EVALS-001` | `aoa-evals` | `requested` | `P1` | Proof obligations attached to quest closure | Eval surface for whether the quest was actually satisfied, with evidence and blind spots. | Proof lives in `aoa-evals` when the closure claim needs defense. |
| `ORQ-QUESTBOOK-MEMO-001` | `aoa-memo` | `requested` | `P2` | Lessons retained after quest completion | Memory object for reusable lesson, provenance, recall, and forgetting after quest closure. | Lesson integrity may route to `aoa-evals`. |
| `ORQ-QUESTBOOK-ROUTING-001` | `aoa-routing` | `requested` | `P2` | Cross-repo obligation handoff and thin route surfaces | Routing entry that sends repo-local obligations to their owners without centralizing task truth. | Route behavior can be checked through evals if public. |

## Center sources

- [README.md](README.md)
- [model-spine](parts/model-spine/README.md)
- [provenance bridge](PROVENANCE.md)
- [QUESTBOOK.md](../../QUESTBOOK.md)
- [quests README](../../quests/README.md)

## Stop-lines

- `ORQ-QUESTBOOK-PLAYBOOKS-001`: Questbook must not become a second roadmap.
- `ORQ-QUESTBOOK-EVALS-001`: The center must not treat a closed quest as proof without evidence.
- `ORQ-QUESTBOOK-MEMO-001`: Quest items must not become private scratch memory.
- `ORQ-QUESTBOOK-ROUTING-001`: Routing must not author repo-local task truth.

## Validation

Use the central Questbook validation matrix in [Questbook AGENTS](AGENTS.md#validation).

## Next route

Carry the request ID into the owner repository. Do not promote center language to owner-local truth without owner acceptance, owner landing, and proof where proof is required.
