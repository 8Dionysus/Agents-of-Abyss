# Agon Packet Sequence Model

The initial pre-protocol sequence is:

```text
gate -> charter -> sealed_commit -> commit_receipt -> reveal_request -> reveal_view -> engagement packets -> revision_statement -> adjudication_request -> inscription_candidate -> closeout_candidate
```

This is not a live state machine. It is a sequence grammar for future session models.

The strongest invariant is simple: reveal may only be meaningful if commit came first.
