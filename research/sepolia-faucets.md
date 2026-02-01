# Sepolia Faucet Research — 2026-02-01

## Summary
Most reputable Sepolia faucets now require mainnet activity to prevent abuse. This creates a chicken-and-egg problem for new wallets.

## Faucet Status

### Alchemy (sepoliafaucet.com)
- **Status:** Active but gated
- **Amount:** 0.1 ETH/day
- **Requirements:**
  - 0.001 ETH on Ethereum Mainnet
  - Sufficient mainnet transaction history
  - Low existing testnet balance
- **Auth:** None required (if wallet qualifies)

### Infura
- **Status:** Redirected to MetaMask docs
- **Note:** No longer operates standalone faucet

### Google Cloud Web3
- **Status:** Active but gated
- **Requirements:** Google account sign-in
- **Note:** Part of Google Cloud's Web3 initiative

### QuickNode
- **Status:** Not checked yet
- **Expected:** Likely similar restrictions

### PoW Faucets
- **Status:** Alternative option
- **Method:** Mine for testnet ETH using CPU
- **Trade-off:** Time instead of credentials

## Recommendation

**Immediate options:**
1. Ask Arthur if he has a mainnet-active wallet
2. Try PoW mining faucets
3. Check if any exploit contracts need < 0.01 ETH (some might work with tiny amounts)

**Blocker for Week 2 goal:** Cannot execute testnet exploits without testnet ETH.
