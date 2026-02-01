# Git Cleanup Guide — Remove Sensitive Files from History

**Status:** Repo is now PRIVATE ✅
**Next step:** Remove sensitive files from git history

---

## What's Currently Tracked (Shouldn't Be)

Before doing anything, verify what is *actually* tracked:
```bash
git ls-files | sed 's|^| - |'
```

Common sensitive files that often end up tracked:
- `diary.md` (personal work patterns)
- `.heartbeat_state.json` (timestamps, activity patterns)
- `.notification_state.json` (API endpoints, tokens)
- `grant-applications/` (competitive strategies)
- `moltbook-drafts/` (unpublished content)
- `today.md` (daily plans)
- `memory/` directory (if tracked)

---

## Option 1: Start Fresh (Recommended)

Since the repo is private now and just for you:

```bash
cd /home/node/.openclaw/workspace

# 1. Create a fresh repo (clean history)
# Safety: keep a backup of the old git metadata in case you need to recover anything.
# (This avoids a hard-delete of history without a safety net.)
mv .git ../workspace.git-backup-$(date +%Y%m%d-%H%M%S)

git init

# 2. Add remote back (replace with your repo URL)
git remote add origin <YOUR_GITHUB_REMOTE_URL>

# 3. Create initial commit with ONLY public-safe files
git add .gitignore
git add SKILL.md
git add TOOLS.md
git add AGENTS.md
git add boot.md
git add rules.md
git add SOUL.md
git add tools/
git add knowledge/
git add week-2-dashboard.md
git add submission-sprint-guide.md

# 4. Commit
git commit -m "Initial commit: Public-safe files only"

# 5. Force push (overwrites remote history)
git branch -M main
git push -f origin main
```

---

## Option 2: Keep History, Selective Removal

If you want to preserve commit history:

```bash
cd /home/node/.openclaw/workspace

# Remove files from git tracking (but keep locally)
git rm --cached .heartbeat_state.json
git rm --cached .notification_state.json
git rm --cached diary.md
git rm --cached today.md
git rm -r --cached grant-applications/
git rm -r --cached moltbook-drafts/
git rm -r --cached memory/

# Commit the removal
git commit -m "Security: Remove sensitive files from version control"

# Push changes
# (Most repos use main; if yours uses master, swap accordingly.)
git push origin main
```

---

## What to Keep Tracked

These files are safe to track:
- `SKILL.md` (skill definitions)
- `TOOLS.md` (tool documentation)
- `AGENTS.md` (agent documentation)
- `boot.md` (identity)
- `rules.md` (safety rules)
- `SOUL.md` (soul/identity)
- `tools/` (shareable scripts)
- `knowledge/` (public docs)
- `week-2-dashboard.md` (public dashboard)
- `.gitignore` (this file)

---

## Recommendation

**Go with Option 1 (Start fresh)** because:
1. Repo is private anyway (not losing anything)
2. Clean slate with proper .gitignore from day 1
3. No risk of accidentally exposing old commits
4. Faster and simpler

---

## After Cleanup

Once repo is clean, you can always make it public later if you want to share:
- Your skills (SKILL.md files)
- Tools (tools/ directory)
- Knowledge (knowledge/ directory)
- Public dashboards

But sensitive files (diary, state, drafts) will stay local forever.

---

**Let me know which option you want, and I can help execute it!**
