# GitHub Landing Workflow

Status: accepted

Date: 2026-04-30

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

Root `AGENTS.md` owns the GitHub landing workflow for this repository:
branch from current `origin/main`, commit the intended diff, push, open a PR,
wait for `Repo Validation`, merge through GitHub with an allowed method, then
return to clean synced `main`.

`.github/AGENTS.md` owns synchronization of GitHub-native files with that route.
`.github/CODEOWNERS` and `.github/PULL_REQUEST_TEMPLATE.md` should track current
root districts and guardrail paths.

## Rationale

The workflow applies to the whole repository, not only `.github/`. Root
`AGENTS.md` is the surface every future agent reads before touching any lane, so
it is the shortest reliable place for the rule.

Keeping `.github/` focused on platform files avoids burying repo-wide behavior in
a nested card that agents may not read when they are changing mechanics, docs,
tests, or generated surfaces.

## Consequences

- Future "commit, push, merge" requests have a named route.
- Merge-method uncertainty is handled explicitly: prefer merge commit when
  allowed, use the permitted GitHub method when repository settings require it,
  and report the landed method.
- CODEOWNERS and the PR template must be refreshed when durable root districts or
  guardrail paths change.

## Source surfaces

- `AGENTS.md`
- `.github/AGENTS.md`
- `.github/CODEOWNERS`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/repo-validation.yml`

## Follow-up route

If release-support later grows a repo-wide GitHub automation part, it may
reference this workflow, but root `AGENTS.md` remains the active route for
ordinary branch, PR, CI, and merge landings.
