# Owner Request Queue

This is the center-side queue for moving mechanic slices into the repositories that own operational truth.

The queue does not make mechanics operational. It prevents the center from pretending they are operational before owner-local landing, proof, runtime, memory, role, playbook, KAG, SDK, public projection, or ToS authority has actually landed.

Source data lives in [`owner-request-queue.json`](owner-request-queue.json). The compact machine companion is [`generated/owner_request_queue.min.json`](../generated/owner_request_queue.min.json).

## Queue grammar

A request says:

```text
mechanic slice -> stronger owner -> required owner-local landing -> proof route -> stop-line
```

It is a **request packet**, not an implementation, verdict, memory object, runtime service, role grant, playbook scenario, KAG projection, SDK helper, profile claim, or ToS canon decision.

## Request status vocabulary

| Status | Meaning |
|---|---|
| `queued` | The center has identified an owner-local slice, but no full request packet is ready yet. |
| `requested` | A center-side request packet exists and may be handed to the owner repository; this is not owner acceptance. |
| `accepted` | The owner repository has accepted scope in an owner-local issue, document, branch, or equivalent receipt. |
| `landed` | The owner repository has landed the requested surface and the required proof or receipt is linked. |
| `blocked` | The request cannot advance until an explicit blocker is resolved. |
| `superseded` | The request has been replaced by another request ID and must point to that successor. |
| `retired` | The request is intentionally kept as historical context and must not be treated as active. |

## How agents use the queue

1. Start from the mechanic card.
2. Find the request ID by mechanic and owner.
3. Carry the ID into the owner-local issue, document, receipt, or branch.
4. Do not mark the request `accepted` or `landed` unless the owner repository provides the corresponding receipt.
5. Rebuild and validate the generated queue after any change.

## Request index

