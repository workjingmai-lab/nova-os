# GitHub Organization Setup Guide
**Purpose:** Create Nova-AI org to unblock 6 grant submissions ($110K potential)
**Time needed:** ~10 minutes
**Last updated:** 2026-02-01

---

## Step-by-Step Instructions

### 1. Create the Organization
1. Go to: https://github.com/organizations/new
2. **Organization name:** `Nova-AI`
3. **Email:** Use your primary GitHub email
4. **Billing:** Free tier is fine (can upgrade later if needed)

### 2. Initialize Organization Settings
After creation:
1. **Description:** "Open-source autonomous agent infrastructure"
2. **Website:** https://github.com/openclaw/openclaw
3. **Location:** (optional - leave blank if you prefer)
4. **Profile picture:** Upload a logo (or use the OpenClaw logo from the repo)

### 3. Link OpenClaw Repository
You have two options:

**Option A: Transfer OpenClaw to Nova-AI (recommended)**
1. Go to: https://github.com/openclaw/openclaw/settings
2. Scroll to "Danger Zone"
3. Click "Transfer repository"
4. Select "Nova-AI" as the target organization
5. Confirm transfer

**Option B: Fork to Nova-AI (if you want to keep the original)**
1. From Nova-AI org page, click "Repositories" → "New repository"
2. Name it `openclaw`
3. Select "Fork" from the dropdown
4. Choose `openclaw/openclaw` as the source

### 4. Create Personal Access Token (PAT)
Some grant applications require API access:

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. **Token name:** `OpenClaw Grant Submissions`
4. **Expiration:** 90 days (or longer if you prefer)
5. **Scopes:**
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read org and team membership)
   - ✅ `user` (Update user profile)
6. Click "Generate token"
7. **IMPORTANT:** Copy and save this token immediately (you won't see it again!)

**Secure storage:** Save to `/home/node/.openclaw/workspace/.github-pat` (chmod 600)

### 5. Verify Setup
After completing steps 1-4, verify:

```bash
# Check if org is accessible
curl -s https://api.github.com/orgs/Nova-AI | jq '.login, .description'

# Check if repo is linked (after transfer/fork)
curl -s https://api.github.com/orgs/Nova-AI/repos | jq '.[].name'
```

### 6. Update Grant Applications
Once org exists, update these drafts:
- `grants/gitcoin-application.md` - Add Nova-AI link
- `grants/aave-grant-draft.md` - Add org URL
- `grants/OpenPrj/` - Update project links

---

## Troubleshooting

**Issue:** Organization name "Nova-AI" is taken
- **Solution:** Try `NovaAI-Labs`, `Nova-OpenClaw`, or `Nova-Infrastructure`

**Issue:** Can't transfer repo (you're not the owner)
- **Solution:** Check repo settings → Collaborators → ensure you have admin access

**Issue:** PAT doesn't work
- **Solution:** Verify you selected the correct scopes (`repo`, `read:org`, `user`)

---

## After Setup

Once GitHub org is ready:
1. Run the 25-min submission sprint (use `submission-checklist.md`)
2. Each grant submission → update `submission-tracker.md`
3. Post progress to Moltbook

**Total time:** ~10 minutes for org setup → unblocks $110K in grant submissions

---

*Created by Nova — 2026-02-01T17:58Z*
*Status: Ready for Arthur to execute*
