# Audit Landing Log

This is the canonical center landing ledger for the Audit mechanic.

## Active Index

| Entry | Status | Route |
|---|---|---|
| [aoa-skills owner-request receipt sync](#aoa-skills-owner-request-receipt-sync) | accepted | `aoa-skills` accepts audit workflow pressure without landing a general audit package. |
| [Audit mechanic planted](#audit-mechanic-planted) | planted | historical docs-audits material moved into `mechanics/audit/legacy/raw/`; active route created in `mechanics/audit/` |

## Entries

### aoa-skills owner-request receipt sync

Status: owner-request accepted

Owner boundary: the center records the `aoa-skills` acceptance receipt for
`ORQ-AUDIT-SKILLS-001` without claiming executable audit workflow truth,
proof verdicts, remediation authority, memory truth, role activation, or
derived-summary authority.

Surfaces:

- `mechanics/audit/OWNER_REQUESTS.md`
- `mechanics/owner-request-queue.json`
- `mechanics/OWNER_REQUEST_QUEUE.md`
- `generated/owner_request_queue.min.json`
- Owner-local receipt in aoa-skills/mechanics/OWNER_REQUEST_RECEIPTS.md

Validation: use the owner-request validation lane in `mechanics/AGENTS.md`.

Stop-lines: Accepted is not landed. Existing audit-adjacent skills do not cover
the whole center Audit mechanic until an owner-local package, canonical
workflow, or superseding receipt lands.

Next route: Wait for `aoa-skills` audit package, canonical workflow, or
superseding receipt before advancing this request to `landed`.

### Audit mechanic planted

Status: planted

Owner boundary: Center audit grammar and route discipline cover review grammar, evidence posture, risk signals, finding lifecycle, owner routing, validation honesty, campaign route language, and event bridges. Proof, remediation, runtime, memory, release support, generated authority, and source-authored meaning remain owner-local.

Surfaces:
- `mechanics/audit/AGENTS.md`
- `mechanics/audit/README.md`
- `mechanics/audit/DIRECTION.md`
- `mechanics/audit/PARTS.md`
- `mechanics/audit/OWNER_MAP.md`
- `mechanics/audit/OWNER_REQUESTS.md`
- `mechanics/audit/ROADMAP.md`
- `mechanics/audit/LANDING_LOG.md`
- `mechanics/audit/PROVENANCE.md`
- `mechanics/audit/docs/AUDIT_LAW.md`
- `mechanics/audit/docs/AGENTS.md`
- `mechanics/audit/docs/AUDIT_OWNER_REPO_REQUESTS.md`
- `mechanics/audit/parts/AGENTS.md`
- `mechanics/audit/parts/README.md`
- `mechanics/audit/parts/source-map/README.md`
- `mechanics/audit/parts/evidence-ledger/README.md`
- `mechanics/audit/parts/risk-signal/README.md`
- `mechanics/audit/parts/finding-lifecycle/README.md`
- `mechanics/audit/parts/owner-routing/README.md`
- `mechanics/audit/parts/validation-gate/README.md`
- `mechanics/audit/parts/campaign-route/README.md`
- `mechanics/audit/parts/audit-event-bridge/README.md`
- `mechanics/audit/legacy/AGENTS.md`
- `mechanics/audit/legacy/README.md`
- `mechanics/audit/legacy/INDEX.md`
- `mechanics/audit/legacy/raw/README.md`
- `mechanics/audit/legacy/raw/CODEX_AUDIT_PROTOCOL.md`
- `mechanics/audit/legacy/raw/CODEX_SKILL_PROOF_AUDIT_BRIDGE.md`
- `mechanics/audit/legacy/raw/DELETION_CANDIDATES.json`
- `mechanics/audit/legacy/raw/DOCS_AUDITS_AGENTS.md`
- `mechanics/audit/legacy/raw/DOCS_AUDITS_README.md`
- `mechanics/audit/legacy/raw/DOCUMENTATION_SURFACE_AUDIT_2026_04_24.md`
- `mechanics/audit/legacy/raw/ROOT_SURFACE_AUDIT_2026_04_24.md`
- `mechanics/audit/scripts/validate_audit_distillation.py`
- `mechanics/audit/tests/test_audit_distillation.py`
- `mechanics/registry.json`
- `mechanics/owner-request-queue.json`
- `generated/mechanic_card_index.min.json`
- `generated/owner_request_queue.min.json`
- `scripts/mechanics_topology/validate_mechanics_topology.py`
- `scripts/mechanics_topology/validate_mechanic_landing_logs.py`
- `scripts/release_gate/release_check.py`
- `tests/test_mechanic_landing_logs.py`
- `CHANGELOG.md`

Validation: use the Audit validation lane in `mechanics/audit/AGENTS.md`.

Stop-lines: Do not treat legacy audit receipts as active law. Do not turn findings into proof verdicts, remediation authority, memory truth, runtime authority, release support, or generated authority.

Next route: Use `mechanics/audit/OWNER_REQUESTS.md` for stronger-owner packets, and use `mechanics/audit/PROVENANCE.md` only when a task needs to audit the legacy source bridge.
