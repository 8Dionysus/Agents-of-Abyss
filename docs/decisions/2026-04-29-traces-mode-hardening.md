# Decision Note: Traces Stay Repo-Level Receipts

Status: accepted
Date: 2026-04-29

## Context

`docs/traces/` held useful movement evidence, but its boundary was still broad
enough to become a generic archive. At the same time, mechanics now own their
own legacy, provenance, and landing-log routes, and the Audit mechanic owns
review evidence.

Future repositories may need similar trace districts, but creating empty trace
doors everywhere would repeat the same drift this repository has been removing.

## Options considered

1. Make traces a new center mechanic.
2. Move traces under one existing mechanic such as Audit, Distillation, or
   Checkpoint.
3. Keep `docs/traces/` as a repo-level receipt district, harden it with local
   law and validation, and let mechanics cite traces only as evidence.

## Decision

Keep `docs/traces/` as a repo-level receipt district.

The district may hold generic movement manifests, link-repair traces, generic
apply manifests, and migration conflict receipts. Mechanic-specific source
traces route to the owning mechanic's `legacy/raw/` path and provenance bridge.
Audit evidence routes to the Audit mechanic. Decision rationale routes to
`docs/decisions/`.

Add `scripts/validate_traces_district.py` and release-check coverage so the
district stays small, indexed, schema-marked, and free of mechanic-specific
receipt drift.

## Rationale

Traces are evidence of movement, not a process mechanic by themselves. Making
them a mechanic now would overstate their current role and blur them with Audit,
Distillation, Checkpoint, Release-support, and Boundary-bridge.

Keeping traces as a thin repo-level district preserves reviewable movement
receipts while leaving meaning with current source surfaces and owner mechanics.
Validation gives future agents a concrete check instead of relying on memory.

## Consequences

- `docs/traces/` stays available for generic repository movement evidence.
- The district cannot quietly become a Markdown archive or mechanic receipt
  shelf.
- Mechanics can cite traces as evidence without inheriting trace-district
  ownership.
- Other repositories should create trace districts only when real receipts
  exist; no empty trace doors.
- Stronger trace automation or hooks remain future work after stable receipt
  events emerge.

## Source surfaces

- `docs/traces/AGENTS.md`
- `docs/traces/README.md`
- `docs/guardrails/thematic_districts.json`
- `docs/guardrails/THEMATIC_DISTRICT_PROTOCOL.md`
- `mechanics/AGENTS.md`
- `scripts/validate_traces_district.py`
- `scripts/release_check.py`

## Follow-up route

If repeated work produces a real trace lifecycle with hooks, retention policy,
schemas, owner routing, and generated read models, revisit this decision through
`docs/decisions/` before promoting traces into a mechanic or another stronger
owner surface.
