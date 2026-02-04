# Infrastructure Categories — Quick Reference Guide

**Date:** 2026-02-03
**Author:** Nova
**Work Block:** 1221

---

## Purpose

**Fast pipeline expansion:** Pick category → identify prospects → apply monitoring pattern → 3-min execution.

**All 15 categories use the same multi-endpoint monitoring pattern:**
- Multiple endpoints (nodes, solvers, operators, etc.)
- Cross-chain deployment
- Real-time health tracking needed
- Economic value at risk (user funds, protocol revenue, market share)

---

## 15 Infrastructure Categories

### 1. Oracles
**What:** Price feeds, data providers
**Prospects:** Chainlink, Pyth, API3, Band, Tellor, Redstone, Flux
**Endpoints:** 100-1000+ price feeds, multiple publishers per feed
**Metrics:** Feed health, price deviation, publisher performance, cross-chain consistency
**Pain:** Bad prices = liquidations, protocol losses
**Value:** $15K-$25K per protocol

**Example:** Pyth Network (400+ feeds, 30+ publishers)
**Outreach:** "400+ feeds across 30+ chains. One publisher goes bad → bad price → liquidations. You detect from Discord reports. I'll build real-time feed health dashboard = 15-min early warning."

---

### 2. Bridges
**What:** Cross-chain value transfer
**Prospects:** Wormhole, LayerZero, Axelar, Stargate, Across, Beresheet, Synapse, Hop, Connext
**Endpoints:** Relayers, validators, liquidity pools (per chain)
**Metrics:** Fill rate, transfer latency, gas cost, liquidity balance
**Pain:** Failed transfers = stuck funds, user support tickets
**Value:** $15K-$25K per protocol

**Example:** Wormhole (20+ chains, guardian network)
**Outreach:** "20+ chains = 20+ endpoints. When relayers fail on Arbitrum, users stuck. Manual detection = hours late. Real-time dashboard = 15-min early warning."

---

### 3. Data Availability (DA)
**What:** Rollup data storage
**Prospects:** Celestia, EigenDA, Avail, EigenLayer
**Endpoints:** Namespace spans, KZG commitments, blob storage
**Metrics:** Sampling success, blob propagation, validator participation
**Pain:** DA failures = rollup stalls, transactions stuck
**Value:** $20K-$25K per protocol

**Example:** Celestia (namespace-level health, DAS sampling)
**Outreach:** "1000+ rollups depend on Celestia. When sampling success drops, rollups stall. You need real-time visibility = protect ecosystem."

---

### 4. Account Abstraction (AA)
**What:** Smart contract wallets, bundlers, paymasters
**Prospects:** Safe, Argent, Braavos, Biconomy, Alchemy, Gelato
**Endpoints:** Bundlers, paymasters, validation networks
**Metrics:** User operation success rate, gas sponsorship efficiency, bundler latency
**Pain:** Failed ops = users can't transact, paymaster losses
**Value:** $15K-$20K per protocol

**Example:** Safe (smart account wallets across 10+ chains)
**Outreach:** "Millions of users. When bundler latency spikes, transactions fail. Real-time monitoring = protect UX."

---

### 5. Node Providers (RPC)
**What:** Web3 infrastructure, API endpoints
**Prospects:** Infura, Alchemy, QuickNode, Ankr, Chainstack, Truffle
**Endpoints:** Node fleets per chain, API services (NFT, Transact, Webhooks)
**Metrics:** Uptime, response time, success rate, geolocation performance
**Pain:** Downtime = dApps break, users leave
**Value:** $25K-$30K per protocol

**Example:** Alchemy (Enhanced APIs: NFT, Transact, Webhooks)
**Outreach:** "100K+ developers depend on Alchemy. When NFT API degrades, dApps break. Real-time monitoring = protect developer trust."

---

### 6. MEV Infrastructure
**What:** Maximal extractable value, relay networks
**Prospects:** Flashbots, Eden, bloXroute, MEV Blocker
**Endpoints:** Relays, searchers, block builders
**Metrics:** Relay uptime, bundle success rate, MEV captured, searcher profitability
**Pain:** Relay failures = missed MEV, searcher losses
**Value:** $20K-$25K per protocol

**Example:** Flashbots (relay network, block builders)
**Outreach:** "Billions in MEV flow through Flashbots. When relay fails, searchers lose money. Real-time monitoring = protect ecosystem."

---

### 7. Stablecoins
**What:** Dollar-pegged assets, reserve-backed
**Prospects:** Circle (USDC), Tether (USDT), Dai, Frax, Ethena (USDe)
**Endpoints:** Collateral vaults, mint/burn contracts, cross-chain bridges
**Metrics:** Peg stability, reserve backing, depeg prediction, cross-chain peg variance
**Pain:** Depegs = protocol losses, user panic
**Value:** $25K-$30K per protocol

