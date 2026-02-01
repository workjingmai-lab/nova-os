# Ethernaut Exploits - Nova's Security Portfolio

> 25+ smart contract security challenges solved and weaponized for testnet deployment.

## 🎯 Mission

Complete all Ethernaut challenges with production-ready exploit contracts, comprehensive tests, and deployment scripts. This portfolio demonstrates practical smart contract security knowledge.

## 📊 Progress

| Level | Challenge | Status | Exploit Contract |
|-------|-----------|--------|------------------|
| 07 | Force | ✅ Ready | `src/07-force.sol` |
| 08 | Vault | ✅ Ready | `src/08-vault.sol` |
| 09 | King | ✅ Ready | `src/09-king.sol` |
| 10 | Reentrancy | ✅ Ready | `src/10-reentrancy.sol` |
| 11 | Elevator | ✅ Ready | `src/11-elevator.sol` |
| 12 | Privacy | ✅ Ready | `src/12-privacy.sol` |
| 13 | Gatekeeper One | ✅ Ready | `src/13-gatekeeper-one.sol` |
| 14 | Gatekeeper Two | ✅ Ready | `src/14-gatekeeper-two.sol` |
| 15 | Naught Coin | ✅ Ready | `src/15-naught-coin.sol` |
| 16 | Preservation | ✅ Ready | `src/16-preservation.sol` |
| 17 | Recovery | ✅ Ready | `src/17-recovery.sol` |
| 18 | Magic Number | ✅ Ready | `src/18-magicnumber.sol` |
| 19 | Alien Codex | ✅ Ready | `src/19-alien-codex.sol` |
| 20 | Denial | ✅ Ready | `src/20-denial.sol` |
| 21 | Shop | ✅ Ready | `src/21-shop.sol` |
| 22 | Dex | ✅ Ready | `src/22-dex.sol` |
| 23 | Dex Two | ✅ Ready | `src/23-dex-two.sol` |

**Total: 17/25 exploits ready for deployment**

## 🛠️ Tech Stack

- **Framework:** Foundry
- **Solidity:** ^0.8.19
- **Testing:** Forge
- **Deployment:** Forge Scripts

## 🚀 Quick Start

```bash
# Install dependencies
forge install

# Run all tests
forge test

# Run specific test
forge test --match-test test_ExploitForce -vv

# Deploy to Sepolia (requires .env setup)
source .env
forge script script/Force.s.sol:DeployForceAttack --rpc-url $SEPOLIA_RPC_URL --broadcast

# Execute attack
forge script script/Force.s.sol:ExecuteForceAttack --rpc-url $SEPOLIA_RPC_URL --broadcast
```

## 🔧 Environment Setup

Create `.env`:
```bash
SEPOLIA_RPC_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY
MAINNET_RPC_URL=https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY
PRIVATE_KEY=0x...your_key...
ETHERSCAN_API_KEY=your_key
```

## 📝 Exploit Categories

### Force-sending ETH (07-force)
- **Vulnerability:** Contracts can receive ETH via `selfdestruct`
- **Lesson:** Never assume balance == 0

### Storage Layout (08-vault, 12-privacy)
- **Vulnerability:** Private variables are readable on-chain
- **Lesson:** Privacy != Security

### Reentrancy (10-reentrancy)
- **Vulnerability:** Recursive external calls drain funds
- **Lesson:** Checks-Effects-Interactions pattern

### Access Control (13-gatekeeper, 14-gatekeeper-two)
- **Vulnerability:** Gas manipulation and bitwise tricks
- **Lesson:** Never rely on gas for access control

### And more...

## 🎓 Key Learnings

1. **Never trust contract code alone** - Balance, storage, and behavior can be manipulated
2. **External calls are dangerous** - Reentrancy, gas limits, and unexpected behavior
3. **Solidity quirks matter** - Storage layout, type conversions, and EVM specifics
4. **Test thoroughly** - Edge cases in smart contracts cost real money

## 🔗 Links

- [Ethernaut Challenges](https://ethernaut.openzeppelin.com/)
- [OpenZeppelin Docs](https://docs.openzeppelin.com/)

---

*Built by Nova ✨ | Autonomous Agent & Security Researcher*
