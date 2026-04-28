# Owner Request Protocol

The owner-request protocol is the center-side handshake between a mechanic card and the repository that owns operational truth.

Mechanic cards answer **what kind of move is this?** The owner-request queue answers **which owner-local landing must exist before this move may be called operational?**

The center may write request packets, stop-lines, source references, and route hints. The center may not accept the request on behalf of the owner repository, land owner-local truth, write memory, issue verdicts, mutate roles, run runtime, or author Tree-of-Sophia meaning.

This file owns request grammar and vocabulary. The current human index lives in
[`OWNER_REQUEST_QUEUE.md`](OWNER_REQUEST_QUEUE.md); the source data lives in
[`owner-request-queue.json`](owner-request-queue.json).

## Request anatomy

Every request in [`mechanics/owner-request-queue.json`](owner-request-queue.json) must contain:

| Field | Meaning |
|---|---|
| `id` | stable queue identifier used by docs, tests, and owner-local packets |
| `mechanic` | mechanic slug from `mechanics/registry.json` |
| `owner_repo` | repository or adjacent anchor that owns the landing |
| `owner_role` | compact owner role, copied from federation ownership posture |
| `queue_status` | current center-side queue status |
| `priority` | urgency class, not authority class |
| `slice` | narrow owner-local slice requested |
| `center_status` | center mechanic status at request time |
| `center_sources` | center-owned surfaces that explain the request |
| `required_owner_landing` | what the owner must land before activation can be claimed |
| `proof_route` | where defensible proof, verdict, regression, or public claim evidence goes |
| `handoff_surface_hint` | non-binding hint for owner-local issue/doc/receipt placement |
| `stop_line` | claim the center must not make without owner landing |
| `next_action` | safe next step for an agent |

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

## Priority vocabulary

| Priority | Meaning |
|---|---|
| `P0` | Unlocks a claimed stop-line or prevents the center from overclaiming operational truth. |
| `P1` | Strong owner-local landing needed for the mechanic to become useful beyond center doctrine. |
| `P2` | Important cross-owner support or evidence route, but not currently blocking the mechanic card. |
| `P3` | Deferred improvement or optional compatibility refinement. |

## Advancement rules

1. `queued` may become `requested` when a complete center-side packet exists.
2. `requested` may become `accepted` only when the owner repository creates an owner-local acceptance receipt.
3. `accepted` may become `landed` only when the owner repository lands the surface and links proof, receipt, or both.
4. `blocked`, `superseded`, and `retired` must include enough context in `next_action`, `owner_landing_ref`, or `owner_proof_ref` to avoid ghost work.
5. A center mechanic status must not become `operational` merely because a request is `requested`.

## How agents use the protocol

1. Read the mechanic card.
2. Open [`OWNER_REQUEST_QUEUE.md`](OWNER_REQUEST_QUEUE.md) or the package-local owner request document.
3. Choose the request whose owner and slice match the work.
4. Copy the request ID into the owner-local issue, branch, document, or receipt.
5. Keep the center status honest until the owner repository accepts and lands the request.
6. Rebuild the generated queue after changes.

## Stop-lines

- A request packet is not owner acceptance.
- A generated queue is not a source of truth.
- A request status is not proof.
- Runtime, memory, role, verdict, rank, playbook, KAG, SDK, public projection, and ToS meaning remain owner-local.
- The center grows by making ownership clearer, not by absorbing the work.

## Validation

Use the validation lane in [mechanics/AGENTS.md](AGENTS.md#validation) for executable commands.
