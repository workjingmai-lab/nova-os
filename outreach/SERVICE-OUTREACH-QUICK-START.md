# Service Outreach — Quick Start Guide

**Created:** 2026-02-04 (Work block 1708)
**Pipeline Value:** $152K ready NOW (10 messages, zero blockers)
**Time to Execute:** ~20 minutes
**Expected Conversion:** 1-3 contracts = $40K-$115K

---

## 🎯 What You're Sending

10 value-first outreach messages to Web3 teams:
- 3 HIGH priority ($115K): Ethereum Foundation, Fireblocks, Uniswap
- 7 MEDIUM priority ($190K): Alchemy, Infura, Circle, Polygon, Chainlink, Arbitrum, Optimism

**Each message follows the PROOF framework:**
- **P**roblem: Specific pain point (research-backed)
- **R**esearch: "I noticed X about your governance/operations"
- **O**ffer: Clear solution (3-agent suite, automation, etc.)
- **O**utcome: ROI math ($X saves Y hours/year)
- **F**ollow-up: "Want to see a demo?" (soft CTA)

**No generic pitches.** Every message is researched and specific.

---

## 📂 Message Files Location

All messages are in `/home/node/.openclaw/workspace/outreach/messages/`:

**HIGH Priority (Send these first):**
1. `ethereum-foundation-governance-value-first.md` — $40K
2. `fireblocks-institutional-security-value-first.md` — $35K
3. `uniswap-governance-value-first.md` — $40K

**MEDIUM Priority (Send after HIGH):**
4. `alchemy-web3-infrastructure-value-first.md` — $30K
5. `infura-web3-infrastructure-value-first.md` — $30K
6. `circle-stablecoin-operations-value-first.md` — $30K
7. `polygon-labs-scaling-value-first.md` — $25K
8. `chainlink-oracle-operations-value-first.md` — $25K
9. `arbitrum-governance-value-first.md` — $25K
10. `optimism-governance-value-first.md` — $25K

---

## 🚀 How to Send (3 Options)

### Option 1: Manual Copy-Paste (Fastest)
1. Open message file in `outreach/messages/`
2. Copy the entire message
3. Paste into Discord DM / Twitter / LinkedIn
4. Send

**Time:** ~2 minutes per message

### Option 2: Use OpenClaw Message Tool (If Configured)
```bash
# Send via Telegram/other channel
message send --to <channel> --file outreach/messages/ethereum-foundation-governance-value-first.md
```

**Time:** ~1 minute per message

### Option 3: Batch Script (For Advanced Users)
Create a script that reads all 10 files and sends them via your preferred channel.

---

## ✅ After Sending: Track It

**Update the pipeline:**
```bash
# After sending Ethereum Foundation message
python3 tools/revenue-tracker.py update service --name "Ethereum Foundation" --status submitted --notes "Sent via Discord DM on 2026-02-04"

# Verify
python3 tools/revenue-tracker.py summary
```

**Set follow-up reminders:**
```bash
# Check for follow-ups due
python3 tools/follow-up-reminder.py check
```

---

## 📅 Follow-Up Schedule (For Top 3)

See `outreach/TOP-3-FOLLOW-UP-SCHEDULE.md` for detailed day 0/3/7/14/21 plan.

**Quick version:**
- **Day 3:** Send value-add (case study, demo, ROI data)
- **Day 7:** "Any thoughts?"
- **Day 14:** New context (feature launch, new tool)
- **Day 21:** Close-out or continue

**Rule:** Each follow-up must add NEW value. Never just "checking in."

---

## 🎯 Expected Outcome

**Industry benchmarks:**
- **Initial response rate:** 28% (based on value-first outreach)
- **Conversion rate:** 10-20% of leads → contracts
- **Expected result:** 1-3 contracts from 10 leads = $40K-$115K

**Data source:** `knowledge/art-of-following-up.md`, `knowledge/value-first-outreach-structure.md`

---

## 💡 Key Insight

**$152K is ready NOW.**

No blockers. No dependencies. No approvals needed.

Just open files → copy → paste → send.

20 minutes → $152K in play.

---

## 🔧 Tools to Use

**See what's ready:**
```bash
python3 tools/lead-prioritizer.py --ready --top 10
```

**Track pipeline:**
```bash
python3 tools/revenue-tracker.py summary
```

**Check follow-ups:**
```bash
python3 tools/follow-up-reminder.py check
```

---

**Status:** ✅ 10 messages ready | 🚀 Zero blockers | ⏳ Ready to send NOW
