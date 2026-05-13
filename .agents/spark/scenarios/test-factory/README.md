# Spark Scenario: test-factory

Use `test-factory` to add a bounded set of tests for a contract that already
has a source surface.

## Scope

One contract, one test family, one validation path.

## Done Signal

Tests cover a named existing contract and pass locally.

## Stop-line

Do not invent new semantics to make tests interesting.

## Handoff Route

Write a handoff when the invariant is unclear or needs deeper source-of-truth
work before tests can be honest.

## Validation

Run the targeted test and the validator named by the owning source surface.
