# Deployment Event Kind Registry

Canonical event kinds:

```text
experience.deployment.plan.created
experience.deployment.ring.activated
experience.canary.probe.ran
experience.watch.record.observed
experience.drift.alarm.raised
experience.rollback.triggered
experience.rollback.executed
experience.ring.promotion.decided
experience.incident.reentered
experience.retention.post_release.checked
experience.deployment.completed
```

Unknown names should fail validation before dashboard generation.
