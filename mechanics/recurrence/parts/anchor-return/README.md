# Anchor Return

Anchor Return names the basic recurrence move: when a route loses its axis, it
returns to the last valid anchor before continuing.

## Use When

- A route can no longer name its goal, phase, owner, artifact, or proof boundary.
- The next step needs a valid anchor before re-entry.
- Safe stop is more honest than fluent continuation.

## Do Not Use When

- The route only needs ordinary routing help without axis loss.
- The anchor is vague chat residue rather than an inspectable artifact.
- The caller wants a blind retry or hidden context inflation.

## Route Check

Ask whether the route can name the lost axis, valid anchor, anchor owner, and
bounded re-entry step. If any are missing, safe-stop or route to the owner that
can restore them.

## Active Outputs

- return reason
- anchor reference
- re-entry note
- safe stop
- owner handoff

## Next Route

Route navigation to `aoa-routing`, recall support to `aoa-memo`, actor handoff
to `aoa-agents`, proof to `aoa-evals`, and source meaning to the source owner.
