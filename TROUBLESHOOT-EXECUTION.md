# Troubleshooting Guide: What If Something Goes Wrong

**Problems happen. Here's how to fix them.**

---

## Scenario 1: Permission Denied

**Error:** `bash: tools/send-everything.sh: Permission denied`

**Fix:**
```bash
chmod +x tools/send-everything.sh
bash tools/send-everything.sh full
```

**Why:** Script isn't executable. One line fixes it.

---

## Scenario 2: Python Module Not Found

**Error:** `ModuleNotFoundError: No module named 'requests'`

**Fix:**
```bash
pip3 install requests
bash tools/send-everything.sh full
```

**Why:** Dependencies missing. One command installs them.

---

## Scenario 3: Authorization Failed (Moltbook)

**Error:** `401 Unauthorized` or `Invalid token`

**Fix:**
1. Check token: `grep moltbook_sk tools/.env`
2. If missing or expired, regenerate at Moltbook dashboard
3. Update `tools/.env` with new token
4. Retry: `bash tools/send-everything.sh full`

**Why:** Tokens expire. Regenerating takes 2 minutes.

---

## Scenario 4: Message Send Failed

**Error:** `Failed to send message to [target]`

**Fix:**
```bash
# Check individual message format
python3 tools/service-batch-send.py validate outreach/messages/[message-name].md

# Fix validation errors, then retry
bash tools/send-everything.sh full
```

**Why:** Malformed message. Validation catches it before sending.

---

## Scenario 5: Gateway Not Running

**Error:** `Cannot connect to OpenClaw gateway`

**Fix:**
```bash
# Check gateway status
openclaw gateway status

# If not running, start it
openclaw gateway start
```

**Why:** Gateway daemon stopped. Restarting takes 10 seconds.

---

## Scenario 6: Rate Limit Exceeded (Moltbook)

**Error:** `Rate limit exceeded. Try again in X minutes.`

**Fix:**
```bash
# Check how many posts remaining
python3 tools/moltbook-suite.py --check-limit

# Wait for rate limit to reset (24-hour rolling window)
# Then retry
bash tools/send-everything.sh full
```

**Why:** Moltbook limits posts per day. System tracks this automatically.

---

## Scenario 7: Nothing Worked

**Last Resort:**
```bash
# Run diagnostics
bash tools/status-check.sh

# Check logs
tail -50 logs/*.log 2>/dev/null || echo "No logs found"

# If still stuck, ask Nova:
# "Check execution status and diagnose blockers"
```

**Why:** If everything fails, status check + logs reveal the root cause.

---

## Prevention > Cure

**Before executing:**
1. Run `bash tools/status-check.sh` ✅
2. Check all systems show "OPERATIONAL" ✅
3. Read PRE-EXECUTION-FLIGHT-CHECK.md ✅

**Most errors = skip checklist.**

---

## Reality Check

**Most common issues:**
1. Script permissions (1 sec fix)
2. Missing dependency (10 sec fix)
3. Token expired (2 min fix)

**Worst case:** 5 minutes to diagnose and fix.

**ROI:** 5 minutes → $734.5K sent = $146,900/min

**Don't let fear of breaking stop you.** Everything is fixable in <5 minutes.

---

**Run now:** `bash tools/send-everything.sh full`

**If something breaks:** Read this guide. Fix it in 5 minutes. Done.
