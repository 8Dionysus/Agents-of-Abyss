# AoA Federation Rules

This document records the most important ownership rules across the AoA ecosystem.

## Rule 1: source repositories own meaning

A specialized repository owns the primary meaning of its object class.

Examples:
- `aoa-techniques` owns technique meaning
- `aoa-skills` owns skill meaning
- `aoa-evals` owns eval meaning
- `aoa-memo` should own memory meaning
- `aoa-agents` should own role and persona meaning

## Rule 2: navigation layers do not become source-of-truth layers

`aoa-routing` should remain a navigation and dispatch surface.
It may aggregate, compress, and route.
It should not become the primary authoring home of techniques, skills, evals, or memory objects.

## Rule 3: ecosystem-center repos do not absorb specialized corpora

`Agents-of-Abyss` exists to keep the ecosystem intelligible.
It should describe the federation, not swallow it.

## Rule 4: derived surfaces must stay derived

Capsules, indexes, registries, and routing manifests should remain derived from source repositories whenever possible.
They may accelerate access, but they must not silently replace canonical bundles.

## Rule 5: new complexity should become a new layer when justified

If a surface begins to answer a genuinely different class of question, it should usually become a distinct layer rather than distort an existing one.

## Rule 6: memory is not proof

Recall and provenance are valuable, but memory surfaces should not be mistaken for evaluation surfaces.
Bounded proof still belongs to eval layers.

## Rule 7: proof is not execution

An eval may test a workflow, but it does not own the workflow as an execution surface.
Operational truth should remain in skill and technique layers.

## Rule 8: compactness is a virtue at the center

The root AoA repository should stay compact and legible.
If it starts growing specialized corpus weight, the growth probably belongs elsewhere.
