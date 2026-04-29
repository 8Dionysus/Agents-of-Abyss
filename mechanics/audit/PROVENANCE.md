# Audit Provenance

This file is the controlled bridge from old audit surfaces into the active Audit mechanic. Default work starts in `README.md`, `DIRECTION.md`, and `PARTS.md`; this file is for provenance checks and source-lineage review.

## Legacy Source Map

| Legacy source | Active landing |
|---|---|
| `legacy/raw/DOCS_AUDITS_README.md` | package role, owner boundary, and historical docs-audit posture distilled into `README.md`, `DIRECTION.md`, and `docs/AUDIT_LAW.md` |
| `legacy/raw/DOCS_AUDITS_AGENTS.md` | local lane law distilled into `AGENTS.md`, `legacy/AGENTS.md`, and `legacy/raw/README.md` |
| `legacy/raw/CODEX_AUDIT_PROTOCOL.md` | sequence and audit-before-patch posture distilled into `parts/source-map`, `parts/evidence-ledger`, `parts/finding-lifecycle`, and `parts/validation-gate` |
| `legacy/raw/CODEX_SKILL_PROOF_AUDIT_BRIDGE.md` | proof and skill boundary distilled into `OWNER_MAP.md`, `OWNER_REQUESTS.md`, `parts/owner-routing`, and `parts/validation-gate` |
| `legacy/raw/DOCUMENTATION_SURFACE_AUDIT_2026_04_24.md` | documentation cleanup evidence distilled into `parts/source-map`, `parts/risk-signal`, and docs guardrail route updates |
| `legacy/raw/ROOT_SURFACE_AUDIT_2026_04_24.md` | root surface review evidence distilled into root route references, `parts/source-map`, and `parts/owner-routing` |
| `legacy/raw/DELETION_CANDIDATES.json` | deletion-candidate evidence preserved for antifragility and audit route checks |

## Active Extraction

- Source-first reading became `parts/source-map`.
- Evidence listing and missing-evidence posture became `parts/evidence-ledger`.
- Drift and cleanup pressure became `parts/risk-signal`.
- Observation-to-route movement became `parts/finding-lifecycle`.
- Owner and proof split became `parts/owner-routing` and `OWNER_REQUESTS.md`.
- Check reporting became `parts/validation-gate`.
- Repeated audit sequences became `parts/campaign-route`.
- Cross-mechanic linkage became `parts/audit-event-bridge`.

## Stop-lines

- Raw files remain historical receipts.
- Active audit work should not start in `legacy/raw/`.
- If old text conflicts with active route surfaces, the active route wins unless a new landing intentionally changes it.

## Validation

Use the validation lane in [mechanics/audit/AGENTS.md](AGENTS.md#validation).
