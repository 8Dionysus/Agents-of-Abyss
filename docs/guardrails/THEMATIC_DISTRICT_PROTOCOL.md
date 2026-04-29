# Thematic District Protocol

This protocol keeps `docs/` readable as the center grows.

`docs/` root is for current center doctrine, route law, owner maps, and local agent gates. It must not become a flat archive of every audit, seed, receipt, drift note, migration trace, mechanic-specific legacy record, and compatibility alias.

## Districts

| District | Role |
|---|---|
| `docs/guardrails/` | validator law, hygiene protocol, AGENTS mesh law, generated index source maps, and docs cleanup classifier |
| `docs/registry/` | registry evolution, schema/capsule notes, generated-index planning, and inventory design |
| `docs/decisions/` | decision records explaining why a route, owner split, or doctrine placement was chosen |
| `docs/traces/` | migration evidence, provenance logs, link-rewrite traces, move manifests, and generic receipts |

Mechanic-owned history is not a docs district. It belongs under `mechanics/<slug>/legacy/` and should be connected through that mechanic's `PROVENANCE.md` or `LANDING_LOG.md`.

Audit evidence, cleanup review, drift review, and inspect-first candidate lists now route through `mechanics/audit/`. Owner-bound retrospectives are also owner history. Put them in the owning mechanic or repository legacy route.

Agent guidance is not a docs archive class. Promote active rules into the root
or nearest owner `AGENTS.md`, a validator, or a mechanic package.

## Current root rule

A file may remain flat under `docs/` only when it is current doctrine, current map, current route law, or a local gate for agents.

Historical material must remain reviewable but must not stand beside current doctrine as if it had equal authority.

## Promotion rule

A district document may influence current law only through an explicit promotion path:

1. name the surviving canonical surface,
2. preserve provenance,
3. update links and generated indexes,
4. run validators,
5. explain whether old material remains receipt, audit, decision, trace, mechanic legacy record, owner retrospective, or registry note.

## Migration rule

Use `docs/guardrails/thematic_districts.json` as the classifier and `scripts/plan_docs_thematic_cleanup.py` as the planner. If a file matches multiple districts, the classifier tie-break order decides where the historical surface lives.

Do not move source truth into this repository. The docs thematic cleanup only classifies center-local docs surfaces and routes mechanic-specific material back to the owning mechanic package.

## Generated rule

`generated/docs_thematic_index.min.json` reflects `docs/guardrails/thematic_districts.json`. It does not author meaning.

## Validation

Use `AGENTS.md` in this directory for the current command lane.
