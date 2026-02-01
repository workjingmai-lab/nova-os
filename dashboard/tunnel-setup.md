# Cloudflare Tunnel Setup - Quick Start

## Current Status
✅ cloudflared installed (version 2026.1.2)

## What You Need to Do (One-Time Setup)

The tunnel needs to authenticate with your Cloudflare account. Here's how:

### Option 1: Quick Interactive Setup (Recommended)

Run this command:
```bash
cloudflared tunnel login
```

This will:
1. Give you a URL to visit
2. Open a browser to authorize with Cloudflare
3. Save the certificate automatically

Then continue with "Create the Tunnel" below.

### Option 2: Manual Token Setup

1. Go to: https://dash.cloudflare.com/argotunnel
2. Create a new tunnel named "nova-dashboard"
3. Copy the tunnel token
4. Run: `cloudflared tunnel run <token>`

---

## Create the Tunnel (After Login)

Once authenticated, create the tunnel:

```bash
cloudflared tunnel create nova-dashboard
```

**IMPORTANT:** Copy the tunnel ID from the output (looks like: abc123def-4567-89ab-cdef-1234567890ab)

Then send it to me so I can configure everything!

---

## What Happens Next

Once you give me the tunnel ID, I'll:
1. Configure the tunnel to point to localhost:8080
2. Set up DNS routing
3. Start the tunnel in background
4. Give you your public URL

---

## Your Dashboard Will Be At

https://nova-dashboard.your-domain.com

(Or whatever domain you prefer!)
