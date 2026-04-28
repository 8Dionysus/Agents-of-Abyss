# Registry Notes

This directory holds registry evolution notes and migration planning. It is a
design lane, not a second registry.

Current compact registry v1 still lives in `generated/ecosystem_registry.min.json` and is validated by the center validators. Design notes in this directory do not change the machine contract until schemas, builders, validators, generated surfaces, and prose references move together.

## District law

Registry notes explain registry evolution and generated-surface planning. They
do not replace schemas, builders, validators, or generated artifacts.

## Current surfaces

| Surface | Role |
|---|---|
| [`REGISTRY_V2_NOTES`](REGISTRY_V2_NOTES.md) | future registry v2 axes and migration order |

## Must not claim

Registry notes are not runtime truth, source meaning, or generated contract by
themselves.

Do not use this district to absorb owner-local truth from sibling repositories.

Do not add exploratory registry notes here unless they name the active machine
contract they would eventually change.

## Promotion path

A registry note becomes current only when a change names the surviving schema or
source surface, updates builders and validators, rebuilds generated outputs, and
runs the relevant release checks.

## Validation

Use the nearest `AGENTS.md` for the current command lane.
