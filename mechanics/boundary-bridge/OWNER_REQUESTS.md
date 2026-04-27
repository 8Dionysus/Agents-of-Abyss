# Boundary Bridge Owner Requests

This is the center-side request packet list for `boundary-bridge`.

It names the stronger owner slices that must land outside `Agents-of-Abyss`
before a bridge may be treated as operational beyond center doctrine, routes,
and stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance.
It may be copied into an owner-local issue, document, branch, or receipt, but
it remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../owner-request-queue.json)

Generated companion:
[`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-BRIDGE-TOS-001` | `Tree-of-Sophia` | `requested` | `P0` | ToS canon, source interpretation, and growth law touched by AoA support | ToS-owned source or concept node decision, growth-law acceptance, or canon receipt. | AoA support can be evaluated, but ToS acceptance is source authority. |
| `ORQ-BRIDGE-KAG-001` | `aoa-kag` | `requested` | `P1` | Derived counterpart graph and bridge-ready projections | Provenance-aware derived graph/readiness surfaces pointing back to ToS and AoA sources. | Derived-readiness proof routes to `aoa-evals`. |
| `ORQ-BRIDGE-ROUTING-001` | `aoa-routing` | `requested` | `P1` | Boundary-aware handoff and bridge route surfaces | Thin dispatch surface from AoA routes into owner-owned seams without semantic override. | Route behavior proof routes to `aoa-evals` when needed. |
| `ORQ-BRIDGE-MEMO-001` | `aoa-memo` | `requested` | `P1` | Witness memory, provenance, and compost-facing recall | Witness memory objects with provenance, retention, forgetting, and recall posture. | Witness integrity routes to `aoa-evals`. |
| `ORQ-BRIDGE-EVALS-001` | `aoa-evals` | `requested` | `P1` | Integrity and provenance proof for bridge support | Eval surface for source linkage, provenance, bridge reversibility, and non-authoring discipline. | Proof lives in `aoa-evals`. |
| `ORQ-BRIDGE-PLAYBOOKS-001` | `aoa-playbooks` | `requested` | `P2` | Witness, compost, and owner-handoff scenario routes | Playbook route for witness intake, compost cycle, handoff, review, and closure. | Scenario proof routes to `aoa-evals`. |

## Center sources

- [README.md](README.md)
- [PARTS.md](PARTS.md)
- [OWNER_MAP.md](OWNER_MAP.md)
- [PROVENANCE.md](PROVENANCE.md)
- [COUNTERPART_BRIDGE.md](docs/COUNTERPART_BRIDGE.md)
- [WITNESS_COMPOST.md](docs/WITNESS_COMPOST.md)
- [TOS_GROWTH_SUPPORT.md](docs/TOS_GROWTH_SUPPORT.md)

## Stop-lines

- `ORQ-BRIDGE-TOS-001`: AoA must not author ToS meaning.
- `ORQ-BRIDGE-KAG-001`: KAG projections must not become source canon.
- `ORQ-BRIDGE-ROUTING-001`: Routing must not become owner authority.
- `ORQ-BRIDGE-MEMO-001`: Witness memory must not rewrite source meaning.
- `ORQ-BRIDGE-EVALS-001`: The center must not treat bridge posture as proof
  unless evidence lands.
- `ORQ-BRIDGE-PLAYBOOKS-001`: Scenario support must not become source canon.

## Validation

Use the validation lane in [AGENTS.md](AGENTS.md#validation).

## Next route

Carry the request ID into the owner repository. Do not promote center language
to owner-local truth without owner acceptance, owner landing, and proof where
proof is required.
