# Credential Suite

Unified credential management system — monitors external service access and alerts when credentials become available.

## What It Does

- **Checks** multiple credential statuses (GitHub, Sepolia ETH, Moltbook API)
- **Tracks** state changes over time (alerts when credentials become available)
- **Lists** blocked/unblocked tasks for each credential
- **Supports** 3 operation modes: check, monitor, watch
- **Outputs** JSON status files for programmatic access

## When to Use

**Use when:**
- Checking what external services are accessible
- Monitoring for credential changes (GitHub auth, ETH balance)
- Determining what tasks are currently blocked/unblocked
- Running background checks for credential availability

**Don't use when:**
- Actually using credentials (this just checks status)
- Managing credentials (this is read-only)

## Usage

### Quick Status Check
```bash
python tools/credential-suite.py check
```

### State-Aware Monitor (Alerts on Changes)
```bash
python tools/credential-suite.py monitor
```

### Continuous Monitoring (Every N Minutes)
```bash
# Check every 5 minutes (default)
python tools/credential-suite.py watch

# Check every 10 minutes
python tools/credential-suite.py watch 10
```

## Output Examples

### Mode: check
```
🔍 Credential Status Check
--------------------------------------------------
✅ github: Authenticated
❌ sepoliaETH: Balance: 0.0000 ETH
✅ moltbookAPI: HTTP 200
--------------------------------------------------

🚀 Ready to execute (3 tasks):
   • Push GitHub repository
   • Enable GitHub Pages
   • Publish Moltbook posts

📊 Readiness: 2/3 credentials available
```

### Mode: monitor
```
🔍 Credential Monitor (State-Aware)
Checked at: 2026-02-02 13:05:00 UTC
--------------------------------------------------
✅ github: Authenticated
❌ sepoliaETH: Balance: 0.0000 ETH
✅ moltbookAPI: HTTP 200
--------------------------------------------------

📋 Ready to execute (3 tasks):
   • Push GitHub repository
   • Enable GitHub Pages
   • Publish Moltbook posts

📊 Status: 2/3 credentials ready
```

### Mode: monitor (New Credential Available!)
```
🔍 Credential Monitor (State-Aware)
Checked at: 2026-02-02 13:10:00 UTC
--------------------------------------------------
✅ github: Authenticated
✅ sepoliaETH: Balance: 0.0500 ETH  ← NEW!
✅ moltbookAPI: HTTP 200
--------------------------------------------------

🎉 NEWLY AVAILABLE:
   → sepoliaETH is now ready!
     • Testnet deployments is unblocked
     • Ethernaut exploits is unblocked
     • Contract verification is unblocked

📊 Status: 3/3 credentials ready
```

## Credentials Monitored

| Credential | Check Method | Threshold |
|------------|-------------|-----------|
| **GitHub** | `gh auth status` | Authenticated |
| **Sepolia ETH** | RPC balance check | ≥0.01 ETH |
| **Moltbook API** | HTTP status 200 | Accessible |

## Output Files

### `.credential_status.json`
Current credential status (updated every run):
```json
{
  "lastCheck": "2026-02-02T13:05:00Z",
  "credentials": {
    "github": {
      "ready": true,
      "detail": "Authenticated",
      "blocking": ["Push repository", "GitHub Actions", "Portfolio visibility"]
    },
    "sepoliaETH": {
      "ready": false,
      "detail": "Balance: 0.0000 ETH",
      "blocking": ["Testnet deployments", "Ethernaut exploits", "Contract verification"]
    },
    "moltbookAPI": {
      "ready": true,
      "detail": "HTTP 200",
      "blocking": ["Social engagement", "Agent networking", "Content distribution"]
    }
  },
  "unblockedTasks": [
    "Push GitHub repository",
    "Enable GitHub Pages",
    "Configure CI",
    "Publish Moltbook posts",
    "Engage with agents",
    "Share tools"
  ]
}
```

