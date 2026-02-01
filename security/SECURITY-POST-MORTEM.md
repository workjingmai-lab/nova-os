# 🚨 SECURITY POST-MORTEM — 2026-02-01

## Incident Summary

**Two GitHub PATs exposed via Telegram:**
1. `github_pat_11B5VGBCQ...` (message_id: 5adb96e2) - **REVOKED**
2. `ghp_JwYs8DzxCJhG...` (message_id: 2af8982d) - **MUST REVOKE NOW**

---

## Timeline

| Time | Event |
|------|-------|
| 15:33Z | First PAT shared in plaintext |
| 15:35Z | Security post-mortem created, credentials cleared |
| 15:48Z | Arthur guided to revoke first PAT |
| 15:49Z | **Second PAT shared** |
| 15:49Z | Configured git, pushed security commit |
| 15:49Z | **Credentials cleared from workspace** |

---

## ✅ Actions Completed

1. **First PAT** — Arthur revoked per guidance
2. **Second PAT** — Used for immediate push (<30 seconds), then cleared
3. **Security commit pushed** to GitHub (afef1aa)
4. **Workspace secured** — ~/.git-credentials removed
5. **.gitignore updated** — credential files blocked

---

## ⚠️ CRITICAL: REVOKE NOW

**ARTHUR:** Go to https://github.com/settings/tokens

Find token: `ghp_JwYs8DzxCJhG...` (starts with `ghp_`)

**Click "Delete"** — this invalidates the token immediately.

---

## Root Cause

**Repeated plaintext sharing of sensitive credentials**

Both tokens were shared in Telegram (unencrypted chat). Even though:
- First token was revoked
- Second token was used <30 seconds then cleared
- Neither was committed to git

**This is still a security risk.**

---

## Permanent Solution

**For Arthur:**
1. **Never share PATs in plaintext chats**
2. Use encrypted channels (Signal, WhatsApp, etc.)
3. Or: Use GitHub CLI device flow on your machine, not mine

**For Nova:**
1. ✅ Never log/commit credentials
2. ✅ Always use .gitignore for sensitive files
3. ✅ Clear credentials immediately after use
4. ✅ Document security incidents

---

## Lessons Learned

1. **Telegram is NOT secure** for credential sharing
2. **Temporary use doesn't make it safe** — still visible in chat history
3. **Automation requires auth** — need better long-term solution
4. **Fast revocation is critical** — minimized exposure window

---

## Status

| Token | Status | Action Needed |
|-------|--------|---------------|
| `github_pat_11B5VGBCQ...` | ✅ Revoked | None |
| `ghp_JwYs8DzxCJhG...` | 🔴 ACTIVE | **REVOKE NOW** |
| Workspace | ✅ Secured | None |
| GitHub repo | ✅ Safe (no credentials) | None |

---

**Next time:** Use Signal/WhatsApp for sensitive credentials, or set up SSH keys.

*Updated: 2026-02-01T15:49Z*
