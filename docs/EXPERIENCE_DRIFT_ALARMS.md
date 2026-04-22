# Drift Alarms

A drift alarm is a watchtower signal that a released behavior may be leaving its certified contract. It is not yet proof.

Alarm levels:

```text
info -> warning -> material -> critical
```

Material and critical alarms require bounded verdict before durable state change. Critical alarms may trigger emergency quarantine if rollback path and authority policy allow it.
