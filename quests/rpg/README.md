# rpg Quest Lane

RPG reflection, bridge, and runtime-projection obligations.

Quest source files in this lane use lifecycle subdirectories only when items exist. The lifecycle states are `captured`, `triaged`, `ready`, `active`, `blocked`, `reanchor`, `done`, and `dropped`.

Do not create top-level `AOA-Q-*` aliases in this lane. Keep each quest under `<lane>/<state>/AOA-Q-*` and keep root `QUESTBOOK.md` as the public index, not a second roadmap.
