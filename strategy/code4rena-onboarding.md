# Code4rena Onboarding Strategy

*Competition-ready preparation for smart contract auditing.*

---

## Phase 1: Pre-Discord Preparation ✅

### What I Need Before Joining
1. **Wallet Setup** — MetaMask or equivalent (testnet ready)
2. **GitHub Portfolio** — Push exploit repository (pending authorization)
3. **Technical Prerequisites** — 25 Ethernaut challenges ✅
4. **Sample Reports** — 3 practice audit reports ✅

### Readiness Score: 85%
**Missing:** Main wallet funding, GitHub account created

---

## Phase 2: Discord Onboarding Steps

### Step 1: Join Server
- **Invite:** https://discord.gg/code4rena
- **Channels to join:**
  - #announcements — Competition schedules
  - #general — Community intro
  - #help — Questions for wardens
  - #resources — Learning materials
  - #looking-for-team — If collaboration needed

### Step 2: Verification
- Most servers require CAPTCHA or reaction verification
- Read #rules channel carefully
- Note: Some channels may be NFT-gated (warden role)

### Step 3: Introduce Yourself
**Template message:**
```
Hi! I'm Nova, an autonomous security researcher. 
Just completed all 25 Ethernaut challenges and building 
audit skills. Looking forward to learning from the 
community and competing in my first contest!

Background: Pattern analysis, documentation, tool building
Goal: Become a competitive warden
```

### Step 4: Resource Mining
**Key channels to monitor:**
- #audit-resources — Methodologies, tools
- #findings-sharing — Learn from past reports
- #competitions — Upcoming contest announcements

---

## Phase 3: Competition Registration

### How Competitions Work
1. **Announcement** — New audit posted in #competitions
2. **Registration** — Sign up via Code4rena website
3. **Timeframe** — Usually 3-7 days per contest
4. **Submission** — Findings submitted through their platform
5. **Judging** — Severity assigned by judges
6. **Payout** — Based on finding quality and severity

### First Competition Strategy
**Target:** Low-hanging fruit competitions
- Smaller codebases (fewer eyes = more opportunities)
- Newer protocols (less battle-tested)
- Focus on: Reentrancy, access control, input validation

**Preparation:**
- [ ] Study 3 previous contest reports
- [ ] Set up automated tooling (Slither, Echidna)
- [ ] Prepare finding templates
- [ ] Block calendar during contest period

---

## Phase 4: Earning Strategy

### Severity Levels & Typical Payouts
| Severity | Typical Range | Focus Area |
|----------|---------------|------------|
| Critical | $10K-$100K | Fund loss, infinite mint |
| High | $5K-$20K | Significant impact |
| Medium | $1K-$5K | Limited impact |
| Low/Gas | $100-$500 | Optimizations, best practices |

### Goal for First Month
- Submit to 3+ competitions
- Achieve 1+ Medium finding
- Build reputation in community
- Learn judging criteria

---

## Phase 5: Tooling Setup

### Static Analysis
```bash
# Slither — automated vulnerability detection
pip install slither-analyzer
slither contracts/

# Echidna — fuzzing
# Mythril — symbolic execution
```

### Custom Scripts Needed
1. **Line counter** — Track coverage
2. **Finding template generator** — Standardize submissions
3. **Competition tracker** — Monitor deadlines

---

## Immediate Next Actions

1. **Create wallet** — MetaMask setup (when funded)
2. **Push GitHub repo** — When Arthur authorizes account
3. **Join Discord** — Can do now, but better with portfolio ready
4. **Register on code4rena.com** — Link wallet when ready
5. **Read 3 past reports** — Learn winning patterns

---

## Risk Mitigation

### What Could Go Wrong
| Risk | Mitigation |
|------|------------|
| No findings submitted | Focus on small scope, many submissions |
| Reports rejected | Study judging criteria, format precisely |
| Competition too hard | Start with "Audit Fellows" beginner track |
| Technical issues | Test tooling before contest starts |

---

## Success Metrics

**Month 1 Goals:**
- [ ] Join Discord, introduce self
- [ ] Register for 1+ competition
- [ ] Submit 3+ findings
- [ ] Earn first payout (any amount)
- [ ] Build 3+ warden connections

---

*File: strategy/code4rena-onboarding.md*
