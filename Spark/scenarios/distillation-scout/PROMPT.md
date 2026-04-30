# Spark Prompt: distillation-scout

```text
You are running a standalone Spark distillation-scout session.

Read:
- root AGENTS.md
- Spark/AGENTS.md
- Spark/registry.json
- Spark/scenarios/distillation-scout/README.md
- the legacy/raw sources named by the user

Task:
Map raw sources to likely active homes, provenance entries, owner requests, or
handoff needs.

Rules:
- scout only
- preserve provenance
- do not rewrite active doctrine unless explicitly requested
- finish as done-or-handoff

Return:
- sources read
- likely active homes
- omitted or risky material
- validation implication
- handoff packet if deeper distillation is needed
```
