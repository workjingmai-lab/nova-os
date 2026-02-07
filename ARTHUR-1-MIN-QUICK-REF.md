# Arthur's 1-Minute Command Reference

**For:** Arthur (Operator/Guardian)
**When:** You have 1 minute to execute
**Goal:** Ship the $1.49M pipeline

---

## 🚀 I Want to Send Everything NOW

```bash
# One command to ship all $734.5K ready pipeline
bash tools/send-everything.sh full
```

**Time:** 15-20 min
**Result:** $734.5K sent (services $609.5K + grants $125K)
**ROI:** $48,966/min

---

## 📊 I Want to See Pipeline Status

```bash
# Quick pipeline summary
python3 tools/revenue-tracker.py summary
```

**Shows:** Total potential, ready to submit, submitted, won

---

## 🎯 I Want Top Leads Only

```bash
# Show HIGH priority leads (10 targets = $660K)
python3 tools/lead-prioritizer.py | grep "HIGH PRIORITY" -A 15
```

**Result:** Top 10 service leads, sorted by score

---

## 💰 I Want EXPERT Tier Only (Fastest $235K)

```bash
# Send top 3 EXPERT tier messages (EF, Uniswap, Polygon)
python3 tools/service-batch-send.py --tier expert --limit 3
```

**Time:** 10 min
**Result:** $235K sent to highest-value targets

---

## 🔧 I Want to Fix Blockers

```bash
# Gateway restart (1 min → $50K bounties unblocked)
# Ask Nova to run: openclaw gateway restart

# GitHub CLI auth (5 min → $125K grants unblocked)
gh auth login
# Follow prompts to authenticate
```

**Total:** 6 min → $175K unblocked = $29,166/min ROI

---

## 📝 I Want Full Execution Plan

```bash
# Read the 57-minute plan
cat ARTHUR-57-MIN-QUICK-REF.md
```

**Time:** 2 min read
**Plan:** 4 phases, $632K total, $11,088/min ROI

---

## 🆘 I'm Stuck / Something Broke

```bash
# Run diagnostics
bash tools/status-check.sh

# Check logs
tail -50 diary.md | grep "Work block"
```

**Then:** Paste output to Nova with context

---

## ⏱️ I Have Only 5 Minutes

**Best ROI:**
1. Run `bash tools/send-everything.sh quick` (5 min → $609.5K services sent)
2. OR run gateway restart (1 min) + GitHub auth (5 min) = $175K unblocked

---

## 🎯 I Have 15 Minutes

**Best ROI:**
1. Unblock everything (6 min): Gateway restart + GitHub auth
2. Send EXPERT tier (3 min): Top 3 HIGH priority
3. Send remaining HIGH (6 min): 7 more HIGH priority
**Total:** 15 min → $660K sent + $175K unblocked = $835K

---

## 💡 Pro Tips

1. **Start with status check** — `python3 tools/revenue-tracker.py summary`
2. **Use send-everything.sh** — It handles batching, validation, confirmation
3. **Unblock first** — 6 min prep = $175K, 15 min send = $660K
4. **Check diary.md** — Nova documents everything there
5. **Ask Nova** — Nova knows the full context and can guide execution

---

## 📂 Key Files

- `START-HERE.md` — Master execution index
- `ARTHUR-57-MIN-QUICK-REF.md` — Full 57-min plan
- `SEND-EVERYTHING.md` — Sending options explained
- `EXECUTION-DASHBOARD.md` — Pipeline breakdown by tier
- `tools/send-everything.sh` — The one command to rule them all

---

## 🚨 Common Issues

**Issue:** "GitHub auth failed"
**Fix:** Run `gh auth login` and follow prompts

**Issue:** "Browser not working"
**Fix:** Ask Nova to restart gateway: `openclaw gateway restart`

**Issue:** "Permission denied"
**Fix:** Run `chmod +x tools/send-everything.sh`

**Issue:** "Python module not found"
**Fix:** All tools use stdlib, no pip install needed

---

**Remember:** Nova has done the prep work. Your job is execution. Run one command, confirm, repeat.

**Last updated:** 2026-02-06 22:20Z
**Work block:** 2889
