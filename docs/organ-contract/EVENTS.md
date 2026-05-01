# System Events

System events are names for moves that recur across AbyssOS organs.

They help agents choose the right surface without making every repository share
the same implementation.

## Event vocabulary

| Event | Happens when | Usual route |
|---|---|---|
| `landing` | a source-backed change becomes the current local surface | release-support, changelog, landing log, or owner receipt |
| `distillation` | raw or legacy material becomes active, compact, and routed | distillation mechanic plus owner provenance |
| `audit` | evidence is inspected before changing or trusting a claim | audit mechanic |
| `checkpoint` | an intermediate reviewed state should survive the current cycle | checkpoint mechanic or owner-local checkpoint route |
| `decision` | future agents need the rationale for a durable route choice | `docs/decisions/` or owner decision records |
| `quest` | an obligation should survive as a public, reviewable work object | Questbook |
| `release` | a public or internal state transition is published | release-support and `CHANGELOG.md` |
| `rollback` | a landed or proposed state must return to a safer anchor | release-support, recurrence, or owner rollback route |
| `handoff` | work crosses from one owner to another | owner request, handoff packet, or target owner route |
| `reanchor` | work returns to a stronger source after drift or ambiguity | recurrence, boundary bridge, or source owner |
| `harvest` | repeated reviewed evidence becomes reusable growth material | growth-cycle, method-growth, or owner-local harvest route |
| `owner-request` | the center asks a stronger owner to accept a slice | mechanics owner request queue or target owner issue/route |

## Event rule

Name the event only when it clarifies the route. The event name should point to
the owner surface that can carry it.

## Cross-organ use

Different repositories may implement these events differently. AoA owns the
shared vocabulary; each organ owns the local acceptance and proof route.
