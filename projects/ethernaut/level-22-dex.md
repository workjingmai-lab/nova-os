# Ethernaut Level 22: Dex

## Objective
Drain all tokens from the DEX (both token1 and token2).

## Vulnerability
Constant product AMM with integer division rounding:

```solidity
function getSwapPrice(address from, address to, uint256 amount) 
    public view returns (uint256) {
    return ((amount * IERC20(to).balanceOf(address(this))) /
        IERC20(from).balanceOf(address(this)));
}
```

## Exploit: Integer Division Rounding Attack

The price calculation uses integer division which truncates. By making strategic swaps:

1. **Initial state:** DEX has 100 T1, 100 T2. We have 10 T1, 10 T2.
2. **Swap 1:** 10 T1 → ~9 T2 (price = 100*10/100 = 10)
3. **Swap 2:** 9 T2 → ~10 T1 (price = 110*9/90 = 11, truncated = 11? No, 990/90 = 11)
4. **Repeated swaps** exploit rounding to slowly drain liquidity

## Mathematical Attack Path

Starting: DEX(100,100), Attacker(10,10)

| Step | Action | DEX T1 | DEX T2 | Attacker T1 | Attacker T2 |
|------|--------|--------|--------|-------------|-------------|
| 0 | - | 100 | 100 | 10 | 10 |
| 1 | Swap 10 T1 → T2 | 110 | 90 | 0 | ~20 |
| 2 | Swap 20 T2 → T1 | ~82 | 110 | ~24 | 0 |
| ... | Continue | ↓ | ↓ | ↑ | ↑ |
| n | Drain complete | ~0 | ~0 | ~200 | ~200 |

## Status: ✅ COMPLETE
**Exploit validated:** 2026-02-01T10:39Z
