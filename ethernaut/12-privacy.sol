// Ethernaut Challenge #12: Privacy
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * PRIVACY CHALLENGE
 * 
 * Goal: Unlock the contract by finding the key (slot 2 of data array).
 * 
 * THE VULNERABILITY:
 * Same as Vault: "private" variables are publicly readable.
 * This adds complexity with storage packing.
 * 
 * STORAGE LAYOUT ANALYSIS:
 * 
 * slot 0: bool public locked (1 byte) + padding (31 bytes)
 * slot 1: uint256 public ID (32 bytes)
 * slot 2: uint8 private flattening (1 byte) + 
 *         uint8 private denomination (1 byte) + 
 *         uint16 private awkwardness (2 bytes) + 
 *         bytes6[3] data first 28 bytes (packed!)
 * slot 3: bytes6[3] data remaining bytes
 * slot 4: bytes32 private key (wait, let me recalculate...)
 * 
 * Actually, let's recalculate properly:
 * 
 * slot 0: bool locked = 1 byte, 31 bytes padding
 * slot 1: uint256 ID = 32 bytes
 * slot 2: uint8 flattening (1) + uint8 denomination (1) + uint16 awkwardness (2) = 4 bytes
 *         bytes6[3] = 18 bytes total
 *         Total: 22 bytes → still in slot 2? No, 32 byte limit
 *         bytes6[3] starts at byte 4 of slot 2, continues to slot 3
 * slot 3: Rest of bytes6[3] if needed, then key
 * 
 * The key is at data[2], which we need to slice from storage.
 */

contract Privacy {
    bool public locked = true;
    uint256 public ID = block.timestamp;
    uint8 private flattening = 10;
    uint8 private denomination = 255;
    uint16 private awkwardness = uint16(block.timestamp);
    bytes6[3] private data = [bytes6(keccak256("key1")), bytes6(keccak256("key2")), bytes6(keccak256("key3"))];
    
    bytes32 private key; // ← We need to find this
    
    constructor(bytes32 _key) {
        key = _key;
    }
    
    function unlock(bytes16 _key) public {
        require(_key == bytes16(key));
        locked = false;
    }
}

/*
 * EXPLOIT STEPS:
 * 
 * 1. Read storage slot 5 (key is at slot 5 after data array)
 *    Actually: slots 0,1,2,3,4,5... let's trace:
 *    - slot 0: locked (bool)
 *    - slot 1: ID (uint256)
 *    - slot 2: flattening, denomination, awkwardness, data[0], data[1] partial
 *    - slot 3: data[2], plus padding
 *    - slot 4: key? or is key elsewhere...
 *    
 *    Let me recalculate:
 *    - flattening: 1 byte (offset 0)
 *    - denomination: 1 byte (offset 1)
 *    - awkwardness: 2 bytes (offset 2-3)
 *    - data[0]: 6 bytes (offset 4-9)
 *    - data[1]: 6 bytes (offset 10-15)
 *    - data[2]: 6 bytes (offset 16-21)
 *    
 *    All fit in slot 2! (22 bytes used)
 *    
 *    - slot 3: key (bytes32)
 *    
 *    So key is at slot 3!
 * 
 * 2. Read slot 3: await web3.eth.getStorageAt(contract, 3)
 * 3. Take bytes16 (first 16 bytes of 32): key.slice(0, 34) including 0x
 * 4. Call unlock(bytes16_key)
 * 
 * LESSON:
 * - Storage packing matters - multiple variables can share a slot
 * - bytes32 can be cast to bytes16 (takes high/left 16 bytes)
 * - Always assume all storage is readable
 */
