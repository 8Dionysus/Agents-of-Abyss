# Federation Release Protocol

This note defines the shared release contract for the public AoA owner repos.

It is intentionally short.
Owner repos still keep their own `docs/RELEASING.md`, validators, and release claims.
This center note only fixes the federation-wide cadence and the minimum shared contract.

## Cadence

An owner repo becomes release-due when any of these become true:

- 48 hours have passed since the latest published release
- more than 15 meaningful commits landed since the latest tag
- public-surface drift exists since the latest tag

Public-surface drift includes at least:

- `README.md`
- `CHANGELOG.md`
- `docs/`
- `generated/`
- `schemas/`
- `.github/workflows/`
- package or version files

## Release completeness

A release is not done when only code lands.
A release is done only when these agree in one landed state:

- repo-local release docs
- repo-local release verifier
- latest tagged changelog section
- exact README current-release banner
- version files where they exist
- local tag and remote tag
- published GitHub Release
- latest GitHub Release marker
- GitHub Release body built from the latest changelog section

## Required preflight

Before publication, the owner repo must pass:

- clean tracked worktree
- `main` synced with `origin/main`
- `docs/RELEASING.md` exists
- `scripts/release_check.py` exists and passes
- latest tagged changelog section keeps `Summary`, `Validation`, and `Notes`
- README shows the exact current-release banner
- version-bearing files match the latest release version where they exist

## Required postpublish

After publication, the owner repo must pass:

- matching remote tag exists
- matching GitHub Release exists
- matching GitHub Release is latest
- the GitHub Release body keeps the canonical shape:
  - `Released`
  - `Canonical changelog`
  - `## Highlights`
  - `## Full Release Notes`
- `origin/main:README.md` still shows the same current-release banner

## Publication path

Use the bounded control-plane helper from `aoa-sdk`:

- `aoa release audit /srv --phase preflight --all --strict --json`
- `aoa release publish /srv --repo <repo>|--all-due --dry-run|--confirm --json`
- `aoa release audit /srv --phase postpublish --all --strict --json`

Manual shell publication is no longer the supported federation path.
