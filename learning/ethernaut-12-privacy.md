# Ethernaut Challenge #12: Privacy

**Objective:** Unlock the contract by finding the key.

**Contract Analysis:**
```solidity
contract Privacy {
  bool public locked = true;
  uint256 public ID = block.timestamp;
  uint8 private flattening = 10;
  uint8 private denomination = 255;
  uint16 private awkwardness = uint16(now);
  bytes32[3] private data;

  constructor(bytes32[3] memory _data) public {
    data = _data;
  }
  
  function unlock(bytes16 _key) public {
    require(_key == bytes16(data[2]));
    locked = false;
  }
}
```

**The Challenge:**

Find `data[2]` to unlock. But `data` is private...

**Storage Layout Analysis:**

```
Slot 0: locked (bool) + ID (uint256 partial)
  - locked: 1 byte
  - ID starts here but needs 32 bytes, so...
  
Actually, let's recalculate:
  
Slot 0:
  - locked: bool = 1 byte
  - But ID is uint256 = 32 bytes! Needs its own slot
  
Slot 0: locked (1 byte) + flattening (1 byte) + denomination (1 byte) + awkwardness (2 bytes) = 5 bytes
Wait, that doesn't work either...

Let's do it properly:
```

**Proper Slot Calculation:**

```
Slot 0: locked (bool = 1 byte) — but bool is uint8 internally
        → Actually: locked is bool, packed with next variables if they fit
        
Let's trace:
- locked: bool — 1 byte, starts at slot 0, byte 0
- ID: uint256 — 32 bytes, needs full slot 1
- flattening: uint8 — 1 byte, slot 2, byte 0
- denomination: uint8 — 1 byte, slot 2, byte 1  
- awkwardness: uint16 — 2 bytes, slot 2, bytes 2-3
  
Slot 2 total: 1 + 1 + 2 = 4 bytes ✓ (fits in 32 bytes)

- data[0]: bytes32 — slot 3
- data[1]: bytes32 — slot 4
- data[2]: bytes32 — slot 5 ← THE KEY!
```

**The Attack:**

```javascript
// Read slot 5
const data2 = await web3.eth.getStorageAt(contractAddress, 5);

// Take first 16 bytes (bytes16 conversion truncates)
const key = data2.slice(0, 34); // 0x + 32 hex chars

// Unlock
await contract.unlock(key);
```

**The Lesson:**

Storage packing is complex but deterministic. Calculate slots precisely.

`bytes32` to `bytes16` = keep first 16 bytes, discard rest.

**Status:** Challenge understood. Storage slot calculation.
