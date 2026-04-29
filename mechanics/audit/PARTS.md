# Audit Parts

This file is the active map of functioning Audit parts. Each part owns a real slice of the mechanic: purpose, boundary, validation route, and next owner.

## Part Map

| Part | Center function | Stronger owner route |
|---|---|---|
| [Source Map](parts/source-map/README.md) | locate the surface, owner, authority level, and source chain before any finding is made | source repositories own their surfaces; `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md` resolve owner uncertainty |
| [Evidence Ledger](parts/evidence-ledger/README.md) | list reviewable evidence, missing evidence, and evidence freshness without turning it into a verdict | `aoa-memo` owns memory writeback; `aoa-evals` owns proof and quality claims |
| [Risk Signal](parts/risk-signal/README.md) | name visible risk, ambiguity, drift, or cleanup pressure in a routeable form | `mechanics/antifragility` owns pruning pressure; owner repos own local remediation |
| [Finding Lifecycle](parts/finding-lifecycle/README.md) | carry observations from signal to finding, routed request, supersession, or closure | `aoa-playbooks` owns recurring campaign choreography; source owners close local findings |
| [Owner Routing](parts/owner-routing/README.md) | send findings to proof, memory, release, runtime, skill, technique, playbook, stats, or source-owner lanes | the target owner accepts, rejects, lands, or supersedes the request |
| [Validation Gate](parts/validation-gate/README.md) | report checks run, checks skipped, evidence limits, and residual risk | `aoa-evals` owns proof gates; repo-level validators own executable check results |
| [Campaign Route](parts/campaign-route/README.md) | coordinate multi-surface audits without turning the center into a task warehouse | `aoa-playbooks` owns recurring campaign routes and handoff choreography |
| [Audit Event Bridge](parts/audit-event-bridge/README.md) | connect audit events to checkpoint, questbook, release, growth-cycle, and distillation routes | crossed mechanics keep their local authority and landing logs |

## Active Part Contract

Every part keeps three working surfaces:

- `README.md`: what the part is for and where to start.
- `CONTRACT.md`: owner boundary, stop-lines, and allowed outputs.
- `VALIDATION.md`: validation route and evidence expectations.

A part may grow, split, merge, shrink, or retire when that improves its function and keeps the route cleaner. The move should leave the active path easier to follow.

Prefer clearer routing over broader catalogs.

## Provenance Bridge

Historical audit source accounting stays outside part docs. Use [PROVENANCE](PROVENANCE.md) when a task must audit how older audit material landed.

## Validation

Use the validation lane in [mechanics/audit/AGENTS.md](AGENTS.md#validation).
