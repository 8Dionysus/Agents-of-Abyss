# Questbook Distillation Log

## 2026-04-26 - Parts and Legacy Split

Status: landed

Moved the first-wave source contour into `legacy/raw/` and routed active
Questbook behavior through `parts/`.

Active destinations:

- `parts/model-spine/`
- `parts/public-index/`
- `parts/quest-store/`
- `parts/lifecycle-law/`
- `parts/generated-views/`
- `parts/relation-shape/`
- `parts/execution-passport/`
- `parts/harvest-route/`
- `parts/owner-handoffs/`
- `parts/lane-owner-routes/`

`INDEX.md` records which first-wave source pressures fed each active route and
marks later derived routes separately.

Stop-line: legacy preserves provenance; it is not the normal first route for
current Questbook edits.

## 2026-04-26 - Source Contract Runway

Status: landed

Added `parts/source-contract/` as the active home for Questbook source object
reviewability. This runway was completed by the full source contract
distillation pass below.

Active destinations:

- `parts/source-contract/`
- `mechanics/questbook/scripts/validate_questbook_source_contract.py`

Stop-line: this entry records the staging step; current source law is the full
distillation entry below.

## 2026-04-26 - Full Source Contract Distillation

Status: landed

Promoted all Markdown quest source files under `quests/<lane>/<state>/` to
`quest_markdown_contract_v1`. The old uncontracted Markdown shape no longer
remains as an active Questbook source contract.

Active destinations:

- `quests/agon/ready/`
- `quests/agon/done/`
- `quests/experience/ready/`
- `quests/experience/done/`
- `parts/source-contract/`
- `mechanics/questbook/scripts/validate_questbook_source_contract.py`

Stop-line: keep legacy/raw as provenance only; do not reintroduce uncontracted
Markdown quest sources as active obligations.

## 2026-04-26 - Route-default and Validation Centralization

Status: landed

Compressed repeated strict Markdown route/default sections into lane README
defaults for Agon and Experience. Centralized executable validation commands in
`mechanics/questbook/AGENTS.md`; other Questbook Markdown surfaces now route to
that matrix instead of carrying duplicate command blocks.

Active destinations:

- `mechanics/questbook/AGENTS.md`
- `quests/agon/README.md`
- `quests/experience/README.md`
- `quests/agon/*/AOA-Q-*.md`
- `quests/experience/*/AOA-Q-*.md`
- `mechanics/questbook/scripts/validate_questbook_distillation.py`

Stop-line: do not let command blocks or generic route defaults regrow across
active Questbook docs.
