# Thematic District Protocol

This protocol keeps `docs/` readable as the center grows.

`docs/` root is for current center doctrine, route law, owner maps, and local agent gates. It must not become a flat archive of every wave, audit, seed, receipt, drift note, migration trace, mechanic-specific legacy record, and compatibility alias.

## Districts

| District | Role |
|---|---|
| `docs/agent-lane/` | Agent-lane references that support, but do not replace, `AGENTS.md`. |
| `docs/audits/` | Audit evidence, cleanup candidates, drift review, review protocols, and inspect-first lists. |
| `docs/landings/` | Historical seed manifests, wave receipts, landing notes, and planted-change evidence. |
| `docs/registry/` | Registry evolution, schema/capsule notes, generated-index planning, and inventory design. |
| `docs/decisions/` | Decision records explaining why a route, owner split, or doctrine placement was chosen. |
| `docs/postmortems/` | Failure-learning, incident review, repair retrospectives, and improvement loops. |
| `docs/traces/` | Migration evidence, provenance logs, link-rewrite traces, and before/after maps. |
| `docs/agon/` | Historical or transitional Agon center records not owned by current `mechanics/agon/` surfaces. |
| `docs/experience/` | Historical or transitional Experience center records not owned by current `mechanics/experience/` surfaces. |
| `docs/legacy/` | Compatibility aliases and superseded flat surfaces preserved only for provenance. |

## Current root rule

A file may remain flat under `docs/` only when it is current doctrine, current map, current route law, or a local gate for agents.

Historical material must remain reviewable but must not stand beside current doctrine as if it had equal authority.

## Promotion rule

A district document may influence current law only through an explicit promotion path:

1. name the surviving canonical surface,
2. preserve provenance,
3. update links and generated indexes,
4. run validators,
5. explain whether old material remains receipt, audit, decision, postmortem, trace, legacy surface, mechanic legacy record, or registry note.

## Migration rule

Use `docs/thematic_districts.json` as the classifier and `scripts/plan_docs_thematic_cleanup.py` as the planner. If a file matches multiple districts, the classifier tie-break order decides where the historical surface lives.

Do not move source truth into this repository. Wave D only classifies center-local docs surfaces.

## Generated rule

`generated/docs_thematic_index.min.json` reflects `docs/thematic_districts.json`. It does not author meaning.
