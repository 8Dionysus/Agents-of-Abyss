# Antifragility Provenance

This file is the only default bridge from active antifragility parts to old
wave/raw material.

Use it when you are auditing how old source material was distilled, not when
you need the current operating contract.

## Current route first

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts/](parts/)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [FRAGILITY_BLACKLIST](FRAGILITY_BLACKLIST.md)

If those surfaces answer the task, stop there. Do not pull raw history into
the active route.

## Raw sources

| Raw source | Distilled into | Notes |
|---|---|---|
| [ANTIFRAGILITY_FIRST_WAVE](legacy/raw/ANTIFRAGILITY_FIRST_WAVE.md) | `DIRECTION.md`, `OWNER_MAP.md`, `OWNER_REQUESTS.md`, `parts/stress-review`, `parts/repair-proof`, `parts/memory-return` | Preserves the first concrete stressor family and cross-repo wave shape. |
| [VIA_NEGATIVA_CHECKLIST](legacy/raw/VIA_NEGATIVA_CHECKLIST.md) | `PARTS.md`, `parts/via-negativa`, `parts/sprawl-control`, `parts/owner-handoff` | Preserves the old checklist after the active route became part-based. |

## Active doctrine sources

- [ANTIFRAGILITY](docs/ANTIFRAGILITY.md)
- [VIA_NEGATIVA](docs/VIA_NEGATIVA.md)
- [ANTI_AUTHORITY_RULES](docs/ANTI_AUTHORITY_RULES.md)
- [ONE_IN_ONE_OUT](docs/ONE_IN_ONE_OUT.md)
- [FRAGILITY_BLACKLIST](FRAGILITY_BLACKLIST.md)

## External provenance anchors

- `docs/audits/DELETION_CANDIDATES.json` remains an inspect-first audit
  surface.
- Root `FRAGILITY_BLACKLIST.md` remains a compatibility route only.
- Owner-local proof, memory, runtime, stats, playbook, technique, and skill
  landings remain outside this package until their owners accept a request.

## Distillation rule

Do not copy raw wave text into active parts. Distill the route, keep the trace
here, and leave owner-local truth with the owner repository.
