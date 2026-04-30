# Spark Scenario: audit

Use `audit` for fast drift, noise, duplicate, broken route, and path hygiene
passes.

## Scope

Read-only by default. Touch files only when the user explicitly asks for audit
plus fix.

## Done Signal

Findings are scoped, evidenced, and routed to the correct owner or validator.

## Stop-line

Do not rewrite the audited surface during audit-only work.

## Handoff Route

Write a handoff when findings require architecture, owner-local decisions,
large rewrites, or cross-repo synthesis.

## Validation

Use the smallest validator tied to the audited surface. If no validator exists,
report a manual consistency pass.
