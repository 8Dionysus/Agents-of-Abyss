# Releasing Route

This is the repo-level release entry required by the federation release audit.
It keeps the GitHub release route visible from `docs/` while the
release-support mechanic owns the active runbook.

Use this surface when preparing or publishing an `Agents-of-Abyss` GitHub
release.

## Route

1. Prepare release surfaces: `CHANGELOG.md`, the `README.md` release banner,
   and the `ROADMAP.md` released contour.
2. Run the broad local gate through `scripts/release_check.py`.
3. Merge the release-prep PR to `main` after GitHub `Repo Validation` is green.
4. Run federation release preflight for this repository.
5. Publish through the bounded release helper, first as a dry run, then with
   confirmation.
6. Run federation postpublish audit and verify the tag and GitHub Release.

## Source Surfaces

- `CHANGELOG.md`
- `README.md`
- `ROADMAP.md`
- `mechanics/release-support/docs/RELEASING.md`
- `mechanics/release-support/docs/FEDERATION_RELEASE_PROTOCOL.md`
- `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md`
- `scripts/release_check.py`

## Boundary

This route proves only the center-owned GitHub release path for this
repository. Sibling repositories keep their own owner-local release truth,
acceptance, proof, runtime, SDK, and rollback surfaces.

## Validation

Use root `AGENTS.md`, `docs/AGENTS.md`, and
`mechanics/release-support/AGENTS.md` for executable validation commands.
