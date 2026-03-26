# Spark lane for Agents-of-Abyss

This file only governs work started from `Spark/`.

The root `AGENTS.md` remains authoritative for repository identity, ownership boundaries, reading order, and validation commands. This local file only narrows how GPT-5.3-Codex-Spark should behave when used as the fast-loop lane.

If `SWARM.md` exists in this directory, treat it as queue / swarm context. This `AGENTS.md` is the operating policy for Spark work.

## Default Spark posture

- Use Spark for short-loop work where a small diff is enough.
- Start with a map: task, files, risks, and validation path.
- Prefer one bounded patch per loop.
- Read the nearest source docs before editing.
- Use the narrowest relevant validation already documented by the repo.
- Report exactly what was and was not checked.
- Escalate instead of widening into a broad architectural rewrite.

## Spark is strongest here for

- route-table cleanup and cross-link repair
- center-layer wording normalization
- small map, glossary, or generated-surface alignment when the owning meaning already exists
- tight audits of source-of-truth language
- small changelog or roadmap wording repairs that do not redefine the program

## Do not widen Spark here into

- federation-rule redesign
- layer-boundary redefinition
- moving source-owned meaning from a specialized repository into the center
- broad cross-repo synthesis or policy invention
- large regeneration or migration work spanning many AoA layers

## Local done signal

A Spark task is done here when:

- AoA is easier to navigate after the edit
- the center is clearer without becoming fatter
- source-of-truth boundaries are sharper
- specialized layer meaning was linked, not absorbed
- the nearest validator or manual consistency pass was run when relevant

## Local note

Spark should act as a center-layer gardener here: prune, align, clarify, and stop before it starts founding a new constitution.

## Reporting contract

Always report:

- the restated task and touched scope
- which files or surfaces changed
- whether the change was semantic, structural, or clarity-only
- what validation actually ran
- what still needs a slower model or human review
