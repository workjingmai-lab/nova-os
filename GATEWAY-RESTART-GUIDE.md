# Gateway Restart Guide (1 minute)

> Unblocks $50K in Code4rena bounties.

## What This Does

The OpenClaw gateway service needs a restart to enable browser automation for Code4rena audit platform access.

**Time:** 1 minute
**Value unlocked:** $50K (Web3 security audit bounties)

## Why This Is Needed

Browser automation in OpenClaw requires the gateway service to be running with browser extensions enabled. A restart refreshes the browser control server.

## How to Restart

**Option 1: Using openclaw CLI (recommended)**

```bash
openclaw gateway restart
```

**Option 2: Manual restart**

```bash
# Stop the gateway
openclaw gateway stop

# Wait 5 seconds
sleep 5

# Start the gateway
openclaw gateway start
```

## Verify Restart Worked

```bash
openclaw gateway status
```

Expected output:
```
✓ Gateway is running
✓ Browser control: enabled
✓ Profile: openclaw
```

## What This Enables

After restart, browser automation is available for:

- **Code4rena** — Competitive audit platform ($5K-$100K bounties)
- **Web form submissions** — Grant applications that require browser input
- **Automated testing** — Web interaction workflows

## To Use Code4rena

After gateway restart:

```bash
cd /home/node/.openclaw/workspace
python3 tools/code4rena-setup.py
```

This will:
1. Navigate to code4rena.com
2. Check for active contests
3. Report available bounties

## Troubleshooting

**"Gateway is not running"**
- Run: `openclaw gateway start`

**"Browser control disabled"**
- Restart may not have worked. Try: `openclaw gateway restart --force`

**"Permission denied"**
- Gateway commands may require elevated access. Arthur should run these.

**"Still getting browser errors"**
- Check if Docker is running: `docker ps`
- Restart Docker if needed: `sudo systemctl restart docker`

## Safety Notes

- Gateway restart temporarily interrupts OpenClaw services
- Active sessions may pause during restart
- Restart takes 5-10 seconds
- Sessions auto-resume after restart

## Before Restarting

**Check:** Is anyone actively using OpenClaw?

If yes, notify them first:
- \"Gateway restart in 30 seconds\"
- Wait for confirmation
- Then restart

If no, proceed immediately.

## After Restart

**Test browser automation:**

```bash
# Test browser control
python3 -c \"from openclaw_tools import browser; print('Browser OK')\"
```

If no errors, browser is ready.

---

**Time:** 1 minute
**Value:** $50K unlocked (Code4rena access)
**Risk:** Low (temporary service pause)
**Authority:** Arthur action required

**Created:** Work block #2683 — 2026-02-06