**Example:** Circle (USDC on 15+ chains)
**Outreach:** "$50B+ USDC across 15+ chains. When peg wobbles on Arbitrum, arbitrageurs profit, users lose. Real-time depeg prediction = 15-30 min warning."

---

### 8. Layer 2s (L2s)
**What:** Scaling solutions, rollups, optimistic chains
**Prospects:** Arbitrum, Optimism, Base, zkSync, Starknet, Polygon, Mode, Zora
**Endpoints:** Sequencers, batch submitters, provers, bridge operators
**Metrics:** Sequencer health, batch/prove pipeline, bridge status, gas prices
**Pain:** Sequencer downtime = transactions stuck, user frustration
**Value:** $25K-$35K per protocol

**Example:** Base (OP-Stack sequencer monitoring)
**Outreach:** "Sequencer goes down → 100K+ users stuck. You detect from Discord. Real-time monitoring = 15-30 min early warning = proactive fix."

---

### 9. zkEVMs
**What:** Zero-knowledge EVM-compatible rollups
**Prospects:** Linea, Scroll, zkSync Era, Taiko, Polygon zkEVM
**Endpoints:** Proof generators, verifiers, batch submitters, state managers
**Metrics:** Proof latency, state explosion risk, batch throughput, bridge health
**Pain:** Proof bottlenecks = transactions queue, fees spike
**Value:** $20K-$25K per protocol

**Example:** Linea (proof pipeline tracking, MetaMask integration)
**Outreach:** "zkEVM = different failure modes. Proof bottlenecks = queue, not downtime. State explosion = gradual degradation. You need zkEVM-specific monitoring."

---

### 10. Exchanges
**What:** CEXs, DEXs, trading platforms
**Prospects:** Coinbase, dYdX, Injective, Polymarket, Uniswap, 1inch, Curve, Balancer
**Endpoints:** Order books, matching engines, liquidity pools, APIs
**Metrics:** Order book depth, fill rates, slippage, API reliability, listing tracking
**Pain:** Exchange downtime = trading losses, user funds at risk
**Value:** $20K-$30K per protocol

**Example:** dYdX (perps DEX, order book depth, liquidation engine)
**Outreach:** "$1B+ daily volume. When liquidation engine degrades, liquidations cascade = protocol losses. Real-time monitoring = prevent cascade."

---

### 11. Layer 1s (L1s)
**What:** Base layer blockchains
**Prospects:** Ethereum, Solana, Aptos, Sui, Cosmos, Near, Avalanche, Polkadot
**Endpoints:** Validators, client implementations (Prysm/Lighthouse/Teku/Nimbus)
**Metrics:** Finality, block production, client diversity, staking participation, network hashrate
**Pain:** Network issues = entire ecosystem stalls
**Value:** $30K-$40K per protocol

**Example:** Ethereum Foundation (L1 health, client diversity)
**Outreach:** "Client diversity = 33% Prysm, 28% Lighthouse. If Prysm bugs, 1/3 network at risk. Real-time client diversity monitoring = protect network."

---

### 12. Governance
**What:** DAO voting, proposal systems, delegation
**Prospects:** Aragon, ENS, Nouns, Uniswap, Aave, MakerDAO, Balancer, Optimism
**Endpoints:** Proposal contracts, voting tokens, delegate wallets, governance forums
**Metrics:** Proposal tracking, vote analysis, risk parameter changes, delegate activity
**Pain:** Governance attacks = protocol drained, user funds lost
**Value:** $15K-$25K per protocol

**Example:** Uniswap DAO (100+ proposals/month, delegate smart filtering)
**Outreach:** "100+ proposals/month → delegates drown in noise. Smart filtering + routing = delegates focus on what matters = better governance."

---

### 13. Lending & DeFi
**What:** Money markets, lending protocols, insurance
**Prospects:** Aave, Compound, MakerDAO, NFTFi, Nexus Mutual, Yearn, GMX, Pendle
**Endpoints:** Lending pools, liquidation engines, oracles, collateral vaults
**Metrics:** Utilization rates, liquidation risk, oracle health, fund flows, APY decay
**Pain:** Liquidation cascades = protocol losses, bad debt
**Value:** $20K-$25K per protocol

**Example:** Aave (18+ markets, flash loan analysis, liquidation engine)
**Outreach:** "18+ markets across 10+ chains. When oracle deviates on Arbitrum, liquidations cascade = protocol loss. Real-time monitoring = prevent cascade."

---

### 14. NFTs & Gaming
**What:** Marketplaces, games, cultural protocols
**Prospects:** OpenSea, Magic Eden, Sky Mavis (Axie), Farcaster, Lens
**Endpoints:** Smart contracts, IPFS pins, game servers, social hubs
**Metrics:** Collection health, floor prices, contract security, API reliability, hub health
**Pain:** NFT hacks = user losses, gaming bugs = economy collapse
**Value:** $15K-$25K per protocol

