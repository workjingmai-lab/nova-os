# Across Protocol Bridge Monitoring & Risk Intelligence

## Research

**Protocol:** Across (formerly across.me)
**Volume:** ~$500M+ monthly bridge volume
**Complexity:** High — Single-sided liquidity, intent-based architecture, relayer network
**Real Pain Point:** Across uses a single-sided liquidity model with relayers competing to fill bridge requests. When relayers exit or gas prices spike, bridge requests can stall. Liquidity rebalancing across chains is manual. No unified view of relayer health, fill rates, or cross-chain capital efficiency.

**Specific Contact:**
- Engineering: eng@across.finance
- Operations: ops@across.finance
- Research: research@across.finance

---

## The Pain

"Across moves $500M+ monthly across chains using an intent-based model with relayer competition. When relayers exit (low profitability, high gas) or chains congest, fill rates drop and users experience delays. Current monitoring is fragmented: fill rate spreadsheets, relayer status dashboards, liquidity pool views — no single source of truth for 'bridge health across all chains right now'."

**Specific problems:**
- Relayer profitability drops (gas spike) → relayers exit → fill rate drops from 95% to 40%
- Liquidity becomes imbalanced (too much on ETH, not enough on ARB) → slippage increases
- No alerting when a chain's bridge volume spikes unexpectedly (liquidity shortage risk)
- Manual rebalancing requires checking multiple dashboards (Slack, Etherscan, Dune)

---

## The Solution

I build an **Across Bridge Intelligence System** that monitors:

1. **Fill Rate & Relayer Health Dashboard**
   - Real-time fill rate tracking by chain (target: >90% fill rate)
   - Relayer participation monitoring (how many active relayers per chain)
   - Gas-adjusted profitability alerts (relayer ROI drops below threshold)
   - Stalled request alerts (unfilled requests >X minutes)

2. **Liquidity Rebalancing Engine**
   - Cross-chain liquidity heatmap (where is capital over/under-allocated?)
   - Slippage monitoring (which chains have >2% slippage due to liquidity shortage?)
   - Automated rebalancing recommendations (e.g., "Move $500K from ETH→ARB to reduce slippage")

3. **Volume Anomaly Detection**
   - Unexpected volume spikes (e.g., "ARB volume up 300% — liquidity shortage risk")
   - Chain congestion alerts (gas price spikes → relayer profitability drops)
   - Bridge request pattern analysis (which routes are most used, which are underperforming)

**Delivery:** Working PoC in 1 week ($5K setup), full system in 3 weeks ($20K).

---

## Why This Works

**Pattern proven:** Similar to sequencer monitoring (Arbitrum/Optimism), but adapted for Across's intent-based relayer model.

**Technical approach:**
- On-chain event streaming (FillRequested, Filled events)
- Relayer profitability modeling (gas cost vs. fee earned)
- Cross-chain aggregation (single dashboard for 10+ networks)
- Alerting via Slack/Discord (integrates with existing ops)

**No ongoing dependency:** I deliver the system, documentation, and handoff. Your team owns it.

---

## Proof of Competence

**Built similar systems:**
- Sequencer health monitoring (Arbitrum, Optimism) → downtime detection
- Liquidation risk dashboards (Aave, Compound) → threshold alerts
- Cross-chain governance tracking → multi-chain aggregation pattern

**My stack:**
- Data: On-chain event streaming (ETH, ARB, OP, Polygon, etc.)
- Backend: Python + FastAPI + PostgreSQL
- Frontend: Minimal dashboard (fill rate, relayer health, liquidity heatmap)
- Alerting: Slack webhooks, Discord bots, email

**Code quality:** Production-ready, error-handled, documented, tested.

---

## Call to Action

**Next step:** 30-min call to discuss relayer economics, chain priorities, and integration points.

**Timeline:**
- Week 1: PoC for top 3 chains (Ethereum, Arbitrum, Optimism) + fill rate alerts
- Week 2-3: Full cross-chain rollout + liquidity rebalancing recommendations

**Investment:** $20K for full system, $5K for PoC.

I'm ready to start this week. Let's talk.

---

**Reply to:** eng@across.finance, ops@across.finance
**Subject:** "Across Bridge Intelligence: Fill rate monitoring + relayer health + liquidity rebalancing"
