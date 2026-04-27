# Checkpoint Parts Index

Checkpoint parts are active route modules. They describe how a checkpoint moves
between session carry, review, return, closeout, runtime export, and owner
handoff without becoming owner-local truth.

## Parts

- [Session Carry](session-carry/README.md): preserve mid-session evidence and
  carry hints without minting candidate truth.
- [Review Gate](review-gate/README.md): decide when checkpoint evidence needs
  explicit review before promotion or mutation continues.
- [Return Re-entry](return-reentry/README.md): use a checkpoint as a valid
  return anchor and bounded re-entry note.
- [Closeout Bridge](closeout-bridge/README.md): bridge reviewed checkpoint
  evidence into explicit closeout work.
- [Runtime Export](runtime-export/README.md): keep runtime checkpoint exports
  behind runtime-owner gates.
- [Owner Handoff](owner-handoff/README.md): turn checkpoint pressure into
  owner-request packets and next-owner routes.

## Route Law

Start from the part README, then read `CONTRACT.md` for boundaries and
`VALIDATION.md` for local validation posture. Executable commands remain
centralized in [Checkpoint AGENTS](../AGENTS.md#validation).
