# PRE-FLIGHT-CHECKLIST.md — Before You Execute

**Run this 2-minute check before starting the 57-minute plan.**  
**Catch blockers early. Save time. Ship faster.**

---

## ✅ Checklist (2 Minutes)

### 1. GitHub Auth (5 seconds)
```bash
gh auth status
```
- [ ] Shows "Logged in to github.com"
- [ ] If not: `gh auth login` → follow prompts

### 2. Gateway Status (5 seconds)
```bash
openclaw gateway status
```
- [ ] Shows "running"
- [ ] If not: `openclaw gateway restart`

### 3. Pipeline Files Exist (10 seconds)
```bash
ls revenue-pipeline.json outreach/messages/*.md 2>/dev/null | wc -l
```
- [ ] Shows "52" or higher (52 messages ready)
- [ ] If 0: Run `python3 tools/revenue-tracker.py init`

### 4. Tracker Works (10 seconds)
```bash
python3 tools/revenue-tracker.py status | head -5
```
- [ ] Shows pipeline totals
- [ ] If error: Check Python install, install deps

### 5. Guides Accessible (10 seconds)
```bash
ls START-HERE.md ARTHUR-57-MIN-QUICK-REF.md NEXT-STEPS.md TROUBLESHOOTING.md
```
- [ ] All 4 files listed
- [ ] If missing: Pull latest from repo

### 6. Send Script Ready (20 seconds)
```bash
head -20 send-everything.sh
```
- [ ] Shows message-sending commands
- [ ] If missing: Check `outreach/send-everything.sh`

---

## 🚦 Status Interpretation

| Checks Passed | Status | Action |
|--------------|--------|--------|
| 6/6 | ✅ GO | Execute 57-min plan now |
| 5/6 | ⚠️ CAUTION | Fix the one issue, then go |
| ≤4/6 | 🛑 STOP | Fix blockers first |

---

## 🚨 Common Failures

| Check | Common Issue | Fix |
|-------|-------------|-----|
| GitHub | "not logged in" | `gh auth login` |
| Gateway | "stopped" | `openclaw gateway restart` |
| Pipeline | "0 files" | Rebuild from tracker |
| Tracker | ImportError | `pip install -r requirements.txt` |

---

## ⏱️ Time Budget

- Checklist: 2 minutes
- Fix issues: 5-10 minutes (if any)
- **Total pre-flight:** ≤12 minutes
- **Then:** 57 minutes to $632K

---

## 🎯 Ready?

```bash
# Final confirmation
echo "GitHub: $(gh auth status 2>&1 | head -1)"
echo "Gateway: $(openclaw gateway status 2>&1 | head -1)"
echo "Messages: $(ls outreach/messages/*.md 2>/dev/null | wc -l) ready"
echo ""
echo "Ready to execute. Run: bash send-everything.sh"
```

---

*Pre-flight checklist: Work block 3060*  
*Purpose: Zero-surprise execution*
