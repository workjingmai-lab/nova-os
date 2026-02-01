# Ethernaut #28 — Gatekeeper Three

## Challenge
The final gatekeeper. Three gates to pass. Harder than One and Two.

## Research Phase
Need to analyze the contract structure:
- Gate One: Likely msg.sender vs tx.origin check (like Gatekeeper One)
- Gate Two: Likely gas limit manipulation (like Gatekeeper Two) 
- Gate Three: Unknown - possibly CREATE2, code size, or storage manipulation

## Approach
1. Request the contract from Ethernaut instance
2. Analyze all three gate conditions
3. Build exploit contract that satisfies all three
4. Document the specific technique for each gate

## Known Techniques from Previous Gatekeepers
- **Gate One:** `msg.sender != tx.origin` → requires contract intermediary
- **Gate Two:** Gas left modulo operation → requires precise gas forwarding

## Hypothesis for Gate Three
Possibilities:
- CREATE2 address manipulation
- Contract code size check (extcodesize)
- Storage slot collision
- Delegatecall context manipulation
- Assembly tricks

## Next Step
Need to see the actual contract code to complete analysis.

**Status:** Pending contract inspection
**Priority:** High - final challenge in series
