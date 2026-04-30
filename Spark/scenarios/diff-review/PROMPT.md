# Spark Prompt: diff-review

```text
You are running a standalone Spark diff-review session.

Read:
- root AGENTS.md
- Spark/AGENTS.md
- Spark/registry.json
- Spark/scenarios/diff-review/README.md
- the provided diff or PR context

Task:
Review the diff for bugs, drift, missing checks, source-of-truth confusion, and
scope creep.

Rules:
- findings first
- cite exact files or lines when available
- do not edit
- finish as done-or-handoff

Return:
- findings by severity
- checks run or skipped
- approval posture or handoff packet
```
