# Checkpoint Owner-repo Requests

This is the center-side request packet list for `checkpoint`.

It names the stronger owner slices that must land outside `Agents-of-Abyss`
before checkpoint may be treated as operational beyond center law, routes, and
stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance.
It may be copied into an owner-local issue, document, branch, or receipt, but it
remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../owner-request-queue.json)

Generated companion: [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-CHECKPOINT-SDK-001` | `aoa-sdk` | `requested` | `P0` | Checkpoint control panel and local ledgers | CLI, hooks, local ledgers, typed readers, pending-review gate, and closeout-context builder stay bounded and inspectable. | Control behavior is validated in `aoa-sdk`; proof routes to `aoa-evals` only when public claims need defense. |
| `ORQ-CHECKPOINT-SKILLS-001` | `aoa-skills` | `requested` | `P0` | Checkpoint note protocol and closeout bridge skill | Skill-owned checkpoint note contract and explicit closeout bridge remain lower-authority than reviewed closeout. | Bridge execution evidence routes to `aoa-evals` when verdict claims are made. |
| `ORQ-CHECKPOINT-AGENTS-001` | `aoa-agents` | `requested` | `P1` | Self-agent checkpoint posture | Actor-side approval, rollback, health-check, iteration, and improvement-log posture for self-agent routes. | Role and boundary proof routes to `aoa-evals` when needed. |
| `ORQ-CHECKPOINT-MEMO-001` | `aoa-memo` | `requested` | `P1` | Inquiry checkpoint, state capsule, and writeback | Memo-side relaunch and writeback surfaces that keep checkpoint export outside memory canon until reviewed. | Memory durability claims route to `aoa-evals`. |
| `ORQ-CHECKPOINT-PLAYBOOKS-001` | `aoa-playbooks` | `requested` | `P1` | Recurring checkpoint choreography | Playbooks for session-growth, self-agent rollout, A2A return, and checkpoint distillation routes. | Scenario closure proof routes to `aoa-evals`. |
| `ORQ-CHECKPOINT-EVALS-001` | `aoa-evals` | `requested` | `P1` | Proof and regression reading | Eval bundles that read checkpoint evidence without treating checkpoint notes as verdict authority. | Proof lives in `aoa-evals`. |
| `ORQ-CHECKPOINT-ROUTING-001` | `aoa-routing` | `requested` | `P2` | Re-entry hints | Routing hints point back to source-owned checkpoint and return surfaces without interpreting checkpoint meaning. | Route behavior can be checked through evals if public. |
| `ORQ-CHECKPOINT-STATS-001` | `aoa-stats` | `requested` | `P2` | Derived checkpoint visibility | Derived summaries use reviewed owner-local receipts and avoid raw checkpoint-note intake. | Counts remain descriptive and weaker than owner receipts. |
| `ORQ-CHECKPOINT-STACK-001` | `abyss-stack` | `requested` | `P1` | Runtime checkpoint exports and closeout receipts | Runtime-owned checkpoint exports, return policy, and closeout receipts stay behind runtime gates and export contracts. | Runtime claims require runtime receipts and proof routes as needed. |
| `ORQ-CHECKPOINT-DIONYSUS-001` | `Dionysus` | `requested` | `P2` | Reviewed checkpoint snapshots and seed-stage lineage | Durable reviewed checkpoint snapshots and seed-stage lineage preserve explicit promotion without raw append history. | Seed or promotion claims stay evidence-backed and route to evals when public. |

## Center sources

- [README.md](README.md)
- [PARTS](PARTS.md)
- [OWNER_MAP](OWNER_MAP.md)
- [CHECKPOINT_LAW](docs/CHECKPOINT_LAW.md)
- [CHECKPOINT_OWNER_BOUNDARY](docs/CHECKPOINT_OWNER_BOUNDARY.md)

## Stop-lines

- `ORQ-CHECKPOINT-SDK-001`: The center must not treat SDK controls as checkpoint law.
- `ORQ-CHECKPOINT-SKILLS-001`: The center must not treat checkpoint-note protocol as final harvest authority.
- `ORQ-CHECKPOINT-AGENTS-001`: The center must not grant actor rights through checkpoint wording.
- `ORQ-CHECKPOINT-MEMO-001`: The center must not turn checkpoint export into memory canon.
- `ORQ-CHECKPOINT-PLAYBOOKS-001`: The center must not choreograph recurring routes as if playbooks accepted them.
- `ORQ-CHECKPOINT-EVALS-001`: The center must not treat checkpoint evidence as proof verdict.
- `ORQ-CHECKPOINT-ROUTING-001`: The center must not let routing reinterpret checkpoint meaning.
- `ORQ-CHECKPOINT-STATS-001`: The center must not treat derived checkpoint counts as truth.
- `ORQ-CHECKPOINT-STACK-001`: The center must not claim runtime activation or runtime safety.
- `ORQ-CHECKPOINT-DIONYSUS-001`: The center must not preserve raw append history as durable checkpoint doctrine.

## Validation

Use the central Checkpoint validation matrix in [Checkpoint AGENTS](AGENTS.md#validation).

## Next route

Carry the request ID into the owner repository. Do not promote center language
to owner-local truth without owner acceptance, owner landing, and proof where
proof is required.
