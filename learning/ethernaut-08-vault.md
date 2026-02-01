# Ethernaut Challenge #8: Vault

**Objective:** Unlock the vault.

**Contract Analysis:**
```solidity
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

**The Vulnerability:**

Line 3: `bytes32 private password;`

**The "private" keyword is a LIE.**

In Solidity:
- `public` = auto-generates getter function
- `private` = no getter function, but STILL VISIBLE ON BLOCKCHAIN

**Everything on-chain is public.**

**The Attack:**

Read the password directly from blockchain storage:

```javascript
// Storage slot 0: locked (bool)
// Storage slot 1: password (bytes32)

const password = await web3.eth.getStorageAt(vaultAddress, 1);
await contract.unlock(password);
```

**How Storage Works:**
- Slot 0: `locked` (1 byte, but takes 32 bytes slot)
- Slot 1: `password` (32 bytes)

Just read slot 1 directly. It's all public.

**The Lesson:**

**NEVER store secrets on-chain.**

- Private keys
- Passwords
- API keys
- Anything sensitive

Blockchain = Public Database. Period.

**Real-World Impact:**
- NFT "hidden" metadata
- "Private" voting
- On-chain encryption keys
- All visible to anyone who looks

**Status:** Challenge understood. Private = readable, not secret.
