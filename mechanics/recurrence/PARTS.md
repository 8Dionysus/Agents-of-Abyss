# Recurrence Parts

This file is the active map of functioning recurrence parts. Each part owns one
bounded center route shape. Sibling repositories own their local implementation
and meaning.

## Part Map

| Part | Center function | Stronger owner route |
|---|---|---|
| [Anchor Return](parts/anchor-return/README.md) | name axis loss, valid anchors, return, re-entry, and safe stop | source owner, `aoa-routing`, `aoa-memo`, and `aoa-agents` own local return surfaces |
| [Continuity Window](parts/continuity-window/README.md) | keep continuity tied to explicit revision windows and reanchor artifacts | `aoa-agents`, `aoa-playbooks`, `aoa-memo`, `aoa-evals`, and `aoa-sdk` own local continuity surfaces |
| [Component Refresh](parts/component-refresh/README.md) | route drifting technical components through owner refresh law and receipts | component owner repos, `aoa-sdk`, `aoa-stats`, `aoa-playbooks`, and `aoa-memo` own local refresh behavior |
| [Control Plane Carry](parts/control-plane-carry/README.md) | keep recurrence manifests, graph closure, projections, and handoff carry typed and review-only | `aoa-sdk` owns programmable carry and must stop before owner mutation |
| [Reentry Routing](parts/reentry-routing/README.md) | keep return navigation thin and source-referring | `aoa-routing` owns navigation hints without recurrence meaning |
| [Memory Recall](parts/memory-recall/README.md) | keep anchors, checkpoints, recall, and provenance explicit without memory sovereignty | `aoa-memo` owns memory objects and writeback meaning |
| [Scenario Choreography](parts/scenario-choreography/README.md) | route recurring return patterns into scenario-owned method | `aoa-playbooks` owns repeatable choreography and fallback posture |
| [Proof Gates](parts/proof-gates/README.md) | require proof before recovery, continuity, or control-plane claims harden | `aoa-evals` owns proof bundles and verdict boundaries |
| [Runtime Return](parts/runtime-return/README.md) | keep runtime recovery downstream of owner gates and explicit anchors | `abyss-stack` and product-local runtime owners own runtime policy and logs |
| [Recursor Boundary](parts/recursor-boundary/README.md) | separate recursor readiness, witness posture, and no-spawn stop-lines | `aoa-sdk`, `aoa-agents`, and `aoa-evals` own local readiness and proof surfaces |

## Active Part Contract

Every part keeps three working surfaces:

- `README.md`: when to use the part.
- `CONTRACT.md`: center boundary, allowed outputs, and stop-lines.
- `VALIDATION.md`: validation route, with executable commands centralized in
  `parts/AGENTS.md`.

Every part should keep the same active-route shape:

- `## Use When`
- `## Do Not Use When`
- `## Route Check`
- `## Active Outputs`
- `## Next Route`

## Provenance Bridge

Use [PROVENANCE](PROVENANCE.md) when a recurrence source must be audited. Active
part docs should not carry sibling inventories, wave receipts, or raw runtime
history.

## Validation

Use the validation lane in [mechanics/recurrence/AGENTS.md](AGENTS.md#validation)
for package commands and [parts/AGENTS.md](parts/AGENTS.md#validation) for part
commands.
