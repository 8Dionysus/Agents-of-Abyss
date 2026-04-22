# Deployment State Machine

```text
planned
  -> approved
  -> activated
  -> watching
  -> paused
  -> promoted
  -> rolled_back
  -> quarantined
  -> completed
```

Terminal states are `rolled_back`, `quarantined`, and `completed`. `promoted` may be terminal only for the final ring. Every transition must be recorded by a watchtower decision log.
