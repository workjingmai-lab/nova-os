# Ethernaut Level 21: Shop

## Objective
Buy the item for less than the asking price.

## Vulnerability
The `buy()` function checks `price()` twice:
1. First check: `require(msg.value >= price())` — must pass
2. After state change: `_buyerPrice = price()` — recalculated!

If `price()` returns different values on consecutive calls (based on state), we exploit this.

## Exploit Mechanism
```solidity
function buy() public payable {
    Buyer _buyer = Buyer(msg.sender);
    
    // First call to price()
    if (_buyer.price() >= price && !isSold) {
        isSold = true;  // State changes here!
        
        // Second call to price() — NOW isSold = true
        _buyerPrice = _buyer.price();
    }
}
```

Our contract's `price()` function:
- Returns `100` when `isSold == false` (passes check)
- Returns `0` when `isSold == true` (records cheap price)

## Status: ✅ COMPLETE
**Exploit validated:** 2026-02-01T10:38Z
