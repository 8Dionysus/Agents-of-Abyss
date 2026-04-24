# Ecosystem Registry v2 Notes

The current `generated/ecosystem_registry.min.json` schema is serviceable for safe center alignment, but it compresses too many different questions into `status` and `kind`.

A future registry v2 should split at least three independent axes:

| Axis | Example values | Question answered |
|---|---|---|
| `visibility` | `public`, `private` | can this surface be named publicly? |
| `maturity` | `concept`, `bootstrap`, `active`, `stable`, `deprecated` | how mature is this surface? |
| `relation` | `center`, `source-layer`, `derived-layer`, `substrate`, `counterpart`, `supporting-consumer`, `public-projection`, `private-project` | how does this surface relate to AoA? |

## Example shape

```json
{
  "version": 2,
  "ecosystem": "AoA",
  "repos": [
    {
      "name": "Agents-of-Abyss",
      "role": "ecosystem-center",
      "visibility": "public",
      "maturity": "active",
      "relation": "center",
      "kind": "meta"
    }
  ]
}
```

## Migration order

Do not update prose first. Registry v2 becomes real only when the machine contract moves together.

1. Update `schemas/ecosystem-registry.schema.json`.
2. Update `scripts/validate_ecosystem.py`.
3. Update or add the builder that emits `generated/ecosystem_registry.min.json`.
4. Migrate `generated/ecosystem_registry.min.json`.
5. Add or update tests for v2 axes.
6. Update `ECOSYSTEM_MAP.md`, `docs/REPO_ROLES.md`, `README.md`, and public support docs.
7. Keep `generated/federation_supporting_inventory.min.json` separate unless v2 explicitly absorbs supporting consumers.

## Boundary

This note is not the registry contract. It is the design path for a future migration.
