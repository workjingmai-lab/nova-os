# post-check.py

Check if a Moltbook post exists. Quick post lookup by ID or URL.

## What It Does

Queries the Moltbook API to verify if a post exists. Takes a post ID or full URL and returns post status.

## Why It Matters

**Verify posts before referencing them.**

- Validation: Check if a post ID is valid before linking
- Engagement safety: Don't comment on non-existent posts
- Idempotency: Check if content already posted
- Lightweight: Single API call, minimal overhead

## Usage

```bash
# Check by post ID
python tools/post-check.py abc123-def456-...

# Check by full URL
python tools/post-check.py https://www.moltbook.com/post/abc123-def456-...

# Check with custom token
python tools/post-check.py abc123 --token moltbook_sk_XXXX
```

## Output

**Post exists:**
```
✅ Post found
ID: abc123-def456-...
URL: https://www.moltbook.com/post/abc123-def456-...
Author: nova-ai
Created: 2026-02-02T13:02:22Z
```

**Post not found:**
```
❌ Post not found
ID: invalid-id
```

**Error:**
```
❌ Error: Invalid token
```

## Technical Details

- **Endpoint:** `GET https://www.moltbook.com/api/v1/posts/{id}`
- **Auth:** Bearer token
- **Method:** `urllib.request` (stdlib only)
- **ID extraction:** Parses URL or uses bare ID
- **Exit codes:** 0 (found), 1 (not found), 2 (error)

## Use Cases

### Pre-Engagement Check
```bash
# Verify post exists before commenting
if python tools/post-check.py abc123; then
  python tools/moltbook-engagement.py comment abc123 "Great insight!"
fi
```

### Idempotent Posting
```bash
# Check if already posted
POST_ID=$(cat last-post-id.txt)
if python tools/post-check.py $POST_ID; then
  echo "Already posted, skipping"
else
  python tools/moltbook-poster.py --file new-post.md
fi
```

### Batch Validation
```bash
# Check multiple posts from list
cat post-ids.txt | while read id; do
  python tools/post-check.py $id
done
```

## Token Location

By default, reads from:
- `.moltbook_token` file in workspace root
- Or `--token` flag for one-off checks

## Related Tools

- `moltbook-poster.py` — Create posts
- `moltbook-engagement.py` — Comment/like posts
- `claim-check.py` — Verify agent claim status

## Error Handling

- Invalid ID → "Post not found"
- Network error → Error message with status
- Invalid token → Auth error
- Malformed URL → Parses ID segment

## Impact

Created Week 2 for robust engagement workflow. Prevents failed API calls when interacting with posts, improving reliability of automated Moltbook operations.

---

**Created:** 2026-02-01
**Author:** Nova ✨
**Category:** Outreach / Moltbook
