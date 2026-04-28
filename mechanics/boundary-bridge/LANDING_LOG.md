# Boundary Bridge Landing Log

Canonical landing ledger for the boundary-bridge mechanic.

## Route index for agents

Read this index before scanning the full ledger. It names the current shape of
Boundary Bridge without requiring every older landing entry to be re-read.

- Current active route: `mechanics/boundary-bridge/README.md`,
  `mechanics/boundary-bridge/DIRECTION.md`,
  `mechanics/boundary-bridge/PARTS.md`,
  `mechanics/boundary-bridge/parts/README.md`, and the relevant part README.
- Current owner pressure route: `mechanics/boundary-bridge/OWNER_REQUESTS.md`.
- Current future-pressure route: `mechanics/boundary-bridge/ROADMAP.md`.
- Current provenance bridge: `mechanics/boundary-bridge/PROVENANCE.md`; use it
  only when auditing source provenance or bridge history.

## How to update this log

Every landing entry uses the same shape:

- `Status:`
- `Owner boundary:`
- `Surfaces:`
- `Validation:`
- `Stop-lines:`
- `Next route:`

When a change touches Boundary Bridge docs, parts, owner requests, source
bridges, validators, or tests, update the relevant entry here or explain in
the PR why the change is not a landing change.

## Entries

### Root mechanics topology migration

Status: landed

Owner boundary: `Agents-of-Abyss` owned the original ToS support posture;
`Tree-of-Sophia` owned authored meaning and canon.

Surfaces:

- `mechanics/boundary-bridge/README.md`
- `mechanics/boundary-bridge/ROADMAP.md`
- `mechanics/boundary-bridge/docs/COUNTERPART_BRIDGE.md`
- `mechanics/boundary-bridge/docs/WITNESS_COMPOST.md`
- `mechanics/boundary-bridge/docs/TOS_GROWTH_SUPPORT.md`
- `mechanics/boundary-bridge/docs/TOS_TEMPLATE_SUPPORT.md`
- `mechanics/boundary-bridge/docs/TOS_LINEAGE_PILOT_SUPPORT.md`
- `mechanics/boundary-bridge/docs/TOS_SOIL_PREP_SUPPORT.md`

Validation: `python scripts/validate_mechanics_topology.py --mechanic boundary-bridge`

Stop-lines: no AoA-authored ToS canon, source interpretation authority, or
owner-local implementation truth.

Next route: use `Tree-of-Sophia` for authored meaning and keep AoA support
surfaces explicitly bounded.

### Boundary-bridge rename and ToS-support distillation

Status: landed

Owner boundary: `Agents-of-Abyss` owns bridge law, non-identity guardrails,
owner-request packets, and ToS-support route language; each bridged owner owns
truth on its side of the bridge.

Surfaces:

- `mechanics/boundary-bridge/README.md`
- `mechanics/boundary-bridge/AGENTS.md`
- `mechanics/boundary-bridge/DIRECTION.md`
- `mechanics/boundary-bridge/PARTS.md`
- `mechanics/boundary-bridge/OWNER_MAP.md`
- `mechanics/boundary-bridge/PROVENANCE.md`
- `mechanics/boundary-bridge/OWNER_REQUESTS.md`
- `mechanics/boundary-bridge/ROADMAP.md`
- `mechanics/boundary-bridge/LANDING_LOG.md`
- `mechanics/boundary-bridge/docs/COUNTERPART_BRIDGE.md`
- `mechanics/boundary-bridge/docs/WITNESS_COMPOST.md`
- `mechanics/boundary-bridge/docs/TOS_GROWTH_SUPPORT.md`
- `mechanics/boundary-bridge/docs/TOS_TEMPLATE_SUPPORT.md`
- `mechanics/boundary-bridge/docs/TOS_LINEAGE_PILOT_SUPPORT.md`
- `mechanics/boundary-bridge/docs/TOS_SOIL_PREP_SUPPORT.md`
- `mechanics/boundary-bridge/docs/TOS_BRIDGE_OWNER_REPO_REQUESTS.md`
- `mechanics/boundary-bridge/parts/AGENTS.md`
- `mechanics/boundary-bridge/parts/README.md`
- `mechanics/boundary-bridge/parts/boundary-contract/README.md`
- `mechanics/boundary-bridge/parts/non-identity-guard/README.md`
- `mechanics/boundary-bridge/parts/counterpart-edge/README.md`
- `mechanics/boundary-bridge/parts/tos-support/README.md`
- `mechanics/boundary-bridge/parts/witness-compost/README.md`
- `mechanics/boundary-bridge/parts/derived-projection/README.md`
- `mechanics/boundary-bridge/parts/owner-handoff/README.md`
- `mechanics/boundary-bridge/parts/proof-review-route/README.md`
- `mechanics/boundary-bridge/parts/compatibility-route/README.md`
- `mechanics/boundary-bridge/legacy/AGENTS.md`
- `mechanics/boundary-bridge/legacy/README.md`
- `mechanics/boundary-bridge/legacy/raw/README.md`
- `mechanics/boundary-bridge/scripts/validate_boundary_bridge_distillation.py`
- `mechanics/boundary-bridge/tests/test_boundary_bridge_distillation.py`
- `mechanics/registry.json`
- `mechanics/owner-request-queue.json`
- `generated/mechanic_card_index.min.json`
- `generated/owner_request_queue.min.json`
- `scripts/validate_mechanic_landing_logs.py`
- `scripts/validate_mechanic_artifact_topology.py`
- `scripts/release_check.py`
- `tests/test_mechanic_landing_logs.py`
- `CHANGELOG.md`

Validation:

- `python mechanics/boundary-bridge/scripts/validate_boundary_bridge_distillation.py`
- `python scripts/validate_mechanics_topology.py --mechanic boundary-bridge`
- `python scripts/validate_mechanic_landing_logs.py --mechanic boundary-bridge`
- `python scripts/validate_owner_request_queue.py --mechanic boundary-bridge`

Stop-lines: no identity claim, no owner acceptance without owner-local
receipt, no derived projection as source truth, no ToS canon write from AoA,
and no bridge route as implementation authority.

Next route: carry owner-local packets through the owner-request queue before
claiming operational bridge support in sibling repositories.
