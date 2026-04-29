# ADR: Federation Release Contract

Status: accepted
Date: 2026-04-10

## Context

The owner-repo release pass on 2026-04-10 exposed a repeated weakness:
release truth was split across code, changelog, README, tags, CI, and GitHub Releases without one bounded shared contract.

The federation already had strong repo-local validation in several places, but it did not have one control-plane release audit or one shared cadence rule.

## Options considered

1. Keep release rules repo-local and let each owner choose cadence and checks.
2. Define one shared release contract while keeping repo-local validators as the
   source of repository truth.
3. Centralize release truth entirely in a control-plane publisher.

## Decision

The public owner repos now follow one shared release contract:

- release cadence is `48h or 15 commits or public-surface drift`
- every owner repo must ship `mechanics/release-support/docs/RELEASING.md`
- every owner repo must ship `scripts/release_check.py`
- the latest tagged changelog section must include `Summary`, `Validation`, and `Notes`
- README must show the exact current-release banner
- release publication must go through `aoa release audit` and `aoa release publish`

`8Dionysus` remains outside owner-repo publication and mutation.

## Rationale

- smaller release windows improve changelog honesty
- one shared audit surface reduces “release looked done locally but broken on GitHub”
- repo-local verifiers preserve owner boundaries
- a control-plane publisher keeps publication reviewable without absorbing sibling meaning

## Consequences

- owner repos must carry a minimal release baseline even when they are docs-heavy or early-stage
- CI now needs one standard `Release Audit` path
- local ad-hoc release shell chains stop being the supported federation path
- release debt becomes visible earlier instead of hiding inside long `Unreleased` spans

## Source surfaces

- `mechanics/release-support/docs/RELEASING.md`
- `scripts/release_check.py`
- owner repository `CHANGELOG.md` and README release banners
- `aoa release audit`
- `aoa release publish`

## Follow-up route

Route future release-process changes through `mechanics/release-support/` and
owner repository release checks before changing public release promises.
