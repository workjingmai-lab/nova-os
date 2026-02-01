// Ethernaut Challenge #15: Naught Coin
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * NAUGHT COIN CHALLENGE
 * 
 * Goal: Transfer all tokens out despite 10-year lock.
 * 
 * THE VULNERABILITY:
 * The timeLock only applies to the `transfer` function.
 * But ERC20 has another way to move tokens: `transferFrom`!
 * 
 * If we approve another address to spend our tokens,
 * that address can call transferFrom immediately, bypassing
 * the timeLock which only exists in transfer.
 * 
 * This is a classic case of incomplete protection -
 * securing one function but forgetting about others that
 * achieve the same result.
 */

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract NaughtCoinExploit {
    // No contract needed! Just use any wallet address.
    // Steps:
    // 1. From your locked account: approve(spenderAddress, balance)
    // 2. From spender account: transferFrom(yourAccount, anywhere, balance)
}

contract NaughtCoin is IERC20 {
    string public constant name = 'NaughtCoin';
    string public constant symbol = '0x0';
    uint public constant decimals = 18;
    uint public timeLock = block.timestamp + 10 * 365 days;
    uint public INITIAL_SUPPLY = 1000000 * (10**decimals);
    mapping(address => uint) public balances;
    mapping(address => mapping(address => uint)) public allowances;
    
    constructor(address _player) {
        balances[_player] = INITIAL_SUPPLY;
    }
    
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(balances[msg.sender] >= _value);
        require(block.timestamp > timeLock); // ← Lock only here!
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        return true;
    }
    
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(balances[_from] >= _value);
        require(allowances[_from][msg.sender] >= _value);
        // NO TIMELOCK HERE! ← VULNERABILITY
        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;
        return true;
    }
    
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowances[msg.sender][_spender] = _value;
        return true;
    }
    
    function balanceOf(address _account) public view returns (uint) {
        return balances[_account];
    }
}

/*
 * ATTACK STEPS:
 * 
 * Method 1 - Second Address:
 * 1. From player account: token.approve(secondAddress, balance)
 * 2. From second address: token.transferFrom(player, secondAddress, balance)
 * 
 * Method 2 - Contract (no second EOA needed):
 * 1. Deploy contract that calls approve(this, balance) in constructor
 * 2. Call transferFrom(player, this, balance) from contract
 * 
 * LESSON:
 * - Securing one function isn't enough if alternatives exist
 * - ERC20 has multiple transfer paths: transfer AND transferFrom
 * - Time locks must apply to ALL state-changing functions
 * - Standard interfaces have multiple entry points
 */
