# Agon Direction

Agon is the center mechanic for making pressure lawful. This file owns the
current operating direction only; it does not replace the part map, landing
ledger, roadmap, owner-request packet, or source-document bridge.

## Source-of-truth split

- `README.md`: package entry card and shortest route.
- `DIRECTION.md`: current operating direction.
- `PARTS.md`: map of functioning Agon parts.
- `parts/`: concise active part contracts.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `LANDING_LOG.md`: canonical landing ledger.
- `ROADMAP.md`: future contour, not a historical ledger.
- `PROVENANCE.md`: the only active bridge back to detailed source-doc
  accounting.
- `legacy/`: preserved source documents, models, handoffs, and stop-lines.
- `docs/`: compatibility route only.

## Current direction

- Keep active work routed through [PARTS](PARTS.md) and the owning
  `parts/<slug>/` contract before opening detailed source-docs.
- Keep pressure center-bounded: Agon may name lawful move grammar, stop-lines,
  packets, arena/duel models, verdict contours, retention/rank candidates,
  KAG/ToS thresholds, and owner requests.
- Keep operational authority outside the center. Playbooks, evals, memo, stats,
  routing, agents, runtime, KAG, and ToS acceptance stay with their stronger
  owners.
- Keep landed history in `LANDING_LOG.md` and future pressure in `ROADMAP.md`.
- Keep new source contours or packets distilled into a functioning part instead of
  expanding a flat docs route.

Active parts stay in this order: `imposition-readiness`,
`lawful-move-grammar`, `owner-binding`, `gate-routing`, `trial-handoff`,
`recurrence-adapter`, `packet-arena`, `duel-kernel`,
`verdict-retention-rank`, `epistemic-kag`, `sophian-threshold`,
`compatibility-bridges`.

## Distillation law

New source notes, handoff packets, and long exploratory surfaces must not
become the active route by accumulation. After a packet lands, distill the
surviving function into the relevant part `README.md`, `CONTRACT.md`, or
`VALIDATION.md`, then update source accounting through `PROVENANCE.md`.

A functioning part should make three things clear:

- what does this part own at the center
- what stronger owner keeps operational authority
- which validation or owner route makes the claim reviewable

## Stop-lines

- Do not claim live arena execution from Agon center docs.
- Do not claim assistant contestant, judge, closer, or scar-writer authority.
- Do not claim live rank mutation, durable memory mutation, runtime dispatch,
  proof verdict, KAG canon, or ToS canon write authority.
- Do not let detailed source or model files become the primary route.

## Validation

Use the validation lane in [mechanics/agon/AGENTS.md](AGENTS.md#validation) for executable commands.
