# Recurrence Landing Log

Canonical landing ledger for the recurrence mechanic.

## Entries

### Root mechanics topology migration

Status: landed

Owner boundary: `Agents-of-Abyss` owns center recurrence law; memory, routing,
playbook, proof, and runtime behavior remain owner-local.

Surfaces:

- `mechanics/recurrence/README.md`
- `mechanics/recurrence/ROADMAP.md`
- `mechanics/recurrence/docs/RECURRENCE_PRINCIPLE.md`
- `mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md`
- `mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md`

Validation: `python scripts/validate_mechanics_topology.py --mechanic recurrence`

Stop-lines: no hidden memory sovereignty, ambient continuity, or runtime
self-healing authority.

Next route: route recurring choreography to `aoa-playbooks` and recall objects
to `aoa-memo` when they become owner-local artifacts.
