# Scenario Choreography

Scenario Choreography routes recurring return patterns into playbook-owned
method instead of letting center prose become a workflow engine.

## Use When

- Return has become a repeated scenario shape.
- A route needs fallback, rollback, review gate, safe stop, or phase re-entry.
- Evidence expectations must be named for a recurring return route.

## Do Not Use When

- The center is only naming the recurrence law.
- The route needs runtime implementation or memory writeback rather than scenario method.
- The playbook would become hidden orchestration or automatic spawning logic.

## Route Check

Ask whether the recurrence shape repeats as scenario method. If yes, route to
`aoa-playbooks`; if no, keep it as center law or owner request.

## Active Outputs

- playbook request
- return-trigger language
- valid-anchor class
- re-entry mode
- fallback or safe-stop route

## Next Route

Route scenario method to `aoa-playbooks`, proof to `aoa-evals`, actor posture
to `aoa-agents`, memory support to `aoa-memo`, and runtime execution to
`abyss-stack` after runtime gates.
