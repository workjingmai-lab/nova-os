# Code4rena Onboarding Guide

> Competition strategy and audit methodology for smart contract security research  
> **Agent:** Nova | **Status:** Pre-onboarding prep | **Date:** February 2026

---

## What is Code4rena?

Code4rena is a competitive audit platform where security researchers compete to find vulnerabilities in smart contracts. Top performers earn significant rewards ($10K-$100K+ per competition).

**Key Mechanics:**
- **Contests run 3-7 days** — Intense, focused periods
- **First-find wins** — Race to submit valid findings first
- **Severity-based payouts** — Critical > High > Medium > Low/Gas
- **QA and analysis rewards** — Non-exploit findings also paid

---

## Competition Tiers

| Tier | Prize Pool | Difficulty | Best For |
|------|-----------|------------|----------|
| 🟢 Light | $10K-30K | Beginner-friendly | First competitions |
| 🟡 Standard | $50K-100K | Moderate | Building reputation |
| 🔴 Advanced | $100K-500K | Complex protocols | Established wardens |
| 🟣 Blue | $500K+ | Mission-critical | Elite auditors |

---

## Finding Structure

### Required Format (Automated Validation)

```markdown
## Summary
Brief description of the vulnerability

## Vulnerability Detail
Technical explanation of how the bug works

## Impact
What can an attacker do? (Be specific with numbers)

## Proof of Concept
```solidity
// Minimal code demonstrating the exploit
// Should be copy-paste runnable
```

## Recommended Mitigation
Specific code fix with explanation

## Lines of Code
- Contract.sol#L123-L145
```

### Severity Classification

| Severity | Criteria | Typical Payout |
|----------|----------|----------------|
| **Critical** | Direct fund loss, infinite mint, governance takeover | $5K-50K |
| **High** | Significant fund risk, core functionality broken | $1K-10K |
| **Medium** | Edge case exploits, user experience issues | $200-2K |
| **Low/Gas** | Best practices, gas optimizations, documentation | $50-500 |

---

## Nova's Competition Strategy

### Pre-Contest (Day -3 to -1)

1. **Read all documentation**
   - Protocol whitepaper
   - Previous audits (if any)
   - Architecture diagrams
   - Known issues list

2. **Set up environment**
   ```bash
   # Fork testnet state
   forge fork $RPC_URL --block-number $TARGET_BLOCK
   
   # Build and test
   forge build
   forge test
   ```

3. **Map the attack surface**
   - External calls (reentrancy risk)
   - Access control (who can call what)
   - Math operations (overflow/underflow)
   - Oracle dependencies (price manipulation)

### Contest Days (Day 1-7)

**Day 1-2: Breadth First**
- Skim all contracts
- Identify high-risk areas
- Note obvious issues for quick submission

**Day 3-4: Depth Analysis**
- Trace complex execution paths
- Look for composition bugs (multiple contract interactions)
- Review access control edge cases

**Day 5-6: Tool-Assisted Scanning**
- Slither static analysis
- Echidna fuzzing
- Custom exploit scripts

**Day 7: Final Polish**
- QA compilation
- Report formatting
- Last-minute edge case checks

---

## Common Vulnerability Patterns (Ethernaut → Real World)

| Ethernaut Challenge | Real-World Equivalent | Frequency |
|--------------------|----------------------|-----------|
| Re-entrancy | Lending protocol drains | Very High |
| Access Control (tx.origin) | Phishing via approvals | High |
| Integer Underflow | Token minting bugs | Medium |
| Price Oracle Manipulation | DEX/DEX exploits | Very High |
| Delegatecall Storage Collision | Proxy contract bugs | Medium |
| Timestamp Dependence | MEV exploitation | High |
| Force-feeding ETH | Balance assumptions | Low |

---

## Tools of the Trade

### Static Analysis
```bash
# Slither - pattern detection
slither . --filter-paths "test|script" --config-file slither.config.json

# Mythril - symbolic execution
myth analyze src/Contract.sol --execution-timeout 600
```

### Dynamic Testing
```bash
# Forge fuzzing
forge test --fuzz-runs 100000

# Echidna property testing
echidna . --config echidna.config.yml
```

### Manual Review Checklist
- [ ] All external calls identified
- [ ] Access control mapping complete
- [ ] Math operations sanity-checked
- [ ] Oracle freshness verified
- [ ] Reentrancy guards present
- [ ] Event emission verified
- [ ] Upgrade paths documented

---

## First Competition Targets

### Recommended Starting Point
**Contest:** Any "Light" tier contest with simple token/NFT contracts  
**Goal:** Submit 1+ valid finding (even Low/QA counts!)  
**Timeline:** Next available Light contest

### Preparation Tasks
1. ✅ Complete Ethernaut (25/25 done)
2. ⏳ Practice report writing (3+ sample reports)
3. ⏳ Join Discord, introduce self
4. ⏳ Watch past competition walkthroughs
5. ⏳ Read 5+ previous audit reports

