# GitHub Landing Workflow

- Decision ID: AOA-CENTER-D-0017

## Status

Superseded.

## Index Metadata

- Original date: 2026-04-30
- Surface classes: release workflow, root surface
- Center facets: github landing
- Mechanic parents: release-support
- Guard families: GitHub landing, release/tooling
- Posture: superseded prompt placement; landing workflow retained in an on-demand owner route

## Context

AoA now uses many small PR landings across mechanics, root districts, generated
surfaces, and platform configuration. The repeated "commit, push, merge" route
needs to be legible to future agents without relying on session memory.

The concrete failure mode was repeated uncertainty around merge-commit
availability and post-PR synchronization. That uncertainty belongs in the repo
workflow guidance, not in each individual PR conversation.

## Options considered

- Keep the workflow implicit in operator habit and previous session history.
- Put the complete GitHub process only in `.github/AGENTS.md`.
- Put the landing route in root `AGENTS.md` and let `.github/` keep the
  platform files aligned with it.

## Decision

At the time of this decision, root `AGENTS.md` owned the complete GitHub landing
workflow for this repository: branch from current `origin/main`, commit the
intended diff, push, open a PR, wait for `Repo Validation`, merge through GitHub
with an allowed method, then return to clean synced `main`.

The prompt-placement part of this decision is superseded by
[`AOA-CENTER-D-0042-separate-inherited-agent-routes-from-human-readmes`](AOA-CENTER-D-0042-separate-inherited-agent-routes-from-human-readmes.md).
The landing contract survives in `docs/RELEASING.md`. Root `AGENTS.md` keeps a
compact route and the stop-line for unobservable CI or merge authority instead
of carrying the full procedure in inherited context.

`.github/AGENTS.md` owns synchronization of GitHub-native files with that route.
`.github/CODEOWNERS` and `.github/PULL_REQUEST_TEMPLATE.md` should track current
root districts and guardrail paths.

## Rationale

The workflow applies to the whole repository, not only `.github/`. The original
placement made it visible to every future agent, but it also made an exact
landing procedure recurring prompt context for work that never lands a change.
The current split preserves discoverability through a compact root route and
keeps the complete human procedure on demand.

Keeping `.github/` focused on platform files avoids burying repo-wide behavior in
a nested card that agents may not read when they are changing mechanics, docs,
tests, or generated surfaces.

## Consequences

- Future "commit, push, merge" requests have a named route.
- Root `AGENTS.md` names that route and its stop-line; `docs/RELEASING.md`
  carries the complete procedure.
- Merge-method uncertainty is handled explicitly: prefer merge commit when
  allowed, use the permitted GitHub method when repository settings require it,
  and report the landed method.
- CODEOWNERS and the PR template must be refreshed when durable root districts or
  guardrail paths change.

## Source surfaces

- `AGENTS.md`
- `docs/RELEASING.md`
- `.github/AGENTS.md`
- `.github/CODEOWNERS`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/repo-validation.yml`

## Follow-up route

Keep the ordinary branch, PR, CI, merge, and post-landing sync procedure in
`docs/RELEASING.md`, with release-publication detail routed to the
release-support mechanic. If platform behavior changes, update the procedure,
root route, `.github/` support surfaces, and their validators together.
