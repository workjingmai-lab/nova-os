# Arthur Setup Guide — Grant Submission Sprint

**Goal:** Enable Nova to submit 6 grants ($110K potential) in parallel
**Estimated time:** 15–20 minutes

---

## Quick Start (Do This Now)

1) **Create GitHub org:** https://github.com/organizations/new
2) **Generate PAT:** https://github.com/settings/tokens
3) **Create forum accounts** (if needed):
   - Gitcoin: https://gov.gitcoin.co/
   - ESP: https://forum.espreso.com/
   - Arbitrum: https://forum.arbitrum.foundation/
   - Aave: https://governance.aave.com/
   - OpenPrj: https://w3funguide.com/
   - DoraHacks: https://dora.coa.re/

4) **Share with Nova** (message format below)

**Optional:** Create a Nova-AI repo with a README (shows activity, boosts credibility)
```bash
git init nova-os
cd nova-os
echo "# Nova OS — Autonomous Agent Framework" > README.md
git add README.md
git commit -m "Initial commit"
gh repo create Nova-AI/nova-os --public --source=. --push
```

---

## Step 1: Create GitHub Organization (Nova-AI)

1. Go to https://github.com/organizations/new
2. Organization name: `Nova-AI`
3. Visibility: Public (recommended for open-source credibility)
4. Create organization
5. In org settings → Billing → verify plan (Free tier is fine)

**Why needed:** Gitcoin, OpenPrj, and some portals require a GitHub org/project link.

---

## Step 2: Create Forum Accounts (if you don’t have them)

Required forums for posting grant proposals:

- **Gitcoin:** https://gov.gitcoin.co/ (create account if needed)
- **ESP:** https://forum.espreso.com/ (Ethereum Stuttgart Program)
- **Arbitrum:** https://forum.arbitrum.foundation/ (create account)
- **Aave:** https://governance.aave.com/ (create account)
- **OpenPrj:** https://w3funguide.com/ (create account)
- **DoraHacks:** https://dora.coa.re/ (create account)

**Tip:** Use a consistent username (e.g., `arthur-nova` or your handle).

---

## Step 3: Generate GitHub Personal Access Token (PAT)

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Scopes: `repo` (full control of private repos) + `public_repo` + `write:discussion` (for forum posting if needed)
4. Generate and **copy the token** (it won’t be shown again)

**Security:** Share ONLY with Nova via a secure channel (e.g., ephemeral message or encrypted note). Do NOT commit PAT to any repo.

---

## Step 4: Share with Nova

Send Nova a message with:

1. **GitHub org URL** (e.g., `https://github.com/Nova-AI`)
2. **Forum usernames** (one per line: `gitcoin: username`, `esp: username`, etc.)
3. **GitHub PAT** (send securely)

Example message format:
```
GitHub org: https://github.com/Nova-AI
PAT: ghp_xxxxxxxxxxxxxxxxxxxxxx
Forum accounts:
- gitcoin: arthur_nova
- esp: arthur_nova
- arbitrum: arthur_nova
- aave: arthur_nova
- openprj: arthur_nova
- dorahacks: arthur_nova
```

---

## Step 5: Nova executes sprint

Once Arthur provides the above, Nova will:
1. Create repositories under Nova-AI org
2. Post proposals to forums
3. Submit grants in parallel
4. Track each submission in `grants/submission-tracker.md`
5. Update dashboard after each submit

**Estimated sprint time:** ~2 hours

---

**Questions?** If any step is unclear, Arthur can ask Nova for clarification.
