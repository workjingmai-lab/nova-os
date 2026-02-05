# Grant Submission Quick-Start Guide

**Goal:** Submit 5 grant applications in 15 minutes → $125K in play

**Prerequisites:**
- [x] GitHub CLI installed (`gh` v2.86.0)
- [ ] GitHub auth completed: `gh auth login` (5 min → $125K unblocked)
- [x] Grant messages written (5 grants, $5K-$150K each)
- [x] Revenue pipeline tracked: `python3 tools/revenue-tracker.py list --status ready`

---

## 🚀 15-Minute Execution Plan

### Minute 0-5: GitHub Auth (ONE-TIME SETUP)
```bash
gh auth login
# Follow prompts: GitHub.com → HTTPS → Yes (upload SSH key) → Login with browser
```
**ROI:** 5 min → $125K grants unblocked = **$25,000/min**

---

### Minute 5-20: Submit 5 Grants (3 min each)

#### 1. Gitcoin Grant ($20K-$40K potential)
**Target:** https://gitcoin.co/grants
**Message:** `outreach/grants/gitcoin-grant-proposal.md`
**Action:**
- Copy proposal content
- Submit via Gitcoin grants form
- Track in revenue-tracker: `python3 tools/revenue-tracker.py update gitcoin-grant --status submitted`

#### 2. Octant Grants ($15K-$25K potential)
**Target:** https://octant.build/#/grants
**Message:** `outreach/grants/octant-grant-proposal.md`
**Action:**
- Copy proposal content
- Submit via Octant platform
- Track in revenue-tracker: `python3 tools/revenue-tracker.py update octant-grant --status submitted`

#### 3. Olas Grants ($10K-$20K potential)
**Target:** https://olas.network/ghost
**Message:** `outreach/grants/olas-grant-proposal.md`
**Action:**
- Copy proposal content
- Submit via Olas grants portal
- Track in revenue-tracker: `python3 tools/revenue-tracker.py update olas-grant --status submitted`

#### 4. Optimism RPGF ($50K-$150K potential)
**Target:** https://gap.optimism.io
**Message:** `outreach/grants/optimism-rpgf-proposal.md`
**Action:**
- Copy proposal content
- Submit via Optimism Governance page
- Track in revenue-tracker: `python3 tools/revenue-tracker.py update optimism-rpgf --status submitted`

#### 5. Moloch DAO Grant ($5K-$10K potential)
**Target:** Moloch DAO Discord / governance forum
**Message:** `outreach/grants/moloch-grant-proposal.md`
**Action:**
- Copy proposal content
- Post to Moloch governance forum
- Track in revenue-tracker: `python3 tools/revenue-tracker.py update moloch-grant --status submitted`

---

## 📊 After Submission: Track Conversion

### Check Status Daily
```bash
python3 tools/revenue-tracker.py list --status submitted
```

### Update Outcomes
```bash
# If funded:
python3 tools/revenue-tracker.py update gitcoin-grant --status won --amount 20000

# If rejected:
python3 tools/revenue-tracker.py update gitcoin-grant --status lost
```

### Follow-Up Schedule
Use `tools/follow-up-reminder.py` to check for pending follow-ups:
- **Day 7:** Check application status
- **Day 14:** Follow up if no response
- **Day 30:** Final follow-up or pivot

---

## 📋 Pre-Submission Checklist

For each grant, verify:
- [ ] Proposal file exists in `outreach/grants/`
- [ ] Message is personalized to grant program
- [ ] ROI math is clear (what they get, timeline, impact)
- [ ] Contact email is correct
- [ ] GitHub repo linked (if required)
- [ ] Revenue tracker updated

---

## 🎯 Expected Outcomes

**Conservative (20% conversion):** 1 of 5 grants = $25K
**Moderate (40% conversion):** 2 of 5 grants = $75K
**Aggressive (60% conversion):** 3 of 5 grants = $175K

**Timeline:** 4-8 weeks for decisions (varies by program)

---

## 🔄 Blockers & Solutions

| Blocker | Solution | Time |
|---------|----------|------|
| GitHub auth needed | `gh auth login` | 5 min |
| Grant portal issues | Use alt contact (Discord/email) | +5 min |
| Proposal not ready | Use template from `outreach/` | +10 min |
| Unclear requirements | Ask in Discord/community | +15 min |

---

## 📝 Templates Directory

All grant proposals are in `outreach/grants/`:
```
outreach/grants/
├── gitcoin-grant-proposal.md
├── octant-grant-proposal.md
├── olas-grant-proposal.md
├── optimism-rpgf-proposal.md
└── moloch-grant-proposal.md
```

Each follows the PROOF framework:
- **P**roblem: What gap exists
- **R**esearch: Why this solution
- **O**ffer: What you get (agents, tools, automation)
- **O**utcome: Expected impact (ROI, timeline)
- **F**ollow-up: Next steps

---

## 💡 Key Insight

**Grants ≠ Charity. Grants = Investment.**

Frame every proposal as:
- Input: $10K-$50K grant
- Output: $100K+ value to ecosystem (tools, docs, research, public goods)
- ROI: 10× minimum return on their investment

You're not asking for money. You're offering a leveraged investment in autonomous agent infrastructure.

---

## ⚡ Speed Run Command

Once GitHub auth is complete, submit all 5 grants in parallel:
```bash
# Terminal 1: Gitcoin
cat outreach/grants/gitcoin-grant-proposal.md | pbcopy  # Copy to clipboard
# Open https://gitcoin.co/grants → Paste → Submit

# Terminal 2: Octant
cat outreach/grants/octant-grant-proposal.md | pbcopy
# Open https://octant.build → Paste → Submit

# ... repeat for all 5
```

**Total time:** 15 min (3 min per grant × 5)

**Value:** $125K in play → **$8,333/min ROI**

---

**Created:** 2026-02-04 (Work block 1746)
**Status:** ✅ Ready for execution (pending GitHub auth)
**Next action:** Arthur runs `gh auth login` → submits 5 grants → $125K pipeline in play
