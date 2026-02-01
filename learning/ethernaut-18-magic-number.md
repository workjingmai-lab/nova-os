# Ethernaut Challenge #18: Magic Number

**Objective:** Provide the `Solver` contract with a `whatIsTheMeaningOfLife()` function that returns 42.

**The Challenge:**

You need to deploy a contract, but:
- No Solidity source code allowed
- Must be under 10 opcodes
- Must return 42 (0x2a)

**This is raw EVM bytecode.**

**What the function needs to do:**
1. Return 42 (0x2a)
2. In the EVM, return values use `RETURN` opcode
3. `RETURN` takes memory location and size

**The Bytecode:**

```
// Store 42 in memory
60 2a      // PUSH1 0x2a (value 42)
60 00      // PUSH1 0x00 (memory location 0)
52         // MSTORE (store 0x2a at position 0)

// Return it
60 20      // PUSH1 0x20 (32 bytes to return)
60 00      // PUSH1 0x00 (from memory position 0)
f3         // RETURN
```

**Combined:** `602a60005260206000f3`

**That's 10 bytes!** (under the limit)

**Deploying Raw Bytecode:**

```javascript
// Create contract from bytecode
const bytecode = '0x602a60005260206000f3';

// Need init code that returns the runtime code
// Init code: store runtime code, return it
const initCode = '0x600a' + '60' + bytecode.length/2 + '6000' + '39' + '600a' + '6000' + 'f3';
// PUSH1 0x0a (10 bytes runtime)
// PUSH1 0x0c (offset in init code - calculated)
// PUSH1 0x00 (dest memory)
// CODECOPY (copy runtime code to memory)
// PUSH1 0x0a (size)
// PUSH1 0x00 (offset)
// RETURN (return runtime code)

// Actually simpler approach:
// Just send transaction with init code that returns the runtime bytecode
```

**Full Deployment Bytecode:**
```
// Init code: copy runtime code and return it
60 0a  // PUSH1 10 (runtime code size)
60 0c  // PUSH1 12 (runtime code offset in this tx)
60 00  // PUSH1 0 (dest memory)
39     // CODECOPY
60 0a  // PUSH1 10 (return size)
60 00  // PUSH1 0 (return offset)
f3     // RETURN

// Runtime code (above)
60 2a 6000 52 60 20 6000 f3
```

**Final bytecode:**
`600a600c600039600a6000f3602a60005260206000f3`

**Deploy:**
```javascript
const bytecode = '0x600a600c600039600a6000f3602a60005260206000f3';
const tx = await web3.eth.sendTransaction({
  from: player,
  data: bytecode
});
```

**The Lesson:**

Understanding EVM at the bytecode level lets you write ultra-optimized contracts.

Also: EVM is just a stack machine. Push, store, return.

**Status:** Challenge understood. Raw EVM bytecode.
