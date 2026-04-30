# Spark Scenario: micro-patch

Use `micro-patch` for one small patch when the source of truth is already
clear.

## Scope

One small file family and one local validation path.

## Done Signal

One bounded patch is applied and validated.

## Stop-line

Stop when the patch asks for a second owner or broader design.

## Handoff Route

Write a handoff when the patch uncovers source ambiguity, owner conflict, or a
larger migration.

## Validation

Run the nearest local validator plus `git diff --check`.
