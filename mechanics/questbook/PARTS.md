# Questbook Parts

Questbook has three active parts.

## Public Index

- Source: [`QUESTBOOK.md`](../../QUESTBOOK.md)
- Role: compact human-facing frontier and near-obligation index.
- Boundary: it lists public center obligations; it does not own lifecycle law or full quest history.

## Quest Store

- Source: [`quests/`](../../quests/)
- Role: lane-first source objects at `quests/<lane>/<state>/AOA-Q-*`.
- Boundary: lane chooses owner route, state chooses lifecycle posture.

## Generated Views

- Source: [`generated/questbook_index.min.json`](../../generated/questbook_index.min.json) and [`generated/questbook_frontier.min.json`](../../generated/questbook_frontier.min.json)
- Builder: [`build_questbook_index.py`](scripts/build_questbook_index.py)
- Validators: [`validate_questbook_lifecycle.py`](scripts/validate_questbook_lifecycle.py), [`validate_questbook_index.py`](scripts/validate_questbook_index.py)
- Boundary: generated views summarize quest source files; they never author quest meaning.

## Owner Handoffs

- Source: [`QUESTBOOK_OWNER_REPO_REQUESTS.md`](docs/QUESTBOOK_OWNER_REPO_REQUESTS.md)
- Role: requests to stronger owners when quest mechanics must become repeatable choreography, proof, memory, or route behavior.
- Boundary: request packets are not owner acceptance.
