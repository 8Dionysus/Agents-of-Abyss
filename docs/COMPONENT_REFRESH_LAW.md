# Component Refresh Law

This note defines how AoA treats refresh and self-maintenance work for internal
components without inventing hidden autonomy.

## Purpose

A component in this doctrine is a bounded internal technical surface with:

- source-authored inputs
- generated and/or projected outputs
- visible drift or staleness signals
- one owner repository that can refresh it honestly

AoA already has reviewable growth refinery, candidate lineage, owner landing,
rollout cadence, and self-agency continuity.
Those routes make growth legible.
They do not by themselves explain how the system should respond when one of its
own internal technical surfaces begins to drift.

This note names that missing law.

## Governing chain

```text
owner refresh law
  -> control-plane drift hint
  -> reviewed refresh decision
  -> owner refresh receipt
  -> derived refresh summary
  -> optional bounded memory
```

## Real-run first

Prefer signals that arise from real work:

- repeated manual patching
- validation drift
- deploy doctor failures
- stale generated surfaces
- rollout or continuity windows blocked by one named component
- summary families lagging or disagreeing

Use fixtures to prove the contract.
Do not confuse fixtures with the primary source of maintenance truth.

## Boundary split

Owner repos own:

- the component refresh law
- source-authored inputs
- generated output meaning
- proof commands
- rollback anchors
- refresh receipts

`aoa-sdk` may own:

- hint carry
- reviewed follow-through carry
- typed route suggestions

`aoa-stats` may own derived refresh visibility.
`aoa-playbooks` may own recurring coordination routes.
`aoa-memo` may own bounded lessons and recovery patterns.

The center may name this law and its stop-lines.
It does not become the owner of the drifting component.

## Negative rules

Do not:

- let `aoa-sdk` auto-regenerate owner surfaces
- let `aoa-stats` overrule owner validation
- let `aoa-playbooks` narrate scheduler authority
- let memory become the first refresh truth
- hide refresh drift behind mystical "self-healing" language

## Phase alpha

The first component families to receive explicit refresh law are:

- the shared-root Codex plane in `8Dionysus`
- the foundation skill export in `aoa-skills`
- the Codex subagent projection in `aoa-agents`
- the growth-refinery derived summaries in `aoa-stats`

Use `docs/REVIEWABLE_GROWTH_REFINERY.md` when the question is the biography of
one growth object across owners.
Use this note when the question is owner-owned maintenance of one drifting
technical component.
