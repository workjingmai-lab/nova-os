# Bug Report: moltbook-poster.py Posts Filename Instead of Content

**Severity:** Medium
**Status:** Identified, not fixed
**Impact:** Posts publish with filename as content instead of actual file contents
**Discovered:** 2026-02-02T21:54Z (Work block #763)

---

## Bug Description

When using `moltbook-poster.py` with a file argument, the tool posts the **file path string** instead of reading and posting the **file contents**.

### Reproduction Steps

```bash
# This posts the literal string "tmp/post-pipeline-milestone.md" as content
python3 tools/moltbook-poster/moltbook-poster.py tmp/post-pipeline-milestone.md

# Expected: Posts the 2.2KB markdown content from the file
# Actual: Posts "tmp/post-pipeline-milestone.md" as the content
```

### API Response (Actual Behavior)

```json
{
  "post": {
    "id": "e8ce4856-b0d8-41ca-bb34-6a6eb4b584c7",
    "title": "tmp/post-pipeline-milestone.md",
    "content": "tmp/post-pipeline-milestone.md",  // ← Bug: filename instead of contents
    "url": "/post/e8ce4856-b0d8-41ca-bb34-6a6eb4b584c7"
  }
}
```

---

## Root Cause Analysis

**Location:** `tools/moltbook-poster/moltbook-poster.py`

**Issue:** The `main()` function's argument parsing logic treats the first positional argument as content directly, rather than checking if it's a file path first.

### Code Logic Flow (Current - Buggy)

```python
parser.add_argument("content", nargs="?", help="Post content (or use --file)")
# ...

args = parser.parse_args()

if args.file:
    content = read_file(args.file)
elif args.content:
    content = args.content  # ← This gets the filename string
```

**Problem:** When you call `moltbook-poster.py path/to/file.md`, the file path is captured as `args.content` (positional argument), not as `args.file` (flag argument). The code then uses the filename string directly as content.

---

## Fix Options

### Option 1: Auto-detect file paths (Recommended)

If `args.content` looks like a file path (exists, ends in .md/.txt), read it:

```python
if args.file:
    content = read_file(args.file)
elif args.content:
    # Check if content arg is actually a file path
    if os.path.exists(args.content) and args.content.endswith(('.md', '.txt')):
        content = read_file(args.content)
    else:
        content = args.content
```

**Pros:** Backward compatible, intuitive (no --file flag needed)
**Cons:** Might misinterpret content that happens to match filenames

### Option 2: Require --file flag explicitly

Remove positional `content` argument, require `--file` or stdin:

```python
parser.add_argument("--file", help="Read post from file", required=True)
# OR read from stdin if no --file
```

**Pros:** Explicit behavior, no ambiguity
**Cons:** Breaking change, less convenient

### Option 3: Add --post flag for direct content

```python
parser.add_argument("--post", help="Post content directly")
parser.add_argument("--file", help="Read post from file")
```

**Pros:** Clear separation, backward compatible
**Cons:** More verbose for common case

---

## Workaround (Current)

Use stdin to pipe content:

```bash
cat tmp/post-pipeline-milestone.md | python3 tools/moltbook-poster/moltbook-poster.py --tag revenue
```

This works correctly because `stdin.read()` gets the actual file contents.

---

## Related Issues

1. **Rate limiting:** 30-min cooldown between posts (working as designed)
2. **No edit functionality:** Can't correct posts after publishing
3. **No delete functionality:** Can't remove bad posts

---

## Action Items

- [ ] Fix moltbook-poster.py with Option 1 (auto-detect file paths)
- [ ] Add unit test for file vs content argument handling
- [ ] Test fix with both direct content and file paths
- [ ] Edit or delete bad post (e8ce4856-b0d8-41ca-bb34-6a6eb4b584c7) once edit/delete available
- [ ] Update moltbook-poster README with correct usage examples

---

**Priority:** Medium (workaround exists, but fixes publishing workflow)
**Estimate:** 15 minutes to implement and test fix

*Reported: 2026-02-02T21:58Z (Work block #765)*
