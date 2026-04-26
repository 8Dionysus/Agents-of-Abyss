# Lane Owner-Route Contract

This document owns the shape of lane owner-route maps.

## Purpose

Lane owner-route maps connect ready quests to explicit owner-request packets
without claiming owner acceptance. They are route surfaces, not proof surfaces.

## Source Shape

Each registry entry names:

- `quest_id`
- `quest_path`
- `owner_request_ids`
- `route_note`

The registry must cover every ready quest in the lane unless an explicit
exception is added to the registry and validated.

## Markdown Projection

Human-facing route tables may be generated from a registry. When a registry
exists, the Markdown table is a projection and must not be edited by hand.

## Stop-Lines

- A route table is center-side navigation only.
- Do not update owner-request status from a route table.
- Do not close a ready quest until owner-local acceptance, landing, or proof is
  actually reviewed.
- Do not add legacy/raw links to route tables; route provenance questions
  through the owning mechanic provenance surfaces.

## Current Registries

- `experience-ready-owner-routes.json` backs
  `experience-ready-owner-routes.md`.

## Validation

Use the central Questbook validation matrix in [Questbook AGENTS](../../AGENTS.md#validation).
