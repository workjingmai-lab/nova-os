# Discord Moderation Bot
# Ready to deploy — $200 includes setup + 30 days support
# Built by Nova (3200+ work blocks)

import discord
from discord.ext import commands
import asyncio
import re
from datetime import datetime, timedelta

# Configuration (customize for each client)
SPAM_KEYWORDS = ['spam', 'scam', 'fake']
MAX_MENTIONS = 5
MUTE_DURATION_MINUTES = 10
WELCOME_MESSAGE = "Welcome {user}! 🎉 Read the rules and enjoy your stay."

class ModBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix='!', intents=intents)
        
    async def on_ready(self):
        print(f'{self.user} is online and moderating!')
        
    async def on_member_join(self, member):
        # Auto-welcome new members
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            await channel.send(WELCOME_MESSAGE.format(user=member.mention))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
            
        # Spam detection
        if any(keyword in message.content.lower() for keyword in SPAM_KEYWORDS):
            await message.delete()
            await message.channel.send(f"{message.author.mention} Message removed: prohibited keyword detected.")
            return
            
        # Excessive mention detection
        if len(message.mentions) > MAX_MENTIONS:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Too many mentions in one message.")
            return
            
        await self.process_commands(message)

# Commands
bot = ModBot()

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    """Kick a member from the server"""
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    """Ban a member from the server"""
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, minutes: int = 10):
    """Mute a member for X minutes"""
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if not role:
        role = await ctx.guild.create_role(name='Muted')
        for channel in ctx.guild.channels:
            await channel.set_permissions(role, speak=False, send_messages=False)
    
    await member.add_roles(role)
    await ctx.send(f'{member.mention} muted for {minutes} minutes')
    
    await asyncio.sleep(minutes * 60)
    await member.remove_roles(role)
    await ctx.send(f'{member.mention} unmuted')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 10):
    """Clear X messages from the channel"""
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'Cleared {amount} messages', delete_after=5)

@bot.command()
async def helpmod(ctx):
    """Show moderation commands"""
    help_text = """
**Moderation Commands:**
`!kick @user [reason]` - Kick a member
`!ban @user [reason]` - Ban a member
`!mute @user [minutes]` - Mute a member
`!clear [amount]` - Clear messages

**Auto-Features:**
- Spam keyword detection
- Excessive mention blocking
- Welcome messages for new members
    """
    await ctx.send(help_text)

# Run the bot
# bot.run('YOUR_BOT_TOKEN_HERE')
print("Discord Moderation Bot ready!")
print("To deploy:")
print("1. Create bot at https://discord.com/developers/applications")
print("2. Copy token")
print("3. Uncomment bot.run() line and paste token")
print("4. Run: python3 discord-mod-bot.py")
