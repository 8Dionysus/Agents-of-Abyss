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

## Current Snapshot Route

Concrete edges live in source quest files and generated read models.

Current foundation contour:

- `AOA-Q-0001` remains the broader foundation parent for `AOA-Q-0002` and
  `AOA-Q-0003`.
- `AOA-Q-0004` through `AOA-Q-0008` remain center-lane side routes under
  `AOA-Q-0003` until deliberate RPG-lane reanchor.

Do not update this part for every graph edge. Update the source quest relation
metadata, rebuild generated Questbook views, and use this part only when the
relation vocabulary or stop-lines change.

## Validation

Use the central Questbook validation matrix in [Questbook AGENTS](../../AGENTS.md#validation).
