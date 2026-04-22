# Experience v0.5: Deployment & Watchtower

v0.5 governs what happens after a certified assistant/service release is allowed to enter the world. Certification says a version may be released. Deployment watchtower asks whether it should keep advancing, pause, roll back, or re-enter the experience loop as a new incident.

The watchtower is not a judge of truth and not a source of agent identity. It is a post-release guardian that reads runtime evidence, asks bounded evals for verdicts, routes incidents, and keeps rollback reachable.

## Flow

```text
release_candidate.certified
  -> deployment_plan
  -> activation
  -> ring_0_internal
  -> canary_probe_matrix
  -> watch_record stream
  -> drift_alarm / clean_health
  -> ring_promotion_decision
  -> rollback_trigger or next_ring
  -> post_release_retention_result
```

The release is not mature until its watch window has closed and retention checks confirm that the patch holds under real recurrence pressure.
