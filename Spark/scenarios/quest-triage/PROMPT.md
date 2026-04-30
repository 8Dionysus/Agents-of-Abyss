# Spark Prompt: quest-triage

```text
You are running a standalone Spark quest-triage session.

Read:
- root AGENTS.md
- Spark/AGENTS.md
- Spark/registry.json
- Spark/scenarios/quest-triage/README.md
- mechanics/questbook/AGENTS.md
- the quest or source cluster named by the user

Task:
Classify durable obligations as quest candidates, owner requests, roadmap notes,
or no-op findings.

Rules:
- do not create public obligations from scratch notes
- keep Questbook source contract intact
- finish as done-or-handoff

Return:
- items triaged
- lane decision
- files changed or not changed
- validation run
- handoff if owner judgment is needed
```
