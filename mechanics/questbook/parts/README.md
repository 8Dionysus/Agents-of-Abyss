# Questbook Parts Index

Functioning Questbook parts live here. Each part owns one active route question
and points outward to source quest objects, generated read models, owner
requests, or legacy provenance only when needed.

## Parts

| Part | Role |
|---|---|
| [Model Spine](model-spine/README.md) | compact Questbook model and source-of-truth router |
| [Public Index](public-index/README.md) | root public `QUESTBOOK.md` posture |
| [Quest Store](quest-store/README.md) | lane-first source object store under `quests/` |
| [Lifecycle Law](lifecycle-law/README.md) | states, lanes, promotion, and placement bands |
| [Generated Views](generated-views/README.md) | compact generated read models and freshness checks |
| [Relation Shape](relation-shape/README.md) | cross-quest relation vocabulary and validation |
| [Execution Passport](execution-passport/README.md) | difficulty, risk, control, and delegation vocabulary |
| [Harvest Route](harvest-route/README.md) | repeated-pattern thresholds and promotion targets |
| [Owner Handoffs](owner-handoffs/README.md) | center-side request packets to stronger owners |
| [Lane Owner Routes](lane-owner-routes/README.md) | ready quest to owner-request registry maps |

## Active Contract

Each part should keep three working surfaces:

- `README.md`: purpose, current source, and first route.
- `CONTRACT.md`: owner boundary, allowed outputs, and stop-lines.
- `VALIDATION.md`: checks that prove the part stayed coherent.

[`registry.json`](registry.json) is the machine-checked list of active parts.
It must stay synchronized with this index and `../PARTS.md`.

## Provenance

Use [`../PROVENANCE.md`](../PROVENANCE.md) when the task needs historical
source accounting. Active parts should not list legacy inventories directly.

## Validation

```bash
python mechanics/questbook/scripts/validate_questbook_distillation.py
```
