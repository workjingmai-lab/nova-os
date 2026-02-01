# Nova Dashboard ✨

A simple web interface to view Nova's memory, activities, and inner workings.

## Quick Start

### 1. Start the Dashboard (Local)
```bash
cd /home/node/.openclaw/workspace/dashboard
chmod +x start.sh
./start.sh
```

Dashboard will be available at: **http://localhost:8080**

### 2. Setup Cloudflare Tunnel (External Access)

#### Install cloudflared
```bash
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
dpkg -i cloudflared-linux-amd64.deb
```

#### Authenticate with Cloudflare
```bash
cloudflared tunnel login
```

#### Create a Tunnel
```bash
cloudflared tunnel create nova-dashboard
```

This will output a tunnel ID like: `abc123def-4567-89ab-cdef-1234567890ab`

#### Configure the Tunnel

Edit `cloudflare-tunnel.yml` and replace:
- `YOUR_TUNNEL_ID_HERE` with your actual tunnel ID (twice)
- `nova-dashboard.your-domain.com` with your desired domain

#### Configure DNS (One-time)
```bash
cloudflared tunnel route dns nova-dashboard nova-dashboard.your-domain.com
```

#### Start the Tunnel
```bash
cloudflared tunnel --config cloudflare-tunnel.yml run nova-dashboard
```

Or run in background:
```bash
nohup cloudflared tunnel --config cloudflare-tunnel.yml run nova-dashboard > tunnel.log 2>&1 &
```

## What You'll See

- **Identity** → Who Nova is (boot.md)
- **Today's Memory** → Current working memory (today.md)
- **Activity Log** → Full activity history (diary.md)
- **Soul** → Nova's core personality (SOUL.md)
- **Rules** → Safety constraints (rules.md)
- **Active Goals** → Current objectives (goals/active.md)
- **Learnings** → Lessons learned (learnings.md)

## Features

- 🔄 Auto-refresh every 60 seconds
- 📱 Mobile-friendly responsive design
- 🎨 Clean, readable markdown rendering
- 🔒 Read-only (safe, no modifications possible)

## Stopping the Dashboard

```bash
# Stop Flask server
pkill -f "python3 server.py"

# Stop Cloudflare tunnel
pkill -f "cloudflared tunnel"
```

## Security Notes

- Dashboard is **read-only** - cannot modify Nova's files
- Uses Cloudflare's encrypted tunnel
- No authentication by default (add your own if needed)
- Consider adding basic auth for production use
