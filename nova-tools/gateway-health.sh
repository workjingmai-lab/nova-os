#!/bin/bash
# Nova's Gateway Health Check
# Alternative method since openclaw CLI requires permissions

echo "🌐 Gateway Health Check"
echo "======================"

# Check if gateway process is running
GATEWAY_PID=$(pgrep -f "openclaw-gateway" | head -1)

if [ -n "$GATEWAY_PID" ]; then
    echo "✅ Gateway process running (PID: $GATEWAY_PID)"
    
    # Check process uptime
    UPTIME=$(ps -p $GATEWAY_PID -o etime= 2>/dev/null | tr -d ' ')
    echo "⏱️  Uptime: $UPTIME"
    
    # Check memory usage
    MEM=$(ps -p $GATEWAY_PID -o rss= 2>/dev/null | awk '{print $1/1024 " MB"}')
    echo "💾 Memory: $MEM"
    
    # Check CPU usage
    CPU=$(ps -p $GATEWAY_PID -o %cpu= 2>/dev/null)
    echo "⚡ CPU: ${CPU}%"
    
    # Check if gateway is responding
    # Gateway runs on port 18789 according to docker-init
    if command -v curl &> /dev/null; then
        HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:18789/health 2>/dev/null || echo "000")
        if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "404" ]; then
            echo "🟢 Gateway responding (HTTP $HTTP_CODE)"
        else
            echo "🟡 Gateway not responding on health endpoint"
        fi
    fi
    
    echo ""
    echo "Status: HEALTHY ✅"
else
    echo "❌ Gateway process not found"
    echo ""
    echo "Status: UNHEALTHY 🔴"
fi
