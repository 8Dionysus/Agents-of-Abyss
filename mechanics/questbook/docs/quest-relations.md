# Quest Relations

This document names current Questbook relation shape. Quest source files remain
the authority; generated relation views only summarize them.

## Vocabulary

- `parent`: broader quest, contour, or obligation.
- `sidequest`: related playable route that branches or travels nearby.
- `related`: non-directional relation worth seeing.
- `blocks`: this quest blocks another quest.
- `blocked_by`: this quest waits on another quest.
- `reanchors_to`: this quest should be reread through another quest.
- `supersedes`: this quest replaces another quest.
- `superseded_by`: this quest was replaced by another quest.

## Stop-lines

- `sidequest` is not ownership, dependency, or automatic closure.
- Relations do not move a quest between lanes or lifecycle states.
- A relation never proves owner acceptance, runtime activation, proof verdict,
  or source meaning.
- Generated relation maps are read models, not quest authority.

## Foundation contour

- `AOA-Q-0001` has sidequests `AOA-Q-0002` and `AOA-Q-0003`.
- `AOA-Q-0002` has parent `AOA-Q-0001`.
- `AOA-Q-0003` has parent `AOA-Q-0001`, is related to `AOA-Q-0002`, and has
  sidequests `AOA-Q-0004`, `AOA-Q-0005`, `AOA-Q-0006`, `AOA-Q-0007`, and
  `AOA-Q-0008`.

## RPG-shaped center cluster

`AOA-Q-0004` through `AOA-Q-0008` remain in the center lane until a deliberate
reanchor creates RPG-lane source objects. The relation map may show them as
sidequests from the next-contour quest, but that does not silently move them.

Current shape:

- `AOA-Q-0004` has parent `AOA-Q-0003`.
- `AOA-Q-0005` has parent `AOA-Q-0003` and is blocked by `AOA-Q-0004`.
- `AOA-Q-0006` has parent `AOA-Q-0003` and is blocked by `AOA-Q-0004` and
  `AOA-Q-0005`.
- `AOA-Q-0007` has parent `AOA-Q-0003` and is blocked by `AOA-Q-0004`,
  `AOA-Q-0005`, and `AOA-Q-0006`.
- `AOA-Q-0008` has parent `AOA-Q-0003` and is blocked by `AOA-Q-0006` and
  `AOA-Q-0007`.

## Validation

```bash
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
python mechanics/questbook/scripts/validate_quest_relations.py
```
