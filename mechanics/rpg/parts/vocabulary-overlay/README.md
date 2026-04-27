# Vocabulary Overlay

This part owns the checked split between machine-stable RPG keys and themed presentation labels.

## Use When

- a runtime, frontend, or public display needs RPG labels without losing canonical keys
- a new RPG term must be checked against the active terminology contract
- a generated overlay needs to mirror the authored terminology

## Do Not Use When

- the label would replace a canonical key
- the display would imply runtime state, proof, quest closure, role canon, or skill canon
- the term belongs in a stronger owner repository before RPG can reflect it

## Route Check

- Source object: name the canonical key or term being presented.
- Owner route: keep owner-local truth outside the overlay unless accepted by that owner.
- Reading value: themed labels may help humans read, but must not hide machine keys.
- Closeout: say whether authored terminology, schema, example, or generated mirror changed.

## Active Outputs

- canonical vocabulary key
- themed presentation label
- checked example and generated overlay mirror
- validation result

## Surfaces

- [TERMINOLOGY](TERMINOLOGY.md)
- [schema](schemas/dual_vocabulary_overlay.schema.json)
- [example](examples/dual_vocabulary_overlay.example.json)
- [generated overlay](generated/dual_vocabulary_overlay.json)

## Next Route

Runtime and frontend projection routes to `abyss-stack`; public display stays derived and must keep canonical keys available.
