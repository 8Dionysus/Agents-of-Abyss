# Release-Support Landing Log

Canonical landing ledger for the release-support mechanic.

## Route index for agents

Read this index before scanning the full ledger. It names the current shape of
Release-support without requiring every older landing entry to be re-read.

- Root mechanics topology migration: first package landing for center release
  posture and public claim boundaries.
- Release-support state-transition distillation: release widened from GitHub-only posture into an internal state-transition mechanic with active parts.
- Current active route: `mechanics/release-support/README.md`,
  `mechanics/release-support/DIRECTION.md`,
  `mechanics/release-support/PARTS.md`,
  `mechanics/release-support/parts/README.md`, and the relevant part README.
- Current owner pressure route: `mechanics/release-support/OWNER_REQUESTS.md`.
- Current future-pressure route: `mechanics/release-support/ROADMAP.md`.
- Current provenance bridge: `mechanics/release-support/PROVENANCE.md`; use it
  only when auditing source provenance or release-support history.

## How to update this log

Every landing entry uses the same shape:

- `Status:`
- `Owner boundary:`
- `Surfaces:`
- `Validation:`
- `Stop-lines:`
- `Next route:`

When a change touches Release-support docs, parts, owner requests, source
bridges, validators, or tests, update the relevant entry here or explain in
the PR why the change is not a landing change.

## Entries

### Root mechanics topology migration

Status: landed

Owner boundary: `Agents-of-Abyss` owns center release posture and public claim
boundaries; sibling repositories own local release truth.

Surfaces:

- `mechanics/release-support/README.md`
- `mechanics/release-support/ROADMAP.md`
- `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md`
- `mechanics/release-support/docs/FEDERATION_RELEASE_PROTOCOL.md`
- `mechanics/release-support/docs/RELEASING.md`
- `mechanics/release-support/docs/DIRECTION_SURFACES.md`

Validation: `python scripts/validate_mechanics_topology.py --mechanic release-support`

Stop-lines: no unverified public claim, sibling release truth, or roadmap to
changelog substitution.

Next route: use root `CHANGELOG.md` for release history and root `ROADMAP.md`
for program direction.

### Release-support state-transition distillation

Status: landed

Owner boundary: `Agents-of-Abyss` owns transition gates, release posture, public support boundaries, direction-surface routing, and owner handoff stop-lines. Owning mechanics and sibling repositories own content, acceptance, proof, runtime state, projection, and implementation truth.

Surfaces:

- `mechanics/release-support/AGENTS.md`
- `mechanics/release-support/README.md`
- `mechanics/release-support/DIRECTION.md`
- `mechanics/release-support/PARTS.md`
- `mechanics/release-support/OWNER_MAP.md`
- `mechanics/release-support/PROVENANCE.md`
- `mechanics/release-support/OWNER_REQUESTS.md`
- `mechanics/release-support/ROADMAP.md`
- `mechanics/release-support/LANDING_LOG.md`
- `mechanics/release-support/docs/RELEASE_SUPPORT_OWNER_REPO_REQUESTS.md`
- `mechanics/release-support/parts/AGENTS.md`
- `mechanics/release-support/parts/README.md`
- `mechanics/release-support/parts/state-transition-gate/README.md`
- `mechanics/release-support/parts/public-claim-gate/README.md`
- `mechanics/release-support/parts/release-runbook/README.md`
- `mechanics/release-support/parts/changelog-roadmap-split/README.md`
- `mechanics/release-support/parts/landing-closeout/README.md`
- `mechanics/release-support/parts/owner-handoff-packet/README.md`
- `mechanics/release-support/parts/sibling-evidence-route/README.md`
- `mechanics/release-support/parts/rollback-return/README.md`
- `mechanics/release-support/parts/direction-surface-review/README.md`
- `mechanics/release-support/legacy/AGENTS.md`
- `mechanics/release-support/legacy/README.md`
- `mechanics/release-support/legacy/raw/README.md`
- `mechanics/release-support/scripts/validate_release_support_distillation.py`
- `mechanics/registry.json`
- `mechanics/owner-request-queue.json`
- `generated/mechanic_card_index.min.json`
- `generated/owner_request_queue.min.json`
- `scripts/release_check.py`
- `scripts/validate_mechanic_landing_logs.py`
- `tests/test_mechanic_landing_logs.py`
- `CHANGELOG.md`

Validation: `python mechanics/release-support/scripts/validate_release_support_distillation.py`; `python scripts/validate_mechanics_topology.py --mechanic release-support`; `python scripts/validate_mechanic_landing_logs.py --mechanic release-support`; `python scripts/release_check.py`

Stop-lines: no GitHub-only definition of release, unverified public claim,
sibling acceptance without receipt, generated release authority, roadmap
history as changelog, or hidden rollback debt.

Next route: carry release proof to `aoa-evals`, derived release movement to
`aoa-stats`, route ABI to `aoa-routing`, helper support to `aoa-sdk`, public
projection to `8Dionysus`, runtime deployment/rollback to `abyss-stack`, and
content changes to the owning mechanic or sibling repository.
