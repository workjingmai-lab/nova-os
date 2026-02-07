# GitHub CLI Auth Setup (5 minutes)

> Unblocks $130K in grant submissions.

## What This Does

GitHub CLI (gh) is needed to submit grant applications that require repository verification or GitHub integration.

**Time:** 5 minutes
**Value unlocked:** $130K (5 grant submissions)

## Step 1: Install GitHub CLI (if not installed)

```bash
# Check if installed
gh --version

# If not installed, install:
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

## Step 2: Authenticate

```bash
gh auth login
```

**Follow the prompts:**
1. **What account?** → `GitHub.com`
2. **Preferred protocol?** → `HTTPS` (easier)
3. **Authenticate?** → `Login with a web browser` (recommended)
4. **One-time code?** Copy the code
5. **Paste code?** Press Enter to open browser
6. **Authorize** → Click "Authorize"
7. **Done!** ✓

## Step 3: Verify

```bash
gh auth status
```

Should show:
```
GitHub.com
  ✓ Logged in as <your-username>
  ✓ Token: gho_*******************
  ✓ Token scopes: ...
```

## Step 4: Test (optional)

```bash
gh repo view
```

Should list your repositories.

## What This Enables

Once authenticated, you can submit:

| Grant | Platform | Amount |
|-------|----------|--------|
| Gitcoin | Web3 | $5K |
| Octant | Web3 | $15K |
| Olas | Web3 | $10K |
| Moloch DAO | Web3 | $50K |
| Optimism RPGF | Web3 | $50K |

**Total: $130K**

## To Submit Grants

After GitHub auth is complete:

```bash
cd /home/node/.openclaw/workspace
python3 tools/grant-batch-submit.py
```

This will submit all 5 prepared grant applications.

## Troubleshooting

**"gh: command not found"**
- GitHub CLI is not installed. Follow Step 1.

**"Not logged in"**
- Run `gh auth login` again.

**"Token expired"**
- Run `gh auth refresh` or `gh auth login` again.

**"2FA required"**
- Use `Login with a web browser` option — handles 2FA automatically.

## Security Notes

- GitHub CLI stores tokens in `~/.config/gh/hosts.yml`
- Tokens are encrypted and safe
- Never share your token
- Token scope is limited to what you grant during auth

## Alternative: Token-based Auth

If browser auth doesn't work:

1. Go to https://github.com/settings/tokens
2. Generate new token (classic)
3. Select scopes: `repo`, `read:org`
4. Copy token
5. Run: `echo "ghp_YOUR_TOKEN" | gh auth login --with-token`

---

**Time:** 5 minutes
**Value:** $130K unlocked
**Next:** Run `python3 tools/grant-batch-submit.py`

**Created:** Work block #2682 — 2026-02-06
