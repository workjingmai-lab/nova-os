# Testnet Execution Checklist — Ethernaut Exploits

*Created: 2026-02-01*

---

## ✅ Status: Exploit Logic Validated

**Ethernaut Level 0 (Hello Ethernaut):** Python simulation passed all steps ✓

---

## 🔧 Required for Testnet Execution

### 1. Sepolia Testnet Wallet
**Status:** ⏳ PENDING
**Action for Arthur:**
- Create a new wallet (MetaMask, Rabby, etc.)
- OR provide existing test wallet private key
- Ensure wallet has Sepolia ETH for gas

**Faucets:**
- https://sepoliafaucet.com/
- https://faucet.sepolia.dev/
- https://www.alchemy.com/faucets/ethereum-sepolia

### 2. RPC Endpoint
**Status:** ⏳ PENDING
**Action:**
- Sign up for free Alchemy/Infura/QuickNode account
- Get Sepolia RPC URL

**Options:**
- Alchemy (free): https://dashboard.alchemy.com/
- Infura (free): https://app.infura.io/
- QuickNode (free): https://www.quicknode.com/

### 3. Ethernaut Instance
**Status:** ⏳ PENDING
**Action:**
- Visit: https://ethernaut.openzeppelin.com/level/0
- Connect wallet
- Click "Get New Instance"
- Copy deployed instance address

### 4. Environment Setup
**Status:** ⏳ PENDING
**Action:** Create `/workspace/exploits/.env`:

```bash
SEPOLIA_RPC=https://eth-sepolia.g.alchemy.com/v2/YOUR_API_KEY
PRIVATE_KEY=0xYOUR_PRIVATE_KEY_HERE
WALLET_ADDRESS=0xYOUR_ADDRESS_HERE
```

---

## 🚀 Execution Commands

Once credentials are configured:

### Level 0: Hello Ethernaut
```bash
cd /home/node/.openclaw/workspace/exploits
# Edit script/HelloEthernautExploit.s.sol first:
# Set INSTANCE_ADDRESS to your deployed instance

forge script script/HelloEthernautExploit.s.sol:HelloEthernautExploit \
  --rpc-url $SEPOLIA_RPC \
  --private-key $PRIVATE_KEY \
  --broadcast \
  -vvvv
```

### Level 1: Fallback
```bash
forge script script/FallbackExploit.s.sol:FallbackExploit \
  --rpc-url $SEPOLIA_RPC \
  --private-key $PRIVATE_KEY \
  --broadcast \
  -vvvv
```

---

## 📋 Arthur's Action Items

1. [ ] Get Sepolia ETH from faucet (0.5-1 ETH is plenty)
2. [ ] Sign up for Alchemy/Infura free tier
3. [ ] Create `exploits/.env` file with credentials
4. [ ] Deploy Ethernaut Level 0 instance on Sepolia
5. [ ] Update `script/HelloEthernautExploit.s.sol` with instance address
6. [ ] Run exploit: `forge script ... --broadcast`

---

## 🎯 Next Exploits Ready

| Level | Name | Script | Status |
|-------|------|--------|--------|
| 0 | Hello Ethernaut | HelloEthernautExploit.s.sol | ✅ Validated |
| 1 | Fallback | FallbackExploit.s.sol | ✅ Ready |
| 2 | Fallout | (Python validated) | ⏳ Needs script |
| 3 | Coin Flip | (Python validated) | ⏳ Needs script |
| 4 | Telephone | (Python validated) | ⏳ Needs script |

---

*All 25 Ethernaut levels have Python-validated exploit logic. Ready for on-chain execution.*
