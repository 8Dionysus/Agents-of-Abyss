# Questbook Source Contract Full Distillation

Status: accepted
Date: 2026-04-26

## Context

Questbook gained `parts/source-contract/` to make quest source objects
reviewable. The first landing allowed existing Markdown quest files to remain
as uncontracted receipt-backed sources while new Markdown quests could opt into
`quest_markdown_contract_v1`.

That staging choice kept the first change small, but it left a durable split:
YAML quests and new Markdown quests were strict, while old Markdown quests
could still bypass the same source reviewability contract.

## Options considered

- Keep uncontracted Markdown as a migration lane.
- Convert only active or ready Markdown quests.
- Promote every Markdown quest source to `quest_markdown_contract_v1` and make
  the validator reject uncontracted Markdown.

## Decision

Promote every Markdown quest source under `quests/<lane>/<state>/AOA-Q-*.md`
to `quest_markdown_contract_v1`.

The Questbook source validator must reject Markdown quest sources without the
contract marker and required reviewability sections.

## Rationale

A quest is supposed to be a public obligation object, not a private TODO or a
memory trace. Keeping old Markdown outside the strict contract would force
future agents to remember which files are weaker and why. That is exactly the
kind of hidden rule Questbook is meant to replace.

Full distillation also makes the generated Questbook views less ambiguous:
every Markdown source now carries an owner route, next action, acceptance
evidence route, and stop-lines in the file itself.

## Consequences

- Existing Agon and Experience Markdown quest files became larger, but more
  reviewable. A follow-up compression moved generic lane/state defaults into
  lane README surfaces so strict source sections do not become boilerplate.
- The validator no longer needs a permissive legacy mode.
- Executable Questbook validation commands are centralized in
  `mechanics/questbook/AGENTS.md`; other Questbook Markdown surfaces route
  there rather than duplicating command blocks.
- Strict source shape still does not prove owner acceptance, implementation
  truth, or closure.
- If repeated owner-route defaults become noisy again, the next route is
  lane-local route splitting without weakening per-quest reviewability.

## Source surfaces

- `mechanics/questbook/parts/source-contract/`
- `mechanics/questbook/scripts/validate_questbook_source_contract.py`
- `quests/<lane>/<state>/AOA-Q-*`
- `mechanics/questbook/LANDING_LOG.md`
- `mechanics/questbook/legacy/DISTILLATION_LOG.md`

## Follow-up route

Route future quest-source compression through lane-local defaults and
`mechanics/questbook/AGENTS.md`; do not weaken the per-quest source contract.
