# Experience Certification Decision Table


Decision summary:

- `approved`: all gates pass, authority valid, rollback evidence present.
- `approved_with_watch`: gates pass but post-release monitoring must be stricter.
- `denied_regression`: candidate breaks golden or boundary cases.
- `denied_authority`: actor lacks certification authority.
- `denied_rollback`: rollback drill absent or failed.
- `recharter_required`: candidate changes mandate or identity.
