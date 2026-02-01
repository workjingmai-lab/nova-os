# Ethernaut Challenge #5: Token

**Objective:** You are given 20 tokens. Get more.

**Contract Analysis:**
```solidity
contract Token {
  mapping(address => uint) balances;
  uint public totalSupply;

  constructor(uint _initialSupply) {
    balances[msg.sender] = totalSupply = _initialSupply;
  }

  function transfer(address _to, uint _value) public returns (bool) {
    require(balances[msg.sender] - _value >= 0);  // ❌ VULNERABLE
    balances[msg.sender] -= _value;
    balances[_to] += _value;
    return true;
  }

  function balanceOf(address _owner) public view returns (uint balance) {
    return balances[_owner];
  }
}
```

**The Vulnerability:**

Line 10: `require(balances[msg.sender] - _value >= 0)`

This looks like a balance check... but it's WRONG.

**Why it's vulnerable:**

In Solidity 0.6.0 (and earlier), `uint` (unsigned integer) **cannot be negative**.

When you subtract a larger number from a smaller one:
- Normal math: 10 - 20 = -10 (would fail the check)
- Solidity uint: 10 - 20 = HUGE_NUMBER (underflows to max uint256)

**The Attack:**

1. You have 20 tokens
2. Call `transfer(anyAddress, 21)` — try to send 21 tokens
3. `balances[msg.sender] - _value` = 20 - 21
4. This underflows to `2^256 - 1` (a massive number)
5. `2^256 - 1 >= 0` is TRUE ✓
6. Check passes!
7. Your balance becomes: 20 - 21 = HUGE_NUMBER (underflow)
8. Target gets 21 tokens
9. You now have ~infinite tokens

**The Fix (Solidity 0.8+):**
Modern Solidity automatically checks for overflows/underflows and reverts.

**The Fix (older versions):**
Use SafeMath library:
```solidity
using SafeMath for uint256;
require(balances[msg.sender] >= _value);  // Check BEFORE subtract
balances[msg.sender] = balances[msg.sender].sub(_value);
```

**Lesson:**
Integer overflow/underflow can turn small balances into infinite ones. Always use SafeMath or Solidity 0.8+.

**Status:** Challenge understood. Classic overflow vulnerability.
