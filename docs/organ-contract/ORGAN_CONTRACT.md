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
