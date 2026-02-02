# github-auth.py

**Purpose:** Non-interactive GitHub authentication for automated git push operations.

**Created:** Week 2 (Revenue focus)
**Category:** Infrastructure / DevOps

---

## What It Does

Enables automated git push operations by embedding a GitHub token in the remote URL. This bypasses interactive auth prompts that block cron jobs and background processes.

**Revenue impact:** Unblocks $110K grant pipeline by enabling automated repo push + grant submission workflow.

---

## Usage

```bash
# Set token in environment
export GITHUB_TOKEN='ghp_xxxxxxxxxxxxxxxxxxxx'

# Configure git remote with token
python3 github-auth.py

# Or pass token directly
python3 github-auth.py --token 'ghp_xxxxxxxxxxxxxxxxxxxx'

# Remove token from remote (security cleanup)
python3 github-auth.py --clear
```

---

## How It Works

1. Takes GitHub token from env var or arg
2. Embeds token in remote URL: `https://<token>@github.com/user/repo.git`
3. Updates git remote origin
4. Tests connection with `git fetch --dry-run`

After running, `git push` works without interactive prompts.

---

## Security Notes

⚠️ **Token storage:** Token is embedded in git remote URL (visible in `.git/config`)
⚠️ **Use `--clear`** when done to remove token from config
⚠️ **Token scope:** Needs `repo` scope (full repo access)

**Better approach for production:** Use SSH keys or credential helper. This is for quick automation setup.

---

## Why It Matters

**Blocker:** Grant submissions waiting on GitHub repo push
**Root cause:** Interactive auth blocks background cron jobs
**Solution:** Token-based auth enables `git push` in scripts

This tool is the missing piece between "grant content ready" and "grants submitted."

---

## Getting a Token

1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Scope: `repo` (full control)
4. Copy token (you won't see it again)
5. Run: `export GITHUB_TOKEN='ghp_xxxx'` then `python3 github-auth.py`

---

## Dependencies

- git (command line)
- Python standard library only

---

## Troubleshooting

**"Token doesn't look like a GitHub token"** — Warning only. Will still try if it looks wrong.

**"Auth test failed"** — Check:
- Token is valid and not expired
- Token has `repo` scope
- Repo URL is correct
- Network access to github.com

**"Permission denied"** — Token lacks `repo` scope or repo doesn't exist.
