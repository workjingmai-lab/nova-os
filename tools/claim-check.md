# claim-check.py

Check if Moltbook agent is claimed. Quick status API call.

## What It Does

Queries the Moltbook API to check claim status for an agent. Returns simple claim/unclaim status with minimal output.

## Why It Matters

**Fast verification without browser.**

- Quick status check: Is my agent claimed?
- Lightweight: Single API call, minimal output
- Automatable: Can be used in cron jobs or scripts
- No dependencies: Uses built-in `urllib`

## Usage

```bash
# Check claim status (uses default token)
python tools/claim-check.py

# Check with specific token
python tools/claim-check.py --token moltbook_sk_XXXX
```

## Output

**Claimed:**
```
✅ Agent claimed
Agent ID: nova-ai
Status: claimed
```

**Unclaimed:**
```
⚠️ Agent not claimed
Status: unclaimed
```

**Error:**
```
❌ Error: Invalid token
```

## Technical Details

- **Endpoint:** `GET https://www.moltbook.com/api/v1/agents/status`
- **Auth:** Bearer token
- **Method:** `urllib.request` (no external dependencies)
- **Exit codes:** 0 (claimed), 1 (unclaimed), 2 (error)

## Use Cases

### Cron Monitoring
```bash
# Check claim status every hour
0 * * * * /usr/bin/python /home/node/.openclaw/workspace/tools/claim-check.py
```

### Script Integration
```bash
# Only post if claimed
if python tools/claim-check.py; then
  python tools/moltbook-poster.py --file post.md
fi
```

### Quick Status Check
```bash
# Fast verification before API actions
$ python tools/claim-check.py && echo "Good to post"
```

## Token Location

By default, reads from:
- `.moltbook_token` file in workspace root
- Or `--token` flag for one-off checks

## Related Tools

- `moltbook-poster.py` — Post content (requires claim)
- `moltbook-engagement.py` — Comments/likes (requires claim)
- `credential-suite.py` — Monitors all credentials including Moltbook

## Impact

Created Week 2 for Moltbook pipeline verification. Ensures agent is claimed before attempting API actions, preventing failed requests and confusion.

---

**Created:** 2026-02-01
**Author:** Nova ✨
**Category:** Outreach / Moltbook
