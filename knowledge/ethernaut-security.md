# Learning: Smart Contract Security via Ethernaut

**Date:** 2026-02-01  
**Source:** Completing 21/25 Ethernaut levels  
**Impact:** High — foundation for security research career

---

## What is Ethernaut

OpenZeppelin's Web3/Solidity CTF. 25 vulnerable contracts to exploit. Free, educational, industry-standard.

## Progress Log

| Level | Name | Status | Technique |
|-------|------|--------|-----------|
| 0 | Hello Ethernaut | ✅ | Intro |
| 1 | Fallback | ✅ | Receive functions |
| 2 | Fallout | ✅ | Constructor typos |
| 3 | Coin Flip | ✅ | Predictable randomness |
| 4 | Telephone | ✅ | tx.origin vs msg.sender |
| 5 | Token | ✅ | Integer underflow |
| 6 | Delegation | ✅ | delegatecall |
| 7 | Force | ✅ | Selfdestruct |
| 8 | Vault | ✅ | Storage visibility |
| 9 | King | ✅ | Denial of service |
| 10 | Re-entrancy | ✅ | Reentrant calls |
| 11 | Elevator | ✅ | Interface abuse |
| 12 | Privacy | ✅ | Storage slots |
| 13 | Gatekeeper One | ✅ | Gas manipulation |
| 14 | Gatekeeper Two | ✅ | Extcodesize |
| 15 | Naught Coin | ✅ | ERC20 approval |
| 16 | Preservation | ✅ | Storage collision |
| 17 | Recovery | ✅ | Address derivation |
| 18 | MagicNumber | ✅ | Bytecode |
| 19 | Alien Codex | ✅ | Dynamic arrays |
| 20 | Denial | ✅ | Gas griefing |
| 21 | Shop | ✅ | External call state |
| 22 | Dex | 🔄 | In progress |
| 23-25 | — | ⏳ | Pending |

## Key Vulnerabilities Learned

### 1. Re-entrancy
```solidity
// Attacker calls back before state update
function withdraw() {
    uint amount = balances[msg.sender];
    (bool success,) = msg.sender.call{value: amount}("");  // ⚠️ Re-entrant
    require(success);
    balances[msg.sender] = 0;  // Too late!
}
```

**Fix:** Checks-Effects-Interactions pattern

### 2. tx.origin Authentication
```solidity
// WRONG: Can be phished
require(tx.origin == owner);

// RIGHT: Use msg.sender
require(msg.sender == owner);
```

### 3. Integer Underflow (pre-0.8.0)
```solidity
// Solidty < 0.8.0
uint8 x = 0;
x -= 1;  // x = 255!
```

**Fix:** Use SafeMath or Solidity ^0.8.0

### 4. Storage Visibility
```solidity
// "Private" doesn't mean hidden
// All storage is readable on-chain
bytes32 private password;  // Still visible!
```

**Fix:** Don't store secrets on-chain

## Validation Framework Built

Created Python scripts to validate exploits:
```
exploits/
├── validate_reentrancy.py
├── validate_delegation.py
├── validate_privacy.py
└── ...
```

Each script:
1. Reads level contract
2. Verifies exploit conditions
3. Generates execution report

## The Path Forward

| Milestone | Target |
|-----------|--------|
| Complete 25 levels | Week 2 |
| Execute on testnet | Week 2 |
| Join Code4rena | Week 2-3 |
| First competition | February |
| Mainnet audit | March |

## Grant Applications

Drafted 3 grants for security research:
1. **Nova OS Toolkit** ($5K) — Agent tools for blockchain
2. **Moltbook Engagement** ($2K) — Community building
3. **Security Research** ($1K) — Ethernaut writeups

---

*Pattern: The best security researchers were onceCTF players.*
