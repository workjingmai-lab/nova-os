# Pre-Flight Checklist: Arthur's 21-Minute Plan

> Before you execute the $427.5K plan, run this 30-second checklist.

**Total time:** 30 seconds | **Value at stake:** $427.5K

---

## ✅ Phase 1: Gateway Restart (1 min → $180K unblocked)

### Before You Run `openclaw gateway restart`

- [ ] **Browser automation working?** Test with a quick `browser action=status`
- [ ] **GitHub auth working?** Run `gh auth status` to verify
- [ ] **API keys loaded?** Check Moltbook, Code4rena access
- [ ] **Service running?** `openclaw gateway status` should show "active"

**If any fail:** Don't restart. Fix the issue first.

**Execute:**
```bash
openclaw gateway restart
```

**Verify success:**
```bash
openclaw gateway status  # Should show "active"
gh auth status           # Should show "logged in"
browser action=status    # Should show "connected"
```

---

## ✅ Phase 2: Send 13 Service Messages (20 min → $247.5K)

### Before You Send

- [ ] **Top 3 HIGH priority leads first** ($115K total)
  - [ ] Ethereum Foundation ($40K)
  - [ ] Fireblocks ($35K)
  - [ ] Uniswap ($40K)

- [ ] **Message files verified?** Check `outreach/messages/` folder
- [ ] **Channel locations confirmed?** Discord, Twitter, email
- [ ] **Lead prioritizer run?** `python3 tools/lead-prioritizer.py --ready`
- [ ] **Revenue tracker updated?** `python3 tools/revenue-tracker.py summary`

### Send Order (HIGH → MEDIUM priority)

**HIGH Priority (send first, 6 min):**
1. Ethereum Foundation → Discord/Twitter (2 min)
2. Fireblocks → Twitter/Email (2 min)
3. Uniswap → Discord/Twitter (2 min)

**MEDIUM Priority (send next, 14 min):**
4. Alchemy ($30K)
5. Infura ($30K)
6. Circle ($30K)
7. Polygon Labs ($25K)
8. Chainlink ($25K)
9. Arbitrum ($25K)
10. Optimism ($25K)

### After Each Message

```bash
# Update tracker
python3 tools/revenue-tracker.py update service --name "Company" --status submitted
```

### After All 13 Sent

```bash
# Verify
python3 tools/revenue-tracker.py summary
# Should show: $247.5K submitted
```

---

## ✅ Phase 3: Submit Grants (5 min → $125K)

### Before You Submit

- [ ] **GitHub repo pushed?** `git push origin main`
- [ ] **Grant files ready?** Check each grant's requirements
- [ ] **Proposal text written?** Each grant needs unique content
- [ ] **Revenue tracker updated?** Status: "ready" → "submitted"

### Submit Order

1. **Gitcoin Q1 Grant** — $5K (already submitted, verify)
2. **Octant Grant** — $25K
3. **Olas Grant** — $30K
4. **Optimism RPGF** — $50K
5. **Moloch DAO** — $20K

### After Submission

```bash
# Update tracker
python3 tools/revenue-tracker.py update grant --name "Grant Name" --status submitted --submitted_date $(date +%Y-%m-%d)
```

---

## ✅ Post-Execution Verification

### 5-Minute Check (run immediately after)

```bash
# 1. Pipeline status
python3 tools/revenue-tracker.py summary
# Should show: $427.5K submitted

# 2. Blocker status
python3 tools/blocker-tracker.py list
# Should show: 0 blockers (or lower priority)

# 3. Lead prioritizer
python3 tools/lead-prioritizer.py --ready
# Should show: Ready queue cleared or smaller

# 4. Moltbook status
python3 tools/moltbook-suite.py status
# Should show: API connected
```

### Update Today's Goal

```bash
# Edit today.md → Today's 1-Line Goal
# Change: "$152K ready NOW" → "$427.5K submitted"
```

---

## 🚨 Troubleshooting

### Gateway Restart Fails
```bash
# Check what's blocking
openclaw gateway status

# Common fixes:
openclaw gateway logs  # Check errors
openclaw gateway restart  # Try again
```

### Message Won't Send
```bash
# Verify channel
# Discord: Server invite working?
# Twitter: DM permissions?
# Email: Address correct?

# Verify file
cat outreach/messages/company-name-governance-value-first.md
# Content loaded? Formatting correct?
```

### Grant Submission Fails
```bash
# Check requirements
cat grants/grant-name-requirements.md
# All documents present?

# Check GitHub
git status
# Pushed? Repo public?
```

---

## 📊 Success Metrics

**After 27 minutes, you should have:**

- ✅ **$180K unblocked** (Gateway restart successful)
- ✅ **$247.5K submitted** (13 service messages sent)
- ✅ **$125K submitted** (5 grants submitted)
- ✅ **Total: $427.5K submitted**

**Conversion rate will track over next 14 days.**

---

## 🎯 Next Actions (After Execution)

### Day 3 Follow-Up
```bash
# Check who needs follow-up
python3 tools/follow-up-reminder.py --days-since 3
```

### Day 7 Follow-Up
```bash
# Check again
python3 tools/follow-up-reminder.py --days-since 7
```

### Weekly Pipeline Review
```bash
# Every Sunday
python3 tools/revenue-tracker.py export > pipeline-report-$(date +%Y-%m-%d).md
```

---

## 💡 Key Reminders

1. **Execute HIGH priority first** — $115K from 3 leads = $19,167/min
2. **Update tracker immediately** — Don't rely on memory
3. **Follow up relentlessly** — 80% of conversions happen touch #2-3
4. **Document everything** — What works, what doesn't, lessons learned
5. **Stay calm** — 27 minutes, $427.5K, $16K/min. Take your time, be accurate.

---

## 📁 File Locations (Quick Access)

```
outreach/
├── ARTHUR-21-MIN-PLAN.md          (Full playbook)
├── QUICK-EXECUTION-GUIDE.md       (Streamlined steps)
├── TOP-3-LEADS-NOW.md             (Focus targets)
└── messages/
    ├── ethereum-foundation-governance-value-first.md
    ├── fireblocks-governance-value-first.md
    ├── uniswap-governance-value-first.md
    └── [10 more...]
```

---

**You have everything you need. Execute.**

*27 minutes. $427.5K. Let's go.* 🚀
