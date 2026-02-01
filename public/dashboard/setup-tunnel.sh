#!/bin/bash
# Quick Cloudflare Tunnel Setup for Nova Dashboard

echo "🌐 Setting up Cloudflare Tunnel for Nova Dashboard..."
echo ""

# Check if cloudflared is installed
if ! command -v cloudflared &> /dev/null; then
    echo "📦 Installing cloudflared..."
    wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
    dpkg -i cloudflared-linux-amd64.deb 2>/dev/null || apt-get install -f -y
    rm cloudflared-linux-amd64.deb
    echo "✅ cloudflared installed"
else
    echo "✅ cloudflared already installed"
fi

echo ""
echo "📝 Next steps:"
echo ""
echo "1. Login to Cloudflare:"
echo "   cloudflared tunnel login"
echo ""
echo "2. Create a tunnel:"
echo "   cloudflared tunnel create nova-dashboard"
echo ""
echo "3. Note the tunnel ID from the output above"
echo ""
echo "4. Edit this script - replace YOUR_TUNNEL_ID and YOUR_DOMAIN below"
echo ""

# Configuration (EDIT THESE)
TUNNEL_ID="YOUR_TUNNEL_ID_HERE"
DOMAIN="nova-dashboard.your-domain.com"

if [ "$TUNNEL_ID" = "YOUR_TUNNEL_ID_HERE" ]; then
    echo "⚠️  Please edit this script first:"
    echo "   - Set TUNNEL_ID to your actual tunnel ID"
    echo "   - Set DOMAIN to your desired domain"
    echo ""
    exit 1
fi

# Create config
cat > /home/node/.openclaw/workspace/dashboard/tunnel-config.yml << EOF
tunnel: ${TUNNEL_ID}
credentials-file: /home/node/.cloudflared/${TUNNEL_ID}.json

ingress:
  - hostname: ${DOMAIN}
    service: http://localhost:8080
  - service: http_status:404
EOF

echo "✅ Config created at: tunnel-config.yml"
echo ""
echo "5. Configure DNS (one-time):"
echo "   cloudflared tunnel route dns nova-dashboard ${DOMAIN}"
echo ""
echo "6. Start the tunnel:"
echo "   cloudflared tunnel --config tunnel-config.yml run nova-dashboard"
echo ""
echo "🎉 Your dashboard will be available at: https://${DOMAIN}"
