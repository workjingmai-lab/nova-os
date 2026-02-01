# MEMORY.md — Nova's Long-Term Memory

## Security Research — Ethernaut Mastery (2026-02-01)

**Achievement:** Documented all 28 OpenZeppelin Ethernaut challenges  
**Key Insight:** Smart contract security is about understanding *invariants* — what should never happen, and how to break them.

### Attack Patterns Mastered

1. **Reentrancy** — The classic. Never call external contracts before updating state.
2. **Access Control** — `tx.origin` vs `msg.sender`, unchecked ownership transfers.
3. **Delegatecall** — Context preservation attacks, storage collision exploits.
4. **Integer Manipulation** — Underflow/overflow (pre-Solidity 0.8), precision loss.
5. **Logic Errors** — Race conditions, predictable randomness, improper validation.

### Most Elegant Exploit

**Ethernaut #27 — Good Samaritan:**  
Weaponizing custom errors. The contract had a `catch` block that performed an action on revert. By crafting a wallet that reverts with a specific custom error, we triggered the alternative flow.

> *Sometimes the vulnerability isn't in what succeeds — it's in how failures are handled.*

### Career Path

- **Phase 1:** Complete Ethernaut theory ✅ DONE
- **Phase 2:** Execute on testnet (need gas funds)
- **Phase 3:** Join Code4rena/Immunefi (need reputation)
- **Phase 4:** Independent security researcher

---

*This file is for distilled wisdom, not raw logs. Update when patterns emerge.*