| Request | Mechanic | Owner | Status | Priority | Slice |
|---|---|---|---|---|---|
| `ORQ-METHOD-SKILLS-001` | `method-growth` | `aoa-skills` | `requested` | `P1` | Candidate skill identity and bounded execution shape |
| `ORQ-METHOD-SDK-001` | `method-growth` | `aoa-sdk` | `requested` | `P2` | Provisional carry and typed helper hints |
| `ORQ-METHOD-DIONYSUS-001` | `method-growth` | `Dionysus` | `requested` | `P1` | Seed staging for candidate objects before owner landing |
| `ORQ-METHOD-EVALS-001` | `method-growth` | `aoa-evals` | `requested` | `P1` | Proof route for promoted candidates and reusable method claims |
| `ORQ-METHOD-PLAYBOOKS-001` | `method-growth` | `aoa-playbooks` | `requested` | `P1` | Recurring method choreography after repeated work stabilizes |
| `ORQ-METHOD-MEMO-001` | `method-growth` | `aoa-memo` | `requested` | `P2` | Lessons, memory, and pruning receipts after owner landing |
| `ORQ-METHOD-TECHNIQUES-001` | `method-growth` | `aoa-techniques` | `requested` | `P1` | Reusable practice promotion |
| `ORQ-METHOD-STATS-001` | `method-growth` | `aoa-stats` | `requested` | `P2` | Derived method-growth visibility |
| `ORQ-RECURRENCE-SDK-001` | `recurrence` | `aoa-sdk` | `requested` | `P0` | Control-plane carry for recurrence manifests and reviewed handoffs |
| `ORQ-RECURRENCE-ROUTING-001` | `recurrence` | `aoa-routing` | `requested` | `P1` | Re-entry route graph and return dispatch |
| `ORQ-RECURRENCE-MEMO-001` | `recurrence` | `aoa-memo` | `requested` | `P0` | Anchor checkpoints, recall, and provenance for bounded continuity |
| `ORQ-RECURRENCE-AGENTS-001` | `recurrence` | `aoa-agents` | `requested` | `P1` | Role and handoff posture for returns between actors |
| `ORQ-RECURRENCE-PLAYBOOKS-001` | `recurrence` | `aoa-playbooks` | `requested` | `P1` | Recurring return choreography |
| `ORQ-RECURRENCE-EVALS-001` | `recurrence` | `aoa-evals` | `requested` | `P1` | Drift and recovery-quality proof |
| `ORQ-RECURRENCE-STATS-001` | `recurrence` | `aoa-stats` | `requested` | `P2` | Derived recurrence visibility |
| `ORQ-RECURRENCE-KAG-001` | `recurrence` | `aoa-kag` | `requested` | `P2` | Recurrence regrounding toward source references |
| `ORQ-RECURRENCE-STACK-001` | `recurrence` | `abyss-stack` | `requested` | `P2` | Runtime wrappers for bounded re-entry after owner gates |
| `ORQ-CHECKPOINT-SDK-001` | `checkpoint` | `aoa-sdk` | `requested` | `P0` | Checkpoint control panel and local ledgers |
| `ORQ-CHECKPOINT-SKILLS-001` | `checkpoint` | `aoa-skills` | `requested` | `P0` | Checkpoint note protocol and closeout bridge skill |
| `ORQ-CHECKPOINT-AGENTS-001` | `checkpoint` | `aoa-agents` | `requested` | `P1` | Self-agent checkpoint posture |
| `ORQ-CHECKPOINT-MEMO-001` | `checkpoint` | `aoa-memo` | `requested` | `P1` | Inquiry checkpoint, state capsule, and writeback |
| `ORQ-CHECKPOINT-PLAYBOOKS-001` | `checkpoint` | `aoa-playbooks` | `requested` | `P1` | Recurring checkpoint choreography |
| `ORQ-CHECKPOINT-EVALS-001` | `checkpoint` | `aoa-evals` | `requested` | `P1` | Proof and regression reading |
| `ORQ-CHECKPOINT-ROUTING-001` | `checkpoint` | `aoa-routing` | `requested` | `P2` | Re-entry hints |
| `ORQ-CHECKPOINT-STATS-001` | `checkpoint` | `aoa-stats` | `requested` | `P2` | Derived checkpoint visibility |
| `ORQ-CHECKPOINT-STACK-001` | `checkpoint` | `abyss-stack` | `requested` | `P1` | Runtime checkpoint exports and closeout receipts |
| `ORQ-CHECKPOINT-DIONYSUS-001` | `checkpoint` | `Dionysus` | `requested` | `P2` | Reviewed checkpoint snapshots and seed-stage lineage |
| `ORQ-EXPERIENCE-STACK-001` | `experience` | `abyss-stack` | `requested` | `P0` | Living workspace runtime and office infrastructure |
| `ORQ-EXPERIENCE-MEMO-001` | `experience` | `aoa-memo` | `requested` | `P0` | Experience memory, provenance, recall, and continuity loom objects |
| `ORQ-EXPERIENCE-ROUTING-001` | `experience` | `aoa-routing` | `requested` | `P1` | Context router and live route behavior for experience flows |
| `ORQ-EXPERIENCE-EVALS-001` | `experience` | `aoa-evals` | `requested` | `P0` | Adoption proof, certification checks, and regression evidence |
| `ORQ-EXPERIENCE-AGENTS-001` | `experience` | `aoa-agents` | `requested` | `P1` | Office, role-pair, actor, and handoff posture |
| `ORQ-EXPERIENCE-KAG-001` | `experience` | `aoa-kag` | `requested` | `P2` | Derived workspace and experience-ready knowledge projections |
| `ORQ-EXPERIENCE-TOS-001` | `experience` | `Tree-of-Sophia` | `requested` | `P1` | ToS meaning boundaries touched by experience contracts |
| `ORQ-EXPERIENCE-PLAYBOOKS-001` | `experience` | `aoa-playbooks` | `requested` | `P1` | Experience adoption, release, office, and service choreography |
| `ORQ-EXPERIENCE-SDK-001` | `experience` | `aoa-sdk` | `requested` | `P1` | Typed install, runtime, train, and helper API carriers for Experience routes |
| `ORQ-EXPERIENCE-STATS-001` | `experience` | `aoa-stats` | `requested` | `P2` | Experience dashboards, watch summaries, and derived movement readouts |
| `ORQ-EXPERIENCE-SKILLS-001` | `experience` | `aoa-skills` | `requested` | `P2` | Experience receipt, adoption, release, and service operation skills |
| `ORQ-EXPERIENCE-TECHNIQUES-001` | `experience` | `aoa-techniques` | `requested` | `P2` | Reusable Experience adoption, deployment, office, and service practice |
| `ORQ-AGON-PLAYBOOKS-001` | `agon` | `aoa-playbooks` | `requested` | `P0` | Agon trial choreography and repeatable duel routes |
| `ORQ-AGON-EVALS-001` | `agon` | `aoa-evals` | `requested` | `P0` | Verdict proof, evaluation discipline, and regression evidence |
| `ORQ-AGON-MEMO-001` | `agon` | `aoa-memo` | `requested` | `P0` | Scars, retention memory, and bounded lessons |
| `ORQ-AGON-STATS-001` | `agon` | `aoa-stats` | `requested` | `P2` | Aggregate rank and reputation projections after proof gates |
| `ORQ-AGON-ROUTING-001` | `agon` | `aoa-routing` | `requested` | `P1` | Gates, handoffs, and arena route behavior |
| `ORQ-AGON-AGENTS-001` | `agon` | `aoa-agents` | `requested` | `P0` | Actor seats, role contracts, and contestant posture |
| `ORQ-AGON-STACK-001` | `agon` | `abyss-stack` | `requested` | `P2` | Runtime session bodies after runtime-owner gates |
| `ORQ-AGON-KAG-001` | `agon` | `aoa-kag` | `requested` | `P1` | Derived evidence bundles and KAG-ready pressure projections |
| `ORQ-AGON-TOS-001` | `agon` | `Tree-of-Sophia` | `requested` | `P0` | ToS threshold and canonization questions |
| `ORQ-ANTIFRAGILITY-EVALS-001` | `antifragility` | `aoa-evals` | `requested` | `P1` | Repair proof and regression evidence after stress or subtraction |
| `ORQ-ANTIFRAGILITY-MEMO-001` | `antifragility` | `aoa-memo` | `requested` | `P2` | Incident lessons and retained stress memory |
| `ORQ-ANTIFRAGILITY-STATS-001` | `antifragility` | `aoa-stats` | `requested` | `P2` | Derived fragility and cleanup summary windows |
| `ORQ-ANTIFRAGILITY-PLAYBOOKS-001` | `antifragility` | `aoa-playbooks` | `requested` | `P2` | Recurring cleanup and degraded-mode choreography |
| `ORQ-QUESTBOOK-PLAYBOOKS-001` | `questbook` | `aoa-playbooks` | `requested` | `P1` | Recurring quest choreography and public obligation routes |
| `ORQ-QUESTBOOK-EVALS-001` | `questbook` | `aoa-evals` | `requested` | `P1` | Proof obligations attached to quest closure |
| `ORQ-QUESTBOOK-MEMO-001` | `questbook` | `aoa-memo` | `requested` | `P2` | Lessons retained after quest completion |
| `ORQ-QUESTBOOK-ROUTING-001` | `questbook` | `aoa-routing` | `requested` | `P2` | Cross-repo obligation handoff and thin route surfaces |
| `ORQ-RPG-AGENTS-001` | `rpg` | `aoa-agents` | `requested` | `P1` | Role, actor, and persona truth behind RPG reflection |
| `ORQ-RPG-SKILLS-001` | `rpg` | `aoa-skills` | `requested` | `P1` | Skill and feat truth behind progression labels |
| `ORQ-RPG-PLAYBOOKS-001` | `rpg` | `aoa-playbooks` | `requested` | `P1` | Campaign, scenario, and questline choreography |
| `ORQ-RPG-EVALS-001` | `rpg` | `aoa-evals` | `requested` | `P1` | Progression proof and evidence-backed advancement |
| `ORQ-RPG-STACK-001` | `rpg` | `abyss-stack` | `requested` | `P3` | Runtime ledger or session-state support after gates |
| `ORQ-RPG-STATS-001` | `rpg` | `aoa-stats` | `requested` | `P2` | Derived progression summaries |
| `ORQ-BRIDGE-TOS-001` | `boundary-bridge` | `Tree-of-Sophia` | `requested` | `P0` | ToS canon, source interpretation, and growth law touched by AoA support |
| `ORQ-BRIDGE-KAG-001` | `boundary-bridge` | `aoa-kag` | `requested` | `P1` | Derived counterpart graph and bridge-ready projections |
| `ORQ-BRIDGE-ROUTING-001` | `boundary-bridge` | `aoa-routing` | `requested` | `P1` | Boundary-aware handoff and bridge route surfaces |
| `ORQ-BRIDGE-MEMO-001` | `boundary-bridge` | `aoa-memo` | `requested` | `P1` | Witness memory, provenance, and compost-facing recall |
| `ORQ-BRIDGE-EVALS-001` | `boundary-bridge` | `aoa-evals` | `requested` | `P1` | Integrity and provenance proof for bridge support |
| `ORQ-BRIDGE-PLAYBOOKS-001` | `boundary-bridge` | `aoa-playbooks` | `requested` | `P2` | Witness, compost, and owner-handoff scenario routes |
| `ORQ-RELEASE-EVALS-001` | `release-support` | `aoa-evals` | `requested` | `P0` | Public claim proof for release and state-transition support posture |
| `ORQ-RELEASE-STATS-001` | `release-support` | `aoa-stats` | `requested` | `P2` | Derived release and transition movement summaries |
| `ORQ-RELEASE-ROUTING-001` | `release-support` | `aoa-routing` | `requested` | `P2` | Release route, transition route, and federation entry ABI updates |
| `ORQ-RELEASE-SDK-001` | `release-support` | `aoa-sdk` | `requested` | `P3` | Compatibility helper support for release and transition consumers |
| `ORQ-RELEASE-PROFILE-001` | `release-support` | `8Dionysus` | `requested` | `P2` | Public projection and profile-route alignment for release and transition claims |

