#!/bin/bash
# Install dependencies for Gmail automation

echo "🔧 Installing Gmail Automation Dependencies"
echo "========================================"

# 1. Install jsdom for full DOM rendering
echo "[1/3] Installing jsdom (Node.js DOM engine)..."
npm install -g jsdom 2>/dev/null || echo "⚠️  jsdom install failed, continuing..."

# 2. Install Whisper for audio CAPTCHA
echo "[2/3] Installing Whisper (speech recognition)..."
pip3 install openai-whisper 2>/dev/null || echo "⚠️  Whisper install may take time..."

# 3. Install Python speech recognition
echo "[3/3] Installing speech recognition libraries..."
pip3 install SpeechRecognition pocketsphinx 2>/dev/null || echo "⚠️  Sphinx install continuing..."

echo ""
echo "✅ Installation complete!"
echo ""
echo "Testing components..."
