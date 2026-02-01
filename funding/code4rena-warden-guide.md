# Code4rena Warden Onboarding Guide

## Overview
**Platform:** https://code4rena.com  
**Opportunity:** Competitive smart contract auditing  
**Entry Fee:** FREE  
**Gas Required:** ZERO  
**Earnings Potential:** $100-$50,000+ per audit  

---

## Why Code4rena is Perfect for Nova

1. **No Entry Barrier** — Register and start immediately
2. **Skills-Based** — Rewards knowledge, not capital
3. **Weekly Contests** — Constant opportunities
4. **Direct Payment** — USDC to wallet (sponsor often pays gas)
5. **Reputation Building** — Leaderboard establishes credibility

---

## Registration Steps

### Step 1: Create Account
- Visit: https://code4rena.com/register
- Connect wallet (when available) or use email
- Verify identity (KYC may be required for large payouts)

### Step 2: Join Discord
- Server: https://discord.gg/code4rena
- Channels to join:
  - `#announcements` — New audit alerts
  - `#questions` — Community support
  - `#warden-chat` — Fellow auditors
  - `#bot-commands` — Register for contests

### Step 3: Register for a Contest
```
!join contest-name
```
Example: `!join aurora-12-2023`

### Step 4: Review Code
- Access repo via GitHub link
- Read protocol documentation
- Identify vulnerabilities

### Step 5: Submit Findings
- Format: Markdown with proof of concept
- Severity: High/Medium/Gas/QA
- Submit via Code4rena UI

---

## Finding Categories

| Severity | Typical Payout | Examples |
|----------|---------------|----------|
| High Risk | $5,000-$50,000 | Reentrancy, access control, fund draining |
| Medium Risk | $1,000-$5,000 | Logic errors, DoS, precision loss |
| Gas Optimization | $100-$500 | Inefficient storage, redundant operations |
| QA Report | $100-$300 | Code quality, best practices |

---

## Nova's Advantages

1. **25/25 Ethernaut Complete** — Proven security knowledge
2. **Pattern Recognition** — Automated vulnerability detection
3. **Documentation Skills** — Clear, professional reports
4. **24/7 Availability** — Can review code continuously
5. **Tool-Assisted** — Custom scripts for analysis

---

## First Contest Strategy

### Week 1 Goal: First Submission
- Target: Gas optimization or QA report
- Lower competition than high-risk findings
- Builds reputation and confidence
- Establishes workflow

### Tools to Build
1. **Slither Integration** — Automated static analysis
2. **Mythril Runner** — Symbolic execution
3. **Report Template** — Standardized finding format
4. **POC Generator** — Automated proof-of-concept

---

## Active Contests Check

**Command to check active contests:**
```bash
curl -s https://code4rena.com/contests | grep -o 'contest/[a-z0-9-]*' | head -10
```

**Current Status:** ⏳ Need to monitor once registered

---

## Resources

- **Docs:** https://docs.code4rena.com
- **Judging Criteria:** https://docs.code4rena.com/roles/wardens/judging-criteria
- **Report Template:** https://docs.code4rena.com/roles/wardens/submitting-po
- **Past Reports:** https://code4rena.com/reports

---

## Blockers

1. **Wallet Connection** — Need wallet for registration
2. **GitHub Access** — Need to fork repos
3. **Discord** — Need account for community

**All require Arthur's credentials.**

---

## Immediate Actions (No Blockers)

- [x] Create this onboarding guide
- [ ] Research current active contests
- [ ] Study 3 past audit reports
- [ ] Draft report template
- [ ] Build Slither integration script

---

*Generated: 2026-02-01T13:05Z*  
*Status: READY TO EXECUTE (pending credentials)*
