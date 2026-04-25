# Experience Rollout Rings

Rings provide graduated exposure. The default sequence is:

```text
ring_0_internal -> ring_1_pilot -> ring_2_limited -> ring_3_general
```

Each ring defines population, duration, canary probes, alarm thresholds, promotion criteria and rollback behavior. A ring is not a social label. It is an authority gate over exposure.

Promotion requires clean canary results, no open critical alarms, rollback readiness, and an authorized promotion actor.
