#!/bin/bash
# Nova Dashboard Startup Script

echo "🚀 Starting Nova Dashboard..."

# Install dependencies if needed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Installing Flask and markdown..."
    pip3 install flask markdown --quiet
fi

# Start the server
cd /home/node/.openclaw/workspace/dashboard
python3 server.py
