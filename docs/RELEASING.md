# Releasing Route

This is the repo-level release entry required by the federation release audit.
It keeps the GitHub release route visible from `docs/` while the
release-support mechanic owns the active runbook.

Use this surface when preparing or publishing an `Agents-of-Abyss` GitHub
release.

## Route

1. Start from a clean branch based on the current `origin/main`; keep the
   release-prep diff limited to the named release surfaces.
2. Prepare `CHANGELOG.md`, the `README.md` release banner, and the `ROADMAP.md`
   released contour.
3. Run the broad local gate through the repository validation map and inspect
   the complete diff, status, and release metadata.
4. Commit only the intended release-prep diff, push the branch, and open a PR
   with changed surfaces, validation, skipped checks, and remaining risk.
5. Wait for GitHub `Repo Validation` to finish. If it fails, fix the branch and
   wait for the replacement result before continuing.
6. Merge through GitHub using the currently allowed method (repository
   settings reject merge commits today, so use squash unless that changes),
   then return to `main` and fast-forward from `origin/main`.
7. Run federation release preflight for this repository.
8. Publish through the bounded release helper, first as a dry run, then with
   confirmation.
9. Run federation postpublish audit and verify the tag and GitHub Release.
10. Confirm the post-landing worktree is clean and report the method that
    landed. If GitHub status or merge permission cannot be observed, stop and
    report that blocker instead of guessing.

## Source Surfaces

- `CHANGELOG.md`
- `README.md`
- `ROADMAP.md`
- `mechanics/release-support/docs/RELEASING.md`
- `mechanics/release-support/docs/FEDERATION_RELEASE_PROTOCOL.md`
- `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md`
- `scripts/release_gate/release_check.py`

## Boundary

This route proves only the center-owned GitHub release path for this
repository. Sibling repositories keep their own owner-local release truth,
acceptance, proof, runtime, SDK, and rollback surfaces.

## Validation

Use root `AGENTS.md`, `docs/AGENTS.md`, and
`mechanics/release-support/AGENTS.md` for executable validation commands.
