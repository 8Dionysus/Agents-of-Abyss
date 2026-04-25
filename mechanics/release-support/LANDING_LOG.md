# Release-Support Landing Log

Canonical landing ledger for the release-support mechanic.

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
