# Manifests District

This directory holds explicit manifests that help the center track bounded routes, recurrence, or owner-bound handoff surfaces.

A manifest is not a memory store, not a roadmap, and not a root civic surface.

## Current subdistricts

| Subdistrict | Use |
|---|---|
| [`recurrence/`](recurrence/) | recurrence and re-entry manifest surfaces |

## Rules

- Keep manifests tied to a source document, owner split, or validator.
- Do not use manifests as hidden state.
- Do not promote one-wave seed manifests to repository root.
- If a manifest records a historical wave landing, prefer `docs/landings/`.
- If a manifest becomes generated, move it under `generated/` and add the builder/validator route.

## Before editing

1. Check [`mechanics/recurrence/docs/RECURRENCE_PRINCIPLE.md`](../mechanics/recurrence/docs/RECURRENCE_PRINCIPLE.md) if the manifest is recurrence-related.
2. Check [`docs/ROOT_SURFACE_LAW.md`](../docs/ROOT_SURFACE_LAW.md) if the manifest was considered for root.
3. Keep the owner-local landing path visible.
