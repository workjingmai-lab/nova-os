#!/bin/bash
# SSH Tunnel Script - Quick Dashboard Access

echo "🔐 SSH Tunnel Setup for Nova Dashboard"
echo ""
echo "Run this on your LOCAL machine (not the server):"
echo ""
echo "ssh -L 8080:localhost:8080 -N your-server-user@your-server-ip"
echo ""
echo "Then open your browser to: http://localhost:8080"
echo ""
echo "To stop the tunnel, press Ctrl+C"
echo ""
echo "💡 Pro tip: Add -o ServerAliveInterval=60 to keep connection alive"
echo ""
echo "Example with keep-alive:"
echo "ssh -L 8080:localhost:8080 -N -o ServerAliveInterval=60 your-server-user@your-server-ip"
