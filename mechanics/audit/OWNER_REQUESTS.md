# Audit Owner Requests

## Owner request packet

Audit owner requests carry center-visible review pressure into repositories that own stronger truth. A request packet is not owner acceptance.

## Requests

| ID | Owner | Slice | Priority | Status |
|---|---|---|---|---|
| `ORQ-AUDIT-EVALS-001` | `aoa-evals` | proof-strength route for audit findings | `P1` | `requested` |
| `ORQ-AUDIT-MEMO-001` | `aoa-memo` | durable evidence and memory writeback route | `P2` | `requested` |
| `ORQ-AUDIT-PLAYBOOKS-001` | `aoa-playbooks` | recurring audit campaign choreography | `P2` | `requested` |
| `ORQ-AUDIT-SKILLS-001` | `aoa-skills` | executable audit workflow skill shape | `P2` | `requested` |
| `ORQ-AUDIT-AGENTS-001` | `aoa-agents` | audit-facing role and handoff posture | `P3` | `requested` |
| `ORQ-AUDIT-STATS-001` | `aoa-stats` | derived audit movement summaries | `P3` | `requested` |

## Center sources

- `mechanics/audit/README.md`
- `mechanics/audit/DIRECTION.md`
- `mechanics/audit/PARTS.md`
- `mechanics/audit/OWNER_MAP.md`
- `mechanics/audit/OWNER_REQUESTS.md`
- `mechanics/audit/docs/AUDIT_LAW.md`

## Stop-lines

- The center must not claim owner acceptance before the owner lands a receipt.
- The center must not claim proof verdicts, memory truth, recurring choreography, executable skill truth, role activation, or derived-summary authority.
- The center must not use generated audit summaries as source-authored meaning.

## Validation

Use the validation lane in [mechanics/audit/AGENTS.md](AGENTS.md#validation).

## Next route

When a request is ready, copy or reference the relevant request ID in the owner repository and keep the center queue at `requested` until the owner surface records acceptance or landing.
