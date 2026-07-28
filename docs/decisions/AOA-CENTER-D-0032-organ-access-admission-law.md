# Organ Access Admission Law

- Decision ID: AOA-CENTER-D-0032

## Status

Accepted.

## Index Metadata

- Original date: 2026-07-25
- Surface classes: organ contract, federation boundary, access plane
- Center facets: organ alignment, federation boundary
- Mechanic parents: organ-contract
- Guard families: organ admission, owner boundary, effect isolation
- Posture: accepted constitutional boundary

## Context

OS Abyss already has multiple MCP packages, deployed loopback processes, Codex
registrations, and candidate access planes. Those surfaces grew owner by owner.
Their existence does not answer whether an organ should expose MCP, which
authority the adapter has, whether a consumer may activate it, or which
evidence admits it.

A live baseline on 2026-07-25 found active, suspended, candidate, broken, and
legacy registrations at the same time. It also found shared credentials across
read and effectful tools, incomplete provenance, and large always-loaded
catalogs. Treating package or runtime presence as admission would therefore
merge distinct owner, proof, effect, and freshness states.

The bounded public evidence ledger for that observation is
[`OS_ABYSS_MCP_R1_BASELINE_2026-07-25`](../../mechanics/audit/parts/evidence-ledger/OS_ABYSS_MCP_R1_BASELINE_2026-07-25.md).
It records the inspected owner and runtime surfaces, aggregate observations,
raw-evidence digests, freshness limits, and the stronger proof route without
publishing host-private connection details.

## Options considered

1. Keep admission implicit in each MCP package and consumer configuration.
2. Put all organ access behind one stack gateway and let reachability define
   availability.
3. Define center-level admission and owner-boundary law while leaving typed
   control plane, runtime, proof, and owner payloads with their stronger
   repositories.

## Decision

Choose option 3.

An organ is not required to have MCP. The owner first chooses the narrowest
appropriate access form, including no separate access plane.

For an access plane, source, access, control-plane, runtime, proof, and
acceptance roles remain explicit. Adapter or registry presence grants none of
the stronger roles. Admission is deny-by-default and uses the states
`declared`, `package_candidate`, `deploy_candidate`, `shadow`, `admitted`,
`suspended`, `deprecated`, and `retired`.

Capabilities are admitted independently under `read`, `candidate`,
`internal_effect`, or `external_effect` policy families. Read admission never
implies effect admission. Candidate output never becomes durable truth without
the acceptance owner. Runtime effects never accept source truth. External
effects require an exact target and explicit human approval.

The target owner split is:

| Surface | Owner |
|---|---|
| constitutional organ and admission law | `Agents-of-Abyss` |
| typed registry, discovery, compatibility, and activation-plan projection | `aoa-sdk` |
| deploy, process, endpoint, lifecycle, and rollback | `abyss-stack` |
| stack-owned agent runtime observation | `abyss-stack-mcp` |
| owner-specific capability and payload meaning | source owner |
| bounded proof and verdict meaning | `aoa-evals` or a named stronger proof owner |
| durable source, memory, runtime, or external acceptance | named acceptance owner |
| derived maturity and measurements | `aoa-stats`, below owner evidence |

The transitional topology keeps direct per-owner connections and the stable
MCP protocol line. `aoa-sdk` may add discovery and compile activation plans but
does not silently activate servers or proxy owner tools. The transitional
`aoa-routing` authority clause was satisfied and narrowly superseded by
[`AOA-CENTER-D-0035`](AOA-CENTER-D-0035-admit-routing-owner-switch.md):
`aoa-sdk` is now the receipt-bound routing/control-plane owner, while the
predecessor remains maintenance-only and reversible. The target architecture
creates no separate long-lived `aoa-routing-mcp`.

Every admitted route must carry traceable source, package, deploy, process,
endpoint, registry, consumer-schema, canary, and acceptance evidence. A missing
critical link keeps the route in `shadow`, `suspended`, or blocked posture.

Rollback lowers admission first, removes or denies consumer activation, and
then rolls runtime or protocol state back through the runtime owner. It does
not delete source records or compatibility surfaces until consumer-zero is
proven. Protocol migration and authority migration remain separate changes.

## Rationale

Center law can define what a reviewable organ must make explicit without
becoming the registry, runtime, proof layer, memory owner, or workflow engine.
This split preserves direct owner access, permits progressive discovery, and
lets future protocols change without moving domain authority.

It also turns absence of MCP into a valid reviewed result instead of forcing
symmetry across repositories whose useful access route is a skill, CLI, SDK
API, KAG projection, or no plane.

## Consequences

- Admission can be validated independently from package and process health.
- Effectful capabilities need their own policy and acceptance evidence.
- Registry projections must cite owner and runtime evidence instead of
  inventing a top-level truth.
- Direct owner endpoints remain possible; a mega-gateway is not the target.
- Transitional duplicated surfaces may remain until consumer-zero and rollback
  proof exist.
- Cross-repository implementation and proof are required before any current
  shadow route can become admitted.

## Source surfaces

- `docs/organ-contract/ORGAN_CONTRACT.md`
- `docs/organ-contract/README.md`
- `mechanics/audit/parts/evidence-ledger/OS_ABYSS_MCP_R1_BASELINE_2026-07-25.md`

## Follow-up route

`aoa-sdk` should own the typed private-registry, discovery, compatibility, and
activation-plan contracts. `abyss-stack` should own runtime identity,
`abyss-stack-mcp`, effect enforcement, deployment receipts, and rollback.
`aoa-evals` should own central bounded admission proof. Each organ owner should
accept its capability and payload contract before admission.