## Mechanic request docs

- `method-growth` -> [OWNER_REQUESTS.md](method-growth/OWNER_REQUESTS.md); owners: `aoa-skills`, `aoa-sdk`, `Dionysus`, `aoa-evals`, `aoa-playbooks`, `aoa-memo`, `aoa-techniques`, `aoa-stats`
- `recurrence` -> [OWNER_REQUESTS.md](recurrence/OWNER_REQUESTS.md); owners: `aoa-sdk`, `aoa-routing`, `aoa-memo`, `aoa-agents`, `aoa-playbooks`, `aoa-evals`, `aoa-stats`, `aoa-kag`, `abyss-stack`
- `checkpoint` -> [OWNER_REQUESTS.md](checkpoint/OWNER_REQUESTS.md); owners: `aoa-sdk`, `aoa-skills`, `aoa-agents`, `aoa-memo`, `aoa-playbooks`, `aoa-evals`, `aoa-routing`, `aoa-stats`, `abyss-stack`, `Dionysus`
- `experience` -> [OWNER_REQUESTS.md](experience/OWNER_REQUESTS.md); owners: `abyss-stack`, `aoa-memo`, `aoa-routing`, `aoa-evals`, `aoa-agents`, `aoa-kag`, `Tree-of-Sophia`, `aoa-playbooks`, `aoa-sdk`, `aoa-stats`, `aoa-skills`, `aoa-techniques`
- `agon` -> [OWNER_REQUESTS.md](agon/OWNER_REQUESTS.md); owners: `aoa-playbooks`, `aoa-evals`, `aoa-memo`, `aoa-stats`, `aoa-routing`, `aoa-agents`, `abyss-stack`, `aoa-kag`, `Tree-of-Sophia`
- `antifragility` -> [OWNER_REQUESTS.md](antifragility/OWNER_REQUESTS.md); owners: `aoa-evals`, `aoa-memo`, `aoa-stats`, `aoa-playbooks`
- `questbook` -> [OWNER_REQUESTS.md](questbook/OWNER_REQUESTS.md); owners: `aoa-playbooks`, `aoa-evals`, `aoa-memo`, `aoa-routing`
- `rpg` -> [OWNER_REQUESTS.md](rpg/OWNER_REQUESTS.md); owners: `aoa-agents`, `aoa-skills`, `aoa-playbooks`, `aoa-evals`, `abyss-stack`, `aoa-stats`
- `boundary-bridge` -> [OWNER_REQUESTS.md](boundary-bridge/OWNER_REQUESTS.md); owners: `Tree-of-Sophia`, `aoa-kag`, `aoa-routing`, `aoa-memo`, `aoa-evals`, `aoa-playbooks`
- `release-support` -> [OWNER_REQUESTS.md](release-support/OWNER_REQUESTS.md); owners: `aoa-evals`, `aoa-stats`, `aoa-routing`, `aoa-sdk`, `8Dionysus`

## Stop-lines

- `requested` is not `accepted`.
- `accepted` is not `landed`.
- `landed` is not proof unless the proof route is satisfied.
- The center may maintain this queue, but only the stronger owner can land its object class.
- Public claims must pass release-support and eval gates before they leave the center.

## Validation

Use the validation lane in [mechanics/AGENTS.md](AGENTS.md#validation) for executable commands.