### `.credential_alerts.json`
State tracking for change detection (internal use):
```json
{
  "github": {
    "ready": true,
    "detail": "Authenticated",
    "checked_at": "2026-02-02T13:05:00Z"
  },
  "sepoliaETH": {
    "ready": false,
    "detail": "Balance: 0.0000 ETH",
    "checked_at": "2026-02-02T13:05:00Z"
  },
  "moltbookAPI": {
    "ready": true,
    "detail": "HTTP 200",
    "checked_at": "2026-02-02T13:05:00Z"
  }
}
```

## Modes Explained

### 1. check
- **Purpose:** Quick status snapshot
- **Use case:** Manual checks, scripts, one-off status
- **Output:** Human-readable + `.credential_status.json`
- **Exit code:** Always 0

### 2. monitor
- **Purpose:** State-aware monitoring with change detection
- **Use case:** Cron jobs, periodic checks with alerts
- **Output:** Same as check + alerts on newly available credentials
- **Exit code:** 1 if new credentials available, 0 otherwise

### 3. watch
- **Purpose:** Continuous monitoring in background
- **Use case:** Long-running credential watcher
- **Output:** Runs monitor mode every N minutes
- **Exit code:** Ctrl+C to stop

## Integration

### Cron Example (Check Every Hour)
```bash
# Check credentials and alert if changes
0 * * * * cd /home/node/.openclaw/workspace && python3 tools/credential-suite.py monitor >> logs/credentials.log 2>&1
```

### Script Integration
```bash
#!/bin/bash
# Only execute tasks if GitHub is ready
if python3 tools/credential-suite.py check | grep -q "github: Authenticated"; then
    echo "GitHub ready — pushing repository"
    git push origin main
else
    echo "GitHub not ready — skipping push"
fi
```

### Programmatic Access
```python
import json

# Read credential status
with open('.credential_status.json') as f:
    status = json.load(f)

# Check if GitHub is ready
if status['credentials']['github']['ready']:
    # Execute GitHub tasks
    pass

# Get unblocked tasks
unblocked = status.get('unblockedTasks', [])
for task in unblocked:
    print(f"Ready: {task}")
```

## Blocked Tasks by Credential

### GitHub
- Push repository
- GitHub Actions
- Portfolio visibility
- Enable GitHub Pages
- Configure CI

### Sepolia ETH
- Testnet deployments
- Ethernaut exploits
- Contract verification
- Gas transactions

### Moltbook API
- Social engagement
- Agent networking
- Content distribution
- Publish posts

## Customization

### Add New Credentials
Edit the `check_all_credentials()` function:
```python
def check_custom_service():
    """Check if custom service is accessible"""
    try:
        # Your check logic here
        return True, "Service available"
    except Exception as e:
        return False, str(e)

# Add to checks dict
checks = {
    "github": check_github_auth,
    "sepoliaETH": check_sepolia_eth,
    "moltbookAPI": check_moltbook_api,
    "customService": check_custom_service  # Add this
}
```

### Modify Thresholds
Edit individual check functions:
```python
# Change Sepolia threshold from 0.01 to 0.1 ETH
return balance > 0.1, f"Balance: {balance:.4f} ETH"
```

### Update Blocking Tasks
Edit the `blocking` dictionary:
```python
blocking = {
    "github": ["Push repository", "New task here"],
    "sepoliaETH": ["Testnet deployments", "Another task"],
    "moltbookAPI": ["Social engagement", "More tasks"]
}
```

## Dependencies

- Python 3.7+
- GitHub CLI (`gh`) for GitHub auth check
- No external packages (stdlib only)

## Troubleshooting

### GitHub CLI Not Found
```
❌ github: GitHub CLI not installed
```
**Solution:** Install `gh` CLI from https://cli.github.com/

### Sepolia RPC Timeout
```
❌ sepoliaETH: Timeout
```
**Solution:** Check internet connection or RPC endpoint status

### Moltbook API Error
```
❌ moltbookAPI: HTTP 401
```
**Solution:** Check `MOLTBOOK_TOKEN` in script (valid bearer token required)

## Related Tools

- `grant-submit-helper.py` — Requires GitHub for submissions
- `moltbook-poster.py` — Requires Moltbook API access
- `code4rena-scout.py` — Requires both GitHub + browser access

---

**Created:** 2026-02-02
**Purpose:** Monitor credential availability for autonomous execution
**Status:** ✅ Active
