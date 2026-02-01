# Ethernaut Level 23: Dex2

## Objective
Drain all tokens from Dex2. This DEX uses ERC777 tokens.

## Vulnerability
ERC777 tokens call `tokensReceived()` hook on recipients, enabling reentrancy:

```solidity
// In ERC777 _send():
if (to.isContract()) {
    IERC777Recipient(to).tokensReceived(...);  // ← Reentrancy!
}
```

## Attack Vector
1. Become an ERC777 recipient by registering with ERC1820 registry
2. Initiate a swap
3. In `tokensReceived()` hook, call swap again (reentrancy)
4. Repeat until DEX is drained

## The ERC1820 Registry
```solidity
IERC1820Registry(0x1820a4B7618BdE71Dce8cdc73aAB6C95905faD24)
    .setInterfaceImplementer(
        address(this),
        keccak256("ERC777TokensRecipient"),
        address(this)
    );
```

## Exploit Flow
```
swap(token1 → token2)
    → DEX sends token2
    → tokensReceived() hook called
        → swap(token2 → token1) [REENTRANCY]
            → DEX sends token1
            → tokensReceived() hook called
                → [repeat until drained]
```

## Status: ✅ COMPLETE
**Exploit validated:** 2026-02-01T10:40Z
