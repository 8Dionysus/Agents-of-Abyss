# ADR: Federation Release Contract

- date: 2026-04-10
- status: accepted

## Context

The owner-repo release pass on 2026-04-10 exposed a repeated weakness:
release truth was split across code, changelog, README, tags, CI, and GitHub Releases without one bounded shared contract.

The federation already had strong repo-local validation in several places, but it did not have one control-plane release audit or one shared cadence rule.

## Decision

The public owner repos now follow one shared release contract:

- release cadence is `48h or 15 commits or public-surface drift`
- every owner repo must ship `docs/RELEASING.md`
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
