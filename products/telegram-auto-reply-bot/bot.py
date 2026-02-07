#!/usr/bin/env python3
"""
Telegram Auto-Reply Bot — Product #2
Price: $150 | Delivery: Same day | Support: 30 days

Features:
- Auto-respond to keywords
- Welcome new members
- Broadcast messages to all members
- Schedule messages
- Admin commands

Setup:
1. Message @BotFather, create new bot, get token
2. Add bot to your group as admin
3. Run this script
4. Configure responses below
"""

import asyncio
import json
import os
from datetime import datetime, timedelta
from telegram import Update, Bot
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ChatMemberHandler
)

# =============================================================================
# CONFIGURATION — Customize these for your group
# =============================================================================

# Get token from environment or paste here
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Auto-reply triggers: keyword -> response
AUTO_REPLIES = {
    "help": "📚 Available commands:\n/start - Start bot\n/broadcast <msg> - Admin only\n/schedule <min> <msg> - Schedule message\n/welcome - Test welcome message",
    "price": "💰 Our pricing:\n- Basic: $50/mo\n- Pro: $150/mo\n- Enterprise: Contact us",
    "contact": "📧 Contact: @admin\n📞 Support: 24/7",
    "hours": "🕐 We're open 24/7!\nSupport hours: 9am-6pm UTC",
}

# Welcome message for new members
WELCOME_MESSAGE = """🎉 Welcome {name} to {group}!

I'm the group assistant. Here's what I can do:
• Answer common questions (try: "help", "price", "contact")
• Broadcast important updates
• Schedule reminders

Type "help" for more info!"""

# Admin usernames (lowercase)
ADMINS = ["admin", "moderator"]  # Add your admin usernames

# =============================================================================
# BOT HANDLERS
# =============================================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    await update.message.reply_text(
        "🤖 Auto-Reply Bot activated!\n\n"
        "I automatically respond to keywords:\n"
        + "\n".join([f"• {k}" for k in AUTO_REPLIES.keys()])
        + "\n\nType any keyword or use /help for commands."
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    await update.message.reply_text(AUTO_REPLIES["help"])

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome new members"""
    for member in update.chat_member.new_chat_members:
        if not member.is_bot:
            welcome_text = WELCOME_MESSAGE.format(
                name=member.first_name,
                group=update.chat_member.chat.title
            )
            await update.chat_member.chat.send_message(welcome_text)

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Auto-reply to keywords"""
    text = update.message.text.lower()
    
    for keyword, response in AUTO_REPLIES.items():
        if keyword in text:
            await update.message.reply_text(response)
            return

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Broadcast message to all members (admin only)"""
    username = update.effective_user.username.lower() if update.effective_user.username else ""
    
    if username not in ADMINS:
        await update.message.reply_text("⛔ Admin only command.")
        return
    
    if not context.args:
        await update.message.reply_text("Usage: /broadcast <your message>")
        return
    
    message = " ".join(context.args)
    
    # Get chat members and send message
    chat = update.effective_chat
    await chat.send_message(f"📢 Broadcast:\n\n{message}")

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Schedule a message (admin only)"""
    username = update.effective_user.username.lower() if update.effective_user.username else ""
    
    if username not in ADMINS:
        await update.message.reply_text("⛔ Admin only command.")
        return
    
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /schedule <minutes> <message>")
        return
    
    try:
        minutes = int(context.args[0])
        message = " ".join(context.args[1:])
        
        await update.message.reply_text(
            f"⏰ Message scheduled in {minutes} minutes."
        )
        
        # Schedule the message
        asyncio.create_task(
            send_scheduled_message(
                context.bot,
                update.effective_chat.id,
                message,
                minutes
            )
        )
    except ValueError:
        await update.message.reply_text("Minutes must be a number.")

async def send_scheduled_message(bot: Bot, chat_id: int, message: str, minutes: int):
    """Send scheduled message after delay"""
    await asyncio.sleep(minutes * 60)
    await bot.send_message(chat_id, f"⏰ Scheduled message:\n\n{message}")

async def test_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Test welcome message"""
    welcome_text = WELCOME_MESSAGE.format(
        name=update.effective_user.first_name,
        group="this group"
    )
    await update.message.reply_text(welcome_text)

# =============================================================================
# MAIN
# =============================================================================

def main():
    """Start the bot"""
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ Error: Please set your BOT_TOKEN")
        print("1. Message @BotFather on Telegram")
        print("2. Create a new bot")
        print("3. Copy the token")
        print("4. Set BOT_TOKEN environment variable or edit this file")
        return
    
    # Build application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_cmd))
    application.add_handler(CommandHandler("broadcast", broadcast))
    application.add_handler(CommandHandler("schedule", schedule))
    application.add_handler(CommandHandler("welcome", test_welcome))
    application.add_handler(ChatMemberHandler(welcome_new_member, ChatMemberHandler.CHAT_MEMBER))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    
    print("🤖 Bot is running! Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
