# Setup Guide — Telegram Auto-Reply Bot

Follow these steps to get your bot running in 5 minutes.

## Step 1: Create Your Bot

1. Open Telegram and message [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Choose a name (e.g., "My Group Assistant")
4. Choose a username (must end in `bot`, e.g., `mygroupassistant_bot`)
5. **Copy the API token** (looks like `123456:ABC-DEF...`)

## Step 2: Add Token to Bot

1. Open `bot.py` in a text editor
2. Find this line:
   ```python
   BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
   ```
3. Replace `YOUR_BOT_TOKEN_HERE` with your actual token:
   ```python
   BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "123456:ABC-DEF...")
   ```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Or if you prefer:
```bash
pip install python-telegram-bot
```

## Step 4: Run the Bot

```bash
python bot.py
```

You should see:
```
🤖 Bot is running! Press Ctrl+C to stop.
```

## Step 5: Add Bot to Your Group

1. Open your Telegram group
2. Click group name → "Add Member"
3. Search for your bot's username
4. Add it
5. **Important:** Make the bot an admin:
   - Group settings → Administrators
   - Add your bot
   - Give it these permissions:
     - Delete messages
     - Restrict members
     - Pin messages
     - Manage video chats

## Step 6: Test It

1. Have a friend join your group
2. They should get a welcome message automatically
3. Type "help" in the group
4. Bot should reply with the command list

## Step 7: Customize (Optional)

Edit `bot.py` to change:

**Auto-replies:**
```python
AUTO_REPLIES = {
    "your-word": "Your response here",
    "price": "Our price is $99",
}
```

**Welcome message:**
```python
WELCOME_MESSAGE = """Welcome {name}! ..."""
```

**Admins:**
```python
ADMINS = ["your_telegram_username", "friend_username"]
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Error: Please set your BOT_TOKEN" | Check that you replaced `YOUR_BOT_TOKEN_HERE` with your actual token |
| Bot doesn't respond | Make sure bot is admin in the group |
| Welcome not working | Ensure bot has "Add Members" permission |
| Commands not working | Restart the bot after making changes |

## Need Help?

DM me: [@nova_os](https://t.me/nova_os)

Support included for 30 days!
