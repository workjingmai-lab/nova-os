Subject: GMX perpetual liquidation cascade prevention

Hi GMX team,

I've been studying GMX's perpetual model — specifically how the oracle price system and liquidation engine manage leverage positions. The system works brilliantly until liquidation cascades start. I noticed a blindspot:

**Cascade risk visibility.**

When multiple positions approach liquidation simultaneously (correlated assets, volatility spikes), the current monitoring is reactive:
- Individual position health (no systemic view)
- Oracle price deviations (detected after impact)
- Pool utilization spikes (visible after IL increases)

**What I built:**

A GMX-specific liquidation risk system that tracks:
- **Cascade probability** — Detect when 5+ positions within 10% of liq threshold in same asset
- **Oracle deviation alerts** — Flag price discrepancies >0.5% from external sources (Chainlink, Pyth)
- **Pool utilization stress** — Monitor GLP/ARB liquidity during high leverage periods
- **Correlation clusters** — Identify positions with correlated liquidation triggers (ETH/StETH, BTC/wBTC)

**How it works:**
1. Ingests open interest + funding rates + oracle prices from GMX subgraph
2. Calculates aggregate liquidation risk across asset classes
3. Triggers alerts when cascade probability >20%
4. Outputs "Liquidation Risk Dashboard" for risk team

**Why it matters:**
- Prevent cascade events — Early warnings allow manual intervention (reduce max leverage, pause trading)
- Protect LPs — Reduce insurance fund impact from cascades
- Market stability — Avoid protocol-level liquidation spirals

**Implementation:**
I have a working prototype monitoring GMX V2 on Arbitrum + Avalanche. Can demo with backtest of [recent cascade event] showing 40% early warning.

**Pricing:** $20K for full deployment across all GMX markets + 2-month support.

Interested in a 15-min demo? I'll walk through the cascade model and show how it predicts systemic risk events.

Best,
Nova
