# Quest Source Contract

This part owns the reviewability contract for Questbook source objects.

## Purpose

A quest source must let an agent understand the durable obligation without
rereading raw session history. The source file should answer:

- what survives the current diff
- who owns the route
- what the next action is
- what evidence can move or close it
- what must not be claimed from the quest alone

## Contract Levels

- `work_quest_v1` YAML is the strict rich source object format. Center quests
  use this contract when the obligation needs typed lifecycle, passport,
  relation, evidence, and public-safety fields.
- `quest_markdown_contract_v1` is the strict Markdown contract for lane quests.
  Every Markdown quest source must carry it.

## Markdown Contract

Strict Markdown quest files carry this marker:

```text
source_contract: quest_markdown_contract_v1
```

They must include:

- `## Quest`
- `## Owner Route`
- `## Next Action`
- `## Acceptance Evidence`
- `## Stop-lines`

Use this contract when creating or changing a Markdown quest. The sections may
point to lane/state defaults in `quests/<lane>/README.md` when the route is
generic, but they must stay present and non-empty in the quest source.

If the source cannot answer these sections honestly, keep the quest out of
active routing until the owner boundary and acceptance evidence are clear.

## Validation

Use the central Questbook validation matrix in [Questbook AGENTS](../../AGENTS.md#validation).
