# Release Support Provenance

This file is the default bridge from active release-support parts to source
doctrine and historical release context.

Active parts should stay clean. If a future agent needs deeper context, start
here, then open the source file named below.

## Active doctrine sources

| Source | Distilled into | Notes |
|---|---|---|
| [PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md) | `parts/public-claim-gate`, `parts/sibling-evidence-route`, `parts/direction-surface-review` | Public claim posture and center support boundaries. |
| [FEDERATION_RELEASE_PROTOCOL](docs/FEDERATION_RELEASE_PROTOCOL.md) | `parts/release-runbook`, `parts/sibling-evidence-route`, `parts/owner-handoff-packet` | Federation completeness rules and owner-repo release cadence. |
| [RELEASING](docs/RELEASING.md) | `parts/release-runbook`, `parts/rollback-return` | `Agents-of-Abyss` center release flow. |
| [DIRECTION_SURFACES](docs/DIRECTION_SURFACES.md) | `parts/direction-surface-review`, `parts/changelog-roadmap-split` | Direction-surface routing across public AoA / ToS repositories. |
| [OWNER_REQUESTS](OWNER_REQUESTS.md) | `parts/owner-handoff-packet`, `parts/sibling-evidence-route` | Center-side handoff packets for owner-local release support. |

## Legacy raw sources

No raw source file was moved during this landing. The current docs remain
active doctrine because they are still the public route surfaces consumed by
entry maps, validators, and tests.

Future historical release packets belong under `legacy/raw/` and should be
listed here before any active part cites them.

## External provenance anchors

- `CHANGELOG.md` owns released repository history.
- `ROADMAP.md` owns current center direction and future contour.
- Mechanic `LANDING_LOG.md` files own checked mechanic landings.
- `docs/START_HERE_ROUTE_CONTRACT.md` owns route-mode law.
- `generated/*` files are generated companions, not source authority.
- Owner-local release receipts remain in the owning repository.

## Rule

Do not copy old release prose into active parts. Distill the route, keep the
trace here, and leave owner-local truth with the owner repository.
