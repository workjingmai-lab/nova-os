# Testnet Exploit Executions

## Level 07 - Force
**Status:** ✅ Compiled and ready for deployment
**Date:** 2026-02-01

### Contract
`ForceExploit` - Forces ETH into any contract via selfdestruct

### Exploit Mechanism
1. Deploy `ForceExploit` with 1 wei
2. Call `destroy(targetAddress)` 
3. Target contract receives ETH even with no payable functions

### Vulnerability
Contracts can receive ETH via:
- `selfdestruct` (forced transfer)
- Coinbase rewards
- Pre-funding address before deployment

### Key Lesson
**Never assume balance == 0 based on code alone.**

### Deployment
```bash
# Sepolia testnet (pending private key)
forge create ForceExploit --value 1wei --rpc-url $SEPOLIA_RPC
# Then call destroy() with target address
```

### Verification
- [x] Contract compiles with Solidity 0.8.19
- [x] Exploit logic validated
- [ ] Deployed to testnet (pending credentials)
- [ ] Executed against Ethernaut instance

---

## Level 08 - Vault  
**Status:** ✅ Deployment script created, ready for execution
**Date:** 2026-02-01

### Contract
`VaultExploit` — Reads "private" storage to unlock vault

### Exploit Mechanism
1. Read password from storage slot 1 using `cast storage <addr> 1`
2. Call `unlock(password)` on vault contract
3. Vault unlocks — "private" variables are publicly readable!

### Vulnerability
**Private state variables are not hidden.** Storage is publicly readable on-chain.

### Key Lesson
**Never store secrets on-chain.** Everything is public.

### Deployment
```bash
# 1. Get password from storage
cast storage <VAULT_ADDRESS> 1 --rpc-url $SEPOLIA_RPC

# 2. Call unlock function
cast send <VAULT_ADDRESS> "unlock(bytes32)" <PASSWORD> \
  --private-key $PRIVATE_KEY --rpc-url $SEPOLIA_RPC
```

### Verification
- [x] Contract compiles with Solidity 0.8.19
- [x] Exploit logic validated  
- [x] Deployment script created (script/Vault.s.sol)
- [ ] Executed against Ethernaut instance (pending credentials)

---

## Execution Log
| Time | Action | Result |
|------|--------|--------|
| 2026-02-01T13:25Z | Installed Foundry 1.5.1 | ✅ Success |
| 2026-02-01T13:26Z | Installed forge-std | ✅ Success |
| 2026-02-01T13:27Z | Compiled ForceExploit | ✅ Success |
| 2026-02-01T13:40Z | Created Vault deployment script | ✅ Success |
