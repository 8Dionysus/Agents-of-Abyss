# Decision Note: Audit Becomes A Center Mechanic

Status: accepted
Date: 2026-04-29

## Context

Audit work was already central to AoA: documentation cleanup, route review,
owner-bound evidence, proof posture, release readiness, and inspection-first
candidate lists all needed reviewable seeing.

Before this decision, audit material lived under `docs/audits/`. That made
audit visible, but it also left the process as a thin docs district rather than
a functioning mechanic with parts, owner routes, legacy accounting, validation,
and future-growth posture.

## Options considered

1. Keep `docs/audits/` as the active audit district.
2. Move only historical audit files into `mechanics/audit/legacy/raw/` and keep
   active audit guidance in docs.
3. Plant `mechanics/audit/` as a first-class center mechanic and move old
   `docs/audits/` material into legacy/raw with `PROVENANCE.md` as the bridge.

## Decision

AoA plants Audit as a center mechanic under `mechanics/audit/`.

The active route now lives in the mechanic package. Historical `docs/audits/`
sources are preserved in `mechanics/audit/legacy/raw/`, and active readers reach
them through `mechanics/audit/PROVENANCE.md` only when archive accounting is
needed.

## Rationale

Audit is not only a file shelf. It is a repeatable route grammar for source
mapping, evidence ledgers, risk signals, finding lifecycle, owner routing,
validation gates, campaign routes, and audit-event bridges.

Putting it under `mechanics/audit/` lets future agents develop audit parts,
owner requests, skills, playbooks, eval routes, memo routes, and stats routes
without bloating `docs/` or turning old audit receipts into current law.

## Consequences

- `docs/audits/` is no longer an active docs district.
- Audit gets package-local AGENTS law, parts, roadmap, landing log, provenance,
  owner requests, validator, and tests.
- Audit findings remain center-visible route objects; proof, remediation,
  runtime authority, memory truth, release support, generated authority, and
  owner-local action stay with stronger owners.
- Active antifragility and docs routes point to Audit provenance rather than
  direct raw archive paths.

## Source surfaces

- `mechanics/audit/README.md`
- `mechanics/audit/AGENTS.md`
- `mechanics/audit/PARTS.md`
- `mechanics/audit/PROVENANCE.md`
- `mechanics/audit/legacy/raw/`
- `mechanics/audit/scripts/validate_audit_distillation.py`
- `docs/README.md`
- `docs/guardrails/thematic_districts.json`
- `scripts/release_check.py`

## Follow-up route

Route executable audit workflows to `aoa-skills`, proof-strength levels to
`aoa-evals`, recurring audit campaigns to `aoa-playbooks`, durable recall to
`aoa-memo`, and derived audit movement summaries to `aoa-stats`.
