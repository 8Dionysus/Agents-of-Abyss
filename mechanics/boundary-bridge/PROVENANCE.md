# Boundary Bridge Provenance

This file is the default bridge from active boundary-bridge parts to source
doctrine and historical ToS-support context.

Use it when you are auditing how a bridge source feeds an active part, not when
you need the current operating contract.

## Current route first

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts/](parts/)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)

If those surfaces answer the task, stop there. Do not pull ToS-support source
history into the active route.

## Active doctrine sources

| Source | Distilled into | Notes |
|---|---|---|
| [COUNTERPART_BRIDGE](docs/COUNTERPART_BRIDGE.md) | `parts/counterpart-edge`, `parts/non-identity-guard`, `parts/derived-projection` | AoA-side counterpart law and anti-collapse doctrine. |
| [WITNESS_COMPOST](docs/WITNESS_COMPOST.md) | `parts/witness-compost`, `parts/proof-review-route`, `parts/owner-handoff` | Witness and compost support route. |
| [TOS_GROWTH_SUPPORT](docs/TOS_GROWTH_SUPPORT.md) | `parts/tos-support`, `parts/owner-handoff` | ToS growth support without AoA authorship. |
| [TOS_TEMPLATE_SUPPORT](docs/TOS_TEMPLATE_SUPPORT.md) | `parts/tos-support`, `parts/compatibility-route` | ToS scaffold support without template ownership transfer. |
| [TOS_LINEAGE_PILOT_SUPPORT](docs/TOS_LINEAGE_PILOT_SUPPORT.md) | `parts/tos-support`, `parts/boundary-contract` | ToS lineage pilot support without branch authorship. |
| [TOS_SOIL_PREP_SUPPORT](docs/TOS_SOIL_PREP_SUPPORT.md) | `parts/tos-support`, `parts/boundary-contract` | Soil preparation support without claiming active expansion. |
| [OWNER_REQUESTS](OWNER_REQUESTS.md) | `parts/owner-handoff`, `parts/proof-review-route` | Center-side owner-local request packets. |

## Tree-of-Sophia source anchors

The ToS side of this bridge is stronger than AoA support language. Relevant
ToS owner surfaces include:

- `/srv/AbyssOS/Tree-of-Sophia/BOUNDARIES.md`
- `/srv/AbyssOS/Tree-of-Sophia/docs/COUNTERPART_POLICY.md`
- `/srv/AbyssOS/Tree-of-Sophia/docs/CONTEXT_COMPOST.md`
- `/srv/AbyssOS/Tree-of-Sophia/docs/GROWTH_STRUCTURE.md`
- `/srv/AbyssOS/Tree-of-Sophia/docs/CALIBRATION_LINEAGE_PILOT.md`
- `/srv/AbyssOS/Tree-of-Sophia/docs/PRE_EXPANSION_SOIL.md`
- `/srv/AbyssOS/Tree-of-Sophia/docs/*_NODE_TEMPLATE.md`

These are provenance anchors for humans and agents working in the shared
workspace. They are not files owned by this repository.

## Legacy raw sources

No raw source file was moved during this landing. The previous `tos-bridge`
package was renamed and distilled in place because its docs remain active
source doctrine for the ToS-support part.

Future raw bridge packets belong under `legacy/raw/` and should be listed here
before any active part cites them.

## Historical slug

`tos-bridge` was the old mechanic slug. It now survives only as historical
language in this provenance trail, old release history, or old ToS-specific
source titles. The canonical mechanic slug is `boundary-bridge`.

## Distillation rule

Do not copy old wave prose into active parts. Distill the route, keep the trace
here, and leave owner-local truth with the owner repository.
