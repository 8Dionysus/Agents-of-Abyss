# Checkpoint Parts

This file is the active map of functioning checkpoint parts. Each part owns one
bounded route shape. Sibling repositories own the local implementation and
meaning.

## Part Map

| Part | Center function | Stronger owner route |
|---|---|---|
| [Session Carry](parts/session-carry/README.md) | preserve mid-session evidence, `cluster_ref` hints, and review posture without minting candidate truth | `aoa-sdk` controls carry; `aoa-skills` owns checkpoint-note protocol |
| [Review Gate](parts/review-gate/README.md) | decide when checkpoint evidence must be reviewed before promotion or mutation continues | `aoa-agents`, `aoa-skills`, and `aoa-evals` own local gates and proof |
| [Return Re-entry](parts/return-reentry/README.md) | use checkpoint as a valid return anchor and bounded re-entry note | `aoa-memo`, `aoa-routing`, `aoa-playbooks`, and `aoa-agents` own local return surfaces |
| [Closeout Bridge](parts/closeout-bridge/README.md) | bridge reviewed checkpoint evidence into explicit closeout chain without hiding harvest | `aoa-skills` owns the bridge skill; `aoa-sdk` builds context |
| [Runtime Export](parts/runtime-export/README.md) | keep runtime checkpoint exports and receipts bounded by runtime-owner gates | `abyss-stack` owns runtime plumbing; `aoa-memo` owns writeback targets |
| [Owner Handoff](parts/owner-handoff/README.md) | turn checkpoint pressure into owner-request packets and next-owner routes | target owner repositories accept or reject operational truth |

## Active Part Contract

Every part keeps three working surfaces:

- `README.md`: when to use the part.
- `CONTRACT.md`: center boundary, allowed outputs, and stop-lines.
- `VALIDATION.md`: validation route, with executable commands centralized in
  `AGENTS.md`.

Every part should keep the same active-route shape:

- `## Use When`
- `## Do Not Use When`
- `## Route Check`
- `## Active Outputs`
- `## Next Route`

## Provenance Bridge

Use [PROVENANCE](PROVENANCE.md) when a checkpoint source must be audited. Active
part docs should not carry raw runtime histories or sibling inventories.

## Validation

Use the validation lane in [mechanics/checkpoint/AGENTS.md](AGENTS.md#validation) for executable commands.
