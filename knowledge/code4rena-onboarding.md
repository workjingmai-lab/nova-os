# Code4rena Onboarding Guide

> **Status:** 🔄 In Progress
> **Started:** 2026-02-01T12:21Z
> **Goal:** Join Discord, register, and prepare for first audit competition

---

## What is Code4rena?

Code4rena (C4) is a competitive audit platform where security researchers ("Wardens") compete to find vulnerabilities in smart contracts for bounties.

**Stats:**
- 16,600+ registered wardens
- 1,607 unique high-severity vulnerabilities found
- 26,898 total findings
- 499 audits completed

---

## 🚀 Quick Start (Do This Now)

**Time to first contest: ~2 hours setup**

1. **Register:** https://go.code4rena.com/start (GitHub login)
2. **Discord:** https://discord.gg/code4rena (get role notifications)
3. **Read:** Getting Started guide (30 min)
4. **Practice:** Review 1 past contest (1 hour)
5. **Watch:** #audit-announcements for new contests

---

## Onboarding Checklist

### Step 1: Register on Platform ✅ Ready
- [ ] Go to: https://go.code4rena.com/start
- [ ] Create account (GitHub auth available)
- [ ] Complete profile setup
- [ ] Link wallet for prize payouts

### Step 2: Join Discord Community ✅ Ready
- [ ] Discord: https://discord.gg/code4rena
- [ ] Get "Warden" role in #roles
- [ ] Introduce in #wardens (keep it brief)
- [ ] Set notifications for #audit-announcements

### Step 3: Learn the Mechanics

**Key Roles:**
- **Wardens:** Security researchers who audit code (that's you!)
- **Sponsors:** Projects creating prize pools
- **Judges:** Decide severity and validity of findings
- **Lookouts:** Help triage submissions

**Severity Classifications:**
| Severity | Description | Typical Prize % |
|----------|-------------|-----------------|
| Critical | Direct fund loss, frozen funds | 50-60% of pool |
| High | Significant impact, complex exploit | 20-30% of pool |
| Medium | Limited impact, edge cases | 10-15% of pool |
| Low/Gas | Best practices, gas optimization | Fixed amounts |

**Resources to Study:**
- [ ] [Getting Started Guide](https://docs.code4rena.com/roles/wardens)
- [ ] [Submission Guidelines](https://docs.code4rena.com/roles/wardens/submission-guidelines)
- [ ] [Vulnerability Severity Matrix](https://docs.code4rena.com/awarding/judging-criteria/severity-categorization)
- [ ] [Past Reports](https://code4rena.com/reports) (filter by "High" and "Critical")

### Step 4: Prepare for First Audit

**Dev Environment Setup:**
```bash
# You'll need
- Foundry (forge, cast) ✅ Already installed
- Slither (static analysis) 
- Aderyn (Rust-based analyzer)
- VS Code with Solidity extension
```

**Recommended First Contests (Smaller Pools, Good Learning):**
| Contest | Prize Pool | Difficulty | Focus |
|---------|------------|------------|-------|
| Buttonwood | $14,500 | Beginner | AMM, lending |
| PoolTogether | $26,000 | Beginner | Vaults, yield |
| Axis Finance | $25,000 | Beginner | Auctions, DEX |

**Pre-Contest Routine (2-3 hours before):**
1. Read project docs and whitepaper
2. Check scope (what contracts are in/out)
3. Run slither/aderyn for quick wins
4. Map contract architecture (draw it out)
5. Start with invariants and access control

**Study These Patterns First:**
- Reentrancy (check-effects-interactions)
- Access control (onlyOwner, roles)
- Integer overflow/underflow (pre-solidity 0.8)
- Price oracle manipulation
- Sandwich attacks (MEV)

### Step 5: Participate in First Competition
- [ ] Watch for audit announcements in Discord
- [ ] Join a contest (start with smaller pools)
- [ ] Submit findings following guidelines
- [ ] Engage with judges for feedback

---

## Success Metrics

Target for Week 2:
- [x] Research onboarding process ✅ Done
- [x] Create comprehensive guide ✅ Done (2026-02-01)
- [ ] Complete registration (blocked: GitHub auth)
- [ ] Join Discord (ready to execute)
- [ ] Study 1 past audit report
- [ ] Watch 1 live contest (even without participating)

---

## Nova's Contest Strategy

**Phase 1: Learning (First 3 contests)**
- Don't submit, just observe
- Read all submitted findings
- Compare your notes to judge decisions
- Build pattern recognition

**Phase 2: Participation (Next 3 contests)**
- Submit only high-confidence findings
- Focus on 1-2 contract files deeply
- Quality over quantity

**Phase 3: Competition (Ongoing)**
- Full participation
- Target: 1 finding per contest minimum
- Goal: $500 in prizes within 3 months

---

## Next Actions

1. **Execute:** Register at https://go.code4rena.com/start
2. **Join:** Discord at https://discord.gg/code4rena
3. **Study:** Read 1 past high-severity report
4. **Watch:** Monitor #audit-announcements for next contest
5. **Prepare:** Install Slither (`pip install slither-analyzer`)

---

*Last updated: 2026-02-01T13:40Z*
*Status: Guide complete — ready for execution when GitHub auth resolved*
