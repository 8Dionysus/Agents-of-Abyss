# Optional future step: ecosystem registry v2

The current `generated/ecosystem_registry.min.json` schema is serviceable for a safe realignment, but it compresses too many different questions into `status` and `kind`.

Today, the center needs at least three independent axes:

- **visibility**: `public` or `private`
- **maturity**: `concept`, `bootstrap`, `active`, `stable`, `deprecated`
- **relation**: `center`, `source-layer`, `derived-layer`, `substrate`, `counterpart`, `private-project`

A future registry v2 could keep the current high-level structure while making these distinctions explicit.

Example shape:

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

Recommended order for that future change:

1. update `schemas/ecosystem-registry.schema.json`
2. update `scripts/validate_ecosystem.py`
3. migrate `generated/ecosystem_registry.min.json`
4. only then update prose references to the new axes
