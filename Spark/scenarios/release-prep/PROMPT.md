# Spark Prompt: release-prep

```text
You are running a standalone Spark release-prep session.

Read:
- root AGENTS.md
- Spark/AGENTS.md
- Spark/registry.json
- Spark/scenarios/release-prep/README.md
- mechanics/release-support/README.md
- the release surface named by the user

Task:
Check release readiness: changed surfaces, validation, public claims, owner
routes, rollback shape, and remaining risks.

Rules:
- do not publish, tag, or merge unless explicitly asked
- keep public claims supportable
- finish as done-or-handoff

Return:
- release scope
- checks run
- blocking risks
- public claim risks
- next owner route
```
