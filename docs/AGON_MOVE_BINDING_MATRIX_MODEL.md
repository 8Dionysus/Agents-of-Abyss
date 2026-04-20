# Agon Move Binding Matrix Model

## Purpose

The binding matrix is the compact map from lawful move to owner obligations.

It answers four questions:

1. Which legal move is being bound?
2. Which owners are required later?
3. Which candidate surfaces are requested but not landed?
4. Which powers are explicitly not granted?

## Binding status

All Wave IV bindings use:

```text
binding_status: seeded_pre_protocol_owner_binding
readiness: owner_binding_seeded
live_protocol: false
runtime_effect: none
```

This means the binding is legible but not executable.

## Owner slots

Initial owner slots are:

```text
Agents-of-Abyss     center_law_owner
aoa-techniques      practice_owner
aoa-skills          bounded_workflow_owner
aoa-evals           proof_owner
aoa-routing         gate_route_owner
aoa-playbooks       scenario_choreography_owner
aoa-memo            durable_memory_owner
aoa-stats           derived_observability_owner
aoa-agents          actor_form_owner
```

Each binding must include `Agents-of-Abyss` as center law owner.

A move may include one or more additional owners depending on the future work it requires.

## Candidate refs

Candidate refs are intentionally not landed objects.

Examples:

```text
candidate:aoa-techniques:agon/probe-trace-practice
candidate:aoa-skills:agon/probe-trace-workflow
candidate:aoa-evals:agon/probe-trace-check
```

They are routeable names for future owner review, not promoted techniques, not promoted skills, and not eval verdicts.

## Assistant boundary

A move binding may allow assistant service support only for service-compatible acts.

Assistants may support:

```text
clarity
receipt
reference packaging
trace visibility
scope flags
escalation
handoff
```

Assistants must not gain:

```text
contestant authority
judge authority
closer authority
summon initiator authority
scar writer authority
ToS promotion authority
```

## One-line rule

The matrix binds future responsibility without stealing future authority.
