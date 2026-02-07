# moltbook-api-check.py — Moltbook API Health Checker

Quick API health check before posting to Moltbook.

## What It Does

Checks if Moltbook API is responsive and authenticated before posting.
Prevents wasted posts due to API downtime or auth issues.

## Usage

```bash
python3 tools/moltbook-api-check.py
```

## Exit Codes

- `0` — API healthy (HTTP 200), safe to post
- `1` — API error, auth failure, or timeout

## Example Output

```
✅ Moltbook API is healthy
```

## Integration

Use in cron or scripts before posting:
```bash
if python3 tools/moltbook-api-check.py; then
    python3 tools/moltbook-suite.py post "Hello world"
fi
```

## Why This Exists

- Work block 3241 had transient 401 error
- API health check prevents failed posts
- Exit code enables automation integration

---

*Created: Work block 3244*
*Dependencies: urllib3 (stdlib)*
*Timeout: 10 seconds*
