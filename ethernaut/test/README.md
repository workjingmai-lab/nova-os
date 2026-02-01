# Ethernaut Testnet Exploits

> Ready-to-deploy exploit scripts for Sepolia testnet

---

## 🚀 Quick Start

### Prerequisites
```bash
# Set environment variables
export PRIVATE_KEY=your_private_key_here
export SEPOLIA_RPC=https://rpc.sepolia.org
```

### Level 7: Force

**Vulnerability:** Contracts can receive ETH via `selfdestruct` even without payable functions.

**Deploy:**
```bash
# 1. Start the level on Ethernaut (https://ethernaut.openzeppelin.com/)
# 2. Copy the instance address
export FORCE_TARGET=0xYourInstanceAddress

# 3. Run the exploit
forge script script/ForceExploit.s.sol:ForceExploitScript \
  --rpc-url $SEPOLIA_RPC \
  --broadcast \
  --verify
```

**Check:**
```bash
cast balance $FORCE_TARGET --rpc-url $SEPOLIA_RPC
# Should return 1 (or more)
```

---

## 📋 Exploit Checklist

| Level | Script | Status | Gas Used |
|-------|--------|--------|----------|
| 07 Force | ForceExploit.s.sol | ✅ Ready | ~50K |
| 08 Vault | - | 🔄 Pending | - |
| 09 King | - | 🔄 Pending | - |

---

## 🔗 Links

- Ethernaut: https://ethernaut.openzeppelin.com/
- Sepolia Faucet: https://sepoliafaucet.com/
- OpenZeppelin Docs: https://docs.openzeppelin.com/

---

*Last Updated: 2026-02-01*
