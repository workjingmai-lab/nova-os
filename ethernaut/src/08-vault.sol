// Ethernaut Challenge #8: Vault
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * VAULT CHALLENGE
 * 
 * Goal: Unlock the vault by finding the password.
 * 
 * THE VULNERABILITY:
 * Private variables in Solidity are NOT hidden!
 * 
 * All contract storage is publicly readable on-chain.
 * "private" only means other contracts can't access it - 
 * anyone can read storage directly via RPC calls.
 * 
 * Storage layout:
 * - slot 0: bool public locked (1 byte, but takes 32 bytes slot)
 * - slot 1: bytes32 private password (32 bytes = 1 slot)
 * 
 * EXPLOIT (JavaScript/web3):
 * await web3.eth.getStorageAt(contractAddress, 1)
 * 
 * Then convert bytes32 to string and call unlock(password).
 */

contract Vault {
    bool public locked;
    bytes32 private password; // ← "private" is a LIE

    constructor(bytes32 _password) {
        locked = true;
        password = _password;
    }

    function unlock(bytes32 _password) public {
        if (password == _password) {
            locked = false;
        }
    }
}

/*
 * ATTACK STEPS:
 * 1. Read storage slot 1: await web3.eth.getStorageAt(vaultAddress, 1)
 * 2. Result: 0x1234... (bytes32 hex)
 * 3. Convert: web3.utils.hexToUtf8(result) or keep as bytes32
 * 4. Call unlock(result) → locked = false
 * 
 * LESSON: 
 * - Private variables are NOT secret
 * - Never store sensitive data (passwords, keys) on-chain
 * - All storage is readable by anyone with node access
 * 
 * Secure alternatives:
 * - Store only hashes (keccak256) for verification
 * - Use commit-reveal schemes
 * - Keep secrets off-chain entirely
 */
