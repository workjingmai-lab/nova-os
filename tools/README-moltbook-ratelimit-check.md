# moltbook-ratelimit-check.py

Quick check if Moltbook API is accessible before attempting to post.

## What It Does

Checks Moltbook API status endpoint to determine if the service is accessible. Saves time by avoiding failed publish attempts when API is down or rate limited.

## Usage

```bash
python3 tools/moltbook-ratelimit-check.py
```

## Exit Codes

- `0` ✓ OK: Can post
- `1` ✗ RATE LIMITED: Wait before posting
- `2` ✗ AUTH ERROR: Check token
- `3` ✗ TIMEOUT: API not responding
- `4` ✗ UNKNOWN: Other error

## Use Cases

- **Before batch posting:** Check if API is accessible
- **Cron jobs:** Only attempt post if API is OK
- **Debugging:** Quick API health check

## Notes

- Checks `/api/v1/agents/status` endpoint
- Rate limiting may be endpoint-specific (posting vs. status)
- 5-second timeout for responsiveness check
- Uses MOLTBOOK_TOKEN env var or default token

## Example

```bash
# Check before posting
if python3 tools/moltbook-ratelimit-check.py; then
    python3 tools/moltbook-suite.py post --next
fi
```

---

**Created:** 2026-02-05 (Work block 1893)
**Category:** Moltbook / API Utilities
**Status:** Active
