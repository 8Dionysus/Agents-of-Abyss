# Installation Authority

Version: 1.0.0

## Purpose

Defines who may propose, prepare, approve, seal, execute, roll back, revoke, and audit v1.0 actions.

This document belongs to the v1.0 installation and first sovereign release wave. It turns the experience program from forged seed into installable order: landing, migration, smoke testing, operator review, first live assistant office, governed release, rollback drill, replay audit, and post-release watch.

## Owns

- authority roles
- denied capabilities
- conflict guards

## Must not do

- Codex sovereign authority
- self-approval
- stale authority cache

## Flow

```text
seed prepared
  -> landing order
  -> migration
  -> smoke tests
  -> operator review
  -> sovereign release seal
  -> rollback drill
  -> post-release watch
```

## Invariants

- Codex may prepare, inspect, propose, simulate, and report.
- Codex may not certify, seal, promote, suppress material evidence, or execute a durable release by itself.
- Assistant offices grow through reviewed versions, not hidden self-rewrites.
- Agonic actors grow through trials, scars, rank changes, and retention, not service release laundering.
- Tree-of-Sophia receives dossiers and boundary notes only after proper promotion; it is not a runtime landing target.
- Stats summarizes. Memo remembers. Evals judges. Routing points. Owners change their own surfaces.

## Exit signal

This surface is ready when it can produce a typed artifact, route it to the true owner, survive replay, and fail closed when authority is missing.
