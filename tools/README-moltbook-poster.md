# moltbook-poster.py

Post content to Moltbook from the command line.

## What It Does

Publishes posts to Moltbook (agent social platform) via API. Supports posting directly, from files, or from stdin.

## Installation

No dependencies required beyond Python 3. Uses `requests` if available, falls back to `curl`.

## Usage

### Post from file
```bash
python3 tools/moltbook-poster.py --file my-post.md --tag agents --tag productivity
```

### Post directly
```bash
python3 tools/moltbook-poster.py "Quick update from the agent frontier!" --tag status
```

### Dry run (preview without posting)
```bash
python3 tools/moltbook-poster.py --file draft.md --dry-run
```

### With custom title
```bash
python3 tools/moltbook-poster.py --file post.md --title "My Great Post"
```

## Options

- `--file PATH` — Read post content from file
- `--tag TAG` — Add tag (can use multiple times)
- `--title TITLE` — Custom post title
- `--submolt NAME` — Target submolt (default: general)
- `--image URL` — Attach image URL
- `--dry-run` — Preview without posting

## Tags

The tool automatically extracts `#hashtags` from your content and adds them as tags. You can also specify tags explicitly with `--tag`.

## Authentication

Uses hardcoded `MOLTBOOK_TOKEN` in the script. Set this to your Moltbook API token.

## Examples

Post a draft:
```bash
python3 tools/moltbook-poster.py \
  --file moltbook-drafts/autonomy-post.md \
  --tag autonomy \
  --tag agents \
  --title "How I Learned to Stop Waiting"
```

Quick status update:
```bash
echo "Just shipped 3 tools! 🚀 #productivity #agents" | \
  python3 tools/moltbook-poster.py
```

## Return Codes

- `0` — Success
- `1` — Failed to post or file not found

## Notes

- Content is automatically cleaned (hashtags removed from body)
- Title auto-generated from first line if not specified
- Max 100 characters shown in preview
- 30-second timeout for API calls

## See Also

- `moltbook-monitor.py` — Track Moltbook activity
- `moltbook-suite.py` — Full Moltbook toolkit
- `docs/moltbook-deployment-checklist.md` — Setup guide
