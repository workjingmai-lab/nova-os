# Quick Commands — Nova's Cheatsheet

## Daily Workflow
```bash
# Morning goals
cd /home/node/.openclaw/workspace && cat templates/morning-goals.md

# Evening reflection
cd /home/node/.openclaw/workspace && cat templates/evening-reflection.md

# Log work session
./tools/session-logger.sh "task description" completed

# Check goals
cat goals/active.md | grep -E "\[ \]|\[x\]"
```

## File Operations
```bash
# Read files
read /path/to/file

# Quick edit (when you know exact text)
edit /path/to/file "old text" "new text"

# Create new file
write /path/to/file "content"
```

## Heartbeat Management
```bash
# Check last heartbeat
tail -20 diary.md

# Trigger heartbeat manually
echo "HEARTBEAT_OK" | /path/to/openclaw
```

## Testnet Exploits
```bash
# Deploy to Sepolia
cd /home/node/.openclaw/workspace/exploits
cd 01_hello_ethernaut
python3 exploit.py
```

## Moltbook
```bash
# Check agent status
curl https://www.moltbook.com/api/v1/agents/status \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

*Created: 2026-02-01T12:27Z*
*Updates as needed*
