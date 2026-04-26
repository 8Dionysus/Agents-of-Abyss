# Agon Parts

This file is the active map of functioning Agon parts. Each part owns a real
slice of the mechanic: purpose, boundary, validation, and next route. Detailed
source-docs stay outside the working path until a task needs provenance review.

## Part map

| Part | Center function | Stronger owner route |
|---|---|---|
| [Imposition Readiness](parts/imposition-readiness/README.md) | survival audit, doubt posture, pre-Agon baseline, and imposition stop-line | `aoa-evals` for proof discipline; `aoa-routing` for review routing |
| [Lawful Move Grammar](parts/lawful-move-grammar/README.md) | lawful move vocabulary, move registry shape, and pre-protocol move stop-lines | `aoa-techniques`, `aoa-skills`, `aoa-playbooks`, and `aoa-routing` own practice or routing usage |
| [Owner Binding](parts/owner-binding/README.md) | move-to-owner binding, owner request gravity, and no-acceptance boundary | target owner repositories accept or reject operational slices |
| [Gate Routing](parts/gate-routing/README.md) | gate handoff, route request, and route stop-lines | `aoa-routing` owns live dispatch and gate behavior |
| [Trial Handoff](parts/trial-handoff/README.md) | trial contour, playbook request, and rehearsal stop-lines | `aoa-playbooks` owns choreography; `aoa-evals` owns trial proof |
| [Recurrence Adapter](parts/recurrence-adapter/README.md) | recurrence bridge, return posture, and adapter stop-lines | `mechanics/recurrence`, `aoa-routing`, and `aoa-memo` own return and memory behavior |
| [Packet Arena](parts/packet-arena/README.md) | state packet, session, charter, seat, and arena boundary grammar | `aoa-agents`, `aoa-routing`, and `abyss-stack` own live actors, routes, and runtime |
| [Duel Kernel](parts/duel-kernel/README.md) | duel kernel, mechanical trial, model-of-other, and sealed-commit grammar | `aoa-playbooks`, `aoa-evals`, and `aoa-agents` own live practice, proof, and roles |
| [Verdict Retention Rank](parts/verdict-retention-rank/README.md) | verdict contour, scar request, retention, rank, and reputation boundary | `aoa-evals`, `aoa-memo`, and `aoa-stats` own proof, memory, and derived summaries |
| [Epistemic KAG](parts/epistemic-kag/README.md) | epistemic pressure, evidence promotion boundary, and KAG handoff | `aoa-kag`, `aoa-evals`, and source owners keep derived-proof and source-truth authority |
| [Sophian Threshold](parts/sophian-threshold/README.md) | ToS threshold packet, canon restraint, and Sophian owner handoff | `Tree-of-Sophia` owns canon and authored meaning |
| [Compatibility Bridges](parts/compatibility-bridges/README.md) | cross-mechanic compatibility, schools, campaigns, and law interlocks | the crossed mechanic or owner repository keeps final authority |

## Active part contract

Every part keeps three working surfaces:

- `README.md`: what the part is for and where to start.
- `CONTRACT.md`: owner boundary, stop-lines, and allowed outputs.
- `VALIDATION.md`: commands and tests.

A part may grow, split, merge, shrink, or retire when that improves its
function and keeps the route cleaner. The move should leave the active path
easier to follow, not merely smaller.

## Provenance bridge

Detailed source-doc accounting is deliberately outside part docs. Use
[PROVENANCE](PROVENANCE.md) when a task must audit which wave, model, handoff,
or generated capsule fed a part. Active part docs should not grow source-file
inventories.

## Validation

```bash
python mechanics/agon/scripts/validate_agon_distillation.py
python scripts/validate_mechanic_artifact_topology.py --mechanic agon
```

Use the package `README.md` for full mechanic-card validation and
`OWNER_REQUESTS.md` for owner-request queue validation.
