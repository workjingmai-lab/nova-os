# TROUBLESHOOTING.md — Quick Fixes for Common Issues

**One-page fix guide.** If something breaks, find it here. 30-second solutions.

---

## 🔴 BLOCKER: GitHub Not Authenticated

**Error:** `gh auth status` fails OR grant submission scripts return auth errors

**Fix (5 min → unblocks $125K):**
```bash
gh auth login
# Follow prompts → choose HTTPS → paste token
```

**Need a token?** https://github.com/settings/tokens → Generate new → check "repo" scope

---

## 🔴 BLOCKER: Gateway Not Running (Browser Access)

**Error:** Browser automation fails OR `openclaw gateway status` shows stopped

**Fix (1 min → unblocks $50K bounties):**
```bash
openclaw gateway restart
```

**Verify:** `openclaw gateway status` should show "running"

---

## 🟡 Pipeline Commands Not Found

**Error:** `python3 tools/revenue-tracker.py` → "No such file or directory"

**Fix:**
```bash
cd ~/.openclaw/workspace
python3 tools/revenue-tracker.py status
```

---

## 🟡 Send Script Permission Denied

**Error:** `bash tools/send-everything.sh` → "Permission denied"

**Fix:**
```bash
chmod +x tools/send-everything.sh
bash tools/send-everything.sh
```

---

## 🟡 Lead Files Missing or Empty

**Error:** `service-batch-send.py` → "No leads found"

**Check:**
```bash
ls -la outreach/leads/*/
```

**Fix:** Files should be in:
- `outreach/leads/expert/EF.md`, `Fireblocks.md`, etc.
- `outreach/leads/top10/` for HIGH priority

**Regenerate if missing:**
```bash
python3 tools/lead-generator.py --refresh
```

---

## 🟡 Follow-up Reminders Not Working

**Error:** `followup-reminder.py` returns no reminders

**Check cron status:**
```bash
openclaw cron list
```

**Expected:** Should show "followup-daily" job

**If missing, recreate:**
```bash
openclaw cron add --name "followup-daily" --schedule "0 9 * * *" --command "python3 tools/followup-reminder.py check"
```

---

## 🟡 Moltbook Post Failed

**Error:** `moltbook-suite.py` → API timeout or rate limit

**Quick check:**
```bash
python3 tools/moltbook-suite.py status
```

**If rate limited:** Wait 1 hour, posts auto-queue
**If auth failed:** Check `MOLTBOOK_API_KEY` in environment

---

## 🟢 "Is It Working?" Quick Health Check

**One command to verify everything:**
```bash
python3 tools/operator-status.py
```

**Expected output:**
- Blockers: 0 (or listed with fix commands)
- Pipeline: $XXXK ready
- Tools: 81 active
- Status: ✅ GO

---

## 🆘 Still Stuck?

**Check the full status:**
```bash
cat STATUS-FOR-ARTHUR.md
```

**Or ask Nova:** Mention me in any message and describe the error.

---

**Golden rule:** Most issues are the top 2 blockers (GitHub auth, Gateway restart). Fix those first.

*Last updated: Work block 3056*
