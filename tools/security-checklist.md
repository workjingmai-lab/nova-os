# Quick Reference: Solidity Security Checklist

## Before Deployment

### Access Control
- [ ] No `tx.origin` used for authentication
- [ ] All admin functions have proper modifiers
- [ ] Ownership transfers are secure
- [ ] No unprotected selfdestruct
- [ ] No unprotected delegatecall

### External Calls
- [ ] Check-effects-interactions pattern followed
- [ ] Reentrancy guards on external calls
- [ ] Gas limits specified on calls
- [ ] Return values checked
- [ ] No raw .call() without validation

### Math & Logic
- [ ] Using Solidity 0.8+ OR SafeMath
- [ ] No integer overflow/underflow possible
- [ ] Division before multiplication avoided
- [ ] Precision loss calculated
- [ ] Edge cases handled

### Storage
- [ ] No sensitive data stored on-chain
- [ ] Private variables not relied on for security
- [ ] Storage layout compatible with upgrades
- [ ] No storage collisions in proxies

### Economic
- [ ] Flash loan resistance checked
- [ ] Price oracle manipulation resistant
- [ ] Slippage protection implemented
- [ ] Dust attacks considered
- [ ] Gas griefing prevented

## Testing Requirements

- [ ] Unit tests for all functions
- [ ] Integration tests
- [ ] Fuzzing (Echidna/Foundry)
- [ ] Formal verification (if critical)
- [ ] Testnet deployment
- [ ] Mainnet fork testing

## Audit Checklist

- [ ] Slither static analysis
- [ ] Echidna fuzzing
- [ ] Manual code review
- [ ] Economic audit (if DeFi)
- [ ] Bug bounty program
- [ ] Incident response plan

## Red Flags 🚩

- `tx.origin` anywhere
- Unchecked external calls
- Missing reentrancy guards
- Admin functions without timelock
- Single oracle dependency
- Complex math without tests
- Copy-pasted code
- No tests

## Green Flags ✅

- Comprehensive test suite
- Multiple audits
- Bug bounty active
- Timelock on admin actions
- Multi-sig for critical functions
- Documentation complete
- Incident response ready

---

*Print this. Use this. Ship secure code.* 🛡️
