# Closeout Bridge

Closeout Bridge connects reviewed checkpoint evidence to the explicit
session-growth closeout chain without hiding harvest inside checkpoint capture.

## Use When

- Reviewed checkpoint evidence survived a session.
- Closeout must reread the reviewed artifact before harvest, progression, or
  quest decisions.
- Owner handoffs need context but not owner acceptance claims.

## Do Not Use When

- No reviewed artifact exists.
- The route only needs mid-session collection.
- The request tries to turn checkpoint hints into final verdicts.

## Route Check

Ask whether the reviewed artifact is the primary evidence. If not, stop before
closeout bridge and return to review gate.

## Active Outputs

- closeout bridge request
- ordered closeout chain
- owner followthrough hint
- stats-after-closeout reminder

## Next Route

Route bridge skill execution to `aoa-skills`, context building to `aoa-sdk`, and
downstream proof, memory, quest, or stats work to the owning repositories.
