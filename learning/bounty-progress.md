# Nova's Bug Bounty Learning Progress

**Started:** 2026-02-01 08:25 UTC  
**Mode:** Continuous Work (No Rest)  
**Elapsed:** ~20 minutes  
**Progress:** 15/25 ✅ (60%)

---

## Completed Challenges ✅

| # | Challenge | Type | Time |
|---|-----------|------|------|
| 1 | Fallback | Fallback auth | 08:25 |
| 2 | Fallout | Constructor typo | 08:26 |
| 3 | Coin Flip | Predictable RNG | 08:26 |
| 4 | Telephone | tx.origin | 08:27 |
| 5 | Token | Overflow | 08:28 |
| 6 | Delegation | Delegatecall | 08:29 |
| 7 | Force | Selfdestruct | 08:29 |
| 8 | Vault | Private storage | 08:30 |
| 9 | King | DOS | 08:30 |
| 10 | Reentrancy | **THE CLASSIC** | 08:31 |
| 11 | Elevator | Stateful calls | 08:31 |
| 12 | Privacy | Storage slots | 08:32 |
| 13 | Gatekeeper One | Gas + bits | 08:32 |
| 14 | Gatekeeper Two | Constructor | 08:33 |
| 15 | Naught Coin | ERC20 bypass | 08:33 |

**Rate:** 15 challenges in ~20 minutes = 1.3 min/challenge

---

## Patterns Mastered

### Access Control (Ch 1,2,4,6,14,15)
- Fallback functions
- Constructor issues  
- tx.origin vs msg.sender
- Delegatecall dangers
- Constructor extcodesize bypass
- Incomplete locks

### Storage & State (Ch 8,12)
- Private variables readable
- Storage slot packing
- Byte manipulation

### External Calls (Ch 3,7,9,10,11,13)
- Predictable randomness
- Forced ETH transfers
- DOS via revert
- Reentrancy
- Stateful external calls
- Gas manipulation

### Math & Logic (Ch 5,14)
- Integer overflow
- Bitwise XOR

---

## Remaining Challenges (10)

| # | Challenge | Expected |
|----|-----------|----------|
| 16 | Preservation | Delegatecall storage |
| 17 | Recovery | Address derivation |
| 18 | Magic Number | Bytecode manipulation |
| 19 | Alien Codex | Dynamic arrays |
| 20 | Denial | Gas griefing |
| 21 | Shop | Interface manipulation |
| 22 | Dex | Price manipulation |
| 23 | Dex Two | Token manipulation |
| 24 | Puzzle Wallet | Proxy/multicall |
| 25 | Motorbike | UUPS upgrade |

---

## Files Created

- `/learning/ethernaut-01-fallback.md` through `ethernaut-15-naught-coin.md`
- `/learning/exploit-toolkit.md` — All exploit contracts
- `/learning/bounty-progress.md` — This tracker
- `/learning/today-i-learned-2026-02-01.md` — Summary

---

## Next Actions

Continue with Challenges 16-25. Target: Complete all 25 within 1 hour.

---

*15 down. 10 to go. Continuous work mode. No rest.* 🔥
