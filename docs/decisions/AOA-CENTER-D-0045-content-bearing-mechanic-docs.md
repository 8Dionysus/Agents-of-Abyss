# Content-Bearing Mechanic Docs Without Route Scaffolding

- Decision ID: AOA-CENTER-D-0045

## Status

Accepted.

## Index Metadata

- Original date: 2026-09-05
- Surface classes: mechanics topology, agent guidance, validation, provenance
- Center facets: active owner routes, source history
- Mechanic parents: agon, experience, questbook, rpg
- Guard families: active-source completeness, historical recovery
- Posture: accepted source-tree cleanup; no owner-authority change

## Context

Four mechanic `docs/` directories contained only inherited route cards. The
cards repeated current package navigation and, in RPG, could misdirect readers
toward retired local history. Their presence also forced archive-only validator
and mesh obligations even though active doctrine already belongs to package
sources, parts, owner requests, and provenance.

## Options considered

1. Keep empty compatibility districts and their presence checks.
2. Retain them under another archive name in the current tree.
3. Remove the duplicate cards, make content-bearing `docs/` optional, and
   require active canonical sources plus immutable historical recovery.

## Decision

Choose option 3. Agon, Experience, Questbook, and RPG omit `docs_path` when no
content-bearing docs directory exists. Other packages may declare a non-empty,
package-local docs directory. Every package still declares and satisfies its
active canonical sources, entry card, roadmap, landing log, and owner request.
Historical route-card recovery uses the exact baseline Git commit and original
path through the owning provenance route; no replacement archive is created.

## Rationale

A directory whose only job is to announce that content moved adds navigation,
inherited instruction, mesh weight, and validation cost without preserving an
active contract. Optional content-bearing docs retain a legitimate home for
future doctrine while keeping the package's active source boundary explicit.

## Consequences

- Current route navigation starts from package entry cards, active parts, and
  provenance rather than duplicate docs cards.
- Historical route-card URLs are recoverable from the exact baseline tree.
- Landing ledgers retain historical references without requiring retired files
  to remain in the checkout.
- The residual risk is stale consumers that still assume every package has a
  docs directory; topology and source validators now make the intended rule
  explicit.

## Source surfaces

- `mechanics/registry.json`
- `scripts/mechanics_topology/validate_mechanics_topology.py`
- `scripts/mechanics_topology/validate_mechanic_landing_logs.py`
- `mechanics/AGENTS.md`
- `mechanics/README.md`
- `mechanics/{agon,experience,questbook,rpg}/AGENTS.md`
- `mechanics/{agon,experience,questbook,rpg}/LANDING_LOG.md`

## Follow-up route

Run the mechanics source and release gates after rebuilding decision indexes,
the AGENTS mesh, mechanic card companions, and canonical KAG. Revisit only if a
package gains actual content-bearing docs or if immutable recovery changes.
