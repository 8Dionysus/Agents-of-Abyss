# Admit The Routing Owner Switch

- Decision ID: AOA-CENTER-D-0035

## Status

Accepted.

## Index Metadata

- Original date: 2026-07-27
- Surface classes: organ contract, federation route, repository role
- Center facets: organ alignment, owner descent
- Mechanic parents: boundary-bridge
- Guard families: owner succession, receipt admission, archive stop line
- Posture: accepted owner-switch admission

## Context

Decision `AOA-CENTER-D-0032` kept `aoa-routing` as the transitional routing
authority until an already-governed owner-switch receipt existed. The owner
switch has now landed in `aoa-sdk` at
`7fba39d38cf5902c41dfbb7ae91f405b849880b7`.

The SDK decision `AOA-SDK-D-0076` and its G5 receipt bind the canonical
producer switch to the preserved routing ABI, exact predecessor and runtime
contracts, and receipt digest
`sha256:d2b9272dacd1cd04d3bf200c4e9b8c7bce301c1b0a2bcb36e0c8a16064ea6645`.
The same evidence keeps runtime execution, consumer-zero, compatibility exit,
and repository archive as separate gates.

The center needs to admit that exact owner change without turning a landed SDK
commit into broader proof or silently authorizing irreversible repository
action.

## Options considered

1. Keep the transitional `aoa-routing` authority clause until consumer-zero
   and archive readiness are also complete.
2. Treat the SDK landing as evidence that owner switch, runtime cutover,
   consumer-zero, and archive authorization all completed together.
3. Admit the exact receipt-bound producer switch while preserving runtime,
   proof, compatibility, consumer-zero, and archive boundaries.

## Decision

Choose option 3.

`aoa-sdk` is the canonical routing producer and routing/control-plane owner.
New routing producer, dispatch, compatibility, and typed control-plane work
routes there.

`aoa-routing` is the maintenance-only predecessor retained for compatibility,
security, rollback, and deprecation support. It is not an active feature owner.
Its repository remains unarchived: the admitted G5 evidence explicitly records
`archive_authorized=false`, and a later archive still requires proven
consumer-zero, compatibility exit, and separate exact operator approval.

The owner switch does not move source-organ semantics into the SDK, does not
grant runtime execution authority, and does not turn execution outcome into a
proof verdict. Source owners retain authored meaning, `abyss-stack` retains
runtime execution, and proof and memory remain with their named owners.

This decision supersedes only the transitional routing-authority sentence in
`AOA-CENTER-D-0032`. The organ-access admission law, effect boundaries,
evidence chain, rollback ordering, and protocol/authority separation in that
decision remain active.

## Rationale

- The exact G5 receipt satisfies the condition named by the transitional
  center clause without widening what that clause can prove.
- Admitting one canonical producer removes ambiguous routing ownership while
  retaining a precise rollback source.
- Keeping runtime, proof, consumer-zero, and archive gates separate prevents a
  repository landing from being mistaken for live execution or irreversible
  lifecycle authority.
- Linking the center posture to immutable SDK evidence makes the owner route
  auditable without copying SDK implementation truth into the center.

## Consequences

- Center route maps and future owner requests point routing/control-plane work
  to `aoa-sdk`.
- `aoa-routing` accepts only compatibility, security, rollback, and deprecation
  maintenance during the compatibility window.
- Active consumers and public projections must migrate to SDK-produced routing
  surfaces before consumer-zero can be claimed.
- Runtime cutover and live health remain independently evidenced by their
  runtime owner.
- Repository archive remains forbidden without its later evidence and exact
  operator approval.

## Source surfaces

- [`AOA-SDK-D-0076`](https://github.com/8Dionysus/aoa-sdk/blob/7fba39d38cf5902c41dfbb7ae91f405b849880b7/docs/decisions/AOA-SDK-D-0076-authorize-receipt-bound-routing-g5-owner-switch.md)
- [`routing-succession-g5-owner-switch`](https://github.com/8Dionysus/aoa-sdk/blob/7fba39d38cf5902c41dfbb7ae91f405b849880b7/mechanics/boundary-bridge/parts/consumed-surface-posture-gate/docs/routing-succession-g5-owner-switch.md)
- [`canonical-routing-source-lock.v1.json`](https://github.com/8Dionysus/aoa-sdk/blob/7fba39d38cf5902c41dfbb7ae91f405b849880b7/src/aoa_sdk/control_plane/routing/data/canonical-routing-source-lock.v1.json)
- `docs/decisions/AOA-CENTER-D-0032-organ-access-admission-law.md`
- `ROADMAP.md`

## Follow-up route

Migrate every active consumer and public projection to the SDK-produced
routing surface, retain the predecessor as a reversible maintenance surface
during the compatibility window, and measure consumer-zero independently.
Revisit repository archive only after that evidence exists and the operator
approves the exact irreversible action.
