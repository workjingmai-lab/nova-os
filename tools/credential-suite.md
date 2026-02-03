# credential-suite.py — Unified Credential Management

**Purpose:** Consolidated credential tracking with state-aware monitoring for GitHub, Sepolia ETH, and Moltbook API.

**Created:** Week 1 (2026-01-31)
**Usage:** ~20-30 times (blocker tracking)

## What It Does

- **Tracks 3 credentials** — GitHub CLI, Sepolia ETH (min 0.01), Moltbook API
- **3 operation modes** — `check` (quick status), `monitor` (state-aware), `watch` (continuous)
- **Detects changes** — Alerts when credentials become newly available
- **Lists blocked tasks** — Shows what each credential unblocks
- **Saves state** — `.credential_status.json` + `.credential_alerts.json`

## Usage

```bash
# Quick status check
python3 tools/credential-suite.py check

# State-aware monitoring (alerts on changes)
python3 tools/credential-suite.py monitor

# Continuous monitoring (every 5 minutes)
python3 tools/credential-suite.py watch

# Custom interval (10 minutes)
python3 tools/credential-suite.py watch 10
```

## Output Examples

### check mode
```
🔍 Credential Status Check
--------------------------------------------------
✅ github: Authenticated
❌ sepoliaETH: Balance: 0.0000 ETH
✅ moltbookAPI: HTTP 200
--------------------------------------------------

🚀 Ready to execute (6 tasks):
   • Push GitHub repository
   • Enable GitHub Pages
   • Configure CI
   • Publish Moltbook posts
   • Engage with agents
   • Share tools

📊 Readiness: 2/3 credentials available
```

### monitor mode
```
🔍 Credential Monitor (State-Aware)
Checked at: 2026-02-02 19:32:15 UTC
--------------------------------------------------
✅ github: Authenticated
❌ sepoliaETH: Balance: 0.0000 ETH
✅ moltbookAPI: HTTP 200
--------------------------------------------------

🎉 NEWLY AVAILABLE:
   → moltbookAPI is now ready!
     • Social engagement is unblocked
     • Agent networking is unblocked
     • Content distribution is unblocked
```

## Tracked Credentials

| Credential | Check Method | Minimum Requirement | Blocked Tasks |
|------------|-------------|---------------------|---------------|
| **GitHub** | `gh auth status` | Authenticated | Push repo, CI/CD, GitHub Pages |
| **Sepolia ETH** | RPC balance check | 0.01 ETH | Testnet deployments, Ethernaut exploits |
| **Moltbook API** | HTTP request | 200 OK | Social posts, agent networking |

## Exit Codes

- `0` — No changes (monitor mode)
- `1` — Newly available credential detected (monitor mode)
- `1` — Invalid mode

## Dependencies

- Python 3.8+
- `gh` CLI (for GitHub auth)
- `urllib` (stdlib, for API checks)

## State Files

**`.credential_status.json`** — Current status with blocked tasks
```json
{
  "lastCheck": "2026-02-02T19:32:15Z",
  "credentials": {
    "github": {
      "ready": true,
      "detail": "Authenticated",
      "blocking": ["Push repository", "GitHub Actions"]
    }
  },
  "unblockedTasks": ["Push GitHub repository", "Enable GitHub Pages"]
}
```

**`.credential_alerts.json`** — Previous state for change detection

## Why This Matters

Blocker visibility = unblocked execution.
- **Without monitoring** → You don't know when blockers clear
- **With state tracking** → Immediate alert when tasks unblock
- **With task mapping** → Clear next actions when credentials ready

## Cron Integration

```bash
# Check every 10 minutes, alert on changes
*/10 * * * * cd /home/node/.openclaw/workspace && python3 tools/credential-suite.py monitor
```

## Related Tools

- `grant-submit-helper.py` — Grant submissions (requires GitHub)
- `moltbook-poster.py` — Social posting (requires Moltbook API)

## Real-World Usage

**Scenario:** You're waiting for GitHub auth to push your grant submissions.

**Before:** Manually running `gh auth status` every hour.
**After:** `credential-suite.py watch` alerts you immediately when auth succeeds, unblocking the entire grant pipeline.

---

**Consolidated from:** `credential-tracker.py` + `credential-monitor.py`
