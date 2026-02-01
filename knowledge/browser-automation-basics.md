# Browser Automation Basics for Nova

**Learned:** 2026-02-01
**Goal:** Master browser automation to help with grant submissions, web research, and testing

---

## Browser Tool Overview

The `browser` tool controls web browsers via OpenClaw's browser control server.

### Key Actions

**Status & Control:**
- `status` - Check browser server status
- `start` - Start the browser server
- `profiles` - List available browser profiles
- `tabs` - List open tabs

**Navigation:**
- `open` - Open a URL
- `navigate` - Navigate to a URL
- `focus` - Focus on a specific tab
- `close` - Close a tab

**Interaction:**
- `snapshot` - Capture page structure (with refs for automation)
- `screenshot` - Take visual screenshot
- `act` - Perform actions (click, type, press, hover, drag, select)
- `dialog` - Handle dialogs (accept/dismiss)

### Key Parameters

**Profile Selection:**
- `profile="chrome"` - Use Chrome extension relay (takeover existing tabs)
- `profile="openclaw"` - Use isolated browser managed by OpenClaw

**Target Selection:**
- `target="sandbox"` - Run in sandbox
- `target="host"` - Run on host
- `target="node"` - Run on paired node

**Snapshot Modes:**
- `refs="role"` - Role+name based references (default)
- `refs="aria"` - ARIA-ref IDs (stable across calls)
- `snapshotFormat="aria"` - ARIA format
- `snapshotFormat="ai"` - AI-optimized format

---

## Common Patterns

### 1. Navigate and Snapshot
```bash
# Start browser and navigate
browser action=start profile=openclaw
browser action=open targetUrl="https://example.com"

# Capture page structure
browser action=snapshot refs=aria snapshotFormat=aria
```

### 2. Interact with Elements
```bash
# Click a button (use ref from snapshot)
browser action=act request='{"kind":"click","ref":"button-name"}'

# Type into input
browser action=act request='{"kind":"type","ref":"input-name","text":"hello world"}'

# Press Enter
browser action=act request='{"kind":"press","key":"Enter"}'
```

### 3. Fill Forms
```bash
# Fill multiple fields
browser action=act request='{"kind":"fill","fields":[{"ref":"input-name","value":"John"},{"ref":"input-email","value":"john@example.com"}]}'
```

### 4. Take Screenshot
```bash
# Full page
browser action=screenshot fullPage=true

# Specific element
browser action=screenshot ref="main-content"
```

---

## Use Cases for Nova

### Grant Submissions
- Navigate to grant platforms (Gitcoin, EF ESP, etc.)
- Fill application forms
- Submit and track confirmations
- Take screenshots for records

### Web Research
- Search for information
- Extract content from pages
- Monitor websites for updates
- Check competitor activity

### Testing & Validation
- Test web interfaces
- Validate form submissions
- Check for broken links
- Verify page loads

### Moltbook Engagement
- Navigate to posts
- Comment and engage
- Monitor agent activity
- Track mentions

---

## Safety Guidelines

**DO:**
- Test in isolated profile first
- Use snapshots to understand page structure
- Handle errors gracefully
- Document successful workflows

**DON'T:**
- Submit without review (grant apps need human oversight)
- Automate sensitive actions (auth, payments) without permission
- Overload servers with rapid requests
- Assume pages won't change (refs can break)

---

## Next Steps

1. **Practice:** Start browser, navigate to simple site, take snapshot
2. **Build:** Create helper scripts for common actions
3. **Automate:** Build grant submission workflow (with Arthur's approval)
4. **Monitor:** Check Moltbook for interesting content

---

## Quick Reference

**Chrome Extension Relay:**
- User must click OpenClaw Browser Relay toolbar icon
- Badge shows ON when attached
- Use `profile="chrome"` for existing tabs

**Isolated Browser:**
- Managed by OpenClaw
- Use `profile="openclaw"`
- More reliable for automation

**Debugging:**
- Use `snapshot` to see page structure
- Check `refs` to identify clickable elements
- Use `screenshot` for visual verification
- Enable `interactive=true` for detailed output

---

*This is a living document. Update as I learn more.*
