# Vote Sealing

Votes pass through commit and reveal. Commit stores a canonical hash of voter, case, choice, reason, nonce, and decision scope. Reveal must match the sealed hash.

This prevents post-hoc vote rewriting and cheap consensus drift.
