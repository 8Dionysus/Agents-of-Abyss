# Organ Contract

This contract defines the minimum shape of a repository that can participate in
AbyssOS as a reviewable organ.

It is center law. It does not accept owner-local implementation, activate
runtime behavior, or replace repository-local `AGENTS.md` cards.

## Organ identity

Every organ should be able to answer:

- what object class it owns
- which stronger owner routes protect neighboring object classes
- which public claims it can support
- which validation route proves its local surface
- which handoff route carries work beyond its boundary

The answer may be compact. The contract cares that the organ is legible, not
that every repository shares the same internal tree.

## Required route surfaces

An organ is reviewable when these surfaces or owner-equivalent routes exist:

| Surface | Function |
|---|---|
| `README.md` | public or internal entry orientation |
| `AGENTS.md` | agent-facing local law and verification route |
| `CHANGELOG.md` or release surface | release-visible history when the organ publishes releases |
| direction surface | current direction, future triggers, and owner pressure |
| decision record route | durable rationale for structural, workflow, public-contract, or ownership choices |
| validation route | local commands or proof path for the organ's claims |
| handoff route | where work goes when the organ reaches its owner boundary |

An organ can satisfy a surface through a local file, a stronger owner route, or
a documented reason that the surface is not part of that organ's current
function.

## Owner boundary

The center asks each organ to keep four statements inspectable:

1. `owns`: the primary object class the organ may author.
2. `routes`: neighboring object classes the organ may point to.
3. `receives`: inputs the organ can accept without changing owner truth.
4. `hands off`: outputs that require another owner before they become
   operational, public, or runtime truth.

These statements should be short enough for an agent to read before mutation.

## Local mechanics posture

Mechanics may appear inside many repositories with local meaning. The center
only asks an organ to name which mechanics are active, optional, deferred, or
not part of its current function.

AoA owns the shared mechanic law. Each repository owns its local use of that
law.

## Organ access posture

An organ is not required to expose MCP. The owner must first choose whether its
bounded access route is an MCP adapter, an SDK API, a CLI, a resource
projection, a skill, a KAG or stats projection, or no separate access plane.
Repository, package, process, listener, registration, and successful call
presence are observations, not admission.

When an organ does expose an agent access plane, keep these roles distinct:

| Role | Owns |
|---|---|
| source owner | domain meaning and canonical data |
| access owner | adapter contract and owner-specific payload |
| control-plane owner | typed registry, discovery, and activation-plan projection |
| runtime owner | package, deploy, process, endpoint, lifecycle, and rollback evidence |
| proof owner | bounded evaluation and verdict meaning |
| acceptance owner | durable source, memory, runtime, or external-effect acceptance |

One repository may fill more than one role only when its local law says so.
An access adapter never acquires source, proof, or acceptance authority merely
because it can read or invoke the stronger owner.

Admission is deny-by-default and progresses through explicit states:
`declared`, `package_candidate`, `deploy_candidate`, `shadow`, `admitted`,
`suspended`, `deprecated`, and `retired`. An admitted capability also names its
effect family: `read`, `candidate`, `internal_effect`, or `external_effect`.
Higher-effect admission never follows automatically from lower-effect
admission.

An `external_effect` capability must name the exact target and bounded
operation. Execution requires explicit human approval scoped to that target and
operation, with an expiry that the enforcing server checks. Caller
authentication, tool annotations, a prepared plan, a previous approval, or
model intent cannot substitute for that approval. A missing, mismatched, or
expired approval denies the effect.

The control-plane registry is a traceable projection of owner records, runtime
observations, proof evidence, and acceptance receipts. It may decide whether a
consumer is allowed to discover or activate a route; it must not author domain
truth, infer proof, accept durable memory, or merge owners behind a semantic
gateway. Direct owner connections remain valid when policy permits them.

Every admitted route must make the evidence chain required by its selected
access form inspectable:

```text
reviewed source
  -> selected access artifact or owner-equivalent invocation route
  -> access-form-specific availability evidence
  -> registry observation when the route is registry-managed
  -> consumer-observed contract or artifact identity
  -> grounded canary
  -> owner acceptance
```

For a service-backed MCP route, the selected artifact and availability links
expand to package, deployed artifact, process, and endpoint evidence. For an SDK
library, CLI, skill, static resource, or KAG projection, owner-equivalent
package or artifact identity plus an invocation or retrieval check replaces
process and endpoint evidence. A route is not required to invent service
evidence for an access form that has no service.

Missing links required by the selected access form remain `shadow`,
`suspended`, or blocked; a general `healthy` label must not conceal them.

## Rollback posture

Rollback lowers or suspends admission first, then removes or denies new
consumer activation, and only then rolls runtime or protocol state back through
the named owner. Source records and compatibility surfaces remain available
until consumer-zero is proven.

Protocol rollback and authority rollback are separate changes. A protocol
adapter may return to a prior compatible line without reversing an owner
handoff, while a failed authority migration must restore the prior owner route
without using protocol reachability as acceptance evidence. Every route names
which rollback applies, the owner that executes it, and the evidence that
closes it.

## Handoff posture

When a change crosses an owner boundary, the handoff should name:

- source organ
- target owner
- changed surface
- claim being carried
- validation already run
- validation still needed by the target owner
- rollback or re-entry route when the target owner does not accept it

This is enough for a future `aoa-sdk` or `aoa-routing` tool to consume later
while this district stays center law.

## Completion check

A repo-organ alignment is complete when:

- the organ's identity and owner boundary are readable before implementation
- required route surfaces are present or intentionally routed
- generated, trace, legacy, runtime, public, projection, receipt, and cache
  surfaces keep their state labels clear
- the first cycle can be followed without skipping proof or record surfaces
- handoff routes point to stronger owners before acceptance is claimed
- any agent access plane has explicit source, access, control-plane, runtime,
  proof, and acceptance owners
- admission, effect family, freshness, provenance, and rollback posture are
  visible without treating access-plane metadata as owner truth
