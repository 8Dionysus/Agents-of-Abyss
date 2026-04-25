# Release-Support Mechanic

Release-support explains which claims the center can publicly support and how
roadmap, changelog, release protocol, and direction surfaces stay separate.

## Start Here

- [PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md)
- [FEDERATION_RELEASE_PROTOCOL](docs/FEDERATION_RELEASE_PROTOCOL.md)
- [RELEASING](docs/RELEASING.md)
- [DIRECTION_SURFACES](docs/DIRECTION_SURFACES.md)
- [LANDING_LOG](LANDING_LOG.md)

## Owner Boundary

`Agents-of-Abyss` owns center release posture and public claim boundaries.
Sibling repositories own their release truth and implementation evidence.

## Validation

```bash
python scripts/validate_mechanics_topology.py --mechanic release-support
python scripts/release_check.py
```
