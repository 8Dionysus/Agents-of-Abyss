# Post-Release Retention Law

A release is not mature until its changes survive later checks. Retention watches whether a patch actually changed future behavior or only passed staged regression.

Retention outcomes:

- held
- partially_held
- failed
- superseded
- obsolete_after_patch

Failed retention re-enters the experience loop as a candidate for new review, not as a hidden assistant rewrite.
