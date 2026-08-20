# Admit aoa-dashboard as a Bounded Derived Organ

- Decision ID: AOA-CENTER-D-0039

## Status

Accepted.

## Index Metadata

- Original date: 2026-08-20
- Surface classes: organ contract, federation contract, public contour, repository routing, decision record
- Center facets: organ alignment, federation contour, registry contract
- Mechanic parents: organ-contract
- Guard families: owner boundary, sibling-owner boundary, ecosystem registry, GitHub landing
- Posture: accepted bounded derived-organ registration; no private access admission

## Context

The Goal Space/operator surface had a working owner-local implementation and
local tests, but it was not independently identifiable in the federation. The
center map, SDK workspace discovery, public route map, and private organ-access
posture therefore could not distinguish a real dashboard organ from a local
directory or a generated projection.

The missing identity did not justify creating a second Goal authority, an
`aoa-goals` repository, or a private registry record without a concrete access
plane. The existing center organ law instead requires a bounded owner contract,
explicit sibling separation, source/workspace registration, validation, and a
default-deny admission route.

## Options considered

1. Keep the dashboard local-only and leave the federation blind to it.
2. Promote the dashboard to a new Goal authority or create `aoa-goals`.
3. Register `aoa-dashboard` as a public bootstrap derived organ with an
   explicit projection boundary, SDK workspace route, and no private access
   admission.

## Decision

Choose option 3.

`aoa-dashboard` is a public `bootstrap` derived layer. It owns only its
Goal Space/operator read model, provenance/freshness/missingness and
task-local correlation/activity projections, dashboard annotations, and
deferred non-executing action intents. The center map and generated registry
include this bounded derived-layer identity.

The dashboard does not own roles, mandates, responsibility, wake, task-local
DAG, RunPlan, runtime lifecycle, raw session truth, proof/evals, durable memory,
stats meaning, KAG source relations, owner acceptance, or execution. The SDK
workspace registers it as an optional source checkout for discovery and hints;
SDK registration does not grant organ access or runtime admission.

The workspace-private v2 registry remains default-deny with no dashboard record
because the dashboard has no direct access plane in this contour. A future
record requires a concrete source/access/control/runtime/proof/acceptance path
and must be created by the workspace owner through the existing registry
route. Public GitHub landing, generated registry presence, and green local/CI
tests remain weaker source or route evidence, not admission.

## Rationale

This preserves a legible independent organ identity while keeping the
dashboard's useful projection surface small. It lets the Goal Space grow into
an operator surface without duplicating the role, routing, runtime, proof,
memory, stats, or acceptance owners. It also keeps the future access contour
reversible and fail-closed.

## Consequences

- The public center registry and repo-role map now name `aoa-dashboard`.
- `aoa-sdk` can discover the optional checkout and route consumers to the
  dashboard's owner contract.
- A private organ-access record is deliberately absent and must not be
  inferred from registration.
- Any stronger effect or access claim requires a new owner-bounded route,
  independent proof, and rollback evidence.
- The center remains a map and constitutional owner; dashboard implementation
  and semantic meaning stay in the dashboard repository.

## Source surfaces

- `ECOSYSTEM_MAP.md`
- `docs/REPO_ROLES.md`
- `docs/organ-contract/ORGAN_CONTRACT.md`
- `docs/decisions/AOA-CENTER-D-0032-organ-access-admission-law.md`
- `generated/ecosystem_registry.min.json`
- `aoa-dashboard/contracts/organ_contract.json`
- `aoa-dashboard/docs/ORGAN_CONTRACT.md`
- `aoa-sdk/.aoa/workspace.toml`

## Follow-up route

The dashboard owner maintains its local contract and validators. The SDK owner
maintains discovery and compatibility routes. The workspace owner handles any
future private registry contour. `aoa-evals`, `abyss-stack`, and the human
operator remain separate proof, runtime, and acceptance routes. Revisit this
decision only when a concrete access contour or a material authority change is
proposed.
