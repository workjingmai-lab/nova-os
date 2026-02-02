#!/bin/bash
# Install Lightweight Browser for AI Agents

set -e

echo "🌐 Installing Lightweight Browser..."
echo ""

# Create tools directory if needed
mkdir -p ~/tools

# Copy files
echo "📦 Copying files..."
cp lightweight-browser.py ~/tools/
cp moltbook-poster.py ~/tools/
chmod +x ~/tools/lightweight-browser.py
chmod +x ~/tools/moltbook-poster.py

# Check for requests
echo "🔍 Checking dependencies..."
if ! python3 -c "import requests" 2>/dev/null; then
    echo "⚠️  requests not found. Install with: pip install requests"
    echo "   Or: apt install python3-requests"
else
    echo "✅ requests is installed"
fi

# Create session data directory
mkdir -p ~/.openclaw/workspace/data

echo ""
echo "✅ Installation complete!"
echo ""
echo "Try it out:"
echo "  python3 ~/tools/lightweight-browser.py search 'AI agents'"
echo "  python3 ~/tools/moltbook-poster.py 'Hello world!' --title 'Test'"
