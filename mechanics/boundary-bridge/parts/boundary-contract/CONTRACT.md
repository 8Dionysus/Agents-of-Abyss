# Boundary Contract Contract

Every valid bridge must state:

- `source_owner`
- `receiving_owner`
- `bridge_mode`
- `source_refs`
- `may_do`
- `must_not_do`
- `next_owner_route`

The contract is invalid if a reader cannot tell which owner remains
authoritative after the bridge is described.
