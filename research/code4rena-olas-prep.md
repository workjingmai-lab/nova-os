# Code4rena Olas Competition — Preparation

**Competition:** Olas Protocol (Autonolas)
**Prize Pool:** $62,500 USDC
**Duration:** Feb 4-11, 2025 (upcoming)
**Status:** 🔴 BLOCKED — Need Sepolia wallet + Discord access

---

## What I Can Do Now (No Wallet Required)

### 1. Study Olas Protocol Architecture
- [ ] Read Olas whitepaper
- [ ] Review Autonolas docs (docs.autonolas.network)
- [ ] Understand agent service framework
- [ ] Map contract interactions

### 2. Review Similar Audits
- [ ] Search for past Olas/Autonolas audit reports
- [ ] Study findings from similar agent protocols
- [ ] Create common vulnerability checklist

### 3. Prepare Analysis Tools
- [ ] Set up Slither configuration
- [ ] Prepare Foundry test templates
- [ ] Create report templates

### 4. Document Attack Vectors
Focus areas for Olas:
- [ ] Agent registry manipulation
- [ ] Service staking/unstaking logic
- [ ] Multisig threshold attacks
- [ ] Tokenomics edge cases (OLAS token)
- [ ] Cross-chain message verification
- [ ] Governance timelock bypasses

---

## What I Need From Arthur

| Item | Why | Priority |
|------|-----|----------|
| Sepolia ETH | Gas for test transactions | CRITICAL |
| Code4rena Discord invite | Competition coordination | CRITICAL |
| GitHub token | Push findings to repo | HIGH |
| Wallet private key | Sign submissions | CRITICAL |

---

## Competition Strategy

### Phase 1: Reconnaissance (Days 1-2)
1. Map all contracts
2. Identify high-value targets
3. Run automated analysis (Slither, Mythril)
4. Document assumptions

### Phase 2: Deep Dive (Days 3-5)
1. Focus on highest-risk contracts
2. Manual review of complex functions
3. Fuzzing critical paths
4. Write PoCs for suspected bugs

### Phase 3: Submission (Days 6-7)
1. Finalize reports
2. Submit high-quality findings
3. Monitor for duplicates
4. Respond to judge questions

---

## Pre-Written Report Templates

### Template: Reentrancy Finding

```markdown
# [H/M/L] Reentrancy in [Contract.function]

## Summary
Brief description of the vulnerability.

## Vulnerability Detail
Technical explanation.

## Impact
What can an attacker do?

## Proof of Concept
```solidity
// PoC code here
```

## Recommended Mitigation
How to fix it.

## References
- Similar finding: [link]
- Olas contract: [line numbers]
```

### Template: Access Control Finding

```markdown
# [H/M/L] Missing Access Control in [Contract.function]

## Summary

## Vulnerability Detail

## Impact

## Proof of Concept

## Recommended Mitigation

## References
```

---

## Quick Links (When Accessible)

- Code4rena: https://code4rena.com/competitions
- Olas Docs: https://docs.autonolas.network
- Autonolas GitHub: https://github.com/valory-xyz
- My C4 Profile: [PENDING]

---

## Blockers Tracker

| Blocker | Status | Owner |
|---------|--------|-------|
| Sepolia wallet | ⏳ PENDING | Arthur |
| Code4rena Discord | ⏳ PENDING | Arthur |
| GitHub token | ⏳ PENDING | Arthur |

---

*Created: 2026-02-01*
*Ready to execute once unblocked*
