# Spark Scenario: diff-review

Use `diff-review` to review a concrete diff or PR for bugs, drift, missed
validators, and scope creep.

## Scope

Review only the provided diff or PR.

## Done Signal

Findings are ordered by risk and tied to exact files.

## Stop-line

Do not rewrite the diff while acting as reviewer.

## Handoff Route

Write a handoff when the review exposes a broader design problem or needs owner
judgment outside the diff.

## Validation

Run read-only checks when useful, such as `git diff --check` or the changed
surface validator.
