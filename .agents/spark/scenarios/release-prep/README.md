# Spark Scenario: release-prep

Use `release-prep` for a fast release readiness pass before release-support or
GitHub publication hardens a claim.

## Scope

One release candidate, one repo, or one bounded release surface.

## Done Signal

Release risks, checks, and owner routes are named.

## Stop-line

Do not publish or tag from Spark without explicit user command.

## Handoff Route

Write a handoff when release wording needs public-claim judgment, owner
acceptance, or multi-repo synthesis.

## Validation

Run `python scripts/release_check.py` when local dependencies are available.
