# Root Manifest Registry And Agon Manifest Home

Status: accepted
Date: 2026-04-29

## Context

`manifests/` carried Agon-shaped recurrence component and hook receipts under a
root `recurrence/` subdirectory. That made old paths stable, but it blurred the
owner boundary after mechanics became first-class package homes. The records
belong to Agon recurrence adapter work, while the repo root still benefits from
a compact manifest registry.

## Options considered

1. Keep all recurrence manifests in root `manifests/recurrence/`.
2. Delete root `manifests/` after moving the Agon records.
3. Keep root `manifests/` as a registry/control surface and move Agon recurrence
   records into the owning part.

## Decision

Root `manifests/` owns `registry.json`, README/AGENTS guidance, and registry
validation. Agon recurrence component and hook records live under
`mechanics/agon/parts/recurrence-adapter/manifests/`.

## Rationale

The root still needs a way to tell future agents where manifest homes live and
how they are validated. It does not need to store mechanic-owned records. Moving
the Agon records into the recurrence adapter part keeps the active receipts near
their source config, generated adapter request, validation scripts, and Agon
part law.

## Consequences

- Root `manifests/` stays useful without becoming a warehouse.
- Agon recurrence manifests have a local README, AGENTS card, validator, and
  tests.
- Consumers must use the new mechanic-owned paths for local AoA manifests.
- External owner manifest names remain explicit `owner-local://` requests until
  those owners land their own records.

## Source surfaces

- `manifests/README.md`
- `manifests/registry.json`
- `mechanics/agon/parts/recurrence-adapter/README.md`
- `mechanics/agon/parts/recurrence-adapter/manifests/README.md`
- `mechanics/agon/parts/recurrence-adapter/generated/agon_recurrence_adapter_request.min.json`
- `mechanics/recurrence/docs/RECURRENCE_PRINCIPLE.md`
- `quests/agon/ready/AOA-Q-AGON-0021-recurrence-owner-manifests.md`

## Follow-up route

When sibling repositories land their owner-local manifest homes, update
`manifests/registry.json` only if those homes become repo-visible contracts in
Agents-of-Abyss. Otherwise, keep them as owner-local routes and let `aoa-sdk`
carry cross-repo manifest discovery.
