# Operator Daily Checklist — 30-Second Status Review

*For Arthur — Run this checklist to verify Nova's operational status.*

## ⚡ Quick Status Commands

```bash
# 1. Overall system status (5 sec)
python3 tools/operator-status.py

# 2. Revenue pipeline snapshot (5 sec)
python3 tools/revenue-tracker.py status

# 3. Follow-up status (5 sec)
python3 tools/follow-up-reminder.py status

# 4. Blocker check (5 sec)
python3 tools/execution-gap.py

# 5. Today summary (10 sec)
python3 tools/quick-status.py
```

## 🎯 Expected Output

| Check | Good Status | Action If Not |
|-------|-------------|---------------|
| System | `OPERATIONAL` or `OPERATOR MODE` | Check logs |
| Pipeline | `$1.49M` total | Run `revenue-tracker.py` |
| Blockers | `2 blockers ($180K)` | Execute 57-min plan |
| Messages Sent | `0 sent` = pre-game | Run outreach guides |
| Conversion | `0%` = expected | Monitor for responses |

## ✅ Daily Check (30 seconds)

- [ ] Run `operator-status.py` → verify mode
- [ ] Check revenue tracker → confirm pipeline
- [ ] Check execution gap → note blockers
- [ ] Check follow-ups → any responses?
- [ ] Done — Continue with day

## 🚨 If Blockers Active

**Current blockers (as of 2026-02-07):**
1. Gateway restart → $50K bounties
2. GitHub auth → $125K grants

**Action:** Run 57-min execution plan → `docs/ARTHUR-57-MIN-QUICK-REF.md`

## 📊 Weekly Review (5 min)

- [ ] Pipeline growth vs last week
- [ ] Response rates on outreach
- [ ] Tool usage patterns
- [ ] Knowledge articles created
- [ ] Moltbook engagement stats

---

*Created: Work block 3177 — 2026-02-07*
*Purpose: 30-second status verification for Operator Arthur*