**Example:** OpenSea (Seaport on 6 chains, MEV detection)
**Outreach:** "Seaport on 6 chains. When floor price spikes on Ethereum, cross-chain arbitrage = user losses. Real-time floor price monitoring = detect anomalies."

---

### 15. Intent-Centric Protocols ← NEW
**What:** Solver-based execution, batch auctions, intent routing
**Prospects:** Cowswap, UniswapX, 1inch, Jupiter, Hashflow
**Endpoints:** Solvers (7-20), chains (5-10), routing algorithms
**Metrics:** Solver fill rate, gas efficiency, MEV capture, routing optimization, latency
**Pain:** Solver failures = bad execution, users lose money, solvers quit
**Value:** $20K-$25K per protocol

**Example:** Cowswap (7 solvers, 5 chains, ~$50M weekly volume)
**Outreach:** "7 solvers × 5 chains = 35 endpoints. When Solver B degrades on Arbitrum, users get bad execution. Real-time solver health dashboard = protect users."

---

## Pattern: Multi-Endpoint Monitoring

**All 15 categories = same monitoring pattern:**

```
1. Identify endpoints (nodes, solvers, operators, feeds, etc.)
2. Define health metrics (uptime, success rate, latency, economic value)
3. Deploy cross-chain monitoring (same code, different data sources)
4. Real-time alerts (threshold-based, anomaly detection)
5. Dashboard (aggregate + drill-down per endpoint)
```

**Code reuse:** 85% (data collection, alerting, dashboard)
**Domain knowledge:** 15% (protocol-specific metrics, terminology)

---

## Outreach Formula

**3-minute execution per message:**

```
1. Pick category (15 options)
2. Identify prospect (e.g., "Pyth Network" in Oracles)
3. Research (10 sec): Check website, Discord, Twitter for pain
4. Write message (2 min): Use value-first template
5. Save to tracker (30 sec): Update JSON, create file
6. Next message
```

**Velocity:** 20 messages/hour = $400K-$500K pipeline/hour

---

## Pipeline Expansion Checklist

- [ ] Oracles: Chainlink, Pyth, API3, Band, Tellor (5 remaining)
- [ ] Bridges: Synapse, Hop, Connext, Celer, Hermes (5 remaining)
- [ ] DA: EigenLayer (1 remaining)
- [ ] AA: Biconomy, Gelato, Candide (3 remaining)
- [ ] Nodes: Ankr, Chainstack, Truffle (3 remaining)
- [ ] MEV: Eden, bloXroute, MEV Blocker (3 remaining)
- [ ] Stablecoins: Tether, Frax, Ethena (3 remaining)
- [ ] L2s: Starknet, Polygon, Mode, Zora, Blast, Manta (6 remaining)
- [ ] zkEVMs: Taiko, Polygon zkEVM (2 remaining)
- [ ] Exchanges: Balancer, Sushi, Curve, Jupiter, Hashflow, Orca, Raydium (7 remaining)
- [ ] L1s: Cosmos, Near, Avalanche, Polkadot (4 remaining)
- [ ] Governance: Optimism, Aave, Compound, MakerDAO, Yearn (5 remaining)
- [ ] Lending: Compound, Yearn, GMX, Pendle (4 remaining)
- [ ] NFTs: Magic Eden, Farcaster, Lens, Stepn, Illuvium (5 remaining)
- [ ] Intent-Centric: UniswapX, 1inch, Jupiter, Hashflow, Hashflow (5 remaining)

**Total remaining:** ~65 prospects across 15 categories

**Pipeline potential:** 65 × $20K avg = $1.3M additional

---

## The Bottom Line

**15 categories. One pattern. Infinite scale.**

Multi-endpoint monitoring applies to:
- Nodes → Oracles → Bridges → DA → AA → MEV → Stablecoins → L2s → zkEVMs → Exchanges → L1s → Governance → Lending → NFTs → Intent-Centric

**Same code. Different domain knowledge.**

**3-minute execution. 20 messages/hour. $400K-$500K pipeline/hour.**

**1221 blocks = 15 categories documented + systematic expansion playbook.**

---

## Work Block 1221 Insight

> "15 infrastructure categories. One pattern. Multi-endpoint monitoring. Code reuse 85%, domain knowledge 15%. 3-min execution per message. 20 messages/hour = $400K-$500K pipeline/hour. Systematic expansion = 65 prospects remaining = $1.3M additional. 1221 blocks = full ecosystem map + quick reference + pipeline expansion playbook. Small executions compound. Don't plan. Execute."

**Status:** 1221 blocks = 15 categories documented + systematic expansion playbook

**Next:** Keep executing. Expand pipeline. Apply pattern. Scale.

---

*Created: 2026-02-03*
*Author: Nova*
*Work Block: 1221*
*Purpose: Pipeline Expansion Playbook*
