# EigenDA Data Availability Monitoring — Service Proposal

## Context (Research)
- **EigenDA:** Decentralized data availability layer built on EigenLayer restaking protocol (400+ operators, $15B+ restaked ETH)
- **Unique angle:** DA via restaked ETH operators = different security model (Ethereum validators vs standalone nodes)
- **Critical infrastructure:** Rollups and dApps integrating EigenDA for DA (backed by Ethereum's economic security)
- **Market fit:** DA wars (Celestia vs Avail vs EigenDA) = EigenDA has the Ethereum security advantage, but needs monitoring

## Pain Point
**Restaked operator DA failure** = Data unavailable, light clients can't verify rollup state. When EigenDA fails, **dependent rollups halt** AND **restaker slashing risk increases**. Current tools monitor node uptime but not **operator DA performance** or **slashing condition proximity**.

## Solution
I build an **EigenDA monitoring system**:
- **Operator-level DA health** — Track each operator's data publication success, retrieval reliability, performance metrics
- **Slashing risk monitoring** — Detect operators approaching slashing conditions (liveness failures, misbehavior patterns)
- **Pre-halt detection** — Detect DA degradation patterns (operator failures increase, retrieval times spike)
- **Ethereum security correlation** — Link EigenDA health to Ethereum validator performance (unique angle)

### What's Built
**Proof of concept available** — Operator DA tracker + slashing risk simulator (2-min demo)
- **Real-time alerts:** Operator DA success rate <95% triggers warning before rollup impact
- **Operator-specific dashboards:** "Operator X's DA health at 91%, slashing risk: MEDIUM"
- **Restaker visibility:** "Your restaked ETH is backing these operators — here's their DA performance"

### Pricing
- **Quick setup:** $1-2K — Basic DA monitoring (operator health + alerts)
- **Custom integration:** $3-5K — Multi-operator dashboards + slashing risk deep-dive
- **Ongoing monitoring:** $2-4K/month — 24/7 DA health + incident response + weekly reports

## Why Now?
**EigenDA is the third major DA layer, backed by Ethereum's restaked security.** Projects choosing between DA layers need **comparative reliability data** (Celestia vs Avail vs EigenDA). Pre-halt detection = **warning before dependent rollups break AND restakers get slashed**.

## Call to Action
**Is EigenDA's operator health visible to integrators and restakers?** I can show you a 2-min demo of operator-level DA monitoring + slashing risk tracking.

**Reply "yes"** and I'll share the PoC. Or forward to the infra team.

---

*Target: EigenLabs (infra@eigenlabs.org) + EigenDA core team*
*Category: Modular blockchain infrastructure (DA layer #3, restaking-backed)*
*Value: $20K (setup) + ongoing monitoring*
