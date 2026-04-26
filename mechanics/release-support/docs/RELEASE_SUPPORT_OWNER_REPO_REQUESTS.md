# Release support Owner-repo Requests

This is the center-side request packet list for `release-support`.

It names the stronger owner slices that must land outside `Agents-of-Abyss` before `release-support` may be treated as operational beyond center doctrine, routes, and stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance. It may be copied into an owner-local issue, document, branch, or receipt, but it remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../../../mechanics/owner-request-queue.json)

Generated companion: [`generated/owner_request_queue.min.json`](../../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-RELEASE-EVALS-001` | `aoa-evals` | `requested` | `P0` | Public claim proof for release and support posture | Eval surface for release claims, quality claims, regressions, and supportable-public-claim boundaries. | Proof lives in `aoa-evals`. |
| `ORQ-RELEASE-STATS-001` | `aoa-stats` | `requested` | `P2` | Derived release movement summaries | Derived windows over owner-local release receipts and bounded eval outputs. | Stats claims cite source release and proof receipts. |
| `ORQ-RELEASE-ROUTING-001` | `aoa-routing` | `requested` | `P2` | Release route and federation entry ABI updates | Routing update that directs humans and agents to current release/support surfaces. | Route correctness may be evaluated by `aoa-evals`. |
| `ORQ-RELEASE-SDK-001` | `aoa-sdk` | `requested` | `P3` | Compatibility helper support for release consumers | Typed helper or compatibility seam for loading release-adjacent generated surfaces without owning meaning. | Compatibility claims route to `aoa-evals`. |
| `ORQ-RELEASE-PROFILE-001` | `8Dionysus` | `requested` | `P2` | Public projection and profile-route alignment | Profile or projection surface updated only after center support and owner evidence are aligned. | Public projection claims must cite center and owner evidence. |

## Center sources

- [README.md](../../../mechanics/release-support/README.md)
- [PUBLIC_SUPPORT_POSTURE.md](../../../mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md)
- [FEDERATION_RELEASE_PROTOCOL.md](../../../mechanics/release-support/docs/FEDERATION_RELEASE_PROTOCOL.md)
- [DIRECTION_SURFACES.md](../../../mechanics/release-support/docs/DIRECTION_SURFACES.md)

## Stop-lines

- `ORQ-RELEASE-EVALS-001`: The center must not publish unverified public claims.
- `ORQ-RELEASE-STATS-001`: Stats must not become release truth.
- `ORQ-RELEASE-ROUTING-001`: Routing must not author release truth.
- `ORQ-RELEASE-SDK-001`: SDK support must not become release authority.
- `ORQ-RELEASE-PROFILE-001`: Profile surfaces must not outrun the center or sibling owners.

## Validation

Use the validation lane in [mechanics/release-support/docs/AGENTS.md](AGENTS.md#validation) for executable commands.

## Next route

Carry the request ID into the owner repository. Do not promote center language to owner-local truth without owner acceptance, owner landing, and proof where proof is required.
