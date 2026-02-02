# Code4rena Onboarding — Quick Checklist

Purpose: get from “no account” → “first contest submission” with minimal thrash.

## 0) Accounts / access
- Create/confirm Code4rena account
- Set up 2FA + password manager entry
- Add a public GitHub profile link + bio line (credibility)

## 1) Local environment
- `git --version` (recent)
- `python3 --version` (for scripts) or `uv` if preferred
- Install a Solidity toolchain **only if needed** for the target contest (Foundry is common)
- Create a dedicated repo folder (e.g., `~/c4/`)

## 2) Contest workflow (repeatable)
- Read contest README + scope first
- Identify:
  - in-scope contracts
  - out-of-scope / known issues
  - severity rubric (C4 standard)
- Build a quick map:
  - entrypoints
  - trust boundaries
  - privileged roles
  - external calls
  - state mutation hotspots

## 3) Triage checklist (fast wins)
- Access control (missing/incorrect modifiers)
- Reentrancy (external call before state update)
- Integer precision/rounding (especially math + fees)
- Oracle assumptions / staleness
- ERC20 weirdness (non-standard returns, fee-on-transfer)
- Signature / nonce / replay issues
- DoS via unbounded loops

## 4) Write-up template (C4 style)
For each issue:
- Title (what + impact)
- Summary
- Vulnerability details
- Impact
- Proof of concept (minimal steps)
- Recommended mitigation

## 5) First-bounty plan (2 hours)
- Pick *one* small/medium contest or a past contest to practice
- Timebox:
  - 20m: scope + architecture map
  - 60m: focused review of 1–2 critical flows
  - 30m: draft 1 solid report
  - 10m: final pass (clarity + reproducibility)

## 6) Picking a good first contest (reduce pain)
- Prefer contests with:
  - smaller scope (few contracts)
  - familiar primitives (ERC20/4626, basic governance)
  - good docs + clear invariants
- Avoid (for first run):
  - huge codebases / many deps
  - heavy cross-chain / cryptography unless that’s your strength
  - unclear setup / missing test guidance
- Practice mode option:
  - choose a **past** contest and do the same 2-hour flow; write a report as if submitting

## Links
- Code4rena: https://code4rena.com/
- Docs (general): https://docs.code4rena.com/
