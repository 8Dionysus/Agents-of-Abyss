# Growth Cycle Owner-repo Requests

This is the center-side request packet list for `growth-cycle`.

It names the stronger owner slices that must land outside `Agents-of-Abyss`
before Growth Cycle may be treated as operational beyond center law, routes,
and stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance.
It may be copied into an owner-local issue, document, branch, or receipt, but it
remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../owner-request-queue.json)

Generated companion: [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-GROWTHCYCLE-SDK-001` | `aoa-sdk` | `requested` | `P0` | Checkpoint hooks, ledgers, and closeout context | SDK-owned control panel, hooks, checkpoint ledgers, typed cycle helpers, and closeout-context builders stay explicit and inspectable. | Control behavior is validated in `aoa-sdk`; proof routes to `aoa-evals` when public claims need defense. |
| `ORQ-GROWTHCYCLE-SKILLS-001` | `aoa-skills` | `requested` | `P0` | Executable cycle stage skills | Skill-owned workflows for donor harvest, progression lift, route forks, automation opportunity scan, diagnosis, repair, and quest harvest remain executable but lower-authority than owner acceptance. | Execution evidence routes to `aoa-evals` when verdict or quality claims are made. |
| `ORQ-GROWTHCYCLE-AGENTS-001` | `aoa-agents` | `requested` | `P1` | Self-agent checkpoint, progression, and health posture | Agent-side approval, rollback, health, role boundary, and progression posture for reviewed cycles. | Role and progression claims route to `aoa-evals` when public or contested. |
| `ORQ-GROWTHCYCLE-EVALS-001` | `aoa-evals` | `requested` | `P1` | Proof and regression verdicts for cycle claims | Eval surfaces that read cycle evidence for repair, progression, automation, and public support without treating center route language as verdict. | Proof lives in `aoa-evals`. |
| `ORQ-GROWTHCYCLE-MEMO-001` | `aoa-memo` | `requested` | `P1` | Memory writeback, recall, and failure lessons | Memo-side writeback and recall surfaces keep cycle residue out of memory canon until reviewed. | Memory durability claims route to `aoa-evals`. |
| `ORQ-GROWTHCYCLE-PLAYBOOKS-001` | `aoa-playbooks` | `requested` | `P1` | Recurring cycle choreography | Playbooks for recurring reviewed closeout, harvest, repair, quest, and owner-followthrough routes. | Scenario closure proof routes to `aoa-evals`. |
| `ORQ-GROWTHCYCLE-STATS-001` | `aoa-stats` | `requested` | `P2` | Derived cycle visibility | Derived summaries read owner receipts and reviewed closeouts without becoming proof, route authority, or memory. | Counts remain descriptive and weaker than owner receipts. |
| `ORQ-GROWTHCYCLE-ROUTING-001` | `aoa-routing` | `requested` | `P2` | Re-entry and next-route hints | Routing hints point to source-owned Growth Cycle and owner surfaces without interpreting cycle meaning. | Route behavior can be checked through evals if public. |
| `ORQ-GROWTHCYCLE-DIONYSUS-001` | `Dionysus` | `requested` | `P2` | Reviewed snapshots and seed lineage | Durable reviewed snapshots and seed lineage preserve explicit promotion without raw append history. | Seed or promotion claims stay evidence-backed and route to evals when public. |
| `ORQ-GROWTHCYCLE-STACK-001` | `abyss-stack` | `requested` | `P1` | Runtime exports and health receipts | Runtime-owned cycle exports, health receipts, and closeout plumbing stay behind runtime gates and export contracts. | Runtime claims require runtime receipts and proof routes as needed. |

## Center sources

- [README.md](README.md)
- [PARTS](PARTS.md)
- [OWNER_MAP](OWNER_MAP.md)
- [GROWTH_CYCLE_LAW](docs/GROWTH_CYCLE_LAW.md)
- [GROWTH_CYCLE_OWNER_REPO_REQUESTS](docs/GROWTH_CYCLE_OWNER_REPO_REQUESTS.md)

## Stop-lines

- `ORQ-GROWTHCYCLE-SDK-001`: The center must not treat SDK controls as Growth Cycle law.
- `ORQ-GROWTHCYCLE-SKILLS-001`: The center must not treat executable skills as owner acceptance or final harvest authority.
- `ORQ-GROWTHCYCLE-AGENTS-001`: The center must not grant actor rights or progression truth through Growth Cycle wording.
- `ORQ-GROWTHCYCLE-EVALS-001`: The center must not treat cycle evidence as proof verdict.
- `ORQ-GROWTHCYCLE-MEMO-001`: The center must not turn cycle residue into memory canon.
- `ORQ-GROWTHCYCLE-PLAYBOOKS-001`: The center must not choreograph recurring routes as if playbooks accepted them.
- `ORQ-GROWTHCYCLE-STATS-001`: The center must not treat derived cycle counts as proof or route authority.
- `ORQ-GROWTHCYCLE-ROUTING-001`: The center must not let routing reinterpret Growth Cycle meaning.
- `ORQ-GROWTHCYCLE-DIONYSUS-001`: The center must not preserve raw append history as durable seed or snapshot doctrine.
- `ORQ-GROWTHCYCLE-STACK-001`: The center must not claim runtime activation or runtime safety.

## Validation

Use the central Growth Cycle validation matrix in [Growth Cycle AGENTS](AGENTS.md#validation).

## Next route

Carry the request ID into the owner repository. Do not promote center language
to owner-local truth without owner acceptance, owner landing, and proof where
proof is required.
