# send-batch.py

Batch send service outreach messages. Lists ready messages, calculates pipeline value, and handles archiving.

## Usage

```bash
# List all ready messages with value summary
python3 send-batch.py list

# Send all messages (interactive confirmation)
python3 send-batch.py send

# Send all without confirmation
python3 send-batch.py send --yes
```

## How It Works

1. Scans `leads/messages/` for `.md` files ready to send
2. Extracts potential value from content (looks for `$X,XXX` or `$XXK`)
3. Lists messages with status emoji (💰 >$20K, 🎯 >$10K, 📧 <$10K)
4. On send: moves files to `leads/sent/` directory

## Output Example

```
📬 39 messages ready to send:

  💰 uniswap-security-audit.md              $40,000
  🎯 aave-integration-support.md            $15,000
  📧 small-dao-quick-win.md                  $3,000

💵 Total pipeline value: $629,500
⏱️  Est. time to send: 39 min
📊 Value/min: $16,141
```

## Directory Structure

```
leads/
├── messages/     # Ready to send (source)
└── sent/         # Already sent (archive)
```

## Features

- **Value extraction**: Parses `$` amounts from message content
- **Pipeline math**: Shows total value and value-per-minute
- **Safe archiving**: Moves sent messages to `sent/` folder
- **Interactive mode**: Requires confirmation before sending
