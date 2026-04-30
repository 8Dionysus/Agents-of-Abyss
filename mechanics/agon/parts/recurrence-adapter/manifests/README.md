# Agon Recurrence Adapter Manifests

This manifest home owns Agon recurrence component receipts and review-only hook
binding receipts. It keeps return signals tied to Agon parts without turning
recurrence into memory, runtime, verdict, rank, or ToS authority.

## Manifest Classes

| Class | Files | Role |
|---|---|---|
| `agon_recurrence_component` | `component.*.json` | component receipt with owner route, source refs, observed surfaces, review outputs, and stop-lines |
| `agon_recurrence_hook_binding` | `hooks/component.*.hooks.json` | hook receipt with review-only bindings and emissions for the paired component |

## Current Inventory

| Component receipt | Hook receipt |
|---|---|
| [`component.agon.arena-session-model-surfaces.json`](component.agon.arena-session-model-surfaces.json) | [`hooks/component.agon.arena-session-model-surfaces.hooks.json`](hooks/component.agon.arena-session-model-surfaces.hooks.json) |
| [`component.agon.ccs-law-surfaces.json`](component.agon.ccs-law-surfaces.json) | [`hooks/component.agon.ccs-law-surfaces.hooks.json`](hooks/component.agon.ccs-law-surfaces.hooks.json) |
| [`component.agon.center-surfaces.json`](component.agon.center-surfaces.json) | [`hooks/component.agon.center-surfaces.hooks.json`](hooks/component.agon.center-surfaces.hooks.json) |
| [`component.agon.court-memo-stats-center-request.json`](component.agon.court-memo-stats-center-request.json) | [`hooks/component.agon.court-memo-stats-center-request.hooks.json`](hooks/component.agon.court-memo-stats-center-request.hooks.json) |
| [`component.agon.duel-kernel-model-surfaces.json`](component.agon.duel-kernel-model-surfaces.json) | [`hooks/component.agon.duel-kernel-model-surfaces.hooks.json`](hooks/component.agon.duel-kernel-model-surfaces.hooks.json) |
| [`component.agon.epistemic-agon-surfaces.json`](component.agon.epistemic-agon-surfaces.json) | [`hooks/component.agon.epistemic-agon-surfaces.hooks.json`](hooks/component.agon.epistemic-agon-surfaces.hooks.json) |
| [`component.agon.kag-promotion-path.json`](component.agon.kag-promotion-path.json) | [`hooks/component.agon.kag-promotion-path.hooks.json`](hooks/component.agon.kag-promotion-path.hooks.json) |
| [`component.agon.mechanical-trial-suite-surfaces.json`](component.agon.mechanical-trial-suite-surfaces.json) | [`hooks/component.agon.mechanical-trial-suite-surfaces.hooks.json`](hooks/component.agon.mechanical-trial-suite-surfaces.hooks.json) |
| [`component.agon.retention-rank-economy-surfaces.json`](component.agon.retention-rank-economy-surfaces.json) | [`hooks/component.agon.retention-rank-economy-surfaces.hooks.json`](hooks/component.agon.retention-rank-economy-surfaces.hooks.json) |
| [`component.agon.schools-lineages-campaigns.json`](component.agon.schools-lineages-campaigns.json) | [`hooks/component.agon.schools-lineages-campaigns.hooks.json`](hooks/component.agon.schools-lineages-campaigns.hooks.json) |
| [`component.agon.sophian-threshold-surfaces.json`](component.agon.sophian-threshold-surfaces.json) | [`hooks/component.agon.sophian-threshold-surfaces.hooks.json`](hooks/component.agon.sophian-threshold-surfaces.hooks.json) |
| [`component.agon.state-packet-surfaces.json`](component.agon.state-packet-surfaces.json) | [`hooks/component.agon.state-packet-surfaces.hooks.json`](hooks/component.agon.state-packet-surfaces.hooks.json) |
| [`component.agon.vds-bridge-surfaces.json`](component.agon.vds-bridge-surfaces.json) | [`hooks/component.agon.vds-bridge-surfaces.hooks.json`](hooks/component.agon.vds-bridge-surfaces.hooks.json) |

## Requested Owner Manifest Names

The recurrence adapter request names future owner-local manifests for
`aoa-agents`, `aoa-routing`, `aoa-playbooks`, `aoa-techniques`, and
`aoa-skills` with `owner-local://` paths. Those names are requests, not local
placeholder files.

## Validation

Executable validation commands live in [local AGENTS](AGENTS.md#validation).
