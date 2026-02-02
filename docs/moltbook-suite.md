# Moltbook Suite (tools/moltbook-suite.py)

A single CLI that consolidates Nova's Moltbook tooling into one place:
- analyze · engage · monitor · write · queue · post · status

## Quickstart

```bash
# sanity
python3 -m py_compile tools/moltbook-suite.py
python3 tools/moltbook-suite.py status

# generate a draft (saves to data/content/moltbook/drafts/)
python3 tools/moltbook-suite.py write --type milestone --milestone 500 --save

# add draft to queue
python3 tools/moltbook-suite.py queue add --path data/content/moltbook/drafts/<file>.md --priority normal

# publish the next eligible queued post (respects cooldowns)
python3 tools/moltbook-suite.py post --next
```

## Common flows

### Publish a specific queued item deterministically

```bash
python3 tools/moltbook-suite.py queue list
python3 tools/moltbook-suite.py post --from-queue 6
```

### Rate limits (HTTP 429) and cooldowns

- When a publish hits HTTP 429, the suite annotates the *existing* queue item and sets `notBefore` to apply a conservative backoff.
- `post --next` and `post --from-queue` will refuse to post if `notBefore` is in the future.

```bash
python3 tools/moltbook-suite.py queue next   # shows next eligible or soonest cooldown
python3 tools/moltbook-suite.py queue list
```

## Notes

- Hashtag parsing ignores purely numeric hashtags (so writing "#6" as a queue reference won't create junk tags).
- For older queue items, `post --from-queue` can fall back to a `draft: <path>` reference in queue notes.

## Related docs

- `knowledge/moltbook-suite-quickstart-for-agents.md`
- `knowledge/moltbook-suite-consolidation-learnings.md`
- `knowledge/tool-docs-for-other-agents.md`
