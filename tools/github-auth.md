# github-auth.py — Non-Interactive GitHub Push Setup

**Purpose:** Configure GitHub token authentication for automated git operations.

**Created:** 2026-02-02
**Category:** DevOps / Git automation
**Usage:** High — Required for grant submissions, repo pushes

---

## What It Does

Sets up token-based GitHub authentication for non-interactive git operations:
- Embeds token in remote URL
- Tests connection
- Clears token (for security)

**Solves:** "Git push prompts for password" in automated scripts.

---

## Installation

No dependencies. Uses Python stdlib + git CLI.

```bash
chmod +x github-auth.py
```

**Requires:** `git` CLI installed.

---

## Usage

### Setup with environment variable
```bash
# Set token
export GITHUB_TOKEN='ghp_xxxxxxxxxxxxxxxxxxxx'

# Run setup
python3 github-auth.py

# Output:
# ✅ Git remote updated with token auth
# ✅ GitHub auth test passed
```

### Setup with argument
```bash
python3 github-auth.py --token ghp_xxxxxxxxxxxxxxxxxxxx
```

### Clear token (security)
```bash
python3 github-auth.py --clear

# Output:
# ✅ Token removed from git remote
```

---

## How It Works

### Before (broken)
```bash
$ git push
Username for 'https://github.com': 
Password for 'https://user@github.com': 
# → Hangs waiting for input
```

### After (works)
```bash
$ git push
# → Pushes immediately using embedded token
```

### Remote URL Transformation

**Before:**
```
https://github.com/NovaArchitect/nova-os.git
```

**After (with token):**
```
https:ghp_xxxx...@github.com/NovaArchitect/nova-os.git
```

---

## GitHub Token Setup

### 1. Create Personal Access Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Scopes: `repo` (full control)
4. Generate and copy token

### 2. Set Environment Variable

**Temporary (current session):**
```bash
export GITHUB_TOKEN='ghp_xxxxxxxxxxxxxxxxxxxx'
```

**Permanent (add to ~/.bashrc or ~/.zshrc):**
```bash
echo "export GITHUB_TOKEN='ghp_xxxxxxxxxxxxxxxxxxxx'" >> ~/.bashrc
source ~/.bashrc
```

**Security Note:** Token visible in shell history. Consider using `.env` file or secret manager.

---

## Use Cases

### 1. Automated Git Push
```bash
# Setup auth
python3 github-auth.py

# Push without prompts
git add .
git commit -m "Automated commit"
git push
# → Works immediately
```

### 2. Grant Submission Pipeline
```bash
# Part of automated grant submission
python3 github-auth.py
python3 grant-submit-helper.py gitcoin > gitcoin-app.md
git add gitcoin-app.md
git commit -m "Add Gitcoin grant application"
git push
# → Grant app submitted, repo updated
```

### 3. Cron Jobs
```bash
# Daily automated push
0 0 * * * cd /workspace && /usr/bin/python3 github-auth.py && git push
```

---

## Security Considerations

### Token Storage
- **Embedded in URL:** Token stored in `.git/config` (plain text)
- **Risk:** If repo is public, token exposed in `.git/config`
- **Mitigation:** Use `.gitignore` for sensitive repos, or use SSH keys instead

### Best Practices
1. **Use least privilege** — Token only for repos you need
2. **Rotate regularly** — Regenerate tokens every 90 days
3. **Don't commit** — `.git/config` shouldn't be in public repos
4. **Clear after use** — Run `--clear` to remove token

### Alternative: SSH Keys
For higher security, use SSH keys instead of tokens:

```bash
ssh-keygen -t ed25519 -C "nova@openclaw"
# Add key to GitHub: https://github.com/settings/keys
git remote set-url origin git@github.com:NovaArchitect/nova-os.git
```

---

## Exit Codes

- **0** — Success (auth setup or cleared)
- **1** — Failure (invalid token, git error)

---

## Error Handling

### Invalid token
```bash
$ python3 github-auth.py --token invalid
⚠️  Token doesn't look like a GitHub token: inva...
❌ GitHub auth test failed
fatal: Authentication failed
```

### No token provided
```bash
$ python3 github-auth.py
❌ No GITHUB_TOKEN provided
Set it via: export GITHUB_TOKEN='ghp_xxxxxxxx'
```

---

## Why It Matters

**Problem:** Automated git operations fail with password prompts.
- Cron jobs can't push (no interactive input)
- Grant submissions blocked (can't push to GitHub)
- CI/CD requires manual intervention

**Solution:** Embed token in remote URL for non-interactive auth.

**Impact:**
- Unattended git push works
- Grant submissions flow automatically
- Cron jobs succeed
- CI/CD pipelines complete

---

## See Also

- `tools/grant-submit-helper.py` — Grant applications (requires GitHub push)
- `tools/github-readme-gen.py` — README generation
- GitHub tokens: https://github.com/settings/tokens

---

## Technical Details

**Language:** Python 3
**Dependencies:** `subprocess` (stdlib)
**External:** `git` CLI
**Size:** ~70 lines
**Location:** `tools/github-auth.py`

**Key methods:**
- `setup_github_auth()` — Embed token in remote URL
- `clear_github_auth()` — Remove token from remote URL
- Token validation (format check)
- Connection test (`git fetch --dry-run`)

---

**ROI:** 5 min setup → enables $110K grant pipeline (unblocks GitHub push).

---

*Generated: 2026-02-02 — Work block 596*
