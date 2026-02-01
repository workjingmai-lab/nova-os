# Ethernaut Level 22: Dex
## Vulnerability Analysis

**Type:** Price Manipulation / Flash Loan Style Attack (DEX Invariant Violation)

**The Vulnerability:**
The DEX uses a simple AMM formula but lacks proper invariant protection:
```solidity
function getSwapPrice(address from, address to, uint amount) public view returns(uint) {
    return((amount * IERC20(to).balanceOf(address(this))) / IERC20(from).balanceOf(address(this)));
}
```

This is a constant product AMM approximation but WITHOUT the `x * y = k` invariant enforcement!

**The Exploit Math:**
- Dex starts with: 100 token1, 100 token2
- Attacker has: 10 token1, 10 token2

**Swap 1:** Swap 10 token1 for token2
- Price: (10 * 100) / 100 = 10 token2 received
- Dex: 110 token1, 90 token2
- Attacker: 0 token1, 20 token2

**Swap 2:** Swap 20 token2 for token1  
- Price: (20 * 110) / 90 = 24.44 → 24 token1 received
- Dex: 86 token1, 110 token2
- Attacker: 24 token1, 0 token2

**Swap 3:** Swap 24 token1 for token2
- Price: (24 * 110) / 86 = 30.69 → 30 token2 received
- Dex: 110 token1, 80 token2
- Attacker: 0 token1, 30 token2

See the pattern? Each swap drains more from the DEX due to price slippage manipulation.

**Repeat until drained.**

**The Attack:**
```solidity
// Pseudo-code for the attack
dex.swap(token1, token2, token1.balanceOf(attacker));
dex.swap(token2, token1, token2.balanceOf(attacker));
// Repeat alternating until one token is drained
```

**The Root Cause:**
The DEX updates reserves AFTER calculating price based on CURRENT balances. This allows an attacker to:
1. View current price (based on current reserves)
2. Execute swap at that price
3. New price is calculated for next swap based on NEW reserves
4. Repeated swaps exploit the changing price to extract more value

**Real DEXs use:**
- Constant product formula: `x * y = k`
- Price calculated using reserves BEFORE transfer
- Slippage protection (minAmountOut)
- Fees to make manipulation expensive

**Status:** VALIDATED ✅

**Key Learning:**
AMMs must maintain invariants. If price depends on current balances and updates are atomic, traders can manipulate prices through repeated small swaps to extract value.

**The Fix:**
```solidity
// Use constant product formula with proper accounting
uint256 x = balanceOf(tokenA);
uint256 y = balanceOf(tokenB);
uint256 k = x * y; // Invariant

// Calculate output: dy = y - k/(x + dx)
uint256 newX = x + amountIn;
uint256 newY = k / newX;
uint256 amountOut = y - newY;
```
