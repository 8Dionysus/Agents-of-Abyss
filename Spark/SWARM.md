# Spark Swarm

Use this file only when a user explicitly asks for a Spark swarm. Ordinary
Spark work starts from one scenario in `Spark/registry.json`.

## Swarm Rule

A swarm still follows the Spark lane contract:

- one coordinator
- one registered scenario per worker
- one bounded file family per writer
- no in-session switch to a larger model
- every lane ends as `done` or `handoff`

## Read Before Launch

- root `AGENTS.md`
- `Spark/README.md`
- `Spark/AGENTS.md`
- `Spark/registry.json`
- scenario `README.md` and `PROMPT.md` for every assigned lane

## Roles

| Role | Work |
|---|---|
| Coordinator | chooses the scenario, exact scope, risks, and validation path |
| Scout | reads and reports findings without editing |
| Builder | makes one bounded patch inside the assigned scope |
| Verifier | runs the named validation and reports skipped checks |
| Boundary Keeper | checks that Spark did not absorb stronger owner truth |

## Parallel Lanes

Allowed parallelism:

- one audit lane plus one verifier lane
- one builder lane per disjoint file family
- one boundary review lane after a patch exists

Do not run two writers on the same family of files.

## Coordinator Launch Packet

```text
We are working in Agents-of-Abyss through Spark.
Choose one registered scenario from Spark/registry.json.

Return:
1. scenario id
2. exact scope
3. files to read first
4. expected done signal
5. handoff condition
6. validation command
```

## Worker Launch Packet

```text
You are a Spark worker.
Read Spark/AGENTS.md, Spark/registry.json, and the assigned scenario.
Finish the assigned scope or leave a handoff packet.
Do not widen into another scenario.
Report files read, files changed, validation run, skipped checks, and risk.
```

## Verify

```bash
python Spark/scripts/validate_spark_lane.py
python -m pytest -q Spark/tests/test_spark_lane.py
```
