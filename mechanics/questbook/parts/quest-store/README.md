# Quest Store

This part owns the route to Questbook source objects.

## Source

- [`quests/`](../../../../quests/)

## Role

Keep quest objects in lane-first lifecycle directories:
`quests/<lane>/<state>/AOA-Q-*`.

## Boundary

The lane names the owner route. The state names the current lifecycle posture.
Root-level quest aliases and root lifecycle directories are intentionally
absent.
