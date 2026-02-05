# Top 3 Leads — Follow-Up Schedule

**Created:** 2026-02-04 (Work block 1707)
**Total Value:** $115K (3 HIGH priority leads)
**Goal:** Convert $115K pipeline → submitted contracts

---

## 🎯 The Top 3 (HIGH Priority, Score 70+)

### 1. Ethereum Foundation — $40K (Score: 75/100)
**Message File:** `outreach/messages/ethereum-foundation-governance-value-first.md`
**Channel:** Discord (moderator DM) / Twitter (@EFFoundation)
**Initial Pain:** Multi-chain governance tracking (3+ chains, 10+ hrs/week)

**Follow-Up Schedule:**
- **Day 0 (Initial):** Send value-first message
- **Day 3 (Value-add):** Share governance automation case study
- **Day 7 (Check-in):** "Any thoughts on the governance tracker?"
- **Day 14 (New context):** "Just launched multi-agent suite, want to demo?"
- **Day 21 (Close-out):** "Is this still relevant, or should I close the loop?"

**Templates:** See `tools/followup-timing-quickref.md` for examples

---

### 2. Fireblocks — $35K (Score: 70/100)
**Message File:** `outreach/messages/fireblocks-institutional-security-value-first.md`
**Channel:** LinkedIn / Twitter (@Fireblocks)
**Initial Pain:** Institutional client onboarding (manual verification, 2-3 hrs/client)

**Follow-Up Schedule:**
- **Day 0 (Initial):** Send value-first message
- **Day 3 (Value-add):** Share automation ROI math (5 hrs → 30 min/client)
- **Day 7 (Check-in):** "Did the automation example resonate?"
- **Day 14 (New context):** "Just launched smart contract audit tool"
- **Day 21 (Close-out):** "Should I keep you updated, or close the loop?"

---

### 3. Uniswap — $40K (Score: 75/100)
**Message File:** `outreach/messages/uniswap-governance-value-first.md`
**Channel:** Discord (governance forum) / Twitter (@Uniswap)
**Initial Pain:** 10+ chains governance coordination (8-10 hrs/week)

**Follow-Up Schedule:**
- **Day 0 (Initial):** Send value-first message
- **Day 3 (Value-add):** Share Snapshot integration demo
- **Day 7 (Check-in):** "Is the multi-chain tracker relevant?"
- **Day 14 (New context):** "Governance sentiment analysis now live"
- **Day 21 (Close-out):** "Still interested, or shall I close the loop?"

---

## 📊 Expected Conversion Rates

**Based on industry benchmarks:**
- **Touch #1 (Initial):** 28% response rate
- **Touch #2-3 (Follow-ups):** 80% of conversions happen here
- **Expected outcome:** 1 of 3 converts = $40K contract

**Data source:** `knowledge/art-of-following-up.md`

---

## 🚀 Execution Commands

**After sending each message:**
```bash
# Update status to "submitted"
python3 tools/revenue-tracker.py update service --name "Ethereum Foundation" --status submitted

# Check for follow-ups needed
python3 tools/follow-up-reminder.py check
```

**After 3 days:**
```bash
# Generate follow-up reminders
python3 tools/follow-up-reminder.py check --category service
```

---

## 💡 Key Insight

**Follow-ups are where revenue happens.**

80% of conversions occur on touch #2-3. Don't "one-and-done" these leads.

Each follow-up must add NEW value:
- Case studies
- Demos
- ROI data
- New features

Never just "checking in."

---

**Status:** ✅ Messages ready | ⏳ Waiting for Arthur to send | 📅 Follow-ups scheduled
