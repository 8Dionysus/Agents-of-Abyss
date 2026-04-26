# Agon Owner Request Route

The canonical Agon owner-request packet is now
[`../OWNER_REQUESTS.md`](../OWNER_REQUESTS.md).

This compatibility route remains so older links keep resolving. Do not update
request meaning here; update `mechanics/agon/OWNER_REQUESTS.md` and the central
owner-request queue instead.

## Validation

```bash
python scripts/validate_owner_request_docs.py --mechanic agon
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
```
