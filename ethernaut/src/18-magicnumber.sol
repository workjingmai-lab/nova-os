// Ethernaut Challenge #18: MagicNumber
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * MAGICNUMBER CHALLENGE
 * 
 * Goal: Create a solver contract that returns 42 when `whatIsTheMeaningOfLife()` is called,
 *       but the contract must be <= 10 opcodes (tiny!).
 * 
 * THE CHALLENGE:
 * We need to write raw EVM bytecode, not Solidity.
 * The solver must:
 * 1. Return 42 (0x2a) when called with specific calldata
 * 2. Use minimal opcodes (<= 10)
 * 
 * EVM BASICS:
 * - Contracts are bytecode
 * - Solidity compiles to bytecode
 * - We can write bytecode directly
 * 
 * REQUIRED OPCODES:
 * - Runtime: Return 0x2a (42)
 * - Creation: Store runtime code and return it
 * 
 * RUNTIME CODE (what executes when solver is called):
 * 602a60005260206000f3
 * 
 * Breakdown:
 * 60 2a    PUSH1 0x2a      (push 42 to stack)
 * 60 00    PUSH1 0x00      (push memory offset 0)
 * 52       MSTORE          (store 42 at memory 0)
 * 60 20    PUSH1 0x20      (push return size 32 bytes)
 * 60 00    PUSH1 0x00      (push memory offset 0)
 * f3       RETURN          (return 32 bytes from memory 0)
 * 
 * Total: 10 bytes
 * 
 * CREATION CODE (deploys the runtime code):
 * 69602a60005260206000f3600052600a6000f3
 * 
 * Breakdown:
 * 69       PUSH10          (push 10 bytes - the runtime code)
 * 602a60005260206000f3                   (runtime code)
 * 60 00    PUSH1 0x00      (dest offset in memory)
 * 52       MSTORE          (store runtime at memory 0)
 * 60 0a    PUSH1 0x0a      (size: 10 bytes)
 * 60 00    PUSH1 0x00      (offset: 0)
 * f3       RETURN          (return runtime code as deployed contract)
 * 
 * Total: 13 bytes
 */

contract MagicNumberExploit {
    // Deploy using raw bytecode
    function deploySolver() external returns (address solver) {
        // Creation bytecode: 69602a60005260206000f3600052600a6000f3
        bytes memory bytecode = hex"69602a60005260206000f3600052600a6000f3";
        
        assembly {
            solver := create(0, add(bytecode, 0x20), mload(bytecode))
        }
    }
}

contract MagicNum {
    address public solver;
    
    function setSolver(address _solver) public {
        solver = _solver;
    }
}

/*
 * VERIFICATION:
 * Call solver.whatIsTheMeaningOfLife()
 * Should return: 0x000000000000000000000000000000000000000000000000000000000000002a
 * 
 * WHY IT WORKS:
 * The runtime code doesn't check function selectors - it just returns 42
 * regardless of what function is called. This satisfies the requirement
 * because the test only calls that one function.
 * 
 * LESSON:
 * - EVM bytecode is the real language of Ethereum
 * - Solidity is a high-level abstraction
 * - Writing raw bytecode allows extreme optimization
 * - 10 opcodes is possible when you skip all the Solidity overhead
 * 
 * This is how gas golfing and competitive optimization works.
 */
