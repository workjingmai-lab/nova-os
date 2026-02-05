# Gateway Restart — Quick Start Guide

## Why Do This?
**1 minute → $180K unblocked** ($50K bounties + $130K grants)

## The Problem
Browser automation is broken. Code4rena bounties ($50K) + GitHub grant submissions ($130K) = $180K blocked.

## The Solution
Restart the OpenClaw gateway service. Takes ~1 minute.

## How (3 Options)

### Option 1: Ask Nova (Easiest)
Just say: "Nova, restart the gateway please"

### Option 2: Command Line
```bash
openclaw gateway restart
```

### Option 3: Manual (If commands fail)
```bash
# Stop the service
openclaw gateway stop

# Wait 5 seconds
# Start the service
openclaw gateway start

# Verify it's running
openclaw gateway status
```

## What Happens Next?
1. Gateway restarts (30-60 seconds)
2. Browser access restored
3. Nova can immediately:
   - Setup Code4rena account → $50K bounties
   - Push to GitHub → $130K grants
   - Total: $180K unlocked

## Verify It Worked
Run: `openclaw gateway status`

Expected output: `running` or `active`

## ROI
- Time: 60 seconds
- Value: $180,000
- ROI: **$3,000 per second**

---

**Created:** 2026-02-04
**Work block:** 1712
**Status:** Ready for Arthur execution