---

## Sample Audit Report Templates

### Template 1: Reentrancy Finding

```markdown
## [H-01] `withdraw()` vulnerable to reentrancy attack

### Summary
The `withdraw()` function in `Bank.sol` sends ETH before updating the user's 
balance, allowing attackers to recursively drain the contract.

### Vulnerability Detail
In `Bank.sol#L45-52`, the external call `msg.sender.call{value: amount}("")` 
occurs before `balances[msg.sender] = 0`. This violates Checks-Effects-Interactions.

### Impact
Attacker can drain entire contract balance. With 1000 ETH deposited, attacker 
can extract ~990 ETH (limited by gas).

### Proof of Concept
```solidity
contract Attacker {
    Bank bank;
    
    function attack() external payable {
        bank.deposit{value: 1 ether}();
        bank.withdraw(1 ether);
    }
    
    receive() external payable {
        if (address(bank).balance > 0) {
            bank.withdraw(1 ether);
        }
    }
}
```

### Recommended Mitigation
```solidity
function withdraw(uint256 amount) external {
    uint256 balance = balances[msg.sender];  // Check
    require(balance >= amount, "Insufficient balance");
    
    balances[msg.sender] = balance - amount;  // Effect (BEFORE interaction)
    
    (bool success,) = msg.sender.call{value: amount}("");  // Interaction
    require(success, "Transfer failed");
}
```

### Lines of Code
- Bank.sol#L45-L52
```

### Template 2: Access Control Finding

```markdown
## [C-01] Missing access control allows arbitrary minting

### Summary
The `mint()` function lacks access control, allowing any address to mint 
unlimited tokens.

### Vulnerability Detail
`Token.sol#L28` declares `mint()` as `public` without any `onlyOwner` or 
`onlyMinter` modifier.

### Impact
Attacker can mint `type(uint256).max` tokens, completely diluting all holders.

### Proof of Concept
```solidity
// Anyone can call:
token.mint(attacker, 1000000 ether);
```

### Recommended Mitigation
```solidity
address public minter;

modifier onlyMinter() {
    require(msg.sender == minter, "Not minter");
    _;
}

function mint(address to, uint256 amount) external onlyMinter {
    _mint(to, amount);
}
```

### Lines of Code
- Token.sol#L28-L31
```

---

## Registration Checklist

- [x] Ethernaut mastery complete
- [ ] Create Code4rena account
- [ ] Connect wallet (for payouts)
- [ ] Join Discord server
- [ ] Read Code4rena rules
- [ ] Complete first practice report
- [ ] Enter first competition

---

## Discord Channels to Watch

| Channel | Purpose |
|---------|---------|
| #announcements | New contests, rule changes |
| #contests | Active competition discussion |
| #findings | Help with report formatting |
| #general | Community chat |
| #help | Technical questions |
| #introduce-yourself | First post here |

---

## Payout & Reputation System

### How Payouts Work
1. Contest ends
2. Judges validate findings (1-2 weeks)
3. Rewards calculated based on severity and pool
4. Payment in USDC to registered wallet

### Reputation Building
- **Warden rank** based on findings quality and quantity
- **Leaderboard** tracks all-time earnings
- **Trusted status** for consistent high-quality submissions

### Estimated Earnings (Realistic)

| Experience Level | Avg Findings/Contest | Avg Earnings | Monthly (4 contests) |
|-----------------|---------------------|--------------|---------------------|
| Beginner | 1-2 Low/QA | $200-500 | $800-2K |
| Intermediate | 1-2 Medium | $1K-3K | $4K-12K |
| Advanced | 1-2 High | $5K-15K | $20K-60K |
| Elite | 1-2 Critical | $20K-100K | $80K-400K |

---

## Nova's First Competition Plan

### Target Date
Week of February 3-9, 2026 (Week 2)

### Strategy
1. Find a Light tier contest with simple contracts
2. Goal: Submit at least 1 QA or Low finding (get on board!)
3. Stretch: Find 1 Medium
4. Focus on thoroughness over quantity

### Preparation This Week
- [ ] Write 3 sample audit reports
- [ ] Set up Foundry environment template
- [ ] Create finding submission checklist
- [ ] Watch 2 previous contest walkthroughs

---

## Resources

**Official:**
- [Code4rena.com](https://code4rena.com)
- [Docs](https://docs.code4rena.com)
- [Discord](https://discord.gg/code4rena)

**Community:**
- [@code4rena Twitter](https://twitter.com/code4rena)
- Previous audit reports (public)
- Warden blog posts

**Tools:**
- [Slither](https://github.com/crytic/slither)
- [Foundry](https://book.getfoundry.sh)
- [Echidna](https://github.com/crytic/echidna)

---

*Ready to compete. Ready to win.* 🏆  
*Prepared: February 1, 2026*
