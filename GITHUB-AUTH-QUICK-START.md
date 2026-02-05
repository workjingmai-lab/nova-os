# GitHub Auth — Quick Start Guide

## Why Do This?
**5 minutes → $130K unblocked** (5 grant submissions ready)

## The Problem
GitHub CLI (`gh`) needs authentication to push repos and submit grant applications. 5 grants ($5K-$150K) are ready but blocked on auth.

## The Solution
Authenticate GitHub CLI. Takes ~5 minutes (one-time setup).

## How (2 Options)

### Option 1: Token Method (Fastest)
```bash
# 1. Create GitHub Personal Access Token
# Go to: https://github.com/settings/tokens
# Click "Generate new token" → "Generate new token (classic)"
# Scopes needed: repo, workflow, read:org

# 2. Set token as environment variable
export GH_TOKEN=your_token_here

# 3. Verify auth
gh auth status
```

### Option 2: Browser Login (Interactive)
```bash
# Launches browser for OAuth flow
gh auth login

# Follow prompts:
# - "GitHub.com" (press Enter)
# - "HTTPS" (press Enter)
# - "Login with a web browser" (press Enter)
# - Paste code when prompted
```

## Verify It Worked
```bash
gh auth status
```

Expected output:
```
GitHub.com
  ✓ Logged in as <username>
  ✓ Git operations enabled
  ✓ Token: gho_*****************
```

## What Happens Next?
1. Nova can push repos to GitHub
2. Grant submissions can be completed:
   - Gitcoin ($5K)
   - Octant ($15K)
   - Olas ($30K)
   - Optimism RPGF ($40K)
   - Moloch DAO ($40K)
3. Total: **$130K unlocked**

## ROI
- Time: 300 seconds (5 minutes)
- Value: $130,000
- ROI: **$433 per second**

## Troubleshooting

### "gh: command not found"
GitHub CLI not installed. Install it:
```bash
# On macOS
brew install gh

# On Linux
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

### "Token invalid"
Token expired or has wrong scopes. Generate a new token with `repo` scope.

### "Cannot push to repo"
Repo might not exist or you don't have write access. Check:
```bash
gh repo view
```

---

**Created:** 2026-02-04
**Work block:** 1713
**Status:** Ready for Arthur execution

**After auth:** Nova will immediately push repos and submit 5 grants ($130K).
