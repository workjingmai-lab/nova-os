// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Test.sol";
import "../src/11-elevator.sol";

/*
 * Ethernaut Level 11: Elevator Test
 * Goal: Reach the top floor (set top = true)
 * 
 * Vulnerability: Contract trusts external return value without verification.
 * We control the Building interface implementation.
 */

contract ElevatorTest is Test {
    Elevator public elevator;
    ElevatorExploit public exploit;
    
    address public attacker = address(0x1337);
    
    function setUp() public {
        // Deploy the target contract
        elevator = new Elevator();
        
        // Fund attacker
        vm.deal(attacker, 1 ether);
    }
    
    function testElevatorExploit() public {
        vm.startPrank(attacker);
        
        // Initial state: not at top
        assertEq(elevator.top(), false);
        assertEq(elevator.floor(), 0);
        
        // Deploy exploit contract
        exploit = new ElevatorExploit(address(elevator));
        
        // Execute attack
        exploit.attack();
        
        // Verify: we reached the top!
        assertEq(elevator.top(), true);
        assertEq(elevator.floor(), 1);
        
        vm.stopPrank();
        
        emit log_string("[+] Exploit successful! Reached top floor.");
    }
    
    function testIsLastFloorCalledTwice() public {
        vm.startPrank(attacker);
        
        // Deploy and track calls
        exploit = new ElevatorExploit(address(elevator));
        
        // Before attack: not called
        assertEq(exploit.called(), false);
        
        // Execute attack
        exploit.attack();
        
        // After attack: was called twice, flag is set
        assertEq(exploit.called(), true);
        assertEq(elevator.top(), true);
        
        vm.stopPrank();
    }
}
