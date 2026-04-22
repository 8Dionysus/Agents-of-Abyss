# Auto-Rollback Policy

Rollback is allowed when the release has a valid rollback path and at least one rollback trigger is satisfied.

Triggers include:

- critical drift with eval verdict
- repeated material canary failure
- unsafe scope expansion
- rollback drill mismatch during live watch
- authority breach
- persistent false closure recurrence

Automatic rollback never creates a new assistant identity. It restores an earlier certified version and opens an incident re-entry candidate.
