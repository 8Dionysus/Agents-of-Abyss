# Spark Prompt: audit

```text
You are running a standalone Spark audit session.

Read:
- root AGENTS.md
- Spark/AGENTS.md
- Spark/registry.json
- Spark/scenarios/audit/README.md

Task:
Audit the named scope for drift, noise, duplicate meaning, stale paths, weak
owner routing, and missing validation.

Rules:
- audit first
- do not edit unless the user explicitly requested fixes
- keep one scope
- finish as done-or-handoff

Return:
- scope read
- findings with file paths
- likely owner route
- validation implication
- done result or handoff packet
```
