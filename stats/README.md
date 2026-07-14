# Agents-of-Abyss local stats port

This directory exposes statistical questions whose domain meaning belongs to
the constitutional center. It uses the shared `aoa-stats` grammar without
moving ecosystem-map authority or registry maturity meaning into the central
stats organ.

## Current reference measurement

| Measurement | Question | Reference value |
| --- | --- | --- |
| `Agents-of-Abyss/public-registry-active-maturity-ratio` | What fraction of entries in the current public AoA ecosystem registry v2 carry the center-declared maturity label `active`? | `5 / 12` at evidence revision `62d62bd5f18d94debf85884b0abe91f47a6de16b` |

The population is a census of the unique records in `repos[]` from the
owner-validated registry v2. Supporting consumers, public projections outside
registry v2, workspace checkouts, local stats ports, and runtime or deployment
state are excluded. A complete registry with no `active` rows is an observed
zero; an unsupported version or a malformed, empty, or duplicate population is
unknown.

## Evidence posture

The packet is a public reference snapshot derived from the committed
`generated/ecosystem_registry.min.json`. That generated registry remains a
companion to `ECOSYSTEM_MAP.md`, and the packet is not a live workspace or
remote-repository observation.

## Authority

The ratio reports only the distribution of one center-authored registry label
at one source revision. It does not establish repository health,
implementation quality, owner acceptance, release readiness, current remote
state, local stats-port coverage, or an ecosystem progress score.

## Surfaces

- `port.manifest.json` declares the center-local question and measurement.
- `packets/public-registry-active-maturity-ratio.reference.json` records the
  evidence-linked reference observation.
- `ECOSYSTEM_MAP.md` owns the human public contour and maturity meaning.
- `generated/ecosystem_registry.min.json` is the immediate validated read
  model.
- `aoa-stats` owns shared validation and cross-owner composition.
