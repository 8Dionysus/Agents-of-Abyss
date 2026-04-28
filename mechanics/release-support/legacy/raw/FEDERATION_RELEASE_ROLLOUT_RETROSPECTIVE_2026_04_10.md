# 2026-04-10 Federation Release Rollout Retrospective

This is a no-blame retrospective for the April 10, 2026 owner-repo release pass.

Current release-support work should not start here. Use
`mechanics/release-support/README.md`, `PARTS.md`, and `PROVENANCE.md` first.
This file is retained as raw historical evidence for the release-support
mechanic.

## What went wrong

- code, changelog, tag, README, and GitHub Release were treated as neighboring tasks rather than one release contract
- release ranges had grown too large in several repos, so change harvest and narrative accuracy became fragile
- GitHub Release objects were published later than tags and merged release-prep commits
- validation existed repo-by-repo, but there was no single federation preflight or postpublish audit

## Why it happened

- release cadence had drifted from bounded frequent publication into large catch-up batches
- owner repos had uneven release baselines
- there was no single control-plane command that could answer “is this release actually complete?”
- the visible public surfaces on GitHub were checked too late

## What we are changing

- owner repos now become release-due every 48 hours, after 15 meaningful commits, or when public-surface drift appears
- every owner repo now needs `docs/RELEASING.md` and `scripts/release_check.py`
- changelog release sections now require `Summary`, `Validation`, and `Notes`
- release publication now routes through `aoa release audit` and `aoa release publish`
- GitHub Releases are now treated as mandatory release surfaces rather than optional polish

## Guardrails going forward

- keep releases small enough that reviewers can reason about them directly
- keep `Unreleased` current instead of reconstructing dozens of commits at release time
- never call a release “done” until the GitHub Release page, README banner, and tag all agree
- keep `8Dionysus` out of owner-repo release mutation
