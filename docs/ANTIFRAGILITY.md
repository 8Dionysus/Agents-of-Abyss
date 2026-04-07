# ANTIFRAGILITY

## Why this doctrine exists

AoA already values explicit boundaries, reviewable workflows, portable proof, and source-first meaning.

This document adds one stronger requirement:

**stress should make the system more legible, more bounded, and more teachable.**

If a failure only hurts, or only gets patched locally without leaving reusable evidence, the federation may be resilient, but it is not yet antifragile.

## Working definition

Within AoA, antifragility means that a stress event leads to all of the following:

1. damage is bounded to the owning surface or a clearly named seam
2. the event leaves machine-readable source-owned evidence
3. the system continues in a valid degraded mode or cleanly stops before unsafe widening
4. a later change can cite the stress event and verify that the next similar event is handled better

This definition is stronger than uptime and weaker than fantasy. It does not promise zero failure. It requires failures to become usable structure.

## Core federation invariants

### 1. Source ownership remains explicit

Source repos keep ownership of what happened and what it means.

- owner repos publish source-owned receipts and local interpretations
- `aoa-evals` owns bounded proof surfaces
- `aoa-stats` owns derived views
- `aoa-routing` owns navigation
- `aoa-memo` owns explicit memory and recall, but memory is not proof

Antifragility must not blur these lines.

### 2. Mutating surfaces need an antifragility posture

Any surface that can mutate state, widen authority, or influence future actions should have:

- a degraded-mode posture
- an evidence contract
- an adaptation path

The exact implementation differs by layer. The requirement does not.

### 3. Degraded continuation must remain valid

A degraded mode is acceptable only when it stays:

- bounded
- reviewable
- machine-readable
- weaker than the normal mode, not secretly broader

### 4. Evidence comes before mythology

Failure analysis should prefer receipts, traces, bounded artifacts, and explicit blind spots over anecdote and retrospective confidence.

### 5. Antifragility is a vector, not a throne score

The federation should avoid collapsing antifragility into one sovereign number.

Useful axes include:

- containment
- reversibility
- fallback fidelity
- recovery latency
- evidence density
- adaptation gain
- operator burden
- trust calibration

Not every repo needs every axis, but the split matters.

## Layer posture

### Center
`Agents-of-Abyss` owns the doctrine, federation wording, and layer-level invariants.

### Practice
`aoa-techniques` owns portable practice such as degrade/reground/recover and receipt-first failure analysis.

### Execution
`aoa-skills` owns bounded execution meaning and should make fallback trees and receipt contracts explicit where relevant.

### Proof
`aoa-evals` owns reproducible bounded proof surfaces for antifragility claims.

### Derived view
`aoa-stats` derives vector surfaces from source receipts and eval outputs without becoming an authority layer.

### Concrete owner repos
Concrete repos such as `ATM10-Agent`, `abyss-stack`, `aoa-routing`, or `aoa-memo` emit local receipts and owner-local semantics.

## Anti-patterns

The following patterns violate this doctrine:

- centralizing source-owned meaning in `aoa-stats`
- widening automation in the name of recovery
- silently swallowing failures and pretending normality
- replacing split evidence with one prestige score
- using memory as proof
- publishing a repair story without source-owned evidence

## Promotion rule

Wave 1 should prefer local ownership for concrete contracts unless a shared contract already exists cleanly.

A contract is ready for broader promotion only when:

1. at least two owner repos use near-identical semantics
2. the boundary of ownership stays clear after promotion
3. the promotion reduces duplication without creating authority drift

## Short test

A change strengthens AoA antifragility only if a future reviewer can answer:

- where was the stress bounded
- what source-owned evidence was emitted
- what degraded mode or stop condition was used
- what explicit later change cited this event
- how do we know the next similar event is handled better
