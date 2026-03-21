# Contributing to Agents of Abyss

Thank you for helping shape AoA.

This repository is the ecosystem-center repository of AoA.
It is not the main corpus home of specialized layers.
Contributions here should improve the clarity, coherence, and governance of the AoA federation.

## What belongs here

Good contributions for this repository include:
- improvements to the AoA charter
- clearer ecosystem maps
- better layer definitions
- better federation rules
- glossary improvements
- program-level roadmap updates
- compact machine-readable ecosystem registry improvements
- clearer entrypoints for humans and coding agents

## What usually does not belong here

Do not use this repository as the default home for:
- new technique bundles
- new skill bundles
- new eval bundles
- memory objects
- agent runtime configs
- infrastructure implementation details
- large specialized corpora that already belong in a dedicated AoA repository

If a change mainly belongs to one specialized layer, prefer changing that layer's source repository first.

## Source-of-truth discipline

When contributing, preserve this rule:
- source repositories own meaning
- coordination repositories own maps

Examples:
- `aoa-techniques` owns technique truth
- `aoa-skills` owns skill truth
- `aoa-evals` owns eval truth
- `aoa-routing` should own navigation surfaces
- `aoa-memo` should own memory truth
- `aoa-agents` should own role and persona truth
- `Agents-of-Abyss` owns ecosystem-level truth only

## How to decide where a change belongs

Ask these questions in order:

1. Does this change define or revise the meaning of a specialized object class?
   - If yes, it probably belongs in a specialized repository.
2. Does this change clarify how AoA layers relate to one another?
   - If yes, it may belong here.
3. Does this change add a new ecosystem-level rule, boundary, or roadmap statement?
   - If yes, it may belong here.
4. Does this change duplicate material that already has a better source-of-truth home?
   - If yes, move it to the better home instead.

## Pull request shape

A strong pull request in this repository should explain:
- what ecosystem-level surface changed
- why the change belongs in `Agents-of-Abyss`
- what neighboring repositories are affected
- what is intentionally left to specialized repositories

## Style guidance

Prefer:
- compactness over sprawl
- explicit boundaries over vague ambition
- readable maps over abstract grandiosity
- stable layer distinctions over convenience duplication

## If you are unsure

When in doubt, choose the narrower change.
If the change feels like the beginning of a new layer, name that possibility explicitly instead of forcing it into the wrong repository.
