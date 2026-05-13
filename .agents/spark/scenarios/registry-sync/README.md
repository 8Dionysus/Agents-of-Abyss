# Spark Scenario: registry-sync

Use `registry-sync` when a file moved or appeared and its README, AGENTS,
registry, validator, or release gate needs alignment.

## Scope

One district or one registry family.

## Done Signal

Registered paths and local docs agree with validators.

## Stop-line

Do not create a new source of truth while syncing derived routes.

## Handoff Route

Write a handoff when the registry change implies a new authority boundary or
source contract.

## Validation

Run the local registry validator and any targeted tests for that district.
