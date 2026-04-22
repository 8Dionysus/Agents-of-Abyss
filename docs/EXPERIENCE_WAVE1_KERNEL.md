# Experience Wave 1 Kernel

## Purpose

The first experience wave gives AoA a bounded grammar for turning lived
operator friction into reviewable growth candidates.

It plants the mechanics from the `aoa-experience-*` seed line through v0.3:

1. observe friction
2. prove recurrence
3. declare a candidate
4. record a verdict
5. pass through a memory gate
6. route to the owning repository
7. propose projection only as an owner-local follow-through

This is a kernel for experience capture, not a runtime queue. It names the
flow that later owner repositories can implement, summarize, remember, route,
or rehearse without letting any derived layer become the source of truth.

## Center Ownership

`Agents-of-Abyss` owns the Wave 1 vocabulary and stop-lines:

- the required flow order
- the difference between friction, recurrence, candidate, verdict, memory gate,
  owner route, and projection
- the rule that a projection is never valid before review
- the rule that owner landing truth stays in the owner repository

The center does not own repo-local execution, durable memory writes, derived
stats, pilot choreography, route dispatch, SDK runtime control, or deployment.

## Flow Terms

`friction` is a witnessed operator or agent difficulty that has not yet earned
durable meaning.

`recurrence` is evidence that the friction repeats across more than one
bounded situation.

`candidate` is a reviewable object that states the improvement opportunity,
its evidence, and its intended owner.

`verdict` is the reviewed decision that either accepts the candidate for owner
landing, rejects it, defers it, or asks for revision.

`memory_gate` decides whether any durable recall object may be requested.
Passing this gate does not write memory by itself.

`owner_route` names the first repository that can honestly land the follow-up.
Derived or supporting repositories may receive references, but they cannot
overrule the owner.

`projection` is an owner-local implementation proposal. It remains inert until
the target owner accepts it under that repository's own validation.

## Required Order

The Wave 1 flow is valid only in this order:

```text
friction_observed
recurrence_detected
candidate_declared
review_verdict_recorded
memory_gate_decided
owner_route_selected
projection_proposed
```

An implementation may add local subevents, but it must preserve the ordered
spine above and keep every step reviewable.

## Owner Split

First-wave owner routing should stay narrow:

- `Agents-of-Abyss` owns the center grammar and authority boundaries.
- `Dionysus` owns seed lineage, prep-pack routing, and planting trace.
- `aoa-stats` owns derived summaries only.
- `aoa-playbooks` owns pilot choreography only when a route is explicitly
  accepted there.
- `aoa-evals` owns proof bundles and verdict checks.
- `aoa-memo` owns durable recall only after an explicit memory gate.
- `aoa-routing` owns navigation hints and dispatch posture, not truth.
- `aoa-agents` owns role posture and handoff expectations.
- `aoa-sdk` owns typed control-plane references, not experience authority.
- `abyss-stack` owns infrastructure capture and transport posture only after a
  runtime owner accepts the slice.

## Stop-Lines

Wave 1 must not create:

- hidden runtime execution
- automatic projection
- durable memory writes without a memory gate
- stats authority over owner truth
- routing authority over owner review
- SDK-local verdicts
- deployment or certification claims
- governance, constitution, release, or live-office authority

Those belong to later waves and owner repositories.

## Validation

The center validation surface is:

```bash
python scripts/validate_experience_wave1.py
python -m pytest -q tests/test_experience_wave1.py
```

The structural artifact is
`examples/experience_wave1_flow.example.json`, checked against
`schemas/experience-wave1-flow.schema.json`.
